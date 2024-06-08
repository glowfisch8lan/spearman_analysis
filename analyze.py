import datetime

import openpyxl
import numpy as np
import pandas as pd
import functions as f
import matplotlib
import matplotlib.pyplot as plt
import vaex
# import numpy as npn_rows = 1000000
import dask.dataframe as dd
import phik
import csv

print("Чтение файла")
df = pd.read_excel('files/Restruct_25.xlsx', sheet_name="1311", engine='openpyxl')
df.to_csv('files/int.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")
# # Работа с моделями через dask   https://habr.com/ru/company/otus/blog/527720/

# #Удаляем ненужные столбцы
df = df.drop(columns=['Дата и время', 'Рубеж'], axis=1)

# """"Преобразовываем значения Nan для конкретного толбца в отдельный интервал и меняем тип данных"""
# df['Видимость, шифр'] = df['Видимость, шифр'].replace(np.NaN, 0).astype('category')
# df['Осадки, мм'] = df['Осадки, мм'].replace(np.NaN, 0)

# # print("Определяем количество строк")
# # print(len(df))
# # # print("Ограничиваем количество строк, берем только то, что нужно (Конкатенация)")
# print([df["Дата и время"][3:7]] + [df["Дата и время"][21:24]])
#
print("Отбираем необходимое количсетво столбцов")
"""Записываем полученный результат в df"""
#df["Время суток"] = df["Время суток"].replace(':00:00', '', regex = True)
#df = df[["День недели", "Время суток"]]

# print("Сортируем данные по времени суток")
df = df[
    (df['Время суток'] == datetime.time(5, 0))
    #      &(df['Время суток'] == 17) # Для int
        & (df['День недели'] == 7)
        # & (df['Естественное освещение'] == 0.85)
        & (df['Осадки мм'] == 0)]
print(df)
# """Смотрим процент пропусков (пустые пози)"""
# # print(df.isna().mean().sort_values(ascending=False))
#
# """Создадим таблицу с ИНТЕРВАЛАМИ Интенсивности для анализа"""
# """ДЕНЬ НЕДЕЛИ"""
# df['День недели'] = df['День недели'].astype('category') # Меняем тип данных
#
# """ВРЕМЯ СУТОК"""
# df['Время суток'] = df['Время суток'].astype('category') # Меняем тип данных
# """ТЕМПЕРАТУРА ВОЗДУХА"""
# interval_t_5 = pd.interval_range(start=-40,
#                                    freq=10, #шаг интервала
#                                    end=100)
# df["interval_t_air_5-grup"] = pd.cut(df["t (воздух)"],
#                                     bins=interval_t_5,
#                                         labels=[1,2,3])
#
# interval_t_10 = pd.interval_range(start=-40,
#                                    freq=10, #шаг интервала
#                                    end=100)
# df["interval_t_air_10-grup"] = pd.cut(df["t (воздух)"],
#                                     bins=interval_t_10,
#                                         labels=[1,2,3])
# #
interval_t_15 = pd.interval_range(start=-40,
                                   freq=10, #шаг интервала
                                   end=100)
df["interval_t_air_15-grup"] = pd.cut(df["t (воздух)"],
                                    bins=interval_t_15,
                                        labels=[1,2,3])
# """ТЕМПЕРАТУРА ПОЧВЫ"""
# df["interval_t_soil_5-grup"] = pd.cut(df["t (почва)"],
#                                     bins=interval_t_5,
#                                         labels=[1,2,3])
#
# df["interval_t_soil_10-grup"] = pd.cut(df["t (почва)"],
#                                     bins=interval_t_10,
#                                         labels=[1,2,3])
#
# df["interval_t_soil_15-grup"] = pd.cut(df["t (почва)"],
#                                     bins=interval_t_15,
#                                         labels=[1,2,3])
# """ТЕМПЕРАТУРА РОСЫ"""
# df["interval_t_dew_5-grup"] = pd.cut(df["t (росы)"],
#                                     bins=interval_t_5,
#                                         labels=[1,2,3])
#
# df["interval_t_dew_10-grup"] = pd.cut(df["t (росы)"],
#                                     bins=interval_t_10,
#                                         labels=[1,2,3])
#
# df["interval_t_dew_15-grup"] = pd.cut(df["t (росы)"],
#                                     bins=interval_t_15,
#                                         labels=[1,2,3])
# """АТМОСФЕРНОЕ ДАВЛЕНИЕ"""
# interval_atmosphere_pressure_10 = pd.interval_range(start=700,
#                                    freq=10, #шаг интервала
#                                    end=100000)
# df["interval_atmosphere_pressure_10-grup"] = pd.cut(df["P (парц)"],
#                                     bins=interval_atmosphere_pressure_10,
#                                         labels=[1,2,3])
#
# interval_atmosphere_pressure_20 = pd.interval_range(start=700,
#                                    freq=20, #шаг интервала
#                                    end=100000)
# df["interval_atmosphere_pressure_20-grup"] = pd.cut(df["P (парц)"],
#                                     bins=interval_atmosphere_pressure_20,
#                                         labels=[1,2,3])
#
# interval_atmosphere_pressure_30 = pd.interval_range(start=700,
#                                    freq=30, #шаг интервала
#                                    end=100000)
# df["interval_atmosphere_pressure_30-grup"] = pd.cut(df["P (парц)"],
#                                     bins=interval_atmosphere_pressure_30,
#                                         labels=[1,2,3])
#
# interval_atmosphere_pressure_40 = pd.interval_range(start=700,
#                                    freq=40, #шаг интервала
#                                    end=100000)
# df["interval_atmosphere_pressure_40-grup"] = pd.cut(df["P (парц)"],
#                                     bins=interval_atmosphere_pressure_40,
#                                         labels=[1,2,3])
#
# interval_atmosphere_pressure_50 = pd.interval_range(start=700,
#                                    freq=50, #шаг интервала
#                                    end=100000)
# df["interval_atmosphere_pressure_50-grup"] = pd.cut(df["P (парц)"],
#                                     bins=interval_atmosphere_pressure_50,
#                                         labels=[1,2,3])
# """ВЛАЖНОСТЬ"""
#
# interval_humidity_10 = pd.interval_range(start=0,
#                                    freq=10, #шаг интервала
#                                    end=1000)
# df["interval_humidity_10-grup"] = pd.cut(df["ϕ (процент)"],
#                                     bins=interval_humidity_10,
#                                         labels=[1,2,3])
#
# interval_humidity_20 = pd.interval_range(start=0,
#                                    freq=20, #шаг интервала
#                                    end=1000)
# df["interval_humidity_20-grup"] = pd.cut(df["ϕ (процент)"],
#                                     bins=interval_humidity_20,
#                                         labels=[1,2,3])
#
# interval_humidity_30 = pd.interval_range(start=0,
#                                    freq=30, #шаг интервала
#                                    end=1000)
# df["interval_humidity_30-grup"] = pd.cut(df["ϕ (процент)"],
#                                     bins=interval_humidity_30,
#                                         labels=[1,2,3])
#
# interval_humidity_40 = pd.interval_range(start=0,
#                                    freq=40, #шаг интервала
#                                    end=1000)
# df["interval_humidity_40-grup"] = pd.cut(df["ϕ (процент)"],
#                                     bins=interval_humidity_40,
#                                         labels=[1,2,3])
#
# interval_humidity_50 = pd.interval_range(start=0,
#                                    freq=50, #шаг интервала
#                                    end=1000)
# df["interval_humidity_50-grup"] = pd.cut(df["ϕ (процент)"],
#                                     bins=interval_humidity_50,
#                                         labels=[1,2,3])
# """Дефицит насыщ"""
# interval_aturation_deficit_5 = pd.interval_range(start=-5,
#                                    freq=5, #шаг интервала
#                                    end=1000)
# df["interval_aturation_deficit_5-grup"] = pd.cut(df["Дефицит насыщ. г.Па"],
#                                     bins=interval_aturation_deficit_5,
#                                         labels=[1,2,3])
#
# interval_aturation_deficit_10 = pd.interval_range(start=-5,
#                                    freq=10, #шаг интервала
#                                    end=1000)
# df["interval_aturation_deficit_10-grup"] = pd.cut(df["Дефицит насыщ. г.Па"],
#                                     bins=interval_aturation_deficit_10,
#                                         labels=[1,2,3])
#
# interval_aturation_deficit_15 = pd.interval_range(start=-5,
#                                    freq=15, #шаг интервала
#                                    end=1000)
# df["interval_aturation_deficit_15-grup"] = pd.cut(df["Дефицит насыщ. г.Па"],
#                                     bins=interval_aturation_deficit_15,
#                                         labels=[1,2,3])
# """Давление над уровнем станции"""
# interval_pressure_station_5 = pd.interval_range(start=0,
#                                    freq=5, #шаг интервала
#                                    end=1000)
# df["interval_pressure_station_5-grup"] = pd.cut(df["P (ур, станции)"],
#                                     bins=interval_pressure_station_5 ,
#                                         labels=[1,2,3])
#
# interval_pressure_station_10 = pd.interval_range(start=0,
#                                    freq=10, #шаг интервала
#                                    end=1000)
# df["interval_pressure_station_10-grup"] = pd.cut(df["P (ур, станции)"],
#                                     bins=interval_pressure_station_10 ,
#                                         labels=[1,2,3])
#
# interval_pressure_station_15 = pd.interval_range(start=0,
#                                    freq=15, #шаг интервала
#                                    end=1000)
# df["interval_pressure_station_15-grup"] = pd.cut(df["P (ур, станции)"],
#                                     bins=interval_pressure_station_15 ,
#                                         labels=[1,2,3])
# """Давление над уровнем моря"""
#
# df["interval_pressure_sea_5-grup"] = pd.cut(df["Р (ур, моря)"],
#                                     bins=interval_pressure_station_5 ,
#                                         labels=[1,2,3])
#
# df["interval_pressure_sea_10-grup"] = pd.cut(df["Р (ур, моря)"],
#                                     bins=interval_pressure_station_10 ,
#                                         labels=[1,2,3])
#
# df["interval_pressure_sea_15-grup"] = pd.cut(df["Р (ур, моря)"],
#                                     bins=interval_pressure_station_15 ,
#                                         labels=[1,2,3])
# """ВИДИМОСТЬ"""
# df['Видимость, шифр'] = df['Видимость, шифр'].astype('category') # Меняем тип данных
#
# """ПОГОДА ШИФР"""
# df['Погода, шифр (ww)'] = df['Погода, шифр (ww)'].astype('category') # Меняем тип данных
"""ИНТЕНСИВНОСТЬ"""
# 100
# interval_range_100 = pd.interval_range(start=0,
#                                    freq=500, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_100-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_100,
#                                         labels=[1,2,3])
# 200
interval_range_200 = pd.interval_range(start=0,
                                   freq=100, #шаг интервала
                                   end=200000)
df["Инт_шаг_200-grup"] = pd.cut(df["Интенсивность"],
                                    bins=interval_range_200,
                                        labels=[1,2,3])


# print(df["Инт_шаг_200-grup"])
# print(df["interval_t_air_15-grup"])
#Ранжируем и соединяем значеняи
f = df['rank'] = df["Инт_шаг_200-grup"].rank(pct=True) #Ранжируем интенсивность, приводим от  0 до 1
a = df['rank2'] = df["interval_t_air_15-grup"].rank(pct=True) #Ранжируем погоду, приводим от  0 до 1
b = pd.concat([f, a], axis=1)

"""Готовая ранговая корреляция Спирмана"""
from scipy.stats import spearmanr
#calculate Spearman Rank correlation and corresponding p-value
rho, p = spearmanr(df["Инт_шаг_200-grup"], df["interval_t_air_15-grup"])
#напечатать ранговая корреляция Спирмена и p-значение
print("Коэффициент ранговой корреляции Спирмана = ", rho)
print("p=",p)

exit(1)
# # 250
# interval_range_250 = pd.interval_range(start=0,
#                                    freq=250, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_250-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_250,
#                                         labels=[1,2,3])
# # 300
# interval_range_300 = pd.interval_range(start=0,
#                                    freq=300, #шаг интервала
#                                    end=10000)
# df["Инт_шаг_300-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_300,
#                                         labels=[1,2,3])
# #
# # # 500
# interval_range_500 = pd.interval_range(start=0,
#                                    freq=500, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_500-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_500,
#                                         labels=[1,2,3])
#
# # 750
# interval_range_750 = pd.interval_range(start=0,
#                                    freq=750, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_750-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_750,
#                                         labels=[1,2,3])
# # 1000
# interval_range_1000 = pd.interval_range(start=0,
#                                    freq=1000, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_1000-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_1000,
#                                         labels=[1,2,3])
#
# # 1500
# interval_range_1500 = pd.interval_range(start=0,
#                                    freq=1500, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_1500-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_1500,
#                                         labels=[1,2,3])
#
# # 2000
# interval_range_2000 = pd.interval_range(start=0,
#                                    freq=2000, #шаг интервала
#                                    end=200000)
# df["Инт_шаг_2000-grup"] = pd.cut(df["Интенсивность"],
#                                     bins=interval_range_2000,
#                                         labels=[1,2,3])
# #
# """НАПРАВЛЕНИЕ ВЕТРА"""
#
# interval_direction_of_the_wind_10 = pd.interval_range(start=0,
#                                    freq=10, #шаг интервала
#                                    end=200000)
# df["Напр_ветр_10_град-grup"] = pd.cut(df["Ветер напр. град."],
#                                     bins=interval_direction_of_the_wind_10,
#                                         labels=[1,2,3])
#
# interval_direction_of_the_wind_20 = pd.interval_range(start=0,
#                                    freq=20, #шаг интервала
#                                    end=200000)
# df["Напр_ветр_20_град-grup"] = pd.cut(df["Ветер напр. град."],
#                                     bins=interval_direction_of_the_wind_20,
#                                         labels=[1,2,3])
#
# interval_direction_of_the_wind_30 = pd.interval_range(start=0,
#                                    freq=30, #шаг интервала
#                                    end=200000)
# df["Напр_ветр_30_град-grup"] = pd.cut(df["Ветер напр. град."],
#                                     bins=interval_direction_of_the_wind_30,
#                                         labels=[1,2,3])
#
# interval_direction_of_the_wind_40 = pd.interval_range(start=0,
#                                    freq=40, #шаг интервала
#                                    end=200000)
# df["Напр_ветр_40_град-grup"] = pd.cut(df["Ветер напр. град."],
#                                     bins=interval_direction_of_the_wind_40,
#                                         labels=[1,2,3])
#
# interval_direction_of_the_wind_50 = pd.interval_range(start=0,
#                                    freq=50, #шаг интервала
#                                    end=200000)
# df["Напр_ветр_50_град-grup"] = pd.cut(df["Ветер напр. град."],
#                                     bins=interval_direction_of_the_wind_50,
#                                         labels=[1,2,3])
#
# interval_direction_of_the_wind_60 = pd.interval_range(start=0,
#                                    freq=60, #шаг интервала
#                                    end=200000)
# df["Напр_ветр_60_град-grup"] = pd.cut(df["Ветер напр. град."],
#                                     bins=interval_direction_of_the_wind_60,
#                                         labels=[1,2,3])
# """СКОРОСТЬ ВЕТРА"""
#
# interval_wind_speed_1 = pd.interval_range(start=0,
#                                    freq=1, #шаг интервала
#                                    end=200000)
# df["Скорость_ветра_1мс-grup"] = pd.cut(df["Ветер, скор, м/с"],
#                                     bins=interval_wind_speed_1,
#                                         labels=[1,2,3])
#
# interval_wind_speed_2 = pd.interval_range(start=0,
#                                    freq=2, #шаг интервала
#                                    end=200000)
# df["Скорость_ветра_2мс-grup"] = pd.cut(df["Ветер, скор, м/с"],
#                                     bins=interval_wind_speed_2,
#                                         labels=[1,2,3])
#
# interval_wind_speed_3 = pd.interval_range(start=0,
#                                    freq=3, #шаг интервала
#                                    end=200000)
# df["Скорость_ветра_3мс-grup"] = pd.cut(df["Ветер, скор, м/с"],
#                                     bins=interval_wind_speed_3,
#                                         labels=[1,2,3])
#
# interval_wind_speed_4 = pd.interval_range(start=0,
#                                    freq=4, #шаг интервала
#                                    end=200000)
# df["Скорость_ветра_4мс-grup"] = pd.cut(df["Ветер, скор, м/с"],
#                                     bins=interval_wind_speed_4,
#                                         labels=[1,2,3])
# """ОСАДКИ ММ"""
#
# interval_precipitation_5 = pd.interval_range(start=0,
#                                    freq=5, #шаг интервала
#                                    end=200000)
# df["Осадки_5мм-grup"] = pd.cut(df["Осадки, мм"],
#                                     bins=interval_precipitation_5,
#                                         labels=[1,2,3])
#
# interval_precipitation_10 = pd.interval_range(start=0,
#                                    freq=10, #шаг интервала
#                                    end=200000)
# df["Осадки_10мм-grup"] = pd.cut(df["Осадки, мм"],
#                                     bins=interval_precipitation_10,
#                                         labels=[1,2,3])
#
# interval_precipitation_15 = pd.interval_range(start=0,
#                                    freq=15, #шаг интервала
#                                    end=200000)
# df["Осадки_15мм-grup"] = pd.cut(df["Осадки, мм"],
#                                     bins=interval_precipitation_15,
#                                         labels=[1,2,3])
#
# interval_precipitation_20 = pd.interval_range(start=0,
#                                    freq=20, #шаг интервала
#                                    end=200000)
# df["Осадки_20мм-grup"] = pd.cut(df["Осадки, мм"],
#                                     bins=interval_precipitation_20,
#                                         labels=[1,2,3])
#
# # """ОСВЕЩЕНИЕ"""
# df['Естественное освещение'] = df['Естественное освещение'].astype('category') # Меняем тип данных
#
# """СОРТИРОВКА ПО РУБЕЖАМ"""

# option_1 = df[(df["Рубеж"] == 3321)]
# option_2 = df[(df["Рубеж"] == 3111)]
# option_3 = df[(df["Рубеж"] == 7321)]
# option_4 = df.loc[df["Рубеж"].isin([4011, 4021, 3211, 3221])]
# option_5 = df[(df["Рубеж"] == 5311)]
# option_6 = df[(df["Рубеж"] == 421)]
# option_7 = df[(df["Рубеж"] == 7331)]
# option_8 = df.loc[df["Рубеж"].isin([1511, 1541, 4111, 111, 5321, 821, 3121, 411, 431, 7311, 7341])]
# option_9 = df.loc[df["Рубеж"].isin([1521, 1531, 121])]
# option_10 = df.loc[df["Рубеж"].isin([5331, 811])]
# option_11 = df[(df["Рубеж"] == 3311)]
# option_12 = df[(df["Рубеж"] == 4221)]
# option_13 = df.loc[df["Рубеж"].isin([5211, 1141, 531])]
# option_14 = df[(df["Рубеж"] == 1121)]
# option_15 = df.loc[df["Рубеж"].isin([2521, 521])]
# option_16 = df.loc[df["Рубеж"].isin([5111, 5121, 3441])]
# option_17 = df[(df["Рубеж"] == 5411)]
# option_18 = df[(df["Рубеж"] == 5431)]
# option_19 = df.loc[df["Рубеж"].isin([1111, 1131, 1931, 1821])]
# option_20 = df.loc[df["Рубеж"].isin([2221, 3511])]
# option_21 = df.loc[df["Рубеж"].isin([5221, 3821])]
# option_22 = df.loc[df["Рубеж"].isin([5231, 3911, 2511, 511])]
# option_23 = df[(df["Рубеж"] == 931)]
# option_24 = df[(df["Рубеж"] == 2021)]
# option_25 = df[(df["Рубеж"] == 1311)]
# option_26 = df[(df["Рубеж"] == 3921)]
# option_27 = df[(df["Рубеж"] == 2111)]
# option_28 = df[(df["Рубеж"] == 1421)]
# option_29 = df.loc[df["Рубеж"].isin([2411, 2321, 1211])]
# option_30 = df.loc[df["Рубеж"].isin([711, 921, 941, 2911, 1711, 1731, 1921, 1941, 1811, 3531, 3541, 2431, 1331, 2311, 1231, 3411, 3431, 2531, 2541, 5421])]
# option_31 = df[(df["Рубеж"] == 3711)]
# option_32 = df.loc[df["Рубеж"].isin([911, 1011, 1031])]
# option_33 = df.loc[df["Рубеж"].isin([1721, 1411, 1431, 1911, 2211, 3521, 2421, 1321, 2331, 1221, 3421])]
# option_34 = df[(df["Рубеж"] == 1021)]
# option_35 = df[(df["Рубеж"] == 3721)]
# option_36 = df[(df["Рубеж"] == 611)]
# option_37 = df[(df["Рубеж"] == 2921)]
# option_38 = df.loc[df["Рубеж"].isin([2031, 2121])]
# option_39 = df.loc[df["Рубеж"].isin([311, 321])]
# option_40 = df[(df["Рубеж"] == 721)]
# option_41 = df[(df["Рубеж"] == 3811)]
# option_42 = df[(df["Рубеж"] == 2011)]
# option_43 = df[(df["Рубеж"] == 621)]

# # print(option_1)
# # df.info()
# option = (
# option_1,
# option_2,
# option_3,
# option_4,
# option_5,
# option_6,
# option_7,
# option_8,
# option_9,
# option_10,
# option_11,
# option_12,
# option_13,
# option_14,
# option_15,
# option_16,
# option_17,
# option_18,
# option_19,
# option_20,
# option_21,
# option_22,
# option_23,
# option_24,
# option_25,
# option_26,
# option_27,
# option_28,
# option_29,
# option_30,
# option_31,
# option_32,
# option_33,
# option_34,
# option_35,
# option_36,
# option_37,
# option_38,
# option_39,
# option_40,
# option_41,
# option_42,
# option_43
#     )

# sheets = {'Group1': option_1,
#           'Group2': option_2,
          # 'Group3': option_3,
          # 'Group4': option_4,
          # 'Group5': option_5,
          # 'Group6': option_6,
          # 'Group7': option_7,
          # 'Group8': option_8,
          # 'Group9': option_9,
          # 'Group10': option_10,
          # 'Group11': option_11,
          # 'Group12': option_12,
          # 'Group13': option_13,
          # 'Group14': option_14,
          # 'Group15': option_15,
          # 'Group16': option_16,
          # 'Group17': option_17,
          # 'Group18': option_18,
          # 'Group19': option_19,
          # 'Group20': option_20,
          # 'Group21': option_21,
          # 'Group22': option_22,
          # 'Group23': option_23,
          # 'Group24': option_24,
          # 'Group25': option_25,
          # 'Group26': option_26,
          # 'Group27': option_27,
          # 'Group28': option_28,
          # 'Group29': option_29,
          # 'Group30': option_30,
          # 'Group31': option_31,
          # 'Group32': option_32,
          # 'Group33': option_33,
          # 'Group34': option_34,
          # 'Group35': option_35,
          # 'Group36': option_36,
          # 'Group37': option_37,
          # 'Group38': option_38,
          # 'Group39': option_39,
          # 'Group40': option_40,
          # 'Group41': option_41,
          # 'Group42': option_42,
          # 'Group43': option_43
          # }


"""Запись в ексель на каждый лист"""



for sheet_name in sheets.keys():
    df_cor_phik = sheets[sheet_name]
    print(df_cor_phik)

    df_cor_phik = df_cor_phik.phik_matrix()

    writer = pd.ExcelWriter('./cor.xlsx', engine='xlsxwriter')
    df_cor_phik.to_excel(writer, sheet_name=sheet_name, index=False)
    writer.save()


df.to_csv('correl1.csv', header=True, index=True, sep=';', mode='w', encoding="utf-8-sig")


df = pd.read_csv('correl1.csv', sep=';')
# print(df)
# exit(1)


df_cor_phik = df.phik_matrix()
df_cor_phik.to_csv('correl.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")

# for df_cor_phik in df:
#

exit(1)

"""Смотрим гистограмму нужного раздела"""
# df["t (воздух)"].plot(kind="hist")
# plt.show()

"""Получить общие статистические характеристики непрерывных данных"""
# print(df.describe())

"""Получить обобщенное содержание столбца"""
# print(df["t (воздух)"].value_counts(dropna=False))

"""Фильтрация по квантилю (обрезаем данные с концов)"""

# upper_limit = df["t (воздух)"].quantile(0.05)  # верхний предел от 0,05 до 1
# lower_limit = df["t (воздух)"].quantile(0.95)# нижний предел от 0 до 0,95
# print(df[df["t (воздух)"].between(upper_limit, lower_limit)]["t (воздух)"].hist())
# plt.show()


"""Фильтрация по значению столбца. Например берем "Интенсивность" от 2500 до 3000"""
# df_2500_3000 = df[df['Интенсивность'] > 2500]
# df_2500_3000 = df_2500_3000[df['Интенсивность'] < 3000]
# print(df_2500_3000)

"""Сводники"""
# Сводные таблицы

# Агрегирование столбцов. Сортируем интенсивность от 2500 до 3000 и подбираем под эти значения только те столбцы, котрые нужны приминив при этом нужные расчеты для этих столюцов
# df2_2500_3000 = df_2500_3000.groupby(["Интенсивность"]).agg({
#   "Осадки, мм": "last",
#   "t (воздух)": "last",
#   "Разделитель направлений движения": "last",
#   "Спуск (за 100 м до контр. Участ) ‰": "last",
#   "Кол.ПРАВ полос": "last"
# }).reset_index()

# # Выбираем только нужные столбцы (колонки)
# tmp_df = df[["Интенсивность"] + ["t (воздух)"] + ["Спуск (за 100 м до контр. Участ) ‰"] + ["Кол.ПРАВ полос"]]
# #Сортируем по признакам столбцов
# tmp_df = tmp_df[tmp_df["Интенсивность"] >= 1000]
# tmp_df = tmp_df[tmp_df["Интенсивность"] < 3000]
# tmp_df.sort_values("Интенсивность", ascending=True, inplace=True)
# tmp_df = tmp_df[tmp_df["t (воздух)"] < 10]
# tmp_df = tmp_df[tmp_df["Спуск (за 100 м до контр. Участ) ‰"] > 10]
# tmp_df = tmp_df[tmp_df["Кол.ПРАВ полос"] != 1] # Все кроме 1
# print(tmp_df)
# # Строим сводную таблицу (это неудачный пример)
# print(pd.pivot_table(tmp_df, values="Интенсивность", index="Спуск (за 100 м до контр. Участ) ‰", columns='t (воздух)', aggfunc=np.sum, fill_value=0))

"""СВОДНИКИКИ ДЛЯ НЕПРЕРЫВНЫХ ПЕРЕМЕННЫХ"""
# разбить на 5 ровных интервалов Интенсивность
# df["Интенсивность_grop"] = pd.cut(df["Интенсивность"],5)
# # count - считаем количество попаданий в интервал
# # mean - считаем средние значения
# # Сортируем по интенсивности все что в []
# df.groupby("Интенсивность_grop")["t (воздух)",
#                                   "Время суток"
#                                                 ].agg(["count",
#                                                         "mean",
#                                                          # "sum"
#                                                          ])
#
# print(df.groupby("Интенсивность_grop")["t (воздух)"].agg(["count", "mean",]))
#Строим график Интенсивности

# print(df["Интенсивность"].hist())
# plt.show()

# Можно выборку разбить на 5 одинаковых по размеру интервала и посчитать количество попавших в них данных/переменных
# df["Интенсивность_grop"] = pd.cut(df["Интенсивность"],5)
# print(df.groupby("Интенсивность_grop")["t (воздух)"].agg(["count", "mean"]))
# # А можно выборку разбить на 5 неодинаковых но с равным количеством попавших в него данных/переменных
# df["Интенсивность_grop_q"] = pd.qcut(df["Интенсивность"],5)
# print(df.groupby("Интенсивность_grop_q")["t (воздух)"].agg(["count", "mean"]))

# Строим график средних значений величины температуры воздуха в разных диапазонах интенсивности
# t = df.groupby("Интенсивность_grop_q")["t (воздух)"].agg(["count", "mean"])
# print(t)
# print(t["mean"].plot())
# plt.show()


print(df)
df.info()

"""КОРРЕЛЯЦИЯ (только линейная Пирсона)"""
# Однако, такие сязи как парабола или другие нелинейные зависимости корреляция не определит, поэтому такой подсчет корреляции нельзя назвать разведывательным анализом.
# При помощи корреляции можно только замерить силу ЛИНЕЙНЫХ связей.
# q = df.corr()
# q.to_csv('correl.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")
# print(q)
#
# Для наглядности визуализируем данные корреляции
# import seaborn as sns
# Посмотреть заголовки
# print(df.columns)
# # Строим и подкрашиаем матрицу корреляции
# print(sns.heatmap(q, annot = True).plot())
# # Сохранить в файл
# # plt.savefig('saved_figure.jpg', dpi=100)
# plt.show()



"""КОРРЕЛЯЦИЯ (разведывательный анализ, нелинейный Фик Фк)"""
import phik
from phik.report import plot_correlation_matrix
from phik import report
# df = df.phik_matrix()
# print("КОРРЕЛЯЦИЯ (разведывательный анализ, нелинейный Фик Фк)", df)
# df.to_csv('correl1.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")

# def option (option, df):
#     while option in df:
