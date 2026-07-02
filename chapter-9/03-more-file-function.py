f = open("chapter-9/f.txt")
lines = f.readlines()
print(lines , type(lines))

lines1 = f.readlines()
print(lines1 , type(lines1))
lines2 = f.readlines()
print(lines2 , type(lines2))
lines3 = f.readlines()
print(lines3 , type(lines3))




f.close()