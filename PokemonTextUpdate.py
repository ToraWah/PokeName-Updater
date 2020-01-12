# Text Writer
# Version 0.1
# Melody McGee, 2020
# Designed to update pokemon information in a livestream via text
 
# --TODO--
# Track pokemon catch order?
# Add image copy/rename
# Add revive counter per pokemon
# Maintain database of pokemon caught

# Pokemon type and name variables
p1 = input("Pokemon in slot 1? ")
n1 = input(p1 + " nickname? ")
p2 = input("Pokemon in slot 2? ")
n2 = input(p2 + " nickname? ")
p3 = input("Pokemon in slot 3? ")
n3 = input(p3 + " nickname? ")
p4 = input("Pokemon in slot 4? ")
n4 = input(p4 + " nickname? ")
p5 = input("Pokemon in slot 5? ")
n5 = input(p5 + " nickname? ")
p6 = input("Pokemon in slot 6? ")
n6 = input(p6 + " nickname? ")



# Writing out to file for OBS to read
pokemon1 = open("pokemon1.txt", "w")
pokemon1.write(p1)
pokemon1.close()

nickname1 = open("nickname1.txt", "w")
nickname1.write(n1)
nickname1.close()

pokemon2 = open("pokemon2.txt", "w")
pokemon2.write(p2)
pokemon2.close()

nickname2 = open("nickname2.txt", "w")
nickname2.write(n2)
nickname2.close()

pokemon3 = open("pokemon3.txt", "w")
pokemon3.write(p3)
pokemon3.close()

nickname3 = open("nickname3.txt", "w")
nickname3.write(n3)
nickname3.close()

pokemon4 = open("pokemon4.txt", "w")
pokemon4.write(p4)
pokemon4.close()

nickname4 = open("nickname4.txt", "w")
nickname4.write(n4)
nickname4.close()

pokemon5 = open("pokemon5.txt", "w")
pokemon5.write(p5)
pokemon5.close()

nickname5 = open("nickname5.txt", "w")
nickname5.write(n5)
nickname5.close()

pokemon6 = open("pokemon6.txt", "w")
pokemon6.write(p6)
pokemon6.close()

nickname6 = open("nickname6.txt", "w")
nickname6.write(n6)
nickname6.close()