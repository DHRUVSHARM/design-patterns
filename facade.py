# buffer class can be though of as the raw source data where we have low level operations to hide from the user
class Buffer:
  def __init__(self, width=30, height=20):
    self.width = width
    self.height = height
    self.buffer = [' '] * (width*height)

  # allows indexing of the buffer object giving index access or slicing, internally we use out flat list
  def __getitem__(self, item):
    return self.buffer.__getitem__(item)

  """
  python way to add each character separately at the end of the list 
  a = [1, 2]
  a += [3, 4]   # → [1, 2, 3, 4]
  a += (5, 6)   # → [1, 2, 3, 4, 5, 6]
  a += 'ab'     # → [1, 2, 3, 4, 5, 6, 'a', 'b']
  """
  def write(self, text):
    self.buffer += text

# the viewport class can act as the view which basically helps users interact with underlying data (the buffer / memory) content above
class Viewport:
  def __init__(self, buffer=Buffer()):
    self.buffer = buffer
    self.offset = 0

  def get_char_at(self, index):
    return self.buffer[self.offset+index]

  # the view provides a similar functionality
  def append(self, text):
    self.buffer += text

# at the console level we have a buffer and can have many viewports and buffers, the console helps for a selected 
# viewport perform functionality on underlying bufferm hiding complexity for end user
class Console:
  def __init__(self):
    b = Buffer()
    self.current_viewport = Viewport(b)
    self.buffers = [b]
    self.viewports = [self.current_viewport]

  # high-level
  def write(self, text):
    self.current_viewport.buffer.write(text)

  # low-level
  def get_char_at(self, index):
    return self.current_viewport.get_char_at(index)


if __name__ == '__main__':
  c = Console()
  c.write('hello')
  ch = c.get_char_at(0)