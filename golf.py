x = ["First name: ", "Last name: ", "Volunteer:\n1 None\n2 Gate\n3 Shop\n4 Painting\n", "Date joined: ", "Paid fee?: ", "None", "Gate", "Shop", "Painting", "==Volunteers==\n", "==Gate==\n", "==Shop==\n", "==Painter==\n", "==Expired==\n", "==Paid==\n", "==Planks==\n"]
l = [lambda s: int(s.t[2]) > 1, lambda s: int(s.t[2]) == 2, lambda s: int(s.t[2]) == 3, lambda s: int(s.t[2]) == 4, lambda s: not(s.t[3][6:] == "2022"), lambda s: True if s.t[4].lower() == "y" else False, lambda s: False]
ms = []
class M:
    def __init__(s):
        s.t = []
        for i in range(5): s.t.append(input(x[i]))
        [l.append(f"{s.t[0]} {s.t[1]}: {input('Message: ')}") if input("Add plank?: ").lower() == "y" else None]
    def __str__(s): return f"\n{x[0]}{s.t[0]}\n{x[1]}{s.t[1]}\nVolunteer: {x[int(s.t[2])+4]}\n{x[3]}{s.t[3]}\n{x[4]}{s.t[4]}\n"
while input("Add person?: ").lower() == "y": ms.append(M())
[print(f"{x[i+9]}{''.join([str(v) for v in ms if l[i](v)])}") for i in range(7)]
[print(f"{v}\n") for v in l[7:]]