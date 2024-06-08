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
# print(df['Осадки мм'])

"""Определяем списки анализируемых вариантов и интервалов"""
list_int = [100, 200, 250, 300, 400, 500, 600] # интенсивность
list_temp = [5, 10, 15, 20, 25] # температура
list_time = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23] # время
list_day = [1, 2, 3, 4, 5, 6, 7] # день
"""Создаем базу с ключами"""
data = {'p_air': [], 'p_soil': [], 'p_dew': [], 'rho_air': [], 'rho_soil': [],
        'rho_dew': [], 'day': [],'time': [],'t_air': [],'t_soil': [],'t_dew': [],'int': []}

"""Генерируем интервалы для интенсивности"""
for interval_int in list_int:
    interval_range = pd.interval_range(start=0, freq=interval_int, end=200000)
    df["Инт_шаг"] = pd.cut(df["Интенсивность"], bins=interval_range, labels=[1, 2, 3])
    """Генерируем интервалы для температуры воздуха"""
    for interval_air in list_temp:
        interval_t = pd.interval_range(start=-40,freq=interval_air, end=100)
        df["interval_t_air"] = pd.cut(df["t (воздух)"], bins=interval_t, labels=[1, 2, 3])
        """Генерируем интервалы для температуры почвы"""
        for interval_soil in list_temp:
            interval_t_soil = pd.interval_range(start=-40, freq=interval_soil, end=100)
            df["interval_t_soil"] = pd.cut(df["t (почва)"], bins=interval_t_soil, labels=[1, 2, 3])
            """Генерируем интервалы для температуры точки росы"""
            for interval_dew in list_temp:
                interval_t_dew = pd.interval_range(start=-40, freq=interval_dew, end=100)
                df["interval_t_dew"] = pd.cut(df["t (росы)"], bins=interval_t_dew, labels=[1, 2, 3])
                """Генерируем различные варианты времени суток"""
                for interval_time in list_time:
                    df1 = df[(df['Время суток'] == datetime.time(interval_time, 0))]
                    """Генерируем различные варианты дней недели"""
                    for interval_day in list_day:
                        df2 = df1[(df1['День недели'] == interval_day) & (df1['Осадки мм'] == 0)]
                        """Ранговая корреляция Спирмена"""
                        """Вычислить ранговую корреляцию Спирмена и соответствующее значение p"""
                        rho1, p1 = spearmanr(df2["Инт_шаг"], df2["interval_t_air"], nan_policy='omit')
                        rho2, p2 = spearmanr(df2["Инт_шаг"], df2["interval_t_soil"], nan_policy='omit')
                        rho3, p3 = spearmanr(df2["Инт_шаг"], df2["interval_t_dew"], nan_policy='omit')

                        """Выделяем только значимые p и rho"""
                        if (p1 < 0.05) & (rho1 > 0.7 or rho1 < -0.7) & \
                                (p2 < 0.05) & (rho2 > 0.7 or rho2 < -0.7) & \
                                (p3 < 0.05) & (rho3 > 0.7 or rho3 < -0.7):
                            # print('\n\n==============================================================================')
                            # print('FOUNDED!!!')
                            # print('id ' + str(interval_day))
                            # print('it ' + str(interval_time))
                            # print('ia ' + str(interval_air))
                            # print('ii ' + str(interval_int))


                            # напечатать ранговая корреляция Спирмена и p-значение
                            # print("Коэффициент ранговой корреляции Спирмана = ", rho)
                            # print('{:0.16f}'.format(p))
                            # print('===========================================================================')
                            """Записываем значения различных вариантов, 
                            интервалов и лучших показателей корреляции в созданную базу """
                            data['p_air'].append('{:0.16f}'.format(p1))
                            data['p_soil'].append('{:0.16f}'.format(p2))
                            data['p_dew'].append('{:0.16f}'.format(p3))
                            data['rho_air'].append(rho1)
                            data['rho_soil'].append(rho2)
                            data['rho_dew'].append(rho3)
                            data['t_air'].append(interval_air)
                            data['t_soil'].append(interval_soil)
                            data['t_dew'].append(interval_dew)
                            data['int'].append(interval_int)
                            data['day'].append(interval_day)
                            data['time'].append(interval_time)

"""Записываем базу в файл"""
frame = pd.DataFrame(data)  # собираем фрейм
frame.to_csv('correl.csv', header=True, index=False, sep=';', encoding="utf-8-sig")
