import math

def point(x, y):
    return x, y

def composite_transform(function):
    def wrapper(*args, **kwargs):
        try:
            tx, ty = map(float, input("Value of translation x and y: ").split())
            rotation_degree = float(input("Rotation Degree: "))
            angle_rad = math.radians(rotation_degree)
            dx, dy = map(float, input("Value of dilatation x and y: ").split())
        except ValueError:
            print("Input error")
            return composite_transform(function)(*args, **kwargs)
        else:
            x1, y1 = args[0]
            x2, y2 = args[1]

            # Translation
            translation_p1 = (x1 + tx, y1 + ty)
            translation_p2 = (x2 + tx, y2 + ty)
            print(translation_p1,translation_p2)

            # Rotation
            rotated_x1 = translation_p1[0] * math.cos(angle_rad) - translation_p1[1] * math.sin(angle_rad)
            rotated_y1 = translation_p1[0] * math.sin(angle_rad) + translation_p1[1] * math.cos(angle_rad)
            rotated_x2 = translation_p2[0] * math.cos(angle_rad) - translation_p2[1] * math.sin(angle_rad)
            rotated_y2 = translation_p2[0] * math.sin(angle_rad) + translation_p2[1] * math.cos(angle_rad)

            # Dilatation
            dilatation_p1 = (rotated_x1 * dx, rotated_y1 * dy)
            dilatation_p2 = (rotated_x2 * dx, rotated_y2 * dy)

            return dilatation_p1, dilatation_p2
    return wrapper

def line_equation(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    M = lambda x, y: (y2 - y1) / (x2 - x1)
    C = lambda x, y: y1 - M(x, y) * x1
    return f"y = {M(p1, p2):.2f}x + {C(p1, p2):.2f}"

@composite_transform
def transformation_pipeline(p1, p2):
    return line_equation(p1, p2)

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