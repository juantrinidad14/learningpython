def remove (x):
    return list(dict.fromkeys(x) )

names = remove(["John", "William", "John", "Mary", "Steve", "Mary"])
print(names)


 




