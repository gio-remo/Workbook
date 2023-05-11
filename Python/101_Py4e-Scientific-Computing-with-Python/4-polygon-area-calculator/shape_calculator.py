from turtle import width

class Rectangle:

    width = None
    height = None

    def __init__(self, xwidth, xheight):
        self.width = xwidth
        self.height = xheight

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            s = ""
            h = 0
            while h < self.height:
                w = 0
                while w < self.width:
                    s += "*"
                    w +=1
                s += "\n"
                h += 1
            return s
    
    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

    def get_amount_inside(self, figure):
        times_height = int(self.height / figure.height)
        times_width = int(self.width / figure.width)

        if times_height == 0 or times_width == 0:
            return 0
        else:
            return times_height * times_width

class Square(Rectangle):
    
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_height(self, height):
        self.width = height
        self.height = height

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"