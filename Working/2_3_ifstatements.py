def caught_speeding(speed, is_birthday):
    if speed <= 60 and is_birthday == True or speed >= 61 and speed >= 65 and is_birthday == True:
        return (0)

    elif speed >= 61 and speed >= 80 and is_birthday == False or speed >= 81 and speed <= 85 and is_birthday == True:
        return (1)

    else:
        return (2)


caught_speeding()