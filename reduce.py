from functools import reduce
li = ["Geeks", "for", "Geeks", "is", "portal", "for", "Geeks"]
res = reduce(lambda x, y: x + " " + y, li)
print(res)