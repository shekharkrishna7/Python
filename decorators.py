def my_decorator(func):
    print("------------------")
    print("Starting Decorator")
    print("------------------")


    def greet():
        print("Start")
        func() 
        print("End")
    return greet

0
@my_decorator
def my_function():
    print("This is function on which decorator is applied")

my_function()