def multiplyNumbersBetween(start, end):
    i = start

    while (i < end):
        print(i)
        i += 1
        n = i * end
    return n

multiply = multiplyNumbersBetween(12, 23)

print("multiply:", multiply)
