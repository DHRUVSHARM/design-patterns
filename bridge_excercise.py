from abc import ABC

"""
Bridge Coding Exercise
You are given an example of an inheritance hierarchy which results in Cartesian-product duplication.

Please refactor this hierarchy, giving the base class Shape  a constructor that takes an interface Renderer  defined as

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None
as well as VectorRenderer  and RasterRenderer  classes. 
Each inheritor of the Shape  abstract class should have a 
constructor that takes a Renderer  such that, subsequently, each constructed object's __str__()  operates correctly, for example,

str(Triangle(RasterRenderer()) # returns "Drawing Triangle as pixels" 
"""


# class Shape:
#     def __init__(self):
#         self.name = None
#
#
# class Triangle(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Triangle'
#
#
# class Square(Shape):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Square'
#
#
# class VectorSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as lines'
#
#
# class RasterSquare(Square):
#     def __str__(self):
#         return f'Drawing {self.name} as pixels'

# imagine VectorTriangle and RasterTriangle are here too

class Renderer(ABC):
    @property
    def what_to_render_as(self):
        return None


class VectorRenderer(Renderer):
    
    def __init__(self):
        self.render_method = "lines"
    
    @property
    def what_to_render_as(self):
        return self.render_method


class RasterRenderer(Renderer):

    def __init__(self):
        self.render_method = "pixels"

    @property
    def what_to_render_as(self):
        return self.render_method


# bridge
class Shape():
    def __init__(self , renderer):
        # print("setting the renderer ...")
        self.renderer = renderer

class Triangle(Shape):
    def __init__(self , renderer):
        super().__init__(renderer)
        # print("now making the triangle")
        self.name = "Triangle"
    
    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"

class Square(Shape):
    def __init__(self , renderer):
        super().__init__(renderer)
        self.name = "Square"
    
    def __str__(self):
        return f"Drawing {self.name} as {self.renderer.what_to_render_as}"

tr = Triangle(VectorRenderer())
print(str(tr))
print(str(Triangle(RasterRenderer())))
# TODO: reimplement Shape, Square, Triangle and Renderer/VectorRenderer/RasterRenderer