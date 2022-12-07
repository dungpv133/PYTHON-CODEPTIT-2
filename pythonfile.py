
s = input()
res = s[-3 : ].lower()
# print(res)
count = s.count('.')
if(res == ".py" and count == 1):
    print("yes")
else:
    print("no")
