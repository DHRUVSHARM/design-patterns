# idea here is to make the decorator have access to the underlying object and provide methods so as to
# add functionalit to them
class FileWithLogging:
  def __init__(self, file):
    self.file = file

  # as an example this is the only part of the code that we are adding stuff to 
  def writelines(self, strings):
    self.file.writelines(strings)
    print(f'wrote {len(strings)} lines')

  # the iter, next will be over the file we have
  def __iter__(self):
    return self.file.__iter__()

  def __next__(self):
    return self.file.__next__()

  # getter and setters though will have to be 
  # refirected to the file object that we have  
  # PROXIED 
  # extra calls can have performance penalty
  def __getattr__(self, item):
    return getattr(self.__dict__['file'], item)

  def __setattr__(self, key, value):
    if key == 'file':
      self.__dict__[key] = value
    else:
      setattr(self.__dict__['file'], key)

  def __delattr__(self, item):
    delattr(self.__dict__['file'], item)


if __name__ == '__main__':
  file = FileWithLogging(open('hello.txt', 'w'))
  file.writelines(['hello', 'world'])
  file.write('testing')
  file.close()
