## Testing Units

*Requirements*

Write a unit test suite for each of two different Python programs. 

* For the first test suite, use  this Python program: circle.py Download circle.py. Write a basic test suite consisting of at least 7 distinct test cases.
A test case is something like 'test set_radius' and each test case will have a number of assertions.
 

* For the second test suite, find a suitable Python program for which you can write the required number of test cases. A suitable program will include a set of functions or methods that include sufficient inputs and outputs (parameters and return values).

    * The program you choose to test may be created by you, or it may be created by someone else. Give credit to either yourself or the original creator of the program using a comment at the top of the program source file(s).
    * Write a test suite consisting of 30 or more distinct test cases.
    * It is not required to test the entire program that you choose. Instead, intentionally focus your test cases on one or more specific components of the larger program.
 

* Each test case should test a specific aspect of a specific unit of the program. Each test case should consist of 1-5 assertions. Use a variety of different types of assertions throughout your test cases.

*Commentary*

This assignment asks the students to look at some python code, and write unit tests for 
each unit in the code. circle.py and calc.py are examples. calc.py is usually used in the lecture
to show how to do it. Even though the functions are very simple and straightforward, there are a number
of test cases that need to be visited. Divide is an especially good one because it has a case that causes divide
by 0 error. Note that you can have successful unit tests and still have buggy code. 

*Code Coverage*

Its also a good idea to use the code coverage tool to ensure that all the code has been tested.
pip install coverage

you use coverage run `<your test program>` to run it. Then you use coverage html to produce a report
that you open using the finder.



