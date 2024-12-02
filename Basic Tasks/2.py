""" 
Tehtävä 2:

Kirjoita ohjelma, joka kysyy käyttäjältä 2 numeroa ja tulostaa kaikkien matemaattisten perusoperaattoreiden tuloksen.

Käytä input-funktio arvojen lukemiseen näppäimistöltä ja int- tai float-funktioita muuntaaksesi tekstin numeroksi ja str-funktiota numeron muuttamiseksi tekstiksi. """


print("give me an number")
input1 = input()
print("give me an second number")
input2 = input()


sum = int(input1) + int(input2)
minus = int(input1) - int(input2)
multiply = int(input1) * int(input2)
division = int(input1) / int(input2)
remainder = int(input1) % int(input2)


print("Sum: ", sum)
print("Minus: ", minus)
print("multiply: ", multiply)
print("division: ", int(division))
print("remainder: ", int(remainder))