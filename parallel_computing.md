An example of parallel computing is as follows:<br>
```python
from multiprocessing import Pool
import numpy
def sqrt(x):
    return numpy.sqrt(x)
if __name__ == '__main__':
    pool = Pool()
    roots = pool.map(sqrt, range(100))
    print roots

```
Simple explanation of the above code--
1. pool = Pool() launches one slave process per physical processor on a computer.
2. pool.map(sqrt, range(100)) divides the input list into chunks of roughly equal size and puts the task (function + chunk) on a todo list.
3. Each slave process takes a task (function + a chunk of data) from the todo list, runs map(function,chunk), and puts the result in a results list.
4. The master process waits until all tasks are handled and returns the concatenation of the results list.<br>

The todo list is actually a queue and must be accessible by all processes(master and slaves).The todo list is stored in the master process. A special thread of the master process waits for the task requests from slave processes and returns the task function and arguments. This requires serialization.

### Difference between processes and threads 
A process consists of-
- a block of memory and an executable code
- one or more threads that execute code independently but work on the same memory. 

**Multithreading :** using multiple threads in the same process for concurrency or parallelism
**Multiprocessing :**using multiple processes with separate memory spaces for concurrency or parallelism
