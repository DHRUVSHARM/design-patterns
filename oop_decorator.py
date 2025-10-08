from abc import ABC
# different from the built in functional implementation, these are class based abstract implementation
# here the idea would be to add to the class implementations

class Shape(ABC):
    # simple abstract class
    
    def __init__(self):
        # will help collection
        # this is the correct way to track / aggregate properties across applications
        # we can handle the reapplication many times that may be forced by not applying at the level of the decorator itself
        self.applied_properties = {}

    def __str__(self):
        return ''
    
    


# concrete implementations
# burden of other functionalities / permissions, lies on the concrete classes 
#############################################
class Circle(Shape):
    def __init__(self, radius=0.0):
        super().__init__()
        self.radius = radius
        

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius} '


class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def __str__(self):
        return f'A square with side {self.side}'
##################################################


# these are the decorators which we will apply 
# note these apply to the shape
class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise Exception('Cannot apply ColoredDecorator twice')
        self.shape = shape
        self.color = color
        self.applied_properties = self.shape.applied_properties

        if "color" not in self.applied_properties:
            self.applied_properties["color"] = None
        self.applied_properties["color"] = self.color

    def __str__(self):
        return f'{self.shape} has the color {self.color}'

    def get_color(self):
        return self.color

class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency
        self.applied_properties = self.shape.applied_properties

        if "transparency" not in self.applied_properties:
            self.applied_properties["transparency"] = None
        self.applied_properties["transparency"] = self.transparency
        

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100.0}% transparency'

    def get_color(self):
        return self.color
    
class DisplayProperties(Shape):
    def __init__(self , shape):
        self.shape = shape
        self.properties = []
        if hasattr(self.shape , "color"):
            self.color = self.shape.color
            self.properties.append(self.color)
        if hasattr(self.shape , "transparency"):
            self.transparency = self.shape.transparency
            self.properties.append(self.transparency)
        self.applied_properties = self.shape.applied_properties

    def __str__(self):
        return f"collected properties : {self.properties}"


class DisplayPropertiesApplied(Shape):
    def __init__(self , shape):
        self.shape = shape
        self.properties = self.shape.applied_properties
        self.applied_properties = self.shape.applied_properties
        
    def __str__(self):
        return f"collected Applied properties : {self.applied_properties}"

if __name__ == '__main__':
    circle = Circle(2)
    print(circle)

    # advantage is we do not need to go into circle or square to add anything
    red_circle = ColoredShape(circle, "red")
    print(red_circle)

    # ColoredShape doesn't have resize() since it is a shape level thing and decorator is generic in comparision
    # red_circle.resize(3)

    red_half_transparent_square = TransparentShape(red_circle, 0.5)
    print(red_half_transparent_square)

    # nothing prevents double application
    # mixed = ColoredShape(ColoredShape(Circle(3), 'red'), 'blue')
    # print(mixed)

    # something else to note is that somethin like this is much more difficult to catch or prevent
    mixed_alternate = ColoredShape(TransparentShape(Circle(3), 0.5), 'blue')
    print(mixed_alternate)
    print(f"{mixed_alternate.get_color()}")


    # a different ordering
    mixed_alternate1 = TransparentShape( ColoredShape( Circle(3) , "yellow" ), 0.5)
    print(mixed_alternate1)

    # issue is here we will not get the color since the last decorator decides
    # so we will get error here
    # print(mixed_alternate1.get_color())

    # we can have some decorator that would take note of all the state informational data or atleast what we want for display purposes,
    # maybe can be used optionally for some state transfer later
    # again this does not work , since we cannot track changes inter decorator application
    mixed_alternate1_display = DisplayProperties(TransparentShape( ColoredShape( Circle(3) , "yellow" ), 0.5))
    print(mixed_alternate1_display)
    
    # so finally we apply it on shape
    # EVERY TYPE OF SHAPE WILL HAVE THE PROPERTY AGGREGATOR, SO REFERENCING IN THE DECORATOR IS SIMPLE
    print("###############       FINAL PROPERTIES DISPLAYED      ##################")
    mixed_alternate2_display = DisplayProperties(TransparentShape( ColoredShape( Circle(3) , "yellow" ), 0.5))
    # will give last applied property only
    print(mixed_alternate2_display)
    
    # gives all in transition , note we need some plumbing to keep moving from state to state
    mixed_alternate3_display = DisplayPropertiesApplied(DisplayProperties(TransparentShape( ColoredShape( Circle(3) , "yellow" ), 0.5)))
    print(mixed_alternate3_display)

    # another ex
    mixed_alternate4_display = DisplayPropertiesApplied(TransparentShape( ColoredShape( Circle(3) , "yellow" ), 0.5))
    print(mixed_alternate4_display)

    # add more props and display
    mixed_alternate2_display = ColoredShape(DisplayPropertiesApplied(DisplayProperties(TransparentShape( ColoredShape( Circle(3) , "yellow" ), 0.5))) , "white")
    print(mixed_alternate2_display)

    """
    ###############       FINAL PROPERTIES DISPLAYED      ##################
    collected properties : [0.5]
    collected Applied properties : {'color': 'yellow', 'transparency': 0.5}
    collected Applied properties : {'color': 'yellow', 'transparency': 0.5}
    collected Applied properties : {'color': 'white', 'transparency': 0.5} has the color white
    """