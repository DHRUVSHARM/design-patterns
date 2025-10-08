import time

# like a hoc function returns a function, as a wrapper of sorts 
def time_it(func):
  def wrapper():
    start = time.time()
    result = func()
    end = time.time()
    print(f'{func.__name__} took {int((end-start)*1000)}ms')
  return wrapper

@time_it
def some_op():
  print('Starting op')
  time.sleep(1) # some work simulation
  print('We are done')
  return 123

if __name__ == '__main__':
  # some_op() basic call
  # time_it(some_op)() call wrapper passing function in it 
  some_op() # makes use of the @ syntax decorator , functional useful for initialization, termination, storing values, diagnostics etc;