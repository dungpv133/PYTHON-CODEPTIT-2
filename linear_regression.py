import pandas as pd
import matplotlib.pyplot as pl
dataFrame = pd.read_csv('Advertising.csv')
x = dataFrame.values[ : 150, 2]
y = dataFrame.values[ : 150, 4]

def predict(new_radio, weight, bias):
    return weight * new_radio + bias

# Tính giá trị sai số bình phương MSE
def costFunction(x, y, weight, bias):
    n = len(x)
    sumError = 0
    for i in range(n):
        sumError += (y[i] - weight * x[i] - bias) ** 2
    return sumError / n

# Cập nhật trọng số sử dụng Gradient descent
def updateWeight(x, y, weight, bias, learningRate):
    n = len(x)
    sumWeight = 0
    sumBias = 0
    for i in range(n):
        sumWeight += -2 * x[i] * (y[i] - x[i] * weight - bias)
        sumBias += -2 * (y[i] - x[i] * weight - bias)
    weight -= (sumWeight / n) * learningRate
    bias -= (sumBias / n) * learningRate
    return weight, bias

# Hàm huấn luyện
def training(x, y, weight, bias, learningRate, iteration):
    costList = []
    for i in range(iteration):
        weight, bias = updateWeight(x, y, weight, bias, learningRate)
        cost = costFunction(x, y, weight, bias)
        costList.append(cost)
    return weight, bias, costList

weight, bias, cost = training(x, y, 0.03, 0.0014, 0.001, 30)
print(weight)
print(bias)
print(f"Giá trị hàm mất mát: ")
print(cost)