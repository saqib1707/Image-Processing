**Multiprocessor/Multicore:** Several processors work on data stored in the shared memory<br>
**Co-processor :** The general purpose processor delegates specific tasks to special purpose processors (GPU, FPGA)<br>
**parallelism :** Using multiple processors to make the computation faster.<br>
**Concurrency :** make multiple tasks to proceed without waiting for each other.<br>

Parallel Computing : 
1. Decomposition of the complete task into independent subtasks and data flow between them.
2. Distribution of the independent subtasks over the processors minimizing the total execution time.
3. Synchronization of the individual processes is important.
4. Attributing equal workloads to all processors

### Synchronization issues
1. Deadlock : Two processes waiting for each other to finish
2. Race condition : Two or more processes modify a shared resource( e.g, variable, file) and the result depends on which processor comes first. 

### task farming:
1. One master process supervises the execution of the program. It defines independent tasks and puts them on a to-do list. It also collects the results of these tasks.
2. Any number of slave processes each take a task from the to-do list, execute it and put the result into the master's mailbox. 
3. One advantage is that - no deadlocks since only the master process is waiting for another process to finish.

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
Simple explanation of the above code--<br>
1. pool = Pool() launches one slave process per physical processor on a computer.
2. pool.map(sqrt, range(100)) divides the input list into chunks of roughly equal size and puts the task (function + chunk) on a todo list.
3. Each slave process takes a task (function + a chunk of data) from the todo list, runs map(function,chunk), and puts the result in a results list.
4. The master process waits until all tasks are handled and returns the concatenation of the results list.<br>

The todo list is actually a queue and must be accessible by all processes(master and slaves).The todo list is stored in the master process and its access must be synchronized. A special thread of the master process waits for the task requests from slave processes and returns the task function and arguments. This requires serialization.

### Difference between processes and threads 
A process consists of-
- a block of memory and some executable code
- one or more threads that execute code independently but work on the same memory. 

**Multithreading :** using multiple threads in the same process for concurrency or parallelism.<br>
**Multiprocessing:** using multiple processes with separate memory spaces for concurrency or parallelism.<br>

### Explicit Task Definition
```python
from multiprocessing import Pool
import numpy
def sqrt(x):
    return numpy.sqrt(x)
if __name__ == '__main__':
    pool = Pool()
    results = [pool.apply_async(sqrt, (x,))
               for x in range(100)]
    roots = [r.get() for r in results]
    print roots
```
1. pool.apply_async returns a proxy object immediately<br>
2. proxy.get() waits for task completion and returns the result<br>

Use for:
1. launching different tasks in parallel<br>
2. launching tasks with more than one argument<br>

### Shared Memory
Under Unix, it is possible to share blocks of memory between processes. This eliminates the serialization overhead. Multiprocessing can create shared memory blocks containing C variables and C arrays. A NumPy extension adds shared NumPy arrays. It it not possible to share arbitrary Python objects.

```python
from multiprocessing import Pool
from parutils import distribute
import numpy
import sharedmem
def apply_sqrt(a, imin, imax):
    return numpy.sqrt(a[imin:imax])
if __name__ == '__main__':
    pool = Pool()
    data = sharedmem.empty((100,), numpy.float)
    data[:] = numpy.arange(len(data))
    slices = distribute(len(data))
    results = [pool.apply_async(apply_sqrt, (data, imin, imax))
               for (imin, imax) in slices]
    for r, (imin, imax) in zip(results, slices):
        data[imin:imax] = r.get()
    print data

```
