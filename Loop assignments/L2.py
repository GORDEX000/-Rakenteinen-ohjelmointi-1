def sumNumbersBetween(start, end):
    i = start
    e = i
    while(i < end):
        print(i)
        i += 1
        e += i

    return e


sum = sumNumbersBetween(4, 6)
print("sum is", sum)