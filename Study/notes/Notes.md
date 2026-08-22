
### Priority Queue
和队列基本操作相同:
- top 访问队头元素
- empty 队列是否为空
- size 返回队列内元素个数
- push 插入元素到队尾 (并排序) `pq.push({a, b});`
- emplace 原地构造一个元素并插入队列 `pq.emplace(a, b);`
- pop 弹出队头元素
- swap 交换内容

- 默认是大顶堆
- 需要注意的是，如果使用`less<int>`和`greater<int>`，需要头文件`#include <functional>`

1. 基础类型
```c++
// priority_queue<Type, Container, Functional>;
//升序队列
priority_queue <int,vector<int>,greater<int> > q;
//降序队列
priority_queue <int,vector<int>,less<int> >q;

//greater和less是std实现的两个仿函数（就是使一个类的使用看上去像一个函数。其实现就是类中实现一个operator()，这个类就有了类似函数的行为，就是一个仿函数类了）

//对于基础类型 默认是大顶堆
priority_queue<int> a; 
//等同于 priority_queue<int, vector<int>, less<int> > a;

priority_queue<int, vector<int>, greater<int> > c;  //这样就是小顶堆
```

2. pari的比较，先比较第一个元素，第一个相等比较第二个
```c++
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
int main() 
{
    priority_queue<pair<int, int> > a;
    pair<int, int> b(1, 2);
    pair<int, int> c(1, 3);
    pair<int, int> d(2, 5);
    a.push(d);
    a.push(c);
    a.push(b);
    while (!a.empty()) 
    {
        cout << a.top().first << ' ' << a.top().second << '\n';
        a.pop();
    }
}
// 2 5
// 1 3
// 1 2
```

3. 自定义类型
```c++
#include <iostream>
#include <queue>
using namespace std;

//方法1
struct tmp1 //运算符重载<
{
    int x;
    tmp1(int a) {x = a;}
    bool operator<(const tmp1& a) const
    {
        return x < a.x; //大顶堆
    }
};

//方法2
struct tmp2 //重写仿函数
{
    bool operator() (tmp1 a, tmp1 b) 
    {
        return a.x < b.x; //大顶堆
    }
};

int main() 
{
    tmp1 a(1);
    tmp1 b(2);
    tmp1 c(3);
    priority_queue<tmp1> d;
    d.push(b);
    d.push(c);
    d.push(a);
    while (!d.empty()) 
    {
        cout << d.top().x << '\n';
        d.pop();
    }
    cout << endl;

    priority_queue<tmp1, vector<tmp1>, tmp2> f;
    f.push(c);
    f.push(b);
    f.push(a);
    while (!f.empty()) 
    {
        cout << f.top().x << '\n';
        f.pop();
    }
}
// 3
// 2
// 1

// 3
// 2
// 1
```

4. 其他用法
```c++
unordered_map.erase(const iterator);
unordered_map.erase(const key);
unordered_map.erase(const iteratorStart, const iteratorEnd);

for (auto &[chr, num]: map) pq.emplace(num, chr);
auto [num, chr] = pq.top();
```


### Deque
deque容器为一个给定类型的元素进行线性处理，像向量一样，它能够快速地随机访问任一个元素，并且能够高效地插入和删除容器的尾部元素。但它又与vector不同，deque支持高效插入和删除容器的头部元素，因此也叫做双端队列。deque类常用的函数如下。

1. 构造函数
```c++
deque():创建一个空deque
deque(int nSize):创建一个deque,元素个数为nSize
deque(int nSize,const T& t):创建一个deque,元素个数为nSize,且值均为t
deque(const deque &):复制构造函数
```

2. 增加函数
```c++
void push_front(const T& x):双端队列头部增加一个元素X
void push_back(const T& x):双端队列尾部增加一个元素x
iterator insert(iterator it,const T& x):双端队列中某一元素前增加一个元素x
void insert(iterator it,int n,const T& x):双端队列中某一元素前增加n个相同的元素x
void insert(iterator it,const_iterator first,const_iteratorlast):双端队列中某一元素前插入另一个相同类型向量的[forst,last)间的数据
```

3. 删除函数
```c++
Iterator erase(iterator it):删除双端队列中的某一个元素
Iterator erase(iterator first,iterator last):删除双端队列中[first,last）中的元素
void pop_front():删除双端队列中最前一个元素
void pop_back():删除双端队列中最后一个元素
void clear():清空双端队列中最后一个元素
```

4. 遍历函数
```c++
reference at(int pos):返回pos位置元素的引用
reference front():返回手元素的引用
reference back():返回尾元素的引用
iterator begin():返回向量头指针，指向第一个元素
iterator end():返回指向向量中最后一个元素下一个元素的指针（不包含在向量中）
reverse_iterator rbegin():反向迭代器，指向最后一个元素
reverse_iterator rend():反向迭代器，指向第一个元素的前一个元素
```
5. 其他函数
```c++
bool empty() const:向量是否为空，若true,则向量中无元素
Int size() const:返回向量中元素的个数
int max_size() const:返回最大可允许的双端对了元素数量值
void swap(deque&):交换两个同类型向量的数据
void assign(int n,const T& x):向量中第n个元素的值设置为x
```







