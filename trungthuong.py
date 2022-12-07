
def main():
    t = int(input())
    while(t > 0):
        t = t - 1
        n = int(input())
        arr = []
        num = []
        while(n > 0):
            n = n - 1
            temp = int(input())
            arr.append(temp)
            if(temp not in num):
                num.append(temp)
        max_value = arr[0]
        max_count = 0
        num.sort()
        for k in num:
            count = 0
            for m in arr:
                if(k == m):
                    count = count + 1
            if(count > max_count):
                max_count = count
                max_value = k
        print(f"{max_value}")

if(__name__ == "__main__"):
    main()