# -*- coding: utf-8 -*-
"""Data analysis on soil available potassium.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Kzy7GsmJww8g45P2OaYzjpJF6h9Xo6yp
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_excel('/all_k.xlsx')

d = data["KN"].values
plt.hist(d)
plt.xlabel('K(Kg/ha)')
plt.title('Jibantala')
plt.show()

d = data["1K"].values
plt.hist(d)
plt.xlabel('K (Kg/ha)')
plt.title('Talbagicha')
plt.show()

from google.colab import drive
drive.mount('/content/drive')

d = data["2K"].values
plt.hist(d)
plt.xlabel('K (Kg/ha)')
plt.title('Barkola')
plt.show()

d = data["KGS2"].values
plt.hist(d)
plt.xlabel('K (Kg/ha)')
plt.title('Salua')
plt.show()

d = data["LAX, CAN, KMR, GPN"].values
plt.hist(d)
plt.xlabel('K (Kg/ha)')
plt.title('Kakdwip')
plt.show()

d = data["CS"].values
plt.hist(d)
plt.xlabel('K (Kg/ha)')
plt.title('Sagar Island')
plt.show()

sns.boxplot(x = "KN", data=data)
plt.title('Jibantala')
plt.xlabel('K (kg/ha)')
plt.show()

sns.boxplot(x = "1K", data=data)
plt.title('Talbagicha')
plt.xlabel('K (kg/ha)')
plt.show()

sns.boxplot(x = "2K", data=data)
plt.title('Barkola')
plt.xlabel('K (kg/ha)')
plt.show()

sns.boxplot(x = "KGS2", data=data)
plt.title('Salua')
plt.xlabel('K (kg/ha)')
plt.show()

sns.boxplot(x = "LAX, CAN, KMR, GPN", data=data)
plt.title('Kakdwip')
plt.xlabel('K (kg/ha)')
plt.show()

data = pd.read_excel('/content/Set2_KN.xlsx')

sns.boxplot(x = "CS", data=data)
plt.title('Sagar Island')
plt.xlabel('K (kg/ha)')
plt.show()

e = pd.crosstab(data["K (Kg/ha)"],data["EC (µs/cm)"])

sns.heatmap(e)

