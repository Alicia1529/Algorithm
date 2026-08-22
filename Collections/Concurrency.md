# Concurrency

Overview
- Concurrency questions test whether you can coordinate multiple threads so they
  produce a correct, deterministic result despite running in arbitrary order.
- The core toolkit: **Lock** (mutual exclusion), **Semaphore** (bounded permits),
  **Condition / Event** (wait until a predicate holds), and **Barrier** (rendezvous).
- The winning strategy on almost every problem: ask "what must be true before a
  thread is allowed to proceed?" and **block on that predicate** with a primitive,
  rather than busy-waiting or sleeping.

Primitives cheat-sheet (Python `threading`)
| Need | Primitive | Key methods |
|---|---|---|
| One-at-a-time access to shared state | `Lock` / `RLock` | `acquire()`, `release()`, `with lock:` |
| Allow up to N concurrent, or signal "1 token available" | `Semaphore(N)` | `acquire()`, `release()` |
| Wait for a one-shot signal (flag flips once) | `Event` | `wait()`, `set()`, `clear()` |
| Wait until an arbitrary predicate becomes true | `Condition` | `wait()`, `notify()`, `notify_all()` |
| Make K threads meet before any continues | `Barrier(K)` | `wait()` |

Mental model
- **Semaphore as a gate:** start it at 0 to mean "blocked"; another thread
  `release()`s it to hand over a turn. This is the cleanest tool for "thread A must
  run before thread B" ordering problems.
- **Condition for predicates:** always loop on the predicate (`while not ready:
  cond.wait()`) — `wait()` can return spuriously and the state may change between
  notify and re-acquire.

---

## Pattern 1 — Ordering with semaphores (Print in Order, LeetCode 1114)

Three methods must run `first → second → third` regardless of thread schedule.
Gate each later step behind a semaphore the previous step releases.

```python
from threading import Semaphore

class Foo:
    def __init__(self):
        self.gate2 = Semaphore(0)   # blocks second until first releases
        self.gate3 = Semaphore(0)   # blocks third until second releases

    def first(self, printFirst):
        printFirst()
        self.gate2.release()

    def second(self, printSecond):
        self.gate2.acquire()
        printSecond()
        self.gate3.release()

    def third(self, printThird):
        self.gate3.acquire()
        printThird()
```

---

## Pattern 2 — Alternation with two semaphores (Print FooBar, LeetCode 1115)

Two threads must strictly alternate `foobarfoobar...`. Two semaphores ping-pong
control back and forth.

```python
from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_turn = Semaphore(1)   # foo goes first
        self.bar_turn = Semaphore(0)

    def foo(self, printFoo):
        for _ in range(self.n):
            self.foo_turn.acquire()
            printFoo()
            self.bar_turn.release()

    def bar(self, printBar):
        for _ in range(self.n):
            self.bar_turn.acquire()
            printBar()
            self.foo_turn.release()
```

---

## Pattern 3 — Condition variable on a predicate (Zero Even Odd, LeetCode 1116)

One thread prints `0`, two others print evens/odds in `0102030405...` order.
A single lock + condition coordinates whose turn it is via a shared `state`.

```python
from threading import Condition

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cond = Condition()
        self.turn = 'zero'   # 'zero' | 'even' | 'odd'
        self.i = 1

    def zero(self, printNumber):
        for k in range(self.n):
            with self.cond:
                self.cond.wait_for(lambda: self.turn == 'zero')
                printNumber(0)
                self.turn = 'odd' if self.i % 2 else 'even'
                self.cond.notify_all()

    def even(self, printNumber):
        with self.cond:
            while self.i <= self.n:
                self.cond.wait_for(lambda: self.turn == 'even' or self.i > self.n)
                if self.i > self.n:
                    break
                printNumber(self.i); self.i += 1
                self.turn = 'zero'; self.cond.notify_all()

    def odd(self, printNumber):
        with self.cond:
            while self.i <= self.n:
                self.cond.wait_for(lambda: self.turn == 'odd' or self.i > self.n)
                if self.i > self.n:
                    break
                printNumber(self.i); self.i += 1
                self.turn = 'zero'; self.cond.notify_all()
```

---

## Pattern 4 — Bounded buffer / producer-consumer

Classic: producers add to a fixed-size buffer, consumers remove. Two semaphores
count empty and full slots; a lock protects the buffer itself.

