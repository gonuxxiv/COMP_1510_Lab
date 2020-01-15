
coverage = 400
length = float(input("Length: "))
width = float(input("Width: "))
height = float(input("Height: "))
coat = float(input("Number of coats: "))

surface_area = (length * width) + (2 * (height * width)) + (2 * (height * length))
coverage_needed = surface_area * coat
cans_of_paint_required = (coverage_needed / coverage) * 4

print(cans_of_paint_required)
