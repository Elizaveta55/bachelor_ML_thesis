import re
import numpy as np
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding
from keras.layers import LSTM, SpatialDropout1D
X_train = []
X_test = []
X_test_only = []
X_test_half = []
Y_train = []
Y_test = []
Y_test_only = []
Y_test_half = []
data2 = []


with open("x_train.txt", "r") as fp:
    for line in fp:
        line = re.sub(r'(\d)(\d)(\.)(\d)', r'\1, \2\3\4', line)
        data2 = eval(line)
        X_train.append(data2)
print("Data reading X_train ... done")

l=0
with open("x_test.txt", "r") as fp:
    for line in fp:
        line = re.sub(r'(\d)(\d)(\.)(\d)', r'\1, \2\3\4', line)
        data2 = eval(line)
        X_test.append(data2)
        l=l+1
        if(l<274):
            X_test_only.append(data2)
        if (l<550):
            X_test_half.append(data2)
print("Data reading X_test ... done")

for i in range(len(X_test)):
    for j in range (len(X_test[i])):
        X_test[i][j] = int((abs(X_test[i][j])) * 100000)
        if (X_test[i][j]>9000000):
            print(X_test[i][j])

for i in range(len(X_train)):
    for j in range (len(X_train[i])):
        X_train[i][j] = int(abs(X_train[i][j]) * 100000)
        if (X_train[i][j]>9000000):
            print(X_train[i][j])

l=0
with open("y_test.txt", "r") as fp:
    for line in fp:
        data = re.sub(r'\[', r'', line)
        data = re.sub(r'\]', r'', data)
        data2 = eval(data)
        Y_test.append(data2)
        l = l + 1
        if (l < 274):
            Y_test_only.append(data2)
        if (l < 550):
            Y_test_half.append(data2)
print("Data reading Y_test ... done")

with open("y_train.txt", "r") as fp:
    for line in fp:
        data = re.sub(r'\[', r'', line)
        data = re.sub(r'\]', r'', data)
        data2 = eval(data)
        Y_train.append(data2)
print("Data reading Y_train ... done")

np.random.seed(42)
max_features = 9500000

X_train = sequence.pad_sequences(X_train, dtype='float32')
X_test = sequence.pad_sequences(X_test, dtype='float32')
X_test_only = sequence.pad_sequences(X_test_only, dtype='float32')
X_test_half = sequence.pad_sequences(X_test_half, dtype='float32')
print("Data preparation ... done")

model = Sequential()
model.add(Embedding(max_features, 32))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(1, activation="sigmoid"))
print("NeuralNetwork preparation ... done")

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
print("network compilation ... done")

model.fit(X_train, Y_train, batch_size=64, epochs=9,
          validation_data=(X_test, Y_test), verbose=2)
model.save_weights("model_v2_1500.h5")

scores = model.evaluate(X_test, Y_test, batch_size=64)
print("Точность на тестовых данных: %.2f%%" % (scores[1] * 100))

scores_only = model.evaluate(X_test_only, Y_test_only, batch_size=64)
print("Точность на тестовых данных: %.2f%%" % (scores_only[1] * 100))

scores_half = model.evaluate(X_test_half, Y_test_half, batch_size=64)
print("Точность на тестовых данных: %.2f%%" % (scores_half[1] * 100))