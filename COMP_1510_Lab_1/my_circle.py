pi = 3.14159
radius = float(input("What's the radius? "))

double_radius = 2 * radius

circumference = 2 * pi * radius
print("The circumference of the circle is " + str(circumference))

area = pi * radius * radius
print("The area of the circle is " + str(area))

doubled_circumference = 2 * pi * double_radius

doubled_area = pi * double_radius * double_radius

circumference_difference = circumference / doubled_circumference
area_difference = area / doubled_area

print("The difference between circumstance with doubled radius"
      " and the original circumstance is " + str(circumference_difference))

print("The difference between area with doubled radius"
      " and the original area is " + str(area_difference))