### Queue
```c++
// queue 的生成方式和 stack 相同，下面展示如何创建一个保存字符串对象的 queue:
std::queue<std::string> words;
// 也可以使用拷贝构造函数：
std::queue<std::string> copy_words {words}; // A duplicate of words
// stack<T>、queue<T> 这类适配器类都默认封装了一个 deque<T> 容器，也可以通过指定第二个模板类型参数来使用其他类型的容器：
std::queue<std::string, std::list<std::string>>words;
// 底层容器必须提供这些操作：front()、back()、push_back()、pop_front()、empty() 和 size()。

front()：返回 queue 中第一个元素的引用。如果 queue 是常量，就返回一个常引用；如果 queue 为空，返回值是未定义的。
back()：返回 queue 中最后一个元素的引用。如果 queue 是常量，就返回一个常引用；如果 queue 为空，返回值是未定义的。
push(const T& obj)：在 queue 的尾部添加一个元素的副本。这是通过调用底层容器的成员函数 push_back() 来完成的。
push(T&& obj)：以移动的方式在 queue 的尾部添加元素。这是通过调用底层容器的具有右值引用参数的成员函数 push_back() 来完成的。
pop()：删除 queue 中的第一个元素。
size()：返回 queue 中元素的个数。
empty()：如果 queue 中没有元素的话，返回 true。
emplace()：用传给 emplace() 的参数调用 T 的构造函数，在 queue 的尾部生成对象。
swap(queue<T> &other_q)：将当前 queue 中的元素和参数 queue 中的元素交换。它们需要包含相同类型的元素。也可以调用全局函数模板 swap() 来完成同样的操作。

```

### set
```c++
使用时注意包含头文件<set>    std::set and std::multiset associative containers
s.begin()     　返回set容器的第一个元素
s.end() 　　　　 返回set容器的最后一个元素
s.clear()       删除set容器中的所有的元素
s.empty() 　　　 判断set容器是否为空
s.insert()      插入一个元素
s.erase()       删除一个元素
s.size() 　　　　返回当前set容器中的元素个数
```

// sort, reverse, fill, tolower, to_string, vector.insert, isalnum, isdigit, isnumber, remove(v.begin(), v.end(), xxx)
// INT_MAX and INT_MIN isdigit


```C++
std::sort(intervals.begin(), intervals.end(), [](const vector<int>& v1, const vector<int>& v2) {
    return (v1[0] <= v2[0]) ? true: false;
});


class Solution {
public:
    struct Comparator {
        bool operator() (const vector<int>& l, const vector<int>& r) {
            return l[1] != r[1] ? l[1] < r[1] : l[0] < r[0];
        }    
    };
    int eraseOverlapIntervals(vector<vector<int>>& ints) {
        if (ints.empty()) return 0;
        const int n = ints.size();
        sort(ints.begin(),ints.end(),Comparator());
        int prev = 0; int count = 1;
        for (int i=1; i<n; i++) {
            if (ints[i][0] >= ints[prev][1]) {
                count++; prev=i;
            } 
        }
        return n-count;
    }
};


	cout<<"The postion of the second 'one' is "<<k2<<endl;
	int k3=str1.find_first_of("aeiou");//here k3=1
	while(k3!=string::npos)      //hint:  here "string::npos"means find failed
	{
		str1[k3]='*';
		k3=str1.find_first_of("aeiou",k3+1);



Constant	Meaning	Value
INT_MIN	Minimum value for a variable of type int .	-2147483647 - 1
INT_MAX

std::queue
empty
size
front
back
push_back
pop_front
```


upper_bound, lower_bound
```c++
#include <iostream>     // std::cout
#include <algorithm>    // std::upper_bound
#include <vector>       // std::vector
using namespace std;
//以普通函数的方式定义查找规则
bool mycomp(int i, int j) { return i > j; }
//以函数对象的形式定义查找规则
class mycomp2 {
public:
    bool operator()(const int& i, const int& j) {
        return i > j;
    }
};
int main() {
    int a[5] = { 1,2,3,4,5 };
    //从 a 数组中找到第一个大于 3 的元素
    int *p = upper_bound(a, a + 5, 3);
    cout << "*p = " << *p << endl;
    vector<int> myvector{ 4,5,3,1,2 };
    //根据 mycomp2 规则，从 myvector 容器中找到第一个违背 mycomp2 规则的元素
    vector<int>::iterator iter = upper_bound(myvector.begin(), myvector.end(), 3, mycomp2());
    cout << "*iter = " << *iter;
    return 0;
}
```

sort(nums.begin(), nums.end(), greater<int>());

call to implicitly-deleted default constructor of ‘unordered_map＜pair＜int, int＞, int＞‘ m

https://blog.csdn.net/weixin_42989041/article/details/113183015