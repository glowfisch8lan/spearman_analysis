"""Интервалы для бинаризации"""


def get_air_humidity(): # Влажность
    return [[0, 29.999],
            [30, 59.999],
            [60, 89.999],
            [90, 1000000]]


def get_atmosphere_pressure(): # Атмосферное давление
    return [[0, 969.999],
            [970, 979.999],
            [980, 989.999],
            [990, 999.999],
            [1000, 1009.999],
            [1010, 1019.999],
            [1020, 1029.999],
            [1030, 1000000]]


def get_wind_speed(): # Скорость ветра
    return [[0, 1.999],
            [2, 3.999],
            [4, 5.999],
            [6, 7.999],
            [8, 100000]]


def get_visibility():# Видимость
    return [91, 92, 93, 94, 95, 96, 97, 98]


def get_pressure_interval(): # Давление над уровнем СТАНЦИИ, МОРЯ
    return [[0, 9.999],
            [10, 19.999],
            [20, 29.999],
            [30, 1000000]]

def get_intensive_interval(): # Интенсивность
    return [[0, 500],
            [501, 1000],
            [1001, 1500],
            [1501, 2000],
            [2001, 2500],
            [2501, 3000],
            [3001, 3500],
            [3501, 4000],
            [4001, 4500],
            [4501, 5000],
            [5001, 500000000]]


def get_air_temp_interval(): # температура ВОЗДУХА, ПОЧВЫ, ТОЧКИ РОСЫ
    return [[-100.0, -30.1],
            [-30.0, -25.1],
            [-25.0, -10.1],
            [-10.0, -5.1],
            [-5.0, -0.1],
            [0.0, 4.9],
            [5.0, 9.9],
            [10.0, 14.9],
            [15.0, 19.9],
            [20.0, 24.9],
            [25.0, 29.9],
            [30.0, 100.0]]


def day_of_the_week(): # День недели
    return [1, 2, 3, 4, 5, 6, 7]

# Время суток
def times_of_day():
    return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]


def get_saturation_deficit_interval(): # Дефицит насыщенности
    return [[-5, 0],
            [0.1, 5],
            [5.1, 10],
            [10.1, 15],
            [15.1, 100]]
# Погода шифр ww
def weather_cipher_ww():
    return [0, 2, 3, 4, 10, 13, 17, 20, 21, 22, 25, 26, 27, 28, 29, 30, 34, 36, 43, 44, 45, 46, 47, 50, 51, 52, 53, 60, 61, 70, 71, 73, 75, 80, 81, 83, 85, 86, 87, 91, 95, 96, 239, 257, 322]


def precipitation(): # Количество осадков
    return [[0, 9.999],
            [10, 19.999],
            [20, 29.999],
            [30, 39.999],
            [40, 100000]]

def lanes_according_plan ():   # количество полос по плану и факту
    return [0, 1, 2, 3, 4, 5]

def number_of_lanes_per_turn (): # Кол. ЛЕВ полос,  Кол.ПРАВ полос
    return [0, 0.5, 1, 2]

def turn_lane_view (): # Вид ЛЕВОЙ полосы
    return [0, 0.1, 1]

def caraman_length (): # Длина кармана ПСП
    return [[0, 0.9],
            [1, 40],
            [40.1, 80],
            [80.1, 120],
            [120.1, 160],
            [160.1, 300]]

def type_of_traffic (): # Вид дорожного движения (одностороннее, двухстороннее)
    return [1, 2]

def caraman_length (): # Длина кармана ПСП
    return [[0, 0.9],
            [1, 40],
            [40.1, 80],
            [80.1, 120],
            [120.1, 160],
            [160.1, 300]]


def distance_to_parking (): # Расстояние до парковки при наличии
    return [[0, 20],
            [20.1, 40],
            [40.1, 60],
            [60.1, 80],
            [80.1, 100],
            [100.1, 3000]]
def type_and_method_of_parking (): # Вид парковки и способ постановки на парковку автомобилей (системный)
    return [0, 1, 2]

