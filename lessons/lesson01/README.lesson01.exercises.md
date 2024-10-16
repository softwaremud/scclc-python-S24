# Python Calculations and Variables Lesson
=====================================

In this lesson, we will explore basic concepts such as variables, data
types, and calculations.

### Learning Objectives

* Understand what variables are in Python
* Learn about different data types in Python (integers, floats, strings)
* Practice performing calculations with Python (addition, subtraction,
  multiplication, division)

### Variables and Data Types

In Python, a variable is a name given to a value. This allows us to store and reuse
values throughout our code. We can assign a value to a variable using the assignment
operator (=).

```python
x = 5  # assigns the integer value 5 to x
```

Here are some basic data types in Python:

* **Integers**: whole numbers, e.g., 1, 2, 3
* **Floats**: decimal numbers, e.g., 3.14, -0.5
* **Strings**: sequences of characters, e.g., "hello", 'goodbye'

### Calculations

Python supports basic arithmetic operations:

* **Addition** (+)
* **Subtraction** (-)
* **Multiplication** (\*)
* **Division** (/)

```python
x = 4
y = 2
result = x + y  # results in 6
```

### Exercises

Try these exercises to practice your new skills!

#### Exercise 1: Assign a value to a variable
```python
name = "John"  # assign the string "John" to name
print(name)    # print the value of name
```
#### Exercise 2: Perform addition
```python
x = 5
y = 3
result = x + y  # results in 8
print(result)
```

#### Exercise 3: Subtract two numbers
```python
z = 7
w = 4
result = z - w  # results in 3
print(result)
```

#### Exercise 4: Multiply two integers
```python
a = 6
b = 9
result = a * b  # results in 54
print(result)
```

#### Exercise 5: Divide two numbers
```python
c = 12
d = 3
result = c / d  # results in 4.0
print(result)
```

#### Exercise 6: Calculate the average of three numbers
```python
num1 = 10
num2 = 20
num3 = 30
average = (num1 + num2 + num3) / 3  # results in 20.0
print(average)
```

#### Exercise 7: Find the largest of three integers
```python
p = 5
q = 10
r = 8
max_num = max(p, q, r)  # results in 10
print(max_num)
```

#### Exercise 8: Print a string multiple times
```python
greeting = "Hello, "
name = "Alice!"
print(greeting * 3 + name)  # prints "Hello, Hello, Hello, Alice!"
```

#### Exercise 9: Convert an integer to a float and back to an integer
```python
num = 5
float_num = float(num)
result = int(float_num)  # results in 5
print(result)
```

#### Exercise 10: Use variables to store and print different types of data (int,
float, string)
```python
age = 25
height = 175.0
name = "Sam"
print("My name is:", name)
print("I am", age, "years old.")
print("I am", height, "cm tall.")
```

### Conclusion

Congratulations! You have completed the Python Calculations and Variables lesson.
Practice these exercises to solidify your understanding of basic concepts in Python
programming.

Feel free to ask me if you need any clarification or help with these exercises.
Happy coding!

### Bonus Challenge #1

Here is some code for how we can "add" two strings together.

```python
str1 = 'foo'
str2 = 'baz'
str3 = 'bar'
my_str = str1 + str2
print(my_str)
print(my_str * 2)
```

Can you modify this so that we print out "foofoobazfoofoobazbar"?

Try to do this with using:
* as many variables as you like
* as FEW "+" operations as you can


### Bonus Challenge #2

Create a program that uses a variable to create a customized greeting.  Make sure your code is school appropriate!
(No bad language, no insults, no bathroom talk...)

My example with print out "my favorite pet is a cat"

Your challenge is to create a similar structure where we print out:
but we use only 3 variables and 2 print statements

"Bob is my name.  I like tuna"

"Jane is my name.  I like cherries"

```python
fav_pet = "cat"
sentence = "my favorite pet is a " 
print(sentence + fav_pet)
```


### Bonus Challenge #3

Create a mini mad-libs program using the same structure as Challenge #2
Include:
* 4 sentences
* 3 verbs
* 3 nouns
* As many variables as you like


