import math

#Сегашна позиция
x_old = float(input("Въведи начална X координата: "))
y_old = float(input("Въведи начална Y координата: "))

total_distance = 0

while True:
    x_new = input("Въведи нова X координата: or no to stop typing")
    y_new = float(input("Въведи нова Y координата: "))

    if x_new == "no":
        break
    x_new == float(x_new)
        

    # Разстояние между старата и новата позиция
    distance = math.sqrt((x_new - x_old) ** 2 + (y_new - y_old) ** 2)

    total_distance = total_distance + distance

    #Нова позиция
    x_old = x_new
    y_old = y_new

print("Общо изминато разстояние:", total_distance, "метра")
