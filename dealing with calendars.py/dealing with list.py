catname = []
while True:
    print("enter of the  cat " + str(len(catname) +1) + " or enter nothing to stop ")
    name = input()
    if name =="":
        break
    catname = catname + [name] #list concatenation
    print("the name of the cats are:")
    for name in catname:
        print("" +name)

print("List compression is cool")