# Passing a function as an argument

def greet ():
    return "Hello"
def call_function(func):
    return func

print(call_function(greet()))

# A simple decorator that logs function calls

def log_decorator(function):
    def wrapper():
        print(f"Calling function, {function. __name__}")
        return function()
    return wrapper

@log_decorator
def say_hello():
    print("Hello")

say_hello()

# Another example

def my_decorator(func):
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def say_hi():
    print("Hi!")

say_hi()

# Now Multiple decorator usage

import time

def log(function):
    def inner(patient_name):
        print(f"Recording patient details: {patient_name}")
        return function(patient_name)
    return inner

def timer(function):
    def second_inner(patient_name):
        start = time.time()
        result = function(patient_name)
        end = time.time()
        print (f"consultation time: {end- start: .4f}seconds")
        return result
    return second_inner

@log
@timer
def doctor_consultation(patient_name):
    print(f"doctor is consulting {patient_name}....")
    time.sleep(1)
    print(f"Prescription given to {patient_name}")

doctor_consultation("Usama")

