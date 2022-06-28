# Basic python funtions

from operator import truediv


var1: int = 1
var2: int = 5
var3: bool = False
var4: int = 1
var5: int = 1
var6: list = ["apple", "orange", "blueberry"]

# if and elsif
if var1 > var2:
    print("Is grater")
elif var1 < var2:
    print("Is less")

if var3 == True:
    print("True")
else:
    print("False")

# While
while var4 <= 6:
    print(var4)
    if var4 == 2:
        break
    var4 += 1

# For
for x in var6:
    print(x)

for x in "banana":
  print(x)