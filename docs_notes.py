"""
1. Whetting Your Appetite

2. Using the Python Interpreter
2.1. Invoking the Interpreter
2.1.1. Argument Passing
2.1.2. Interactive Mode
2.2. The Interpreter and Its Environment
2.2.1. Source Code Encoding

3. An Informal Introduction to Python
3.1. Using Python as a Calculator
3.1.1. Numbers
3.1.2. Strings
3.1.3. Lists

3.2. First Steps Towards Programming

4. More Control Flow Tools
4.1. if Statements
4.2. for Statements  ( can not change size )
4.3. The range() Function ( to iterate over a sequence of numbers )
4.4. break and continue Statements, and else Clauses on Loops
4.5. pass Statements
4.6. match Statements
4.7. Defining Functions ( def, name, (parameter list):, docs, code block )

4.8. More on Defining Functions
4.8.1. Default Argument Values
4.8.2. Keyword Arguments
4.8.3. Special parameters
4.8.3.1. Positional-or-Keyword Arguments
4.8.3.2. Positional-Only Parameters    ... /
4.8.3.3. Keyword-Only Arguments      * ...
4.8.3.4. Function Examples
4.8.3.5. Recap  ( p / standard * kw )

4.8.4. Arbitrary Argument Lists   ( *parameter ) ( **par )
4.8.5. Unpacking Argument Lists   ( *collection ) (**dict)
4.8.6. Lambda Expressions        ( lambda parameter list: single line of code )
4.8.7. Documentation Strings                                                                             ---------------- ***
4.8.8. Function Annotations      ( restrict data type ) ( __annotations__ )                              ---------------- ***

4.9. Intermezzo: Coding Style

5. Data Structures
5.1. More on Lists
5.1.1. Using Lists as Stacks ( list.pop() )
5.1.2. Using Lists as Queues ( collections.deque.popleft() )
5.1.3. List Comprehensions
5.1.4. Nested List Comprehensions

5.2. The del statement
5.3. Tuples and Sequences  ( can create with mutable obj ) (multiple assignment, tuple packing, sequence unpacking) ( swap )    ***
x = 1
y = 2
z = 3
x, y, z = 1, 2, 3

5.4. Sets   ( unique value )
5.5. Dictionaries  ( dict to list ) list(), sorted() )
5.6. Looping Techniques  ( enumerate, zip, reversed, sorted )
5.7. More on Conditions                                                                                ---------------- ***
5.8. Comparing Sequences and Other Types                                                               ---------------- ***

6. Modules
6.1. More on Modules ( help("modules") )
6.1.1. Executing modules as scripts
6.1.2. The Module Search Path
6.1.3. “Compiled” Python files

6.2. Standard Modules
6.3. The dir() Function

6.4. Packages
6.4.1. Importing * From a Package
6.4.2. Intra-package References
6.4.3. Packages in Multiple Directories

7. Input and Output
7.1. Fancier Output Formatting
7.1.1. Formatted String Literals
7.1.2. The String format() Method
7.1.3. Manual String Formatting
7.1.4. Old string formatting

7.2. Reading and Writing Files
7.2.1. Methods of File Objects
7.2.2. Saving structured data with json

8. Errors and Exceptions
8.1. Syntax Errors
8.2. Exceptions
8.3. Handling Exceptions
8.4. Raising Exceptions
8.5. Exception Chaining
8.6. User-defined Exceptions
8.7. Defining Clean-up Actions
8.8. Predefined Clean-up Actions
8.9. Raising and Handling Multiple Unrelated Exceptions
8.10. Enriching Exceptions with Notes

9. Classes
9.1. A Word About Names and Objects
9.2. Python Scopes and Namespaces
9.2.1. Scopes and Namespaces Example

9.3. A First Look at Classes
9.3.1. Class Definition Syntax
9.3.2. Class Objects
9.3.3. Instance Objects
9.3.4. Method Objects
9.3.5. Class and Instance Variables

9.4. Random Remarks

9.5. Inheritance
9.5.1. Multiple Inheritance

9.6. Private Variables
9.7. Odds and Ends
9.8. Iterators
9.9. Generators
9.10. Generator Expressions

10. Brief Tour of the Standard Library
10.1. Operating System Interface
10.2. File Wildcards
10.3. Command Line Arguments
10.4. Error Output Redirection and Program Termination
10.5. String Pattern Matching
10.6. Mathematics
10.7. Internet Access
10.8. Dates and Times
10.9. Data Compression
10.10. Performance Measurement
10.11. Quality Control
10.12. Batteries Included

11. Brief Tour of the Standard Library — Part II
11.1. Output Formatting
11.2. Templating
11.3. Working with Binary Data Record Layouts
11.4. Multi-threading
11.5. Logging
11.6. Weak References
11.7. Tools for Working with Lists
11.8. Decimal Floating Point Arithmetic

12. Virtual Environments and Packages
12.1. Introduction
12.2. Creating Virtual Environments
12.3. Managing Packages with pip

13. What Now?

14. Interactive Input Editing and History Substitution
14.1. Tab Completion and History Editing
14.2. Alternatives to the Interactive Interpreter

15. Floating Point Arithmetic: Issues and Limitations
15.1. Representation Error

16. Appendix
16.1. Interactive Mode
16.1.1. Error Handling
16.1.2. Executable Python Scripts
16.1.3. The Interactive Startup File
16.1.4. The Customization Modules

################################################

More Control Flow Tools

4.1. if Statements

4.2. for Statements

################################################

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}

# change dict size
for user, status in users.items(): # ("Mg Mg", "active")
    if status == "inactive":
        del users[user]

print(users)
#RuntimeError: dictionary changed size during iteration

################################################

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}
x = users.copy() # new dict
# iterate copy value to change dict size
for user, status in x.items():
    if status == "inactive":
        del users[user]
print(users)

################################################

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}

# iterate copy value to change dict size
# to avoid memory lose
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
print(users)

################################################

users = {"Mg Mg": "active", "Ma Ma" : "inactive", "Hla Hla" : "active"}

# Create a new collection
active_users = list()
inactive_users = list()

for user, status in users.items():
    if status == "active":
        active_users.append(user)
        #active_users.append((user, status))
        #active_users[user] = status
    else:
        inactive_users.append(user)

print(users)
print(active_users)
print(inactive_users)

################################################

column_name = list(users[0].keys())
print("{:<15}{:<15}{:<5}{:<25}{:<10}".format(*column_name))
for i in users:
    print("{:<15}{:<15}{:<5}{:<25}{:<10}".format(*i.values()))


column_name = list(users[0].keys())
print("{:<15}{:<15}{:<5}{:<25}{:<10}".format(*column_name))
for i in users:
    print("{:<15}{:<15}{:<5}{:<25}{:<10}".format(*i.values()))


################################################

. .  .  .  .  .  . X  ( column )
.
.
.
.
.
Y  ( row )

################################################

users.xlsh

user name      password       age  email address            status

Mg Mg          1234561        20   mgmg123@gmail.com        active
Ma Ma          1234562        25   mama456@gmail.com        inactive
Hla Hla        1234563        30   hlahla789@gmail.com      active


# print(users[2]["email address"])

################################################

users = (

{"user name" : "Mg Mg",
"password" : "1234561",
"age" : 20,
"email address" : "mgmg123@gmail.com",
"status" : "active",
},

{"user name" : "Ma Ma",
"password" : "1234562",
"age" : 25,
"email address" : "mama456@gmail.com",
"status" : "inactive",
},

{"user name" : "Hla Hla",
"password" : "1234563",
"age" : 30,
"email address" : "hlahla789@gmail.com",
"status" : "active",
}
)

# (dict, dict, dict)

# Create a new collection
active_users = []

for user in users:
    if user["status"] == "active":
        #active_users += [user]
        active_users.append(user)

print(users)
print(active_users)

################################################

({'user name': 'Mg Mg', 'password': '1234561', 'age': 20, 'email address': 'mgmg123@gmail.com', 'status': 'active'},
{'user name': 'Ma Ma', 'password': '1234562', 'age': 25, 'email address': 'mama456@gmail.com', 'status': 'inactive'},
{'user name': 'Hla Hla', 'password': '1234563', 'age': 30, 'email address': 'hlahla789@gmail.com', 'status': 'active'})

[{'user name': 'Mg Mg', 'password': '1234561', 'age': 20, 'email address': 'mgmg123@gmail.com', 'status': 'active'},
{'user name': 'Hla Hla', 'password': '1234563', 'age': 30, 'email address': 'hlahla789@gmail.com', 'status': 'active'}]

################################################

# email, password
e_p = []
for u in users:
    l = [u["user name"], u["email address"]]
    e_p.append(l)

print(e_p)

################################################

# [['Mg Mg', 'mgmg123@gmail.com'], ['Ma Ma', 'mama456@gmail.com'], ['Hla Hla', 'hlahla789@gmail.com']]

################################################

users = (

{"user name" : "Mg Mg",
"password" : "1234561",
"age" : 20,
"email address" : "mgmg123@gmail.com",
"status" : "active",
"marks" : {"myn" : 30, "eng" : 30, "math" : 90}
},

{"user name" : "Ma Ma",
"password" : "1234562",
"age" : 25,
"email address" : "mama456@gmail.com",
"status" : "inactive",
"marks" : {"myn" : 60, "eng" : 90, "math" : 70}
},

{"user name" : "Hla Hla",
"password" : "1234563",
"age" : 30,
"email address" : "hlahla789@gmail.com",
"status" : "active",
"marks" : {"myn" : 65, "eng" : 95, "math" : 80}
}

)

# (dict, dict, dict)
# ()
# 2 step

fail_users = []
pass_users = []
g_users = []

for user in users:
    f_sub = dict()# {}
    g_sub = dict()# {"eng" : 90}
    for sub, mark in user["marks"].items(): # ("myn", 30)
        if mark < 40:
            f_sub[sub] = mark
        else:
            if mark >= 80:
                g_sub[sub] = mark
    if f_sub:
        fail_users += [[user["user name"], f_sub]]
    else:
        #pass_users += [user["user name"]]
        pass_users.append([user["user name"], user["marks"]])
        if g_sub:
            g_users += [[user["user name"], g_sub]]

#print(users)
print(fail_users)
print(pass_users)
print(g_users)

################################################

################################################

#4.3. The range() Function     --->  to iterate over a sequence of numbers(int)

# (start, stop, step)
# 10, 9, 8 ,7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5 -6, -7, -8, -9, -10
for i in range(10, -11, -1):
    print(i)

################################################

# start , stop, step
# numbers list  --> range() with list(), tuple

even = list(range(2, 101, 2))
# [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]

print(even)

################################################

# index and value --> range() with ordered list ( list, tuple, str)

l = "abcdefg"
l = ["a", "b", "c", "d", "e", "f", "g", "i"] # 0  to  6
for i in range(10):
    print(i, l[i])

################################################

#  _   --->    for repeat only
for _ in range(10):
    print("i love you.")

################################################

04.4. break and continue Statements, and else Clauses on Loops

break         ---> breaks out of the innermost enclosing for or while loop.

continue      ---> continues with the next iteration of the loop

loop + else   --->   executed
                       when the loop terminates through exhaustion of the iterable (with for) or
                       when the condition becomes false (with while),
                       but not when the loop is terminated by a break statement.

################################################

# isjoin

x = [4, 6, 1, 5, 7, 9]
y = ["a", 2, "b", 3, 4]

c = False

for i in x:
    print(i)
    if i in y:
        c = True
        break

    #print(i, "another code")

print(c)

################################################

def isjoin(x, y):
    c = False
    for i in x:
        if i in y:
            c = True
            break
    return c

print(isjoin(x, y))

################################################

def isjoinr(x, y):
    for i in x:
        if i in y:
            return True
    return False

print(isjoinr(x, y))

################################################

"Return True if two sets have a null intersection."

# isdisjoin

x = [4, 5]
y = [1, "a", 2, "b", 3]

c = True
for i in x:
    if i in y:
        c = False
        break

print(c)

################################################

def isprime(n):
    x = 2
    while x <= n // 2:
        #print(n, " ---> ", x)
        if n % x == 0:
            return False
        x += 1
    return True

pc = []

for i in range(2, 1001):
    if isprime(i):
        pc.append(i)

print(pc)

################################################

[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449,
 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563,
 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653,
 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761,
 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991,
 997]

################################################

n = 31
x = 2

while x < n//2 + 1: # 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
    print(n, " ---> ", x)
    if n % x == 0:
        # print(n, 'equals', x, '*', n // x)
        break
    x += 1

else:
    # loop all items
    print(n, 'is a prime number')

################################################

n = 11
for x in range(2, n//2 + 1, 1):
    print(n , " ---> ", x)
    if n % x == 0:
        break
else:
    # loop all items
    print(n, 'is a prime number')

print(bool([]))

################################################

for num in range(3, 10):#  3, 4, 5, ...
    if num % 2 == 0:
        print("Found an even number", num)
        print()
        continue

    print("Found an odd number", num)
    print()

################################################

# 4.5. pass Statements

The pass statement does nothing.
It can be used when a statement is required syntactically
but the program requires no action.

################################################

n = 3
if n % 2 == 0:
    pass
else:
    print(n, "is odd number")

################################################

def add():
    pass

def sub():
    pass

def mul(*args):
    ans = 1
    for i in args:
        ans *= i
    return ans

def div():
    pass

print(mul(*range(1, 11)))

################################################

4.6. match Statements

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with this code."

error_meaning = http_error(4188)
print(error_meaning)

################################################

def http_error(status):
    if status == 400:
        return "Bad request"
    elif status == 401 or status == 403:
        return "Not allowed"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something's wrong with this code."

error_meaning = http_error(4188)
print(error_meaning)

################################################

# point is an (x, y) tuple

point = [1, 2]
#point = None , " " , ()
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _: # _ is any value
        #print("value error")
        raise ValueError("Not a point")

################################################

point = (1, 1)
#point = None , " " , ()
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case no_point: # _ is any value
        print("value error ---> ", no_point)
        #raise ValueError("Not a point")

################################################

# test pass --> (0, 0), (0, 1), (1, 0), (1, 1), "12", "ab", "", (), [ ],  [1, 2],

# fail test --> None data type ( because of no length )

################################################

point = [1, 2]

# x, y = point
# point value may be list, tuple, str, ... ,
# point value must be unpacked by 2 variables

if len(point) == 2 and point[0] == 0 and point[1] == 0:
    print("Origin")

elif len(point) == 2 and point[0] == 0 and point[1]:
    y = point[1]
    print(f"Y={y}")

elif len(point) == 2 and point[0] and point[1] == 0:
    x = point[0]
    print(f"X={x}")

elif len(point) == 2 and point[0] and point[1]:
    x = point[0]
    y = point[1]
    print(f"X={x}, Y={y}")

else:
    no_point = point
    print("value error ---> ", no_point)
    #raise ValueError("Not a point")

################################################

################################################

# 4.7. Defining Functions

def name(par):
    '''doc-strings'''
    statements
    return value


def  = keyword for standard function definition
name = function name ( identifier for function object )
()   = parenthesized list of formal parameters
:    = code block
____ = indent ( function body)

'''doc'''  = str value for function's documentation
statements = code section in function body
return     = used to exit a function and return a value (keyword)

#####################

The keyword def introduces a function definition. (def)

It must be followed by the function name and the parenthesized list of formal parameters.
(f p)

The statements that form the body of the function start at the next line, and must be indented.

____statements

The first statement of the function body can optionally be a string literal;
this string literal is the function’s documentation string, or docstring.

#####################

# parameter, default parameter, default value,
# argument, positional argument, keyword argument, arbitrary argument list / dict
# doc-string
# effect, result

#####################

# reading doc-string

def add(a, b):
    "It is add function."
    return a + b


# help(add)
# help(print)
# print(add.__doc__)
# print(print.__doc__)

s = {1, 2, 3}  # set obj
help(s.isdisjoint)
print(s.isdisjoint.__doc__)

#####################

# writing doc-string

def isdisjoin(a, b):
    "Return True if two iterable objects have a null intersection."
    c = True
    for i in a:
        if i in b:
            c = False
            break
    return c


d1 = {"myn": 60, "eng": 50}
d2 = {"math": 70, "chemistry": 65, "myn": 60}
s1 = (1, 2, 3)
s2 = [4, 5, 6, 7]
c = isdisjoin(d1.keys(), d2.keys())
print(c)


def isjoin(a, b):
    "Return True if two iterable objects have a intersection."
    c = False
    for i in a:
        if i in b:
            c = True
            break
    return c

s1 = {1, 2, 3, 4}
s2 = {4, 5, 6, 7}
c = isjoin(s1, s2)
print(c)

#####################
#####################

Type of function
1. (effect only) function        ( eg.difference_update )
2. (result only) function        ( eg.difference )
3. (effect and result) function  ( eg.pop )

# (result only) function
# return difference value
print(s.difference(s2))
print(s, s2)


s = {1, 2, 3, 4}
s2 = {1, 2}
# (effect only) function
# effect ---> update
print(s.difference_update(s2))
print(s, s2)


# (effect and result) function
# effect ---> remove
# return poped value
s = {1, 2, 3, 4}
print(s)
print(s.pop()) # result = popped element, effect = delete popped element
print(s)
# help(set)

#####################
#####################

# learning method for using strange function

# example: using difference method
# Return the difference of two or more sets as a new set.

s = {1, 2, 3, 4, 5, 6}

# step.1 --->

# read documentation before use
# determine effect and result.

print(s.difference.__doc__)
print("\n", "- " * 21, "\n")

# effect = no effect
# result = new set of difference result


#####################

# step.2 --->  test doc

s1 = {1, 2}
s2 = {3, 4}
ans = s.difference(s1, s2)
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

#####################

# step.3 ---> test as you like

# test with other iterable obj
# 1. list
s = {1, 2, 3, 4, 5, 6}
l1 = [1, 2]
l2 = [3, 4]
ans = s.difference(l1, l2)
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

# 2. tuple
s = {1, 2, 3, 4, 5, 6}
t1 = (1, 2)
t2 = (3, 4)
ans = s.difference(t1, t2)
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

# 3. dict
s = {1, 2, 3, 4, 5, 6}
d1 = {1 : "apple", 2 : "banana"}
d2 = {3 : "apple", 4 : "banana"}
ans = s.difference(d1, d2) # test with d.keys
actual_result = {5, 6}
print(ans, " --> ", ans == actual_result)

s = {"apple", "banana", "orange", "mangoes"}
d1 = {1 : "apple", 2 : "banana"}
d2 = {3 : "apple", 4 : "banana"}
ans = s.difference(d1.values(), d2.values()) # d.values
actual_result = {"orange", "mangoes"}
print(ans, " --> ", ans == actual_result)

#####################
#####################

# calling function with various arguments

# 1. pos
# 2. key
# 3. pos + key
# 4. *args  ( pack, unpack ) (pos)
# 5. **kwargs ( pack, unpack ) (kw)
# 6. pos + *args
# 7. kw + **kwargs
# 8. pos + **
# 9. pos + kw + **
# 10. pos + * + kw + **

# print     ---> *  +  default par

#####################

def add(a, b, c):
    return a + b + c

print(add(1, 2, 3))          # 1. positional arguments
print(add(b=2, c=2, a=1))           # 2. keyword arguments
print(add(1, 2, c=2))          # 3. pos + key

# add() got multiple values for argument 'b'

#####################

# * ---> packing pos argv  (tuple)
#   ---> unpacking collection (list, tuple, set, . . . )
# ** ---> packing kwargvs
#    ---> unpacking dict

#####################

# 4. *args  ( pack, unpack ) (pos)

def add(*n):  # pack # n = (1, 2, 3, 4, 5), n = (1, 2), n = tuple()
    total = 0
    for i in n:
        total += i
    return total


print(add(1, 2, 3, 4, 5))
print(add(1, 2))
print(add())

l = [1, 1, 1, 100, 100, 200, 200, 200, 300]
total_amount = add(*l) # unpack  # add(1, 1, 1, 100, 100, 200, 200, 200, 300)
print(total_amount)

d = {'a': 1, 'b': 2, 'c': 3, 'item1': 100, 'item2': 200}
print(add(*d.values())) #

print(*l) # unpack
print(1, 1, 1, 100, 100, 200, 200, 200, 300)

#####################

# 5. **kwargs ( pack, unpack ) (kw ) ( dict )

def add(**n): # pack # {'a': 1, 'b': 2, 'c': 3, 'item1': 100, 'item2': 200}
    total = 0
    print(n)
    for i in n.values():
        total += i
    return total

print(add(a=1, b=2, c=3, item1=100, item2=200))


l = {"item1": 500, "item2": 1000, "item3": 3000, "item4": 100}

total = add(item1=500, item2=1000, item3=3000, item4=100)
print(total)

total = add(**l) # upack
print(total)

#####################

def f(a, b, c, *l):
    print(a)
    print(b)
    print(c)
    print(l)

f(1, 2, 3, 4, 2, 3, "apple")   # 6. pos + *args

#####################

def f(a, b, c, **l):
    print(a)
    print(b)
    print(c)
    print(l)

f(d=4, e=5, a=1, g=10, b=2, c=3, name="mg mg")    # 7. kw + **kwargs
f(1, 2, 3, d=4, e=5, g=10, name="mg mg")          # 8. pos + **
f(1, 2, c=3, d=4, e=5, g=10, name="mg mg")          # 9. pos + kw + **

#####################

# 10. pos + * + kw + **
def f(a, b, *l, c, g, **d):
    print(a)
    print(b)
    print(c)
    print(g)
    print(l)
    print(d)

f(1, 2, 3, 4, 5, c=100, name="mg mg", age=20, g=20)

#####################
#####################

4.8. More on Defining Functions
4.8.1. Default Argument Values

Important warning: The default value is evaluated only once.

This makes a difference when the default is a mutable object such as a list, dictionary,
or instances of most classes.

For example, the following function accumulates the arguments passed to it on subsequent calls:

def f(a, L=[]):
    L.append(a) # [1, ]
    return L


print(f(1))  # [1]
print(f(2))  # [1, 2]
print(f(3))  # [1, 2, 3]

#####################

[1]
[1, 2]
[1, 2, 3]

#####################

def f(name, d=dict(), **x):
    d[name] = x
    return d

print(f("user1", age=20, id=12345, password="123456"))
print(f("user2", age=20, id=123456))
print(f("user3", age=20, id=1234567))

#####################

{'user1': {'age': 20, 'id': 12345}}
{'user1': {'age': 20, 'id': 12345}, 'user2': {'age': 20, 'id': 12345}}

#####################

If you don’t want the default to be shared between subsequent calls,
you can write the function like this instead:

# l = [a, b, c]
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

print(f(1)) # f("user1")
print(f(2))
print(f(3))

[1]
[2]
[3]

def f(name, d=None, **x):
    if d == None:
        d = dict()
    d[name] = x
    return d

print(f("user1", age=20, id=12345, password="123456"))
print(f("user2", age=20, id=123456))
print(f("user3", age=20, id=1234567))

{'user1': {'age': 20, 'id': 12345, 'password': '123456'}}
{'user2': {'age': 20, 'id': 123456}}
{'user3': {'age': 20, 'id': 1234567}}

#####################

4.8.2. Keyword Arguments

Functions can also be called using keyword arguments of the form kwarg=value.

When a final formal parameter of the form **name is present,
it receives a dictionary (see Mapping Types — dict) containing all keyword arguments except for those corresponding to a formal parameter.

This may be combined with a formal parameter of the form *name (described in the next subsection)
which receives a tuple containing the positional arguments beyond the formal parameter list.

(*name must occur before **name.)

4.8.3. Special parameters
4.8.3.1. Positional-or-Keyword Arguments   --->   /    *
4.8.3.2. Positional-Only Arguments         --->   p    /        (a, b, c, /)
4.8.3.3. Keyword-Only Arguments            --->   *    p        (*, a, b, c)
4.8.3.4. Function Examples
4.8.3.5. recap အနှစ်ချုပ်                      --->   standard
                                                  p / standard * kw

#####################

# Positional-Only Arguments
def add(a, b, c, /):
    return a + b + c


#positional argument
total = add(1, 2, 3)
print(total)
# keyword argument
#total = add(a=1, c=3, b=2)
print(total)

#####################

# Keyword-Only Arguments
def add(*, a, b, c):
    return a + b + c


#positional argument
#total = add(1, 2, 3)
#print(total)

# keyword argument
total = add(a=1, c=3, b=2)
print(total)

#####################

def info(*, name, age, email, ph):
    pass

info(name="mg mg", ph="0987654", age=20, email="abc@gmail.com")


#####################

# mix / and *
def add(a, b, c, /, d, e, f, *, g, h, i):
    return a + b + c + d + e + f + g + h + i


total = add(1, 1, 1, 1, 1, f=1, g=1, h=1, i=1)
print(total)

#####################

# mix /, *, **

def add(a, b, c, /, d, e, f, *args, g, h, i, **kwargs):
    #print(args)
    #print(kwargs)
    return a + b + c + d + e + f + g + h + i

total = add(1, 1, 1, 1, 1, 2, 2, 2, name="abc", g=1, h=1, i=1, age=30)
print(total)

#total = add(1, 1, 1, 1, e=1, f=2, name="abc", g=1, h=1, i=1, age=30)
#print(total)

###########################

from operator import add
help(add)

add(a=100, b=200)
add(100, 200)
add(100, b=200)

###########################

4.8.4. Arbitrary Argument Lists    --->   * and **
4.8.5. Unpacking Argument Lists    --->   * and **

###########################

from operator import add

qs = [(1, 2), (100, 200), (20, 30)]

for q in qs:
    print(f"adddition of {q} = {add(*q)}")  # unpack

###########################

def add(**kwargs):
    print(kwargs)
    total = 0
    for n in kwargs.values():
        total += n

    return total

qs = [{"first number": 1, "second number": 2, "third number": 3},
      {"first number": 100, "second number": 200, "third number": 300},
      {"first number": 20, "second number": 30, "third number": 3},
      ]

for q in qs:
    print(f"adddition of {q} = {add(**q)}")  # unpack

###########################

4.8.6. Lambda Expressions
int(1)
x = int(1)  # refrence, memory address

def add(a, b, c):  # refrence, memory address
    return a + b + c

x = lambda a, b, c: a + b + c


print(add(1, 2, 3))
print(x(1, 2, 3))

print(add(a=1, b=2, c=2))
print(x(a=1, b=2, c=2))

print(add(1, 2, c=2))
print(x(1, 2, c=2))

###########################

def f1(s):
    print(s.upper())

f2 = lambda s:print(s.upper())

f1("abc")
f2("abc")

###########################

def f1(s):
    return s.upper()

ans = f1("abc")
print(ans)

f2 = lambda s: s.upper()
ans = f2("abc")
print(ans)


###########################
###########################

4.8.7. Documentation Strings
def my_function():
    '''ths is my function.'''

print(my_function.__doc__)

help(my_function)

###########################

4.8.8. Function Annotations မှတ်ချက်
annotations are stored in __annotations__

###########################

def f(x: str, y: str) -> str:
    return f"Hello {x} {y}"

print(f("a", "str"))
print(f.__annotations__)

###########################

def f(x: int, y: int) -> int:
    return x + y

print(f(1, 2.0))

print(add.__annotations__)

###########################
###########################

# need to explain
import sys

def add(x, y):
   return x + y

print(add(int(sys.argv[1]), int((sys.argv[2]))))

###########################

4.9. Coding Style
1. 4 space
2. not exceed 79 characters
3. blank lines
4. comment
5. docstrings
6. space ---> operator ( = )/ comma / colon
7. UpperCamelCase ---> class name
8. lowercase_with_underscores  ---> function, method, variable
9. self  --->   first parameter of method  ( other )
10. UTF-8
11. identifier ---> ASCII

from tkinter import Tk, Button
from operator import add


###########################
###########################


class Kg:

    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        if type(other) is Kg:
            ans = self.weight + other.weight
        elif type(other) is Lb:
            ans = self.weight + (other.weight / 2.2)
        return Kg(ans)

    def __sub__(self, other):
        if type(other) == Kg:
            ans = self.weight - other.weight
        elif type(other) == Lb:
            ans = self.weight - (other.weight / 2.2)
        return Kg(ans)

    def __str__(self):
        return f"{self.weight} kg"


class Lb:

    def __init__(self, weight):
        self.weight = weight

    def __add__(self, other):
        if type(other) is Lb:
            ans = self.weight + other.weight
        elif type(other) is Kg:
            ans = self.weight + (other.weight * 2.2)
        return Lb(ans)

    def __sub__(self, other):
        if type(other) is Lb:
            ans = self.weight - other.weight
        elif type(other) is Kg:
            ans = self.weight - (other.weight * 2.2)
        return Lb(ans)

    def __repr__(self):
        return f"{self.weight} lb"


#  1kg + 2.2lb  ---> 2kg

l = Lb(2.2)
k = Kg(1)
k2 = Kg(2)

print(k + l)

##

print(k + l)
print(l + k)

print(k2 - l)
print(l - k2)

w = [k, k2, l]
print(w)

###########################
###########################

# 6       .
# 5
# 4
# 3       .
# 2
# 1       .
# # # # # # # # # # #
0 1 2 3 4 5 6 7 8 9 10
###########################
5, 3
25, 9

5, 6
3. An Informal Introduction to Python
3.1. Using Python as a Calculator
3.1.1. Numbers
3.1.2. Strings
3.1.3. Lists

3.2. First Steps Towards Programming

4. More Control Flow Tools
4.1. if Statements
4.2. for Statements
4.3. The range() Function
4.4. break and continue Statements, and else Clauses on Loops
4.5. pass Statements
4.6. match Statements

4.7. Defining Functions

4.8. More on Defining Functions
4.8.1. Default Argument Values
4.8.2. Keyword Arguments
4.8.3. Special parameters
4.8.3.1. Positional-or-Keyword Arguments
4.8.3.2. Positional-Only Parameters
4.8.3.3. Keyword-Only Arguments
4.8.3.4. Function Examples
4.8.3.5. Recap

4.8.4. Arbitrary Argument Lists ( tuple )   --->   def print(*args):
4.8.5. Unpacking Argument Lists ( tuple )   --->   l = [1, 2, 3, 4]; print(*l); print(1, 2, 3, 4)
4.8.6. Lambda Expressions
4.8.7. Documentation Strings
4.8.8. Function Annotations    --->    def x(a:int, b:str) -> list:
4.9. Coding Style

5. Data Structures
5.1. More on Lists
5.1.1. Using Lists as Stacks
5.1.2. Using Lists as Queues
5.1.3. List Comprehensions
5.1.4. Nested List Comprehensions

5.2. The del statement
5.3. Tuples and Sequences
5.4. Sets
5.5. Dictionaries
5.6. Looping Techniques
5.7. More on Conditions
5.8. Comparing Sequences and Other Types


6. Modules
6.1. More on Modules
6.1.1. Executing modules as scripts
6.1.2. The Module Search Path
6.1.3. “Compiled” Python files

6.2. Standard Modules
6.3. The dir() Function

6.4. Packages
6.4.1. Importing * From a Package
6.4.2. Intra-package References
6.4.3. Packages in Multiple Directories

7. Input and Output
7.1. Fancier Output Formatting
7.1.1. Formatted String Literals
7.1.2. The String format() Method
7.1.3. Manual String Formatting
7.1.4. Old string formatting

7.2. Reading and Writing Files
7.2.1. Methods of File Objects
7.2.2. Saving structured data with json

8. Errors and Exceptions
8.1. Syntax Errors
8.2. Exceptions
8.3. Handling Exceptions
8.4. Raising Exceptions
8.5. Exception Chaining
8.6. User-defined Exceptions
8.7. Defining Clean-up Actions
8.8. Predefined Clean-up Actions
8.9. Raising and Handling Multiple Unrelated Exceptions
8.10. Enriching Exceptions with Notes

9. Classes
9.1. A Word About Names and Objects
9.2. Python Scopes and Namespaces
9.2.1. Scopes and Namespaces Example

9.3. A First Look at Classes
9.3.1. Class Definition Syntax
9.3.2. Class Objects
9.3.3. Instance Objects
9.3.4. Method Objects
9.3.5. Class and Instance Variables

9.4. Random Remarks

9.5. Inheritance
9.5.1. Multiple Inheritance

9.6. Private Variables
9.7. Odds and Ends
9.8. Iterators
9.9. Generators
9.10. Generator Expressions


"""

