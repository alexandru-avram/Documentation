# Functional Programming

## [If Statements](https://github.com/alexandruavram-rusu/Python_Documentation/blob/main/07.%20If%20Statements/If%20Statements.ipynb)
    If some_condition:
        execute code
    Elif another_condition:
         execute another code
     Else:
        do something else

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: if, if statements, elif, else

## Loops

### [Loops](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Loops/Loops.ipynb)
    for Loops
        for item in object:
            execute something
A for loop goes through items that are iterable (including strings, numbers, lists, dictionaries, variables).

    while Loops
        while condition:
            execute something

A while loop will repeatedly execute a single or more statements as long as the condition is true.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: loops, for loop, while loop, nested loops, working with loops

### [Break, Continue, Pass](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Loops/Break%2C%20Continue%2C%20Pass.ipynb)
break: Breaks out of the current closest enclosing loop.\
continue: Goes to the top of the closest enclosing loop.\
pass: Does nothing at all.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: break, continue, pass

## Functions

### [Functions](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Functions/Functions.ipynb)
Functions are statements or group of statements that can be used more than once, avoiding the need to write the same code more than once. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: creating functions, def, return, if functions, loop functions, interactions between functions, `*args`, `**kwargs`


### [Decorators](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Functions/Decorators.ipynb)
Decorators are a more advanced Python topic related to functions. They allow the user to decorate a function, adding extra functionality to an already existing function.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: decorators, locals, globals, scope, creating decorators

### [Generators](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Functions/Generators.ipynb)
Generators are functions that allow us to write a function that can send back a value and later resume to pick up were it left off. The basic idea is that they allow us to generate a sequnce of value over time.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: using generators, yield, next, iter

### [Code Timing](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Functions/Code%20Timing.ipynb)
Sometimes, you might need to time how long does it take for your code to run. Either because you are running scripts for a process, or you might need to uncover which part of your code is slowing your project down. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: timing code, code timing, start, stop, timeit module

## Classes

### [Classes and Objects](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Classes/Classes%20and%20Objects.ipynb)
    class NameOfClass():
        class attributes = something

        def __init__(self, var1, var2):
            self.var1 = var1
            self.var2 = var 2

        def method(self):
            function

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: classes, oop, objects, init, class object attributes, class methods, inheritance, polymorphism, `super()`

### [Magic Methods](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Classes/Magic%20Methods.ipynb)
Magic methods, also known as special or dunders are methods which have double underscores at the beginning and end of their same, as as with init. They are used to add functionality that can't be represented as a normal method.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: special metohds, magic methods

## Working with Files

### [Working with Files](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Working%20with%20Files/01.%20Working%20with%20Files.ipynb)
Basic Python has a built-in open function that allows us to open, read and write basic file types (like .txt files). Some file types might require the installation of a certain library or module.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: writing a file, opening a file, reading a file, closing a file, appending, alternative file methods, closing files

### [CSV Files](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Working%20with%20Files/02.%20Working%20with%20CSVs.ipynb)
Using the built-in Python `csv` module without using `pandas`. 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: reading CSV files, encoding, writing CSV files

### [Working with PDFs](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Working%20with%20Files/03.%20Working%20with%20PDFs.ipynb)
There are many libraries in Python for working with PDFs, each with their pros and cons, the most common one being `PyPDF2`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: reading PDF, adding to PDF, grabbing all the text, full text, full pdf text

### [Working with Images](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Working%20with%20Files/Images/Working%20with%20Images.ipynb)
The Python Imaging Library (PIL) is a 3rd party Python package that adds image processing capabilities to your Python interpreter. It allows you to process photos and do many common image file manipulations.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: opening images, cropping images, copy/paste images, resize images, rotate images, saving images

## Error Handling

### [Exception Handling](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Error%20Handling/Exceptions%20Handling.ipynb)
One of the biggest headache when coding learning how to code is encountering an error message. They appear when something goes wrong, either due to incorrect code or input, causing the program to stop. In Python, these are caused either by a syntax error or an exception.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: errors, exceptions, debugging, synthax errors, raising exceptions, try, except, finally

### [pdb Module](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Error%20Handling/pdb%20Module%20(Debugger).ipynb)
`pdb` is a built-in Python debugger module, allowing the implementation of an interactive debugging environment. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: pdb, debugging, set_trace

### [Getpass Module](https://github.com/alexandruavram-rusu/Documentation/blob/main/Python/02.%20Functional%20Programming/Error%20Handling/Getpass%20Module.ipynb)
The `getpass` module provides a secure way to handle the password prompts where programs interact with the users via the terminal.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**tags**: getpass, getuser, passowrd, secure password input
