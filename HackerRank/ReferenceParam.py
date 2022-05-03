# Pass by Reference in Python: Use []

def func(valvar, listvar):
    valvar += 1
    listvar.append("ADDED")

    print("Incide the func:", valvar, listvar)

orivalvar = 2
orivallist = ["Ori"]
func(orivalvar, orivallist)

print(orivalvar, orivallist)