"""
###################################

5. list

1. list as stacks ( last_in , first_out ) ( push, pop)
---> append()
---> pop()

l = list()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l)

print(l.pop())
print(l.pop())
print(l.pop())
print(l.pop())
print(l)

###################################

2. list as queues  ( first_in, first_out ) ( enqueue, dequeue)
---> deque from collections
---> popleft()

from collections import deque

l = deque(list())
l.append(1)
l.append(2)
l.append(3)
l.append(4)
print(l)

print(l.popleft())
print(l.popleft())
print(l.popleft())
print(l.popleft())

###################################

3. list comprehensions

l = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 10]]

square = []

for r in l:
    for i in r:
        if i % 2 == 0: square.append(i ** 2)

print(square)

lcsquare = [i ** 2 for r in l for i in r if i % 2 == 0]  # [4, 16, 36, 64, 100]
print(lcsquare)

l2 = []

for r in l:
    for i in r:
        if i % 2 == 0:
            i **= 2
        l2.append(i)

print(l2)

lcl2 = [i ** 2 if i % 2 == 0 else i for r in l for i in r]
print(lcl2)


###################################

s = [i ** 2 for r in l for i in r if i % 2 == 0]
print(s)

###################################

5.1.4. Nested List Comprehensions

3 x 2

 1   2
 3   4
 5   6

2 x 3

 1   3   5
 2   4   6


The transpose AT of a matrix A can be obtained by reflecting the elements along its main diagonal.
Repeating the process on the transposed matrix returns the elements to their original position.

The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.

# m[l, l, l]
m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

[[1, 5, 9],
 [2, 6, 10],
 [3, 7, 11],
 [4, 8, 12]]

###################################

# step .1
# print(m[1][3])


###################################

mt = []

# step.2
row_t0 = []
for row in m:
    row_t0.append(row[0])
    print(row_t0)

mt.append(row_t0)
print(mt)


row_t0 = []
for row in m:
    row_t0.append(row[1])
    print(row_t0)

mt.append(row_t0)
print(mt)

row_t0 = []
for row in m:
    row_t0.append(row[2])
    print(row_t0)

mt.append(row_t0)
print(mt)


row_t0 = []
for row in m:
    row_t0.append(row[3])
    print(row_t0)

mt.append(row_t0)
print(mt)

###################################

m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

[[1, 5, 9],
 [2, 6, 10],
 [3, 7, 11],
 [4, 8, 12]]

c = range(len(m[0]))  # 0, 1, 2, 3
print(list(c))

# step.3
mt = []
for col in c:
    row_t = []
    for row in m:
        row_t.append(row[col])
    mt.append(row_t)

print(m)
print(mt)

###################################

# step.4
lc_mt = [[row[col] for row in m] for col in range(len(m[0]))]
print(lc_mt)

###################################

mt = []
for col in range(len(m[0])):
    for row in m:
        mt.append(row[col])

lc = [row[col] for col in range(len(m[0])) for row in m]
print(lc)

###################################

m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

def transport_matrix(m):
    mt = []
    for col in range(len(m[0])):
        row_t = []
        for row in m:
            row_t.append(row[col])
        mt.append(row_t)
    return mt

t = transport_matrix(m)
print(m)
print(t)
print(transport_matrix(t))

###################################

m = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9, 10, 11, 12]]

def transport_matrix(m):
    return [[row[col] for row in m] for col in range(len(m[0]))]

t = transport_matrix(m)
print(m)
print(t)
print(transport_matrix(t))

###################################

def transport_matrix(m):
    '''
    :param matrix:
    :return: transport matrix

     The transpose AT of a matrix A can be obtained by reflecting the elements along its main diagonal.
     Repeating the process on the transposed matrix returns the elements to their original position.

     The transpose of a matrix was introduced in 1858 by the British mathematician Arthur Cayley.
    '''

    mt = []
    for i in range(len(m[0])):
        row_t = []
        for row in m:
            row_t.append(row[i])
        mt.append(row_t)
    return mt

# help(transport_matrix)

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mt = transport_matrix(m)
print(mt)
print(transport_matrix(mt))

###################################

def transport_matrix(m):
    mt = [[row[i] for row in m] for i in range(len(m[0]))]
    return mt

#help(transport_matrix)

m = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
mt = transport_matrix(m)
print(mt)
print(transport_matrix(mt))

###################################

5.3. Tuples and Sequences
5.4. Sets
5.5. Dictionaries
5.6. Looping Techniques
5.7. More on Conditions
5.8. Comparing Sequences and Other Types

sequence type     ---> list, tuple, range
list      --->   homogeneous sequence of element 
tuple     --->   heterogeneous sequence of element
range     --->   sequence of number

fruits = ["apple", "banana", "orange"]
user1 = ("Mg Mg", "Mycisco1", "09954433460", 21, 0.9)

###############################

5.3. Tuples and Sequences

1. tuple can create with mutable obj

# 1   ---> 001
# 2   ---> 002
# 3   ---> 003

# [1, 2, 3]  ---> 0010  --> [001, 002, 003, a8]

# 4   ---> 004
# 5   ---> 005
# 6   ---> 006

# [4, 5, 6]  --->  0020  --> [004, 005, 006]

# (l , l)    --->  0030  --> (0010, 0020)

# apple      --->  a1

v = ([1, 2, 3],
     [4, 5, 6])

v[0].clear()
print(v)

2. multiple assignment is a combination of tuple packing and sequence unpacking.

# tuple packing
t = 12345, 54321, 'hello!'
print(t)

# sequence unpacking
print(*t)
print(12345, 54321, 'hello!')

x, y, z = t
print(x, y, z)

# multiple assignment
x, y, z = 12345, 54321, 'hello!'

print(x, y, z)

# swap

cup1 = "coffee"
cup2 = "tea"
print(cup1, cup2)

cup_empty = cup1  # coffee
cup1 = cup2  # tea
cup2 = cup_empty

print(cup1, cup2)

cup1 = "coffee"
cup2 = "tea"
print(cup1, cup2)
cup1, cup2 = cup2, cup1
print(cup1, cup2)

#################################

5.4. Sets
1. unique value
2. -, |, &, ^
3. set comprehension

l = [1, 2, 3, 2, 1, 3, 5, "apple", "banana", "apple", "banana"]
a = set(l)  # {1, 2, 3, 5, 'apple', 'banana'}
l2 = list(a)  # [1, 2, 3, 5, 'apple', 'banana']
print(l)
print(l2)

l = [1, 2, 3, 2, 1, 3, 5, "apple", "banana", "apple", "banana"]
l = list(set(l))
print(l)

def r_d(d_l):
    u_l = []
    for i in d_l:
        if i not in u_l:
            u_l.append(i)
    return u_l

l = [1, 2, 3, 2, 1, 3, 5, "apple", "banana", "apple", "banana"]
u = r_d(l)
print(u)

# -, |, &, ^

a = set('abcdef')
b = set('abcijk')

print(a - b)                              # letters in a but not in b
#{'d', 'e', 'f'}

print(a | b)                              # letters in a or b or both
#abcdefijk

print(a & b)                              # letters in both a and b
#a b c

print(a ^ b)                              # letters in a or b but not both
# d e f i j k


Similarly to list comprehensions, set comprehensions are also supported.

a = set()
for i in 'abracadabra':
    if i not in "abc":
        a.add(i)
print(a)

a = {i for i in 'abracadabra' if i not in "abc"}
print(a)

#{'r', 'd'}

################################

5.5. Dictionaries
1. dict to list ---> key list, value list, k & v list  --->  list(), sorted()
2. dict()       ---> identifier/ variable rule
3. list to dict
4. dict comprehension

d = { 
         222 : "banana",
         111 : "apple",
}

# key to list
print(list(d))
print(sorted(d))

print(list(d.keys()))
print(sorted(d.keys()))

# values to list
print(list(d.values()))
print(sorted(d.values()))

print(list(d.items()))
print(sorted(d.items()))

# dict()
# d = dict(222="banana", 111="apple")  # identifier rule
d = dict(mama=222, MgMg=111)
print(d)

# list to dict
l = [(222, "ma ma"), (111, "Mg Mg")]
d = dict(l)

print(l)
print(d)

print(list(d.items()))

d = dict()
for i in range(1, 101):
    d[i] = i ** 2
print(d)

# d comprehension
d = {i: i ** 2 for i in range(1, 101)}
print(d)

##############################

5.6. Looping Techniques

# enumerate([]) ---> position index and corresponding value
# index, value
# can choose index value or another value

# zip([], [])  ---> pair values of two or more sequences
# two or more values

# reversed   ---> sequence in reverse
# sorted     ---> sequence in sorted order


d = {"name": "Mg Mg", "age": 20}
s = {1, "apple", 2} # non sequence
l = ["Mg Mg", "Ma Ma", "Hla Hla"]


for t in enumerate(l): # i, v = (count, value)
    print(t)
    i, v = t
    print(f"index of {v} = {i}")


for i, v in enumerate(l): # i, v = (count, value)
    print(i, v)


l1 = [1, 2]
l2 = ["name", "age"]
l3 = ["Mg Mg", 18]

for a, b, c in zip(l1, l2, l3):
    print(a, b, c)


l = [6, 5, 4, 3, 2, 1, 5, 8, 9]
for i in sorted(l, reverse=True):
    print(i)

################################

5.7. More on Conditions


x, y, z = "", "apple", 2

#print(x or y or z) # first true argument # lastest argument
print(x and y and z)# first false argument # lastest argument

"""

