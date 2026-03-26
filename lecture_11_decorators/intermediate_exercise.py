def log_decorator(function):

    has_run = False
    def wrapper():
        nonlocal has_run
        if not has_run:
            has_run = True
            return function()
        else:
            print("Already ran once")
    return wrapper

@log_decorator         
def greeting():         
    print("Hello!")

greeting()
greeting()
greeting()
greeting()
greeting()
greeting()
greeting()