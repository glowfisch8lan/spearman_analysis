import datetime
import pandas as pd
from scipy.stats import spearmanr
import numpy as np

print("Чтение файла")
df = pd.read_excel('files/Restruct_25.xlsx', sheet_name="1311", engine='openpyxl')
df.to_csv('files/int.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")
"""Удаляем лишние столбцы"""
df = df.drop(columns=['Дата и время', 'Рубеж'], axis=1)
# print(df['Осадки мм'])
df['Осадки мм'] = df['Осадки мм'].replace(np.NaN, 0)
df['Осадки мм'] = df['Осадки мм'].replace([0], 150)

df["Ветер, скор, м/с"] = df["Ветер, скор, м/с"].replace(np.NaN, 0)
# print(df['Ветер, напр, град'])

"""Определяем списки анализируемых вариантов и интервалов"""
list_int = [100, 200, 250, 300, 400, 500, 600] # интенсивность
list_temp = [5, 10, 15, 20, 25] # температура
list_time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] # время
list_day = [1, 2, 3, 4, 5, 6, 7] # день

list_pressure = [5, 10, 15] # Парциальное давление водяного пара, P (парц)
list_humidity = [10, 20, 30, 50] # Относительная влажность воздуха (ϕ), ϕ (%)
list_saturation = [5, 10, 15] # Дефицит насыщения,  Дефицит насыщ, г,Па

list_stations = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # Давление на уровне станции, P (ур, станции)
list_sea = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] # Давление на уровне моря, Р (ур, моря)
list_wind_speed = [2, 3, 4, 5]  # Скорость ветра

"""Создаем список интервалов для направления ветра и присваиваем каждому интервалу значение от 1 до 8"""
def direction_wind_to_matrix(float):  # Направление ветра
    if 22.5 >= float >= 0:
        matrix = 1
    elif 67.5 >= float > 22.5:
        matrix = 2
    elif 112.5 >= float > 67.5:
        matrix = 3
    elif 157.5 >= float > 112.5:
        matrix = 4
    elif 202.5 >= float > 157.5:
        matrix = 5
    elif 247.5 >= float > 202.5:
        matrix = 6
    elif 292.5 >= float > 247.5:
        matrix = 7
    elif 337.5 >= float > 292.5:
        matrix = 8
    elif float > 337.5:
        matrix = 1
    else:
        matrix = -1
        print('no direction value')
    return matrix

"""Меняем градусы градусное значение направление ветра на порядковый номер класса"""
x = 0
for unit in df['Ветер, напр, град']:
    df.loc[x:x, 'Ветер, напр, град'] = direction_wind_to_matrix(unit)
    x += 1
