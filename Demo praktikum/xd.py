import math

def point(x, y):
    return x, y

def translation(function):
    def wrapper(*args, **kwargs):
        try:
            tx, ty = map(float, input("Value of translation x and y: ").split())
        except ValueError:
            print("Input error")
            return translation(function)(*args, **kwargs)
        else:
            x1, y1 = args[0]
            x2, y2 = args[1]
            translation_p1 = (x1 + tx, y1 + ty)
            translation_p2 = (x2 + tx, y2 + ty)
            return translation_p1, translation_p2
    return wrapper

def rotation(function):
    def wrapper(*args, **kwargs):
        try:
            rotation_degree = float(input("Rotation Degree: "))
            angle_rad = math.radians(rotation_degree)
        except ValueError:
            print("Input error")
            return rotation(function)(*args, **kwargs)
        else:
            x1, y1 = args[0]
            x2, y2 = args[1]
            rotated_x1 = x1 * math.cos(angle_rad) - y1 * math.sin(angle_rad)
            rotated_y1 = x1 * math.sin(angle_rad) + y1 * math.cos(angle_rad)
            rotated_x2 = x2 * math.cos(angle_rad) - y2 * math.sin(angle_rad)
            rotated_y2 = x2 * math.sin(angle_rad) + y2 * math.cos(angle_rad)
            return (rotated_x1, rotated_y1), (rotated_x2, rotated_y2)
    return wrapper

def dilatation(function):
    def wrapper(*args, **kwargs):
        try:
            dx, dy = map(float, input("Value of dilatation x and y: ").split())
        except ValueError:
            print("Input error")
            return dilatation(function)(*args, **kwargs)
        else:
            x1, y1 = args[0]
            x2, y2 = args[1]
            dilatation_p1 = (x1 * dx, y1 * dy)
            dilatation_p2 = (x2 * dx, y2 * dy)
            return dilatation_p1, dilatation_p2
    return wrapper

def line_equation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    M = lambda x, y: (y2 - y1) / (x2 - x1)
    C = lambda x, y: y1 - M(x, y) * x1
    return f"y = {M(p1, p2):.2f}x + {C(p1, p2):.2f}"

def transformation_pipeline(p1, p2):
    # Apply decorators manually in the desired order
    dilatation_result = dilatation(line_equation)(p1, p2)
    translation_result = translation(dilatation_result)(p1, p2)
    rotated_result = rotation(translation_result)(p1, p2)
    return rotated_result

# Input for the first line equation
while True:
    try:
        p_1 = tuple(map(int, input("Point 1 x and y axis: ").split()))
        p_2 = tuple(map(int, input("Point 2 x and y axis: ").split()))
        print(f"Line equation of {p_1} and {p_2}:")
        result_firstline_equation = line_equation(point(*p_1), point(*p_2))
    except ValueError:
        print("Input error")
    else:
        print(result_firstline_equation)
        transformed_result = transformation_pipeline(point(*p_1), point(*p_2))
        print("Transformed Result:")
        print(transformed_result)
    break