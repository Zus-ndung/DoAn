f = open("./nhanvat/nhanvatlist.txt", "r")

y = []
for text in f:
    y.append(text.replace(" ", "_").strip())

print(y[0])
