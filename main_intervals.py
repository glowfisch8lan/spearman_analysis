import sys
import openpyxl
import csv
import keras as k
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import functions as f
import nero_config
from keras.models import load_model
# from keras.utils import to_categorical
from keras import models
from keras import layers
import os.path

# # w= data_frame["Ветер_напр_град"]
# w =  [45, 33, 260, 75, 360]
# print(w)
# # str = ''
# for range in w:
#     print(f.direction_wind_to_matrix(range))
# if str:
#     return array_str_to_float(str)
# # print(f.direction_wind_to_matrix(w))
# exit(1)


def dataframe_to_dict(df, data_frame):
    result = dict()
    for column in df.columns:
        values = data_frame[column].values
        result[column] = values
    return result


def make_supervised(raw_input_data, raw_output_data, df):
    return {"inputs": dataframe_to_dict(raw_input_data, df),
            "outputs": dataframe_to_dict(raw_output_data, df)}

"""Интервалы для интенсивности"""
def int ():
  def toBinary(col_int, data_frame):
    arg1ForCut = data_frame[col_int];
    arg2ForCut = [0, 200, 400, 600, 800, 1000,
                  1200, 1400, 1600, 1800, 2000,
                  2200, 2400, 2600, 2800, 3000,
                  3200, 3400, 3600, 3800, 4000,
                  4200, 4400, 4600, 4800, 5000,float("inf")]; # устанавливаем интервалы для интенсвности
    dataForDummies = pd.cut(arg1ForCut, arg2ForCut, labels=["0...200", "201...400", "401...600", "601...800", "801...1000",
                                                            "1001...1200", "1201...1400", "1401...1600", "1601...1800", "1801...2000",
                                                            "2001...2200", "2201...2400", "2401...2600", "2601...2800", "2801...3000",
                                                            "3001...3200", "3201...3400", "3401...3600", "3601...3800", "3801...4000",
                                                            "4001...4200", "4201...4400", "4401...4600", "4601...4800", "4801...5000", "5001...и_более"]); # назначаем заголовки
    dataAppend = pd.get_dummies(dataForDummies);
    dummies_int.append(dataAppend)

  dummies_int = []
  cols_int = ["Интенсивность"]
  for col_int in cols_int:
    toBinary(col_int, data_frame)
  return dummies_int


def encode(data, encoders):
    """Преобразование данных"""
    vectors = []
    for data_name, data_values in data.items():
        encoded = list(map(encoders[data_name], data_values))
        vectors.append(encoded)
    formatted = []
    for vector_raw in list(zip(*vectors)):
        vector = []
        for element in vector_raw:
            for e in element:
                vector.append(e)
        formatted.append(vector)
    return formatted


def init_data_frame(file, sheet):
    return pd.read_excel(file, sheet_name=sheet, engine='openpyxl');



def create_model_nero():
    """Создание модели"""
    # model = k.Sequential()
    # model.add(k.layers.Dense(units=32, activation="sigmoid"))  # входной слой, входных переменных
    # model.add(k.layers.Dense(units=26,
    #                          activation="sigmoid"))  # выходной слой, выходных переменных - 11, sigmoid -  сигмоидная функция активации
    # model.compile(loss="mse", optimizer="sgd", metrics=["accuracy"])
    """Альтернативная модель"""
    INPUT_DIM = 36 # определяется по количеству входов после бинаризации
    OUTPUT_DIM = 26 # определяется по количеству выxодов после бинаризации
    # Определяем модель
    model = k.models.Sequential()
    # model.add(k.layers.Dense(INPUT_DIM, activation='relu', input_dim=INPUT_DIM)) # слой из 36 нейронов
    model.add(k.layers.Dense(OUTPUT_DIM, activation='linear')) # слой из 8 нейронов
    ## Можно добавить больше слоев чтобы настроить свою модель
    # model.add(k.layers.Dense(OUTPUT_DIM, activation='softmax'))
    model.compile(loss="mse", optimizer="adam", metrics=["accuracy"])
    """Альтернативная модель 2 (НЕ РАБОТАЕТ)"""
    # # Input - Layer
    # model = models.Sequential()
    # # Input - Layer
    # model.add(layers.Dense(36, activation="relu", input_shape=(60000,)))
    # # Hidden - Layersinput shape
    # model.add(layers.Dropout(0.3, noise_shape=None, seed=None))
    # model.add(layers.Dense(50, activation="relu"))
    # model.add(layers.Dropout(0.2, noise_shape=None, seed=None))
    # model.add(layers.Dense(50, activation="relu"))
    # # Output- Layer
    # model.add(layers.Dense(1, activation="sigmoid"))
    # model.summary()
    # # compiling the model
    # model.compile(
    #     optimizer="adam",
    #     loss="binary_crossentropy",
    #     metrics=["accuracy"]
    # )
    return model


def fit_model(model, train_x, train_y):
    """"Обучение модели"""
    return model.fit(x=train_x, y=train_y, epochs=100,
                     validation_split=0.2)  # раскладываем по осям, назначаем количество эпох, validation_split=0.2 - 80% данных на тренировку и 20% на валидацию



def get_model(filename):
    print('Получаем модель')
    if os.path.exists(filename):
        model = load_model(filename)
        predictions = model.predict(encoded_inputs)
        print(predictions)


    else:
        model = create_model_nero()
        print('# Обучаем модель на тестовых данных')
        history = fit_model(model, train_x, train_y)  # История ошибок на каждом шагу обучения

        model.save(filename)
        print('\n# Оцениваем на тестовых данных')
        results = model.evaluate(test_x, test_y) # , batch_size=128 убрал
        print('test loss, test acc:', results)

    return model



# Открываем файл Excel

file = "files/Вариант№30-Restruct.xlsx"  # Обучающий файл
sheet_name = "work"
print("Открываем файл")

