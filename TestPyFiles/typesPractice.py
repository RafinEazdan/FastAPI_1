def add(firstName: str,lastName:str):
    firstName = firstName.capitalize()
    return firstName + " " + lastName

fname = "john"
laname = "doe"
print(add(fname,laname))