
import numpy as np
import csv
import math

from sklearn.utils import shuffle

# Tien xu ly du lieu tu file csv
def loadData(source):
    file = open(source, 'r')
    data = csv.reader(file)
    data = np.array(list(data))
    # Xoa dong dau tien chua tieu de
    data = np.delete(data, 0, 0)
    # Xoa cot dau tien chua chi so
    data = np.delete(data, 0, 1)
    # Xao tron ngau nhien du lieu
    np.random.shuffle(data)
    file.close()
    # Tap huan luyen gom 100 quan sat dau tien
    trainSet = data[ : 100]
    # Tap kiem tra gom 51 quan sat con lai
    testSet = data[100 : ]
    return trainSet, testSet

# Tinh khoang cach giua 2 quan sat
def countDistance(a, b, features = 4):
    result = 0
    for i in range(features):
        result += (float(a[i]) - float(b[i])) ** 2
    result = math.sqrt(result)
    return result

# Thuat toan KNN tim k quan sat gan diem du lieu nhat
def KNN(trainSet, point , k):
    distances = []
    for instance in trainSet:
        distances.append({
            "label" : instance[-1], # Nhan cua moi quan sat
            "distance": countDistance(instance, point) # Khoang cach giua quan sat voi diem dang xet
        })
    # Sap xep khoang cach tang dan
    distances.sort(key = lambda x : x["distance"])
    labels = [instance["label"] for instance in distances]
    # Chon k quan sat co khoang cach nho nhat
    return labels[ : k]

# Chon nhan xuat hien nhieu nhat trong k quan sat
def selectLabel(array):
    labels = set(array)
    result = ""
    countMax = 0
    for label in labels:
        count = array.count(label)
        if(count > countMax):
            countMax = count
            result = label
    return result

# Ham main dua ra ket qua du doan voi tap kiem tra
if __name__ == "__main__":
    trainSet, testSet = loadData("Iris.csv")
    correctPredict = 0
    for instance in testSet:
        knn = KNN(trainSet, instance, 5)
        result = selectLabel(knn)
        if(result == instance[-1]):
            correctPredict += 1
        # In ra ket qua du doan va ket qua thuc te voi moi quan sat
        print(f"Kết quả dự đoán: {result} ; Két quả mong muốn: {instance[-1]}")
    print(f"Độ chính xác: {float(correctPredict / len(testSet))}")
