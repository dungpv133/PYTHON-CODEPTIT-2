# Khai báo các thư viện cần thiết
import keras  # thư viện cho mạng neuron nhân tạo
import pandas as pd  # tải dữ liệu dưới dạng bảng, xử lý dữ liệu, xử lý vào ra
import seaborn as sns  # trực quan hóa dữ liệu
import matplotlib.pyplot as plt  # trực quan hóa dữ liệu
import numpy as np  # đại số tuyến tính
from sklearn.preprocessing import normalize  # thư viện chứa các thuật toán học máy

# Mô đun mạng neuron nhân tạo
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.utils import np_utils
import keras.initializers as init

# Đọc dữ liệu từ file csv
data = pd.read_csv("Iris.csv")
# print("Describing the data: ",data.describe())
# print("Info of the data:",data.info())

# Trực quan hóa dữ liệu
# sns.lmplot('SepalWidthCm', 'PetalWidthCm',
#            data=data,
#            fit_reg=False,
#            hue="Species",
#            scatter_kws={"marker": "D",
#                         "s": 50})
# plt.title('SepalWidth vs PetalWidth')
# plt.show()

data.loc[data["Species"] == "Iris-setosa", "Species"] = 0
data.loc[data["Species"] == "Iris-versicolor", "Species"] = 1
data.loc[data["Species"] == "Iris-virginica", "Species"] = 2
# print(data.head())
data = data.iloc[np.random.permutation(len(data))]
X = data.iloc[:, 1:5].values
y = data.iloc[:, 5].values
X_normalized = normalize(X, axis=0)

# Tạo dữ liệu huấn luyện, dữ liệu kiểm tra và xác thực dữ liệu
total_length = len(data)
train_length = int(0.8 * total_length)
test_length = int(0.2 * total_length)

X_train = X_normalized[:train_length]
X_test = X_normalized[train_length:]
y_train = y[:train_length]
y_test = y[train_length:]

# Thay các nhãn bằng các one-hot vector
y_train = np_utils.to_categorical(y_train, num_classes=2)
y_test = np_utils.to_categorical(y_test, num_classes=2)

model = Sequential()
# bias_initializer = init.initializers_v1.RandomUniform(minval=-0.05, maxval=0.05, seed=None)
initializer = keras.initializers.RandomUniform(minval=-0.05, maxval=0.05, seed=None)
model.add(Dense(1000, input_dim=4, activation='relu', kernel_initializer=initializer, bias_initializer='zeros'))
model.add(Dense(500, activation='relu', kernel_initializer=initializer, bias_initializer='zeros'))
model.add(Dense(300, activation='relu', kernel_initializer=initializer, bias_initializer='zeros'))
model.add(Dropout(0.2))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='Adam', metrics=['accuracy'])
model.summary()
model.fit(X_train, y_train, validation_data=(X_test, y_test), batch_size=20, epochs=10, verbose=1)

prediction = model.predict(X_test)
length = len(prediction)
y_label = np.argmax(y_test, axis=1)
predict_label = np.argmax(prediction, axis=1)

accuracy = np.sum(y_label == predict_label) / length * 100
print("Accuracy of the dataset", accuracy)
