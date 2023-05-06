
import csv
import random
from sklearn import svm
from sklearn.linear_model import Perceptron
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier

model = svm.SVC()
with open("banknotes.csv") as f:
    reader = csv.reader(f)
    next(reader)
    data = []
    for row in reader:
     data.append({
        "feature": [float(cell) for cell in row[:4]],
        "label": "Real" if row[4] == "0" else "Fake"
    })


h = int(0.40 * len(data))
random.shuffle(data)
testing = data[:h]
training = data[h:]


# Training model
X_training = [row["feature"] for row in training]
y_training = [row["label"] for row in training]
model.fit(X_training, y_training)


# Making predictions 
X_testing = [row["feature"] for row in testing]
y_testing = [row["label"] for row in testing]
predictions = model.predict(X_testing)


# Compute performance
t = 0
f = 0
total = 0
for actual, predicted in zip(y_testing, predictions):
    total += 1
    if actual == predicted:
        t += 1
    else:
        f += 1



print(f"Results for model {type(model).__name__}")
print(f"Correct: {t}")
print(f"Incorrect: {f}")
print(f"Accuracy: {100 * t / total:.2f}%")