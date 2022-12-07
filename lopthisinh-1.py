
def main():
    arr = []
    for i in range(5):
        arr.append(input())
    diem = float(arr[2]) + float(arr[3]) + float(arr[4])
    print(f"{arr[0]} {arr[1]} {diem:.1f}")

if(__name__ == "__main__"):
    main()