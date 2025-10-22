import pandas as pd

csv_file = pd.read_csv("Newcastle Data Challenge Dataset.xlsx - Sheet1.csv")

# Pandas Series of just time
time = csv_file["time"]
gender = csv_file["gender"]
train10 = csv_file["trained_10_week"]
train_im = csv_file["trained_im"]
has_trainer = csv_file["has_trainer"]
age = csv_file["Age"]
vo2 = csv_file["VO2 Max"]
bmi = csv_file["BMI"]
marathons = csv_file["n Marathons run"]
cadence = csv_file["Cadence"]

import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

xpoints = np.array( train10.to_numpy() )

ypoints = np.array( cadence.to_numpy() )

slope, intercept, r, p, std_error = stats.linregress(xpoints, ypoints)

def linearRegression(x):
  return slope * x + intercept

model = list(map(linearRegression, xpoints))

plt.scatter(xpoints, ypoints)
plt.plot(xpoints, model)
plt.show()