count = int(input("How many checks need to be done? "))

while count > 0:
    data = input("Enter data: ").split(" ")
    speed_barriers = [60, 80]
    if data[1] == "true":
        speed_barriers = [65, 85]

    if int(data[0]) <= speed_barriers[0]:
        print("no ticket")
    elif int(data[0]) <= speed_barriers[1]:
        print("small ticket")
    else:
        print("big ticket")

    count -= 1
