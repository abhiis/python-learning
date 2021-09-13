f = open("F:/Dev/Python/hello/fileHandling/file.txt", "r")
print(f.read())
print(f.read(5))
print(f.readline())
for x in f:
    print(x)
f.close()
