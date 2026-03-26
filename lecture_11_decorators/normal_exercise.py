def log_decorator(function):

    def innerfunction_or_wrapper():
        print("Start")
        return function()
    return innerfunction_or_wrapper

@log_decorator
def greeting():
    print("Hello")


greeting()