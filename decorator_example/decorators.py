# simple decorator

def make_it_hot(fn):

    def wrapper(*args , **kwargs):
        print(f"making it hot for {args[0]}")
        return fn(*args , **kwargs) 

    return wrapper

# at definition time, make_coffee = make_it_hot(fn # which is make_coffee)
# later make_coffee('frappe') call refers to whatever we got, the wrapper basically called with the arg in this case 
@make_it_hot
def make_coffee(coffee):
    print(f"making coffee .... {coffee}")

def simple_decorator():
    make_coffee('frappe')


def get_sugar(fn):

    def wrapper(*args , **kwargs):
        print(f"getting sugar for {args[0]}")
        return fn(*args , **kwargs) 
        
    
    return wrapper

def get_beans(fn):

    def wrapper(*args , **kwargs):
        print(f"getting beans for {args[0]}")
        return fn(*args , **kwargs) 
    
    return wrapper


# basically while building the code 
# we can think stuff goes from bottom to up
# and also here serve_cofee -> get beans(serve coffee fn with args) -> wrapper(same args){body : print + return sevecoffe(with args) call }
# will serve as fn for next upper level then 
# ultimately it will be called in reverse order then 


# basically while building (defining) the code:
# decorators are applied bottom → top.
#
# so here:
# serve_coffee → get_beans(serve_coffee)
#     → returns wrapper(name): prints + calls serve_coffee(name)
# that wrapper becomes the 'fn' for get_sugar,
# whose wrapper again becomes 'fn' for make_it_hot.
#
# at runtime (when called), execution happens in the reverse order:
# make_it_hot → get_sugar → get_beans → serve_coffee
@get_sugar
@get_beans
def serve_coffee(name):
    print(f"serving coffee for {name}")

# here we will try to do an example with multiple decorators
def multiple_simple_decorator():
    
    # these are executed bottom to top while definitions are read wrapper from get_beans propagates up as the fn for get_sugar
    # obviously when we call the 
    serve_coffee('Dhruv')


def make_it_hot(level):
    def decorator(fn):
        def wrapper(*args , **kwargs):
            print(f"heating with level : {level} for {args[0]}")
            return fn(*args , **kwargs)
        return wrapper
    return decorator

@make_it_hot(level = 100)
def make_coffee_level(name):
    print(f"made coffee for {name}")


def decorator_factory():
    make_coffee_level('Dhruv')

if __name__ == '__main__':
    # print("\n----------------------------------------------------\n")
    print("one")
    simple_decorator()
    print("\n----------------------------------------------------\n")
    print("two")
    multiple_simple_decorator()
    print("\n----------------------------------------------------\n")
    print("three")
    decorator_factory()
    print("\n----------------------------------------------------\n")
