from Rectangle import Rectangle

a = float(input("Insert Height: "))
b = float(input("Insert Width: "))

rectangle = Rectangle(a, b)

rectangle.printAttributes()

print(rectangle.calculate_area())