list_direction_wind = [1, 2, 3, 4, 5, 6, 7, 8]  # Направление ветра
list_precipitation = [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] # Осадки
# list_precipitation = [100] # Осадки
"""Создаем базу с ключами"""
# data = {'p_precipitation': [], 'rho_precipitation': [], 'interval_precipitation': [],'int': []}
data = {'p': [],'rho': [],'day': [],'time': [],'t_air': [],'t_soil': [],'t_dew': [],'int': []}
"""Генерируем интервалы для интенсивности"""
for interval_int in list_int:
    interval_range = pd.interval_range(start=0, freq=interval_int, end=200000)
    df["Инт_шаг"] = pd.cut(df["Интенсивность"], bins=interval_range, labels=[1, 2, 3])


    # """Генерируем различные парционного давления"""
    # for interval_pressure in list_pressure:
    #     interval_pressure_range = pd.interval_range(start=0, freq=interval_pressure, end=100)
    #     df["interval_pressure"] = pd.cut(df["P (парц)"], bins=interval_pressure_range, labels=[1, 2, 3])
    # """Генерируем различные варианты валжости воздуха"""
    # for interval_humidity in list_humidity:
    #     interval_humidity_range = pd.interval_range(start=0, freq=interval_humidity, end=1500)
    #     df["interval_humidity"] = pd.cut(df["ϕ (%)"], bins=interval_humidity_range, labels=[1, 2, 3])
    # """Генерируем различные варианты дефицита насыщения"""
    # for interval_saturation in list_saturation:
    #     interval_saturation_range = pd.interval_range(start=0, freq=interval_saturation, end=1500)
    #     df["interval_saturation"] = pd.cut(df["P (ур, станции)"], bins=interval_saturation_range, labels=[1, 2, 3])
    # for interval_stations in list_stations:
    #     interval_stations_range = pd.interval_range(start=0, freq=interval_stations, end=1500)
    #     df["interval_stations"] = pd.cut(df["P (ур, станции)"], bins=interval_stations_range, labels=[1, 2, 3])
    # for interval_sea in list_sea:
    #     interval_sea_range = pd.interval_range(start=0, freq=interval_sea, end=1500)
    #     df["interval_sea"] = pd.cut(df["Р (ур, моря)"], bins=interval_sea_range, labels=[1, 2, 3])
    # """Генерируем интервалы для скорости ветра"""
    # for interval_wind_speed in list_wind_speed:
    #     interval_wind_speed_range = pd.interval_range(start=0, freq=interval_wind_speed, end=2000, closed='left')
    #     t0 = pd.cut(df["Ветер, скор, м/с"], bins=interval_wind_speed_range, labels=[1, 2, 3])
    #     df["interval_wind_speed"] = t0
    #     """Генерируем различные варианты направления ветра"""
    #     for interval_direction_wind in list_direction_wind:
    #         df1 = df[(df["Ветер, напр, град"] == interval_direction_wind)]
    """Генерируем интервалы для осадков"""
    for interval_precipitation in list_precipitation:
        interval_range_precipitation = pd.interval_range(start=0, freq=interval_precipitation, end=200000, closed='left')
        df["interval_precipitation"] = pd.cut(df["Осадки мм"], bins=interval_range_precipitation, labels=[1, 2, 3])
        """Генерируем различные варианты времени суток"""
        for interval_time in list_time:
            df1 = df[(df['Время суток'] == datetime.time(interval_time, 0))]
            """Генерируем различные варианты дней недели"""
            for interval_day in list_day:
                df2 = df1[(df1['День недели'] == interval_day)
                          # & (df1['Осадки мм'] == 0)
                ]

                # print(df3["interval_wind_speed"])
                """Ранговая корреляция Спирмана"""
                """Вычислить ранговую корреляцию Спирмена и соответствующее значение p"""
                # print(df3["Инт_шаг"], df3["interval_wind_speed"])
                x1 = df2["Инт_шаг"]
                x2 = df2["interval_precipitation"]

                rho, p = spearmanr(x1, x2, nan_policy='omit')


                # print('\n\n==============================================================================')
                # print('FOUNDED!!!')
                # print('ii ' + str(interval_int))
                # print('ai ' + str(interval_wind_speed))
                # print('so ' + str(interval_direction_wind))
                # print('de ' + str(interval_time))
                # print('pr ' + str(interval_day))
                # print('hu ' + str(interval_humidity))
                # print('sa ' + str(interval_saturation))
                # print('ti ' + str(interval_time))
                # print('id ' + str(interval_day))

                """Выделяем только значимые p и rho"""
                if (p < 0.05) & (rho > 0.7 or rho < -0.7):




                    # print('\n\n==============================================================================')
                    # print('FOUNDED!!!')
                    # print('id ' + str(interval_day))
                    # print('it ' + str(interval_time))
                    # print('ia ' + str(interval_air))
                    print('ii ' + str(interval_int))


                    #напечатать ранговая корреляция Спирмена и p-значение
                    # print("Коэффициент ранговой корреляции Спирмана = ",rho)
                    # print('{:0.16f}'.format(p))
                    # print('===========================================================================')
                    """Записываем значения различных вариантов, интервалов и лучших показателей корреляции в созданную базу """

                    data['p_precipitation'].append('{:0.16f}'.format(p))
                    data['rho_precipitation'].append(rho)
                    data['interval_precipitation'].append(interval_precipitation)
                    data['int'].append(interval_int)









"""Записываем базу в файл"""
frame = pd.DataFrame(data)  # собираем фрейм
frame.to_csv('correl.csv', header=True, index=False, sep=';', encoding="utf-8-sig")