def ascent_and_descent(): # Подъем и с пуск в, ‰
    return [[0, 5],
            [6, 15],
            [16, 25],
            [26, 35],
            [36, 45],
            [46, 55],
            [56, 65],
            [66, 75],
            [76, 85],
            [86, 300]]

def design_road_width (): # Ширина дороги проектная и фактическая + Сужение проезжей части за 100 метров до рубежа
    return [[0, 3],
            [3.1, 6],
            [6.1, 9],
            [9.1, 12],
            [12.1, 15],
            [15.1, 18],
            [21.1, 24],
            [24.1, 20000]]

def direction_separator (): # Разделитель направлений движения
    return [0, 1, 2, 3]

def area (): # районы
        return [1, 2, 3, 4]

def distance_to_bus_stop (): # Расстояние до автобусной остановки
    return [[0, 50],
            [50.1, 100],
            [100.1, 150],
            [150.1, 1000],
            [1000.1, 2000]] # Последний интервал для значений NaN

def bus_stop_type (): # Тип автобусной остановки
    return [0, 1, 2]  # 0- без кармана, 1 - с карманом, 2 - Nan

def intersection_type (): # Тип перекрестка
    return [0, 1, 2, 3, 4]

def coefficient_number_of_lanes (): # КОЭФ  Фактическое (обеспечиваемое)  Кол. Прям.
    return [0, 1, 1.5, 2, 3]

def taper_ratio_right_and_left (): # КОЭФ  Сужения прямого направления за 100 метров до рубежа контроля, Коэф левоповоротн, Коэф правоповорот
    return [[1, 1.0300],
            [1.0301, 1.0600],
            [1.0601, 1.0900],
            [1.0901, 10]]

def odds_all ():  # КОЭФ с уч лев, прав пол и Фактическое (обеспечиваемое)  Кол. Прям.
    return [[1, 1.0500], # Не учитывался 0
            [1.0501, 1.1000],
            [1.1001, 1.1500],
            [1.1501, 10]]


# 'Ветер_напр_град'
# 'Осадки_мм',
# 'Рубеж',
# 'Планировочное_Кол_Прям_Полос',
# 'Фактическое_(обеспечиваемое)_Кол_Прям',
# 'Кол_ЛЕВ_полос',
# 'Кол_ПРАВ_полос',
# 'Вид ЛЕВОГО_ПРС: 0 с основной; 1 карман; 0.1 оба',
# 'Вид ПРАВОГО ПРС: 0 с основной; 1 карман; к канализир движ',
# 'Длина Левого кармана ПРС',
# 'Длина Правого кармана ПРС',
# 'Вид ДД (одностороннее 1, двухстороннее 2)',
# 'Расстояние до Парковки',
# 'Вид постановки на парковку (0, 1, 2, 3)',
# 'Вид парковкиу (0, 1, 2)',
# 'Подъем (за 100 м до контр. Участ) ‰',
# 'Спуск (за 100 м до контр. Участ) ‰',
# 'Выезд с тупиковой улицы',
# 'Ширина проектная (все полосы: и лев, и прав)',
# 'Ширина прямого направления (без лев и прав)',
# 'Сужение прямого направления за 100 метров до рубежа контроля',
# 'Широта',
# 'Долгота',
# 'Разделитель направлений движения',
# 'Район',
# 'Расстояние до конца авт. Ост. По ходу движения',
# 'Тип автоб остан (0 - без кармана, 1- карман)',
# 'Тип перекрестка (т, у, х, 0, ж)',
# 'Светофорное регулирование(0- нет, 1- есть)',
# 'КОЭФ  Фактическое (обеспечиваемое)  Кол. Прям.',
# 'КОЭФ  Сужение прямого направления за 100 метров до рубежа контроля',
# 'КОЭФ  Сужение прямого направления за 100 метров до рубежа контроля',
# 'Коэф левоповоротн',
# 'Коэф правоповорот ',
# 'КОЭФ с уч лев, прав пол и Фактическое (обеспечиваемое)  Кол. Прям.',

