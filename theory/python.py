"""
Q:: Why python is single threaded?
A:: Introduced to simplify memory management in CPython (the main Python implementation). Because Python's 
    memory management (CPython specifically) isn't thread-safe! So GIL is like a big ol'
    babysitter making sure memory doesn't get corrupted when threads mess around.


Q:: CUDA
A:: It allows developers to use NVIDIA GPUs for general-purpose computing tasks, not just rendering graphics. 
    Essentially, CUDA unleashes the raw power of GPUs to perform high-performance computations, 
    making them useful for tasks like machine learning, scientific simulations, video processing, and more.    


Q:: data types in python, which are immutable?
A:: Immutable:: int, float, boolean, str, tuple()
    Mutable:: array[], set{:}, dict{}    


Q:: difference between '==' and is in python 
A:: '==' checks if 2 values are identical in valuesm when 'is' check whether the're identical from POV
    of memory cell


Q:: what are lambda functions, where are they used?
A:: Used to create one-line simple functions
    lambda var1 var2 varN: expression_with_var1_var2_varN


Q:: Positional vs. Keyword (Named) Arguments in Python
A:: def greet(name, age):
        pass
    greet("Alice", 25) - positional, order matters
    greet(age=25, name="Alice") -keyword, order matters as black lifes

    
Q:: Ways to send args in function
A:: Either as pos args or as named args


Q:: Null vs NaN difference
A:: 1) no value
    2) value resultis confusing or not identified, but present, not null


Q:: Tuples vs. Lists in Python - What's the Difference?
A:: - Lists[]::   mutable        slower*     more memory*      cannot*
    - Tuples()::  immutable      faster      less memory       can be used as dict keys 
    * - cause mutable


Q:: List functions
A:: .append()
    .extend()
    .insert()
    .remove()
    .pop()
    .count()
    .sort()
    .copy()
    ...

    
Q:: Same for str
A:: 
    len()	            Counts how long your string is 📏	            len("hello") ➡️ 5
    find()	            Scans for a substring 🔍	                    "magic vibes".find("vibes") ➡️ 6
    starts/endswith()	Checks if it starts with something ✅	       "alpha moves".startswith("alpha") ➡️ True
    isdigit/alpha()	    Is this whole thing a number? 🤔                "123".isdigit() ➡️ True
    islower/upper()	    Checks if it's all lowercase/caps 🔠	        "vibe".islower() ➡️ True
    -----------------------------------------------------------------------------------------------------
    upper()	            Screams your text in ALL CAPS 🔊	            "yo".upper() ➡️ 'YO'
    lower()	            Whisper mode 📉 	                            "YELL".lower() ➡️ 'yell'
    capitalize()	    Makes the first letter classy 💅	            "vibe check".capitalize() ➡️ 'Vibe check'
    title()	            Capitalizes every word like a title 📚	        "rise of the devs".title() ➡️ 'Rise Of The Devs'
    -----------------------------------------------------------------------------------------------------------
    strip()	            Scrapes off extra spaces 🧼	                    " chill ".strip() ➡️ 'chill'
    replace()	        Swaps one string for another 🔁	                "hot girl summer".replace("hot", "cool") ➡️ 'cool girl summer'
    split()	            Smashes it into a list 🪓	                    "chill vibes only".split() ➡️ ['chill', 'vibes', 'only']
    join()	            Glues strings together with a separator 🧪	    " ".join(['yo', 'fam']) ➡️ 'yo fam'
    

Q:: Suppose I have a queue with huge capacity, and it receives normaly distributed random amound of events, 
    but outputs the same random amound of events. Queue is 50% full. how could I reduce variance in output?
A:: 1) O = O_old*0.8 + O_new*0.2
    2) always output imput mean size
    3) if input is not distributed normaly output sliding mean


Q:: *args and **kwargs
A:: *args allows you to pass a variable number of positional arguments
    **kwargs allows you to pass a variable number of keyword arguments to a function
    - The single asterisk * is used to collect positional arguments into a tuple. In function calls 
        The * symbol can also be used to unpack a collection.
    - The double asterisk ** is used to collect keyword arguments into a dictionary. In function calls 
        The ** symbol is used to unpack a dictionary into keyword arguments

        def my_function(*args):
            [print(arg) for arg in args]

        def my_function(**kwargs):
            [print(f"{key}: {value}") for key, value in kwargs.items()]
                
        my_function(1, 2, 3, 4)
        my_function(name="Alice", age=25, city="New York")


Q:: def func(listok=[]) - is that possible? Should I do that?
A:: 🔍 Yes, it's possible, but you definitely should NOT do that! 🚨
    Python only initializes default arguments once when the function is defined, 
    not each time the function is called.
    
    def func(listok=[]):  # ❌ Bad practice!
        listok.append("😱")
        print(listok)

    func()  # Output: ['😱']
    func()  # Output: ['😱', '😱']  (WTF?!)
    func()  # Output: ['😱', '😱', '😱']  (Keeps growing!)

    
Q:: a=[1, 2, 3], b=(1, 2, 3), c={}: will c[a] and c[b] work?
A:: c[b] will cause it receives immutable


Q:: How to determine whether a hash function is good/bag?
A:: A good hash function should:
        - distribute data uniformly
        - minimize collisions
        - and be fast to compute. 

        
Q:: Are all variables in python just references?
A:: In Python, variables are not the actual data, they're just labels (references) 
    pointing to objects in memory.


Q:: .copy(), .deepcopy()
A:: .copy() - Creates a new object, but does not copy nested objects inside it. The nested objects 
        (like lists or dicts inside a copied list/dict) still reference the original. 
    .deepcopy() - makes entirery new object with new data.


Q:: What is the GIL?
A:: The GIL (Global Interpreter Lock) is a mutex (lock) that ensures only one thread executes Python 
    bytecode at a time, even on multi-core CPUs. Python uses automatic memory management 
    (like garbage collection), and the GIL prevents race conditions when multiple threads 
    modify Python objects simultaneously.
    

Q:: Multithreading vs multiprocessing
A:: 1) Multithreading = One CPU, Many Threads
        - Uses multiple threads inside the same process. Starting a new thread = fast & lightweight.
            Starting a new process = slow & heavyweight. So, if you need many small tasks running quickly, 
            threads win because starting a process takes more time and resources.
        - Threads share memory and resources (RAM, variables, files). Hence, No need to copy data, 
            so it's more memory-efficient.
    2)  Multiprocessing = Many CPUs, Many Processes
        - Uses multiple processes, each with its own memory space.
        - Each process runs independently, so no GIL issues!
        - More efficient at large computational needs. 🧮 Heavy calculations (math, AI, video encoding)
            are much more efficient if we work with multiprocessing 🤙🔥.
    
    
Q:: difference IO-bound vs CPU-bound tasks
A:: 1) The program spends most of its time waiting for external resources (disk, network, database, etc.).
        The CPU is mostly idle, just chilling, waiting for data. Since I/O operations don't 
        use much CPU, we can use multiple threads to handle many tasks concurrently.
    2) The program spends most of its time crunching numbers (calculations, processing data).
        The CPU is constantly working, doing the heavy lifting. Since these tasks fully use the CPU, 
        multiple processes can run in parallel, each on a different CPU core.
           

_ _ _ _ Q:: async tasks, async/await
A:: Asynchronous operations allow a program to start a task without waiting for it to finish. 
    Instead of blocking the program, it allows the program to continue executing other tasks 
    while waiting for the previous one to finish.
    - async is a keyword used to define a function that will work asynchronously. It helps to tell Python 
        that this function is gonna handle tasks that might take some time without blocking the rest of 
        your program.
    - await is used inside async functions to pause execution until a task is completed, 
        allowing other tasks to run in the meantime.
    - async is better for IO tasks, threads for IO computational tasks.


Q:: Immutable classes
A:: class ImmutableRobot:
        def __init__(self, name, brandname):
            self.__name = name
            self.__brandname = brandname

        @property
        def name(self):
            return self.__name

        @property
        def brandname(self):
            return self.__brandname

    robot = ImmutableRobot(name="RoboX", brandname="TechBot")
    print(robot.name)       
    print(robot.brandname)
    robot.name = "RoboY" # error 
    ------------------------------------------------------------------
    @dataclass(frozen=True)
    class Immutable:
        x: int
        y: int

    obj = Immutable(10, 20)
    obj.x = 30
    

Q:: Context managers
A:: - Are used to launch certain functionality before/after execution of certain piece of code.
    - It ensures proper setup and cleanup (like closing files or releasing locks) and can handle 
        exceptions in the __exit__() method and decide whether to suppress them.

    class MyContextManager:
        def __enter__(self):
            print("Entering the context")

        def __exit__(self):
            print("Exiting the context")

    with MyContextManager() as cm:
        print("Inside the context")

    // Entering the context
    // Inside the context
    // Exiting the context

    
Q:: class var
A:: 
    class Dog:
        species = "Canis lupus"  # 🌍 Class variable shared across all dogs!

        def __init__(self, name):
            self.name = name  # 🧍 Instance variable - unique per pupper!


Q:: @classmethod @staticmethod
A:: - A @classmethod is a method that receives the class (not the instance) as the first argument, 
        which is conventionally named cls. This allows you to modify the class state or call 
        other class methods.
        Alien.manual_cls(Alien)  # manually pass the class 🔧 - without @classmethod
    - The @classmethod method is bound to the class, not the instance. It can be called on the class itself, 
        or on an instance of the class.
    - A @staticmethod is a method that doesn't receive either the instance (self) or the class (cls) 
        as its first argument. It's essentially a function that belongs to the class's namespace 
        but doesn't need access to the class or instance data.
    - It is used when you want to define a method that logically belongs to the class 
        but does not require access to any class-specific or instance-specific data.
    ------------------------------------------------------------------------------------------------------
    class Car:
        wheels = 4
        @classmethod
        def get_wheels(cls): // cls instance!!!
            return cls.wheels

    class Math:
        @staticmethod
        def add(a, b):
            return a + b

    print(Math.add(3, 4))  # Returns 7 
    print(Car.get_wheels())  # Returns 4 

    

Q:: list vs np.array()
A:: List:
        1) Can hold elements of any type (integers, strings, other lists, etc.)
        2) Hence, slower for numerical operations.
        3) Hence, takes more memory because each element is an object with additional metadata.
        4) Not fixed in size.
    np.array():
        1) Can only hold elements of a single data type
        2) Hence, faster for numerical operations due to optimized C-based operations.
        3) Hence, more memory-efficient, as elements are stored as contiguous blocks in memory 
            with a fixed data type.
        4) fixed-size

    

Q:: Iterator
A:: An iterator in Python is an object that allows you to traverse (iterate over) all the elements 
    in a collection, like a list, tuple, or dictionary, one at a time.
        numbers = [1, 2, 3]
        iterator = iter(numbers)
        print(next(iterator))  # Outputs: 1
    - Memory Efficiency: Iterators don't require loading all the data into memory at once. 
        They yield items one by one as needed, which is great for large datasets or when working 
        with infinite sequences (like generating Fibonacci numbers).
    - Lazy Evaluation: With iterators, the data is evaluated lazily, meaning only the next item is 
        computed when needed, rather than calculating everything upfront.
    - if redined as class, then::
        class Pupa:
            def __init__():
                self.lupa = "pupa"
                self.index = -1

            def __iter__():
                return self

            def __next__():
                self.index += 1
                return self.data[self.index]


Q:: Generator
A:: Is a type of iterator which is defined with 'yield' word. 
    def my_range(start, end):
        while start < end:
            yield start 
            start += 1 

    gen = my_range(0, 5)
    for number in gen:
        print(number)
    # it stops it's execution at 'yield' point and 
    # unpauses it when new object from func is called.                
                

Q:: handling collisions
A:: Use subsets. Suppose you have a hash table of size 10, and you hash the string "apple" and "orange". 
    If both map to index 4, both "apple" and "orange" are stored at that index in a linked list.
    Then to access it we can use subhash function.
    

Q:: frozenset
A:: A frozenset is an immutable version of a set. Once created, it cannot be changed. Why Use frozenset?
        ✅ Hashable (can be used as dictionary keys & set elements)
        ✅ Immutable (safer, prevents accidental changes)
        ✅ Faster lookups (compared to lists)
    fs = frozenset([1, 2, 3, 4])
    print(fs)  # Output: frozenset({1, 2, 3, 4})                

    
Q:: hashing in python
A:: Hashing converts an object into a fixed-size integer (hash value).
    Exp: hash("hello")  # Hashing a string
    It's mainly used for: 
        ✅ Dictionaries (fast lookups 🔥)
        ✅ Sets (unique elements)
        ✅ Storing objects efficiently in memory
    
        
Q:: What Can Be Hashed in python? How to hash unhashable objects?
A:: 1) Any immutable types. You can define your own __hash__() method in a class.
    2) To hash, for example, a list, convert it to a tuple (which is immutable):


Q:: Magic methods (dunder methods)
A:: Magic methods allow you to define the behavior of your class with built-in Python operations.
    You can modify them in order to use same simple and convenient interface in all python objects
    - __str__ is called when you apply str()
    - __init__() - initializatin
    - __eq__ - called when '==' applied

    
Q:: getters and setters
A:: - are used for safe interractions with private variables, allowing to modify the data in only allowed way
    or get only certain allowed portion of data.
    !!! Python encourages direct attribute access !!!


Q:: What are objects in python?
A:: Instances of classes       


Q:: Is function an object in python?
A:: Yes, and consequence is that it can be treated as any other object 
    (passed as argument, returned as argument, or we can mae a var with func value) 


Q:: Differences Between Tuple and List Initialization in Memory in Python
A:: - A list in Python is implemented as a dynamic array. This means that when you create a list, 
        it allocates a contiguous block of memory that can resize dynamically as elements are added 
        or removed.
        Overhead: The list contains extra overhead to support dynamic resizing, like pointers to the 
            objects inside it and the extra memory for potential resizing.
        Mutability: Since lists are mutable, Python needs to allocate extra memory to manage changes 
            (like appending or removing items).
    - A tuple in Python is implemented as a fixed-size array. When a tuple is created, 
        Python allocates memory for the exact number of elements and doesn't need to resize, 
        making it more memory efficient than a list.
        No Resizing: Since tuples are immutable, the memory allocation does not need to account 
            for resizing. This reduces overhead.
        Performance: The immutable nature of tuples allows Python to store the elements more 
            compactly and access them faster.

            
Q:: Which objects can serve as a key in dict in python?
A:: Any immutable object cause python want to guarrantee that bucket is referenced only by valid key.


Q:: How Do Sets and Lists Store Information?
A:: List: data is stored in contiguous block of mem
    Set: data is stored in randomly distributed hash buckets, where each object - key
        which's value references bucket


Q:: If I need to process 1000000 strings in file, what is better, thread of process
A:: Depends on the nature of the task you're performing.


Q:: O(X) for addition to the beggining/end of list
A:: - Addition to the Beginning of List: O(n). When you add an element to the beginning of a list, 
        all other elements need to be shifted one position to the right to make space for the new element.
    - Addition to the End of List: O(1). Adding an element to the end of a list is typically O(1) 
        because appending an item to the end of the list involves simply placing the item 
        at the next available position in the array.


Q:: quicksort complexity
A:: O(n*log(n)) - on average
    O(n^2) - worst case scenario


Q:: What if set reaches it's max capacity
A:: A new hash function is applied, all hashes are recomputed and reassigned/
        

Q:: Reading in list/set - what's faster
A:: In set cause we don't need to go over all elements


Q:: list comprehension
A:: newlist = [x for x in fruits if "a" in x]


Q:: variables outside the visibility range
A:: Variables that are created outside of a function are known as global variables. 
    If you create a variable with the same name inside a function, this variable will be local, 
    and can only be used inside the function. The global variable with the same name will 
    remain as it was, global and with the original value.


Q:: 
A::     
"""