"""
5.8. Comparing Sequences and Other Types


('_abc', '_ast', '_bisect', '_blake2', '_codecs', '_codecs_cn', '_codecs_hk', '_codecs_iso2022', '_codecs_jp', '_codecs_kr', 
 '_codecs_tw', '_collections', '_contextvars', '_csv', '_datetime', '_functools', '_heapq', '_imp', '_io', '_json', '_locale', 
 '_lsprof', '_md5', '_multibytecodec', '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha256', '_sha3', 
 '_sha512', '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable', '_thread', '_tracemalloc', 
 '_warnings', '_weakref', '_winapi', '_xxsubinterpreters', 'array', 'atexit', 'audioop', 'binascii', 'builtins', 'cmath', 
 'errno', 'faulthandler', 'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys', 'time', 'winreg', 
 'xxsubtype', 'zlib')

import sys
print(sys.builtin_module_names)

import f
from f import n, n 
* for all
as 

"""

"""

import module_test
print(module_test.add(1, 2))

"""
# help("modules")
# help("tkinter")


# from m import add
# from m import pi
# from math import pi as p
# print(p)
"""
import sys
l = ["a", "b", "c"]
sys.path.append("C:\\Users\\User\\PycharmProjects\\")
sys.path += l
for i in sys.path:
    print(i)


password_list = ["123", "456"]
for i in range(3):
    try:
        p = input("Enter password :")
        if p in password_list:
            print("correct password and open door.")
            break
        else:
            raise Exception("incorrect password")
    except:
        pass

else:
    print("You tried many times. ")

################################

"""