import math
import numpy as np
from scipy.stats import kstest
from scipy. stats import lognorm
from scipy.stats import shapiro
import pandas as pd
from numpy import genfromtxt




"""Тест Колмогорова, Смирнова"""

print("Чтение файла")
df_ks = pd.read_excel('files/Restruct_25.xlsx', sheet_name="1311", engine='openpyxl')
df_ks.to_csv('files/int.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")
# переделываем формат в нампи


# print(type(df_ks["Интенсивность"].values))
lognorm_dataset = df_ks["Интенсивность"].values

#generate dataset that contains 1000 log-normal distributed values

lognorm_dataset = lognorm.pdf (s=.5, scale=math. exp (1), size=1000)
# print(type(lognorm_dataset))
#perform Kolmogorov-Smirnov test for normality
print(kstest(lognorm_dataset, 'norm'))




