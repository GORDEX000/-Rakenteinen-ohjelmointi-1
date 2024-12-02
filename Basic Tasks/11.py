print("Hello choose how much u need")

butterballs = int(input("how much butterballs u want (0.50€): "))
monkRings = int(input("how much monk rings u want (0.80€): "))
piggies = int(input("how much piggies u want (1.00€): "))
episcopalMonks = int(input("how much episcopal monks u want (1.20€): "))

totalProducts = butterballs + monkRings + piggies + episcopalMonks

sum = butterballs * 0.50 + monkRings * 0.80 + piggies * 1.00 + episcopalMonks * 1.20


print("total products: ", totalProducts, "sum: ", sum)