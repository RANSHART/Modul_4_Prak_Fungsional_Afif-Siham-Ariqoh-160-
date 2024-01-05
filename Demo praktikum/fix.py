import math

def titik(x, y):
    return x, y

def transformasi(fungsi):
    def pembungkus(*args, **kwargs):
        try:
            tx, ty = map(float, input("Nilai translasi x dan y: ").split())
            rotasi_derajat = float(input("Derajat Rotasi: "))
            sudut_rad = math.radians(rotasi_derajat)
            dx, dy = map(float, input("Nilai dilatasi x dan y: ").split())
        except:
            print("Kesalahan input")
            return transformasi(fungsi)(*args, **kwargs)
        else:
            x1, y1 = args[0]
            x2, y2 = args[1]

            # Translasi
            translasi_p1 = (x1 + tx, y1 + ty)
            translasi_p2 = (x2 + tx, y2 + ty)

            # Rotasi
            berputar_x1 = translasi_p1[0] * math.cos(sudut_rad) - translasi_p1[1] * math.sin(sudut_rad)
            berputar_y1 = translasi_p1[0] * math.sin(sudut_rad) + translasi_p1[1] * math.cos(sudut_rad)
            berputar_x2 = translasi_p2[0] * math.cos(sudut_rad) - translasi_p2[1] * math.sin(sudut_rad)
            berputar_y2 = translasi_p2[0] * math.sin(sudut_rad) + translasi_p2[1] * math.cos(sudut_rad)

            # Dilatasi
            dilatasi_p1 = (berputar_x1 * dx, berputar_y1 * dy)
            dilatasi_p2 = (berputar_x2 * dx, berputar_y2 * dy)

            return dilatasi_p1, dilatasi_p2
    return pembungkus

def persamaan_garis(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    M = (y2 - y1) / (x2 - x1)
    C = y1 - M * x1
    return f"y = {M:.2f}x + {C:.2f}"

@transformasi
def transformasi_garis(p1, p2):
    return p1, p2

# Input untuk persamaan garis pertama
while True:
    try:
        p_1 = tuple(map(int, input("Titik 1 sumbu x dan y: ").split()))
        p_2 = tuple(map(int, input("Titik 2 sumbu x dan y: ").split()))
        print(f"Persamaan garis dari {p_1} dan {p_2}:")
        hasil_persamaan_garis_pertama = persamaan_garis(titik(*p_1), titik(*p_2))
    except:
        print("Kesalahan input")
    else:
        print(hasil_persamaan_garis_pertama)
        hasil_transformasi = transformasi_garis(titik(*p_1), titik(*p_2))
        persamaan_transformasi = persamaan_garis(*hasil_transformasi)
        print("Persamaan garis dari garis yang tertransformasi:")
        print(persamaan_transformasi)
        break
