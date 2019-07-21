import random as rd

with open("points.txt", "w") as file:
    for i in range(200):
        y = (-2) * i + 400
        file.write(str(i) + " " + str(rd.randint(-30, 30) + y) + ",")
