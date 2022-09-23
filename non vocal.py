x = input(" Enter string : ")
y = ["a","i","u","e","o"]
z = " "

for baymax in x :
    if baymax.lower() not in y:
        z = z + baymax
    
print(z)