```python
from threading import Semaphore, Lock
from collections import deque

class BoundedBuffer:
    def __init__(self, capacity):
        self.buf = deque()
        self.lock = Lock()
        self.empty = Semaphore(capacity)   # slots free
        self.full = Semaphore(0)           # items available

    def put(self, item):
        self.empty.acquire()               # wait for a free slot
        with self.lock:
            self.buf.append(item)
        self.full.release()                # one more item to consume

    def get(self):
        self.full.acquire()                # wait for an item
        with self.lock:
            item = self.buf.popleft()
        self.empty.release()               # freed a slot
        return item
```

> In real Python code, prefer `queue.Queue(maxsize=...)` — it implements exactly
> this, thread-safe, out of the box. The manual version is what interviews want.

---

## Pattern 5 — Fan-out / fan-in (parallel map then barrier)

Split work into independent chunks, run each on its own thread, **wait for all to
finish** (the barrier), then combine. Used by *Multithreaded Array Sort*:
partition → sort each segment in parallel → join → k-way merge. Works lock-free
**only because the chunks are disjoint** — no shared mutable state during the
parallel phase.

### Option A — raw `Thread` + `join()`

```python
from threading import Thread

def worker(lo: int, hi: int) -> None:
    nums[lo:hi] = sorted(nums[lo:hi])   # disjoint slice: read + write-back

threads = [Thread(target=worker, args=(lo, hi)) for lo, hi in bounds]
for t in threads:
    t.start()
for t in threads:
    t.join()                            # barrier: block until ALL are done
```

### Option B — `ThreadPoolExecutor` (idiomatic; caps concurrency, surfaces errors)

```python
from concurrent.futures import ThreadPoolExecutor

def sort_segment(lo: int, hi: int) -> None:
    nums[lo:hi] = sorted(nums[lo:hi])

with ThreadPoolExecutor(max_workers=k) as ex:
    futures = [ex.submit(sort_segment, lo, hi) for lo, hi in bounds]
    for f in futures:
        f.result()      # blocks AND re-raises any exception from the worker
# leaving the `with` block joins all pooled threads automatically
```

**Which to use**
- `join()` re-raises *nothing*: an exception in a worker is printed and lost; the
  main thread proceeds as if it succeeded. `future.result()` **re-raises** the
  worker's exception in the caller — you can't silently swallow a failed chunk.
- Raw threads create **one OS thread per item**. A pool reuses `max_workers`
  threads across many tasks — use it when tasks ≫ workers, or to cap concurrency.
- `future.result()` *returns the worker's value*, so workers can `return` their
  result instead of mutating shared state.
- Rule of thumb: **raw `Thread`** for a small fixed set of long-lived workers
  (exactly `k` segments); **pool** for many tasks, bounded concurrency, return
  values, or exception propagation.

> CPython caveat: the GIL means CPU-bound work (the sorts) won't truly run in
> parallel with `threading`; use `ProcessPoolExecutor` for real speedup. The
> *coordination pattern* is identical either way.

---

## Common pitfalls
- **Busy-waiting** (`while not ready: pass`) burns CPU and is wrong — block on a
  primitive instead.
- **Forgetting the predicate loop** with `Condition.wait()` — always re-check the
  condition after waking (use `wait_for(predicate)`).
- **Lock ordering / deadlock** — if a thread needs two locks, all threads must
  acquire them in the same global order.
- **Releasing a lock you don't hold**, or holding a lock across a blocking
  `acquire()` of another primitive → deadlock.
- **GIL ≠ thread safety:** the GIL serializes bytecode, but `x += 1` is still
  multiple bytecodes — you still need a lock for compound updates.

## Related LeetCode problems
- [1114. Print in Order](https://leetcode.com/problems/print-in-order/)
- [1115. Print FooBar Alternately](https://leetcode.com/problems/print-foobar-alternately/)
- [1116. Print Zero Even Odd](https://leetcode.com/problems/print-zero-even-odd/)
- [1117. Building H2O](https://leetcode.com/problems/building-h2o/)
- [1226. The Dining Philosophers](https://leetcode.com/problems/the-dining-philosophers/)
- [1188. Design Bounded Blocking Queue](https://leetcode.com/problems/design-bounded-blocking-queue/)
