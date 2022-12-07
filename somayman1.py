n = input()
dem4 =0
dem7 = 0
for i in n:
    if i == '4':
        dem4 += 1
    elif i == '7':
        dem7 += 1
if(dem4 + dem7 == 4 or dem4 + dem7 == 7):
    print("YES")
else:
    print("NO")