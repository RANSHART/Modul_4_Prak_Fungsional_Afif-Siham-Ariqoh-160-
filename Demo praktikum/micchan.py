import math

def point(x,y):
    return x,y

def line_transformation(p1,p2):
    x1,y1 = p1
    x2,y2 = p2
    def translation():
        try:
            tx, ty = map(float,input("Value of translation x and y: ").split())
        except ValueError:
            print("Input error")
            return translation()
        else:
            translation_p1 = (x1+tx , y1+ty)
            translation_p2 = (x2+tx , y2+ty)
            return translation_p1,translation_p2

    def dilatation():
        try:
            dx, dy = map(float,input("Value of dilatation x and y: ").split())
        except ValueError:
            print("Input error")
            return(dilatation)
        else:
            dilatation_p1 = (x1*dx , y1*dy)
            dilatation_p2 = (x2*dx , y2*dy)
            return dilatation_p1,dilatation_p2
    
    def rotation():
        try:
            rotation_degree = float(input("Rotation Degree: "))
            angle_rad = math.radians(rotation_degree)
        except ValueError:
            print("Input error")
            return rotation()
        else:
            rotated_x1 = x1 * math.cos(angle_rad) - y1 * math.sin(angle_rad)
            rotated_y1 = x1 * math.sin(angle_rad) + y1 * math.cos(angle_rad)
            rotated_x2 = x2 * math.cos(angle_rad) - y2 * math.sin(angle_rad)
            rotated_y2 = x2 * math.sin(angle_rad) + y2 * math.cos(angle_rad)
            return (rotated_x1, rotated_y1), (rotated_x2, rotated_y2)

    print("Translation: ",translation())
    print("Dilatation: ",dilatation())
    print("Rotation: ",rotation())

while True:
    try:
        p_1 = tuple(map(float,input("Point 1 x and y axis: ").split()))
        p_2 = tuple(map(float,input("Point 2 x and y axis: ").split()))
    except:
        print("Input error")
    else:
        line_transformation(point(*p_1),point(*p_2))