names = ["ali", "atefe", "reza", "homa", "amir", "fateme"]
a =int(input("enter number :"))-1
b = str(input("Enter name :"))
c = int(input("enter number :"))-1
n = str(input("Enter name :"))
e =int(input("enter number :"))-1
v = str(input("Enter name :"))
if a < 7 and c < 7 and e < 7:
    names.insert(a , b)
    names.insert(c , n)
    names.insert(e , v )
    print(names)
else:
    print("Not true")