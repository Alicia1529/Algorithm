

#### Principles of Object-Oriented Design
http://www.cs.utsa.edu/~cs3443/notes/designPrinciples/designPrinciples.html

- Single Responsibility Principle.
- Open Closed Principle.
- Liskov Substitution Principle.
- Interface Segregation Principle.
- Dependency Inversion Principle.

Encapsulation
Abstraction
Inheritance
Polymorphism



coupling and cohesion 

#### Consistency in distributed Systems
Consistency here means that a read request for an entity made to any of the nodes of the database should return the same data.

Case 1: Eventual Consistency
Eventual consistency offers low latency at the risk of returning stale data

Case 2: Strong Consistency
It says data will get passed on to all the replicas as soon as a write request comes to one of the replicas of the database.
But during the time these replicas are being updated with new data, response to any subsequent read/write requests by any of the replicas will get delayed as all replicas are busy in keeping each other consistent.

Conclusion:
Strong Consistency offers up-to-date data but at the cost of high latency.
While Eventual consistency offers low latency but may reply to read requests with stale data since all nodes of the database may not have the updated data.


#### Scheduling
Round-robin scheduling