data_frame = init_data_frame(file, sheet_name)
data_frame.info()

""""Преобразовываем значения Nan для конкретного толбца в отдельный интервал"""
# data_frame['Разделитель направлений движения'] = data_frame['Разделитель направлений движения'].replace(np.NaN, 3)
# """"Преобразовываем значения районов к,кр,ц,ж,и в числовые значения """
# data_frame['Район']= data_frame['Район'] = data_frame['Район'].replace("ц", 1).replace("к", 2).replace("и", 3).replace("ж", 4)
# """"Преобразовываем значения Nan для конкретного толбца в отдельный интервал"""
# data_frame['Расстояние до конца авт. Ост. По ходу движения'] = data_frame['Расстояние до конца авт. Ост. По ходу движения'].replace(np.NaN, 1500)
# """"Преобразовываем значения Nan для конкретного толбца в отдельный интервал"""
# data_frame['Тип автоб остан (0 - без кармана, 1- карман)'] = data_frame['Тип автоб остан (0 - без кармана, 1- карман)'].replace(np.NaN, 2)
# """"Преобразовываем значения районов к,кр,ц,ж,и в числовые значения """
# data_frame['Тип перекрестка (т, у, х, 0, ж)'] = data_frame['Тип перекрестка (т, у, х, 0, ж)'] = data_frame['Тип перекрестка (т, у, х, 0, ж)'].replace("т", 1).replace("у", 2).replace("х", 3).replace("ж", 4)

# print(data_frame['Осадки, мм'])
# exit(1)

# Выводим бинарные значения интенсивности
dummies_int = pd.concat(int(), axis=1) #выводим бинарные значения интенсивности
data_frame = pd.concat((data_frame, dummies_int), axis=1) #присоединяем бинарные значения инт. к общим данным
# data_frame.info()



print("Получили данные из файла")
input_names = nero_config.get_input_names()
output_names = nero_config.get_output_names()


raw_input_data = data_frame[input_names]
raw_output_data = data_frame[output_names]

print("Подготавливаем полученные данные")
encoders = nero_config.encoders()

supervised = make_supervised(data_frame[input_names], data_frame[output_names], data_frame)

print("Maked supervised")
encoded_inputs = np.array(encode(supervised["inputs"], encoders))
encoded_outputs = np.array(encode(supervised["outputs"], encoders))

# np.savetxt("correl.csv", encoded_inputs, delimiter=" ; ", fmt=" %.0f ")
# np.savetxt("correl1.csv", encoded_outputs, delimiter=" ; ", fmt=" %.0f ")

# Обучение
train_x = encoded_inputs[:60000]
train_y = encoded_outputs[:60000]

# Валидация
test_x = encoded_inputs[60000:]
test_y = encoded_outputs[60000:]

print("Размерность x", train_x.shape)
print("Размерность y",train_y.shape)

# test = test_x[:3] # test = файл или объект для прогнозтрования (первые 3 значения файла)
filename = 'model_VAR_30.h5'
model = get_model(filename)


predictions = model.predict(encoded_inputs)

real_data = data_frame.iloc[0:][input_names + output_names]
real_data["0...200"] = predictions[:,0]
real_data["201...400"] = predictions[:,1]
real_data["401...600"] = predictions[:,2]
real_data["601...800"] = predictions[:,3]
real_data["801...1000"] = predictions[:,4]
real_data["1001...1200"] = predictions[:,5]
real_data["1201...1400"] = predictions[:,6]
real_data["1401...1600"] = predictions[:,7]
real_data["1601...1800"] = predictions[:,8]
real_data["1801...2000"] = predictions[:,9]
real_data["2001...2200"] = predictions[:,10]
real_data["2201...2400"] = predictions[:,11]
real_data["2401...2600"] = predictions[:,12]
real_data["2601...2800"] = predictions[:,13]
real_data["2801...3000"] = predictions[:,14]
real_data["3001...3200"] = predictions[:,15]
real_data["3201...3400"] = predictions[:,16]
real_data["3401...3600"] = predictions[:,17]
real_data["3601...3800"] = predictions[:,18]
real_data["3801...4000"] = predictions[:,19]
real_data["4001...4200"] = predictions[:,20]
real_data["4201...4400"] = predictions[:,21]
real_data["4401...4600"] = predictions[:,22]
real_data["4601...4800"] = predictions[:,23]
real_data["4801...5000"] = predictions[:,24]
real_data["5001...и_более"] = predictions[:,25]

model.summary()
print(real_data)
real_data.to_csv('output.csv', header=True, index=None, sep=';', mode='w', encoding="utf-8-sig")

# plt.title("Losses train/validation")
# plt.plot(model.fit.history["loss"], label="Train")
# plt.plot(model.fit.history["val_loss"], label="Validation")
# plt.legend()
# plt.show()
#
plt.title("Accuracies train/validation")
plt.plot(model.fit.history["accuracy"], label="Train")
plt.plot(model.fit.history["val_accuracy"], label="Validation")
plt.legend()
plt.show()

# ПРОВЕРКА СТАРАЯ


# Получить дни недели с дат(
# Tuesday –  Вторник
# Wednesday –  Среда
# Thursday –  Четверг
# Friday – Пятница
# Saturday — Суббота
# Sunday –  Воскресенье)
# week = data_frame["Дата и время"].dt.strftime('%a') # # Получить день недели из Даты и время
# print(week)
# time = data_frame["Дата и время"].dt.strftime("%H:%M:%S") # # Получить время из Даты и время
# print(time)
# data_frame.info()
# Фильтруем данные
# Precipitation = data_frame["Осадки мм"]
# print( Precipitation[(week == "Sun")&(time == "07:00:00")]) # Сортируем данные по времени и дням недели