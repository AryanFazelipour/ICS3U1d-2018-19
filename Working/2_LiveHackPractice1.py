# Right_angle_triangle_checker

side_1 = int(input("Enter first side length: "))
side_2 = int(input("Enter second side length: "))
side_3 = int(input("Enter the third side length: "))

side_1_squared = side_1 ** 2
side_2_squared = side_2 ** 2
side_3_squared = side_3 ** 2

if side_1_squared == side_2_squared + side_3_squared or side_2_squared == side_1_squared + side_3_squared or side_3_squared == side_1_squared + side_2_squared:
    print("It is a right angle triangle")

else:
    print("It is not a right angle triangle")
