x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [7, 8, 9, 10, 11, 14]
z = [9, 10, 11, 12, 13, 15]
i = j = k = 0
while(i < 8 and j < 6):
    if(x[i] < y[j]):
        z.append(x[i])
        i = i+1
    else:
        z.append(y[j])
        j = j+1
while(i < 8):
    z.append(x[i])
    i = i+1
while(j < 6):
    z.append(y[j])
    j = j+1

print("\n Merged array : ")
for i in z:
    print(i, end=" ")
