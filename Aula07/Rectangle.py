class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    
    def calculate_area(self):
        return self.width * self.height 

    def printAttributes(self):
        print("Width: " + str(self.width))
        print("Height: " + str(self.height))