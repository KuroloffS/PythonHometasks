#lesson2 #string #problem15
def fxn(stng):

    lst = stng.split()
    oupt = ""

    for word in lst:
        oupt += word[0]
    oupt = oupt.upper()
    return oupt
inpt1 = input("Enter a string: ")
print(fxn(inpt1))