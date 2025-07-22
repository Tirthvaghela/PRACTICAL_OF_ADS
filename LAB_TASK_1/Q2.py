# Import the code from your other two files so we can use their functions.
import Q2_area
import Q2_vol

print(" Shape Calculator ")

# --- Area Calculations ---
print("\n--- Let's Calculate Area ---")

# Circle Area
circle_radius = float(input("Enter the radius of the circle: "))
# Call the function from the area.py file
circle_a = Q2_area.calculate_circle_area(circle_radius)
print(f"The area of a circle with radius {circle_radius} is: {circle_a}")
print("\n")

# Rectangle Area
rect_length = float(input("Enter the length of the rectangle: "))
rect_width = float(input("Enter the width of the rectangle: "))
rect_a = Q2_area.calculate_rectangle_area(rect_length, rect_width)
print(f"The area of a rectangle with length {rect_length} and width {rect_width} is: {rect_a}")
print("\n")

# Sphere Area
sphere_radius = float(input("Enter the radius of the sphere: "))
sphere_a = Q2_area.calculate_sphere_area(sphere_radius)
print(f"The surface area of a sphere with radius {sphere_radius} is: {sphere_a}")
print("\n")

# Cube Area
cube_side = float(input("Enter the side length of the cube: "))
cube_a = Q2_area.calculate_cube_area(cube_side)
print(f"The surface area of a cube with side length {cube_side} is: {cube_a}")


# --- Volume Calculations ---
print("\n--- Now, Let's Calculate Volume ---")

# Sphere Volume
sphere_radius = float(input("Enter the radius of the sphere: "))
sphere_v = Q2_vol.calculate_sphere_volume(sphere_radius)
print(f"The volume of a sphere with radius {sphere_radius} is: {sphere_v}")
print("\n")

# Cube Volume
cube_side = float(input("Enter the side length of the cube: "))
cube_v = Q2_vol.calculate_cube_volume(cube_side)
print(f"The volume of a cube with a side length of {cube_side} is: {cube_v}")