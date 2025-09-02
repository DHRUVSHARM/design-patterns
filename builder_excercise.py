"""

Builder Coding Exercise
You are asked to implement the Builder design pattern for rendering simple chunks of code.

Sample use of the builder you are asked to create:

cb = CodeBuilder('Person').add_field('name', '""') \
                          .add_field('age', '0')
print(cb)
The expected output of the above code is:

class Person:
  def __init__(self):
    self.name = ""
    self.age = 0
Please observe the same placement of spaces and indentation.
"""

"""
Error details
'class Person:\n  def __init__(self):\n   self.name = ""\n   self.age = 0' != 'class Person:\n  def __init__(self):\n    self.name = ""\n    self.age = 0'
  class Person:
    def __init__(self):
-    self.name = ""
+     self.name = ""
? +
-    self.age = 0+     self.age = 0? +


"""

"""
'class Foo:\n  def __init__(self):' != 'class Foo:\n  pass'
  class Foo:
-   def __init__(self):+   pass
"""


"""
'class Person:\n  def __init__(self):\n   self.name = ""\n   self.age = 0' != 'class Person:\n  def __init__(self):\n    self.name = ""\n    self.age = 0'
  class Person:
    def __init__(self):
-    self.name = ""
+     self.name = ""
? +
-    self.age = 0+     self.age = 0? +
"""



class ClassProperty:
    indent = 4

    def __init__(self , type, name):
        self.type = type
        self.name = name

    def __str__(self):
        indent_str = ClassProperty.indent * " " 
        return f"\n{indent_str}self.{self.type} = {self.name}"


class ClassPlaceholder:
    indent  = 2

    def __init__(self):
        pass

    def __str__(self):
        indent_str = ClassPlaceholder.indent * " "
        return f"\n{indent_str}pass"


class ClassInit:
    indent = 2

    def __init__(self):
       # these are the fields here , with the placeholder data in the beginning
       self.children = []

    def __str__(self):
        indent_str = ClassInit.indent * " "         
        self.__repr =  f"\n{indent_str}def __init__(self):"
        for child in self.children:
            self.__repr += str(child)
        return self.__repr

class ClassRoot:
    indent = 1

    def __init__(self , classname):
        self.classname = str(classname)
        # for now this will be a single child enforced 
        self.init_child = ClassPlaceholder()

    def __str__(self):
        indent_str = ClassRoot.indent * " " 
        return f"{indent_str}class {self.classname}:{self.init_child}"

class CodeBuilder:
    def __init__(self, root_name):
        self.__root = ClassRoot(root_name)

    def add_field(self, type, name):
        if isinstance(self.__root.init_child , ClassPlaceholder):
            self.__root.init_child = ClassInit()
        self.__root.init_child.children.append(ClassProperty(type , name))
        return self

    def __str__(self):
        return f"{self.__root}"


cb = CodeBuilder('Person').add_field('name' , 'Dhruv')
print(cb)