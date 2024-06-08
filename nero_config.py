import functions as f
import intervals
import numpy as np

def get_input_names():
    return [
        # 'Дата и время',
        # 'День недели',
        'Время суток',
        # 't (воздух)',
        # 't (почва)',
        # 't (росы)',
        # 'P (парц)',
        # 'ϕ (процент)',
        # 'Дефицит насыщ. г.Па',
        # 'P (ур, станции)',
        # 'Р (ур, моря)',
        'Видимость, шифр',
        # 'Погода, шифр (ww)',
        # 'Ветер напр. град.',
        # 'Ветер, скор, м/с',
        # 'Осадки, мм',
        'Естественное освещение',
        # 'Планировочное кол. прям. полос',
        # 'Фактическое (обеспечиваемое)  кол. прям.',
        # 'Кол. ЛЕВ полос',
        # 'Кол.ПРАВ полос',
        # 'Вид ЛЕВ. ПСП: 0 с основной; 1 карман; 0.1 - и то и то',
        # 'Вид ПРАВ. ПСП: 0 с основной; 1 карман; 0.1 - канализир движ',
        # 'Длина Левого кармана ПРС',
        # 'Длина Правого кармана ПРС',
        # 'Вид ДД (одностороннее 1, двухстороннее 2)',
        # 'Расстояние до Парковки',
        # 'Вид постановки на парковку (0, 1, 2)',
        # 'Вид парковки (0, 1, 2)',
        # 'Подъем (за 100 м до контр. Участ) ‰',
        # 'Спуск (за 100 м до контр. Участ) ‰',
        # 'Выезд с тупиковой улицы',
        # 'Ширина проектная (все полосы: и лев, и прав)',
        # 'Ширина прямого направления (без лев и прав)',
        # 'Сужение прямого направления за 100 метров до рубежа контроля',
        #'Широта',
        #'Долгота',
        # 'Разделитель направлений движения',
        # 'Район',
        # 'Расстояние до конца авт. Ост. По ходу движения',
        # 'Тип автоб остан (0 - без кармана, 1- карман)',
        # 'Тип перекрестка (т, у, х, 0, ж)',
        #'Светофорное регулирование(0- нет, 1- есть)',
        # 'КОЭФ  Фактическое (обеспечиваемое)  Кол. Прям.',
        # 'КОЭФ  Сужения прямого направления за 100 метров до рубежа контроля',
        # 'Коэф левоповоротн',
        # 'Коэф правоповорот',
        #'КОЭФ с уч лев, прав пол и Фактическое (обеспечиваемое)  Кол. Прям.',
    ]



def get_output_names():
    return ["0...200", "201...400", "401...600", "601...800", "801...1000",
            "1001...1200", "1201...1400", "1401...1600", "1601...1800", "1801...2000",
             "2001...2200", "2201...2400", "2401...2600", "2601...2800", "2801...3000",
             "3001...3200", "3201...3400", "3401...3600", "3601...3800", "3801...4000",
             "4001...4200", "4201...4400", "4401...4600", "4601...4800", "4801...5000", "5001...и_более"]




def validate(x):
    return x


def encoders():
    to_float = True
    """Правила обработки и преобразования"""
    return {
        # 'Дата и время': lambda value: f.to_binary_range(value, intervals   ???????
        # "День недели": lambda value: f.to_binary_equal(value, intervals.day_of_the_week(), to_float),
        "Время суток": lambda value: f.to_binary_equal(value, intervals.times_of_day(), to_float),
        # "Интенсивность": lambda value: f.to_binary_range(value, intervals.get_intensive_interval(),to_float),
        # 't (воздух)': lambda value: f.to_binary_range(value, intervals.get_air_temp_interval(), to_float),
        # 't (почва)': lambda value: f.to_binary_range(value, intervals.get_air_temp_interval(), to_float),
        # 't (росы)': lambda value: f.to_binary_range(value, intervals.get_air_temp_interval(), to_float),
        # 'P (парц)': lambda value: f.to_binary_range(value, intervals.get_pressure_interval(), to_float),
        # 'ϕ (процент)': lambda value: f.to_binary_range(value, intervals.get_air_humidity(), to_float),
        # 'Дефицит насыщ. г.Па': lambda value: f.to_binary_range(value, intervals.get_saturation_deficit_interval(), to_float),
        # 'P (ур, станции)': lambda value: f.to_binary_range(value, intervals.get_atmosphere_pressure(), to_float),
        # 'Р (ур, моря)': lambda value: f.to_binary_range(value, intervals.get_atmosphere_pressure(), to_float),
        'Видимость, шифр': lambda value: f.to_binary_equal(value, intervals.get_visibility(), to_float),
        # 'Погода, шифр (ww)': lambda value: f.to_binary_equal(value, intervals.weather_cipher_ww(), to_float),
        # 'Ветер напр. град.': lambda value: f.direction_wind_to_matrix(value),
        # 'Ветер, скор, м/с': lambda value: f.to_binary_range(value, intervals.get_wind_speed(), to_float),
        # 'Осадки, мм': lambda value: f.to_binary_range(0 if np.isnan(value) else value, intervals.precipitation(), to_float),
        'Естественное освещение': lambda value: f.to_binary_equal(value, intervals.daylight(), to_float),
        # 'Планировочное кол. прям. полос': lambda value: f.to_binary_equal(value, intervals.lanes_according_plan(), to_float),
        # 'Фактическое (обеспечиваемое)  кол. прям.': lambda value: f.to_binary_equal(value, intervals.lanes_according_plan(), to_float),
        # 'Кол. ЛЕВ полос': lambda value: f.to_binary_equal(value, intervals.number_of_lanes_per_turn(), to_float),
        # 'Кол.ПРАВ полос': lambda value: f.to_binary_equal(value, intervals.number_of_lanes_per_turn(), to_float),
        # 'Вид ЛЕВ. ПСП: 0 с основной; 1 карман; 0.1 - и то и то': lambda value: f.to_binary_equal(value, intervals.turn_lane_view (), to_float),
        # 'Вид ПРАВ. ПСП: 0 с основной; 1 карман; 0.1 - канализир движ': lambda value: f.to_binary_equal(value, intervals.turn_lane_view (), to_float),
        # 'Длина Левого кармана ПРС': lambda value: f.to_binary_range(0 if np.isnan(value) else value, intervals.caraman_length(), to_float), # "0 if np.isnan(value) else value" - если нет  значений, то ячейка =0
        # 'Длина Правого кармана ПРС': lambda value: f.to_binary_range(0 if np.isnan(value) else value, intervals.caraman_length(), to_float), # "0 if np.isnan(value) else value" - если нет  значений, то ячейка =0
        # 'Вид ДД (одностороннее 1, двухстороннее 2)': lambda value: f.to_binary_equal(value, intervals.type_of_traffic(), to_float),
        # 'Расстояние до Парковки': lambda value: f.to_binary_range(value, intervals.distance_to_parking(), to_float),
        # 'Вид постановки на парковку (0, 1, 2)': lambda value: f.to_binary_equal(value, intervals.type_and_method_of_parking (), to_float),
        # 'Вид парковки (0, 1, 2)': lambda value: f.to_binary_equal(value, intervals.type_and_method_of_parking (), to_float),
        # 'Подъем (за 100 м до контр. Участ) ‰': lambda value: f.to_binary_range(0 if np.isnan(value) else value, intervals.ascent_and_descent(), to_float),
        # 'Спуск (за 100 м до контр. Участ) ‰': lambda value: f.to_binary_range(0 if np.isnan(value) else value, intervals.ascent_and_descent(), to_float),
        # 'Выезд с тупиковой улицы': lambda value: [value],
        # 'Ширина проектная (все полосы: и лев, и прав)': lambda value: f.to_binary_range(value, intervals.design_road_width (), to_float),
        # 'Ширина прямого направления (без лев и прав)': lambda value: f.to_binary_range(value, intervals.design_road_width (), to_float),
        # 'Сужение прямого направления за 100 метров до рубежа контроля': lambda value: f.to_binary_range(value, intervals.design_road_width (), to_float),
        # # 'Широта': lambda value: f.to_binary_range(value, intervals   ???????
        # # 'Долгота': lambda value: f.to_binary_range(value, intervals   ???????
        # 'Разделитель направлений движения': lambda value: f.to_binary_equal(value, intervals.direction_separator(), to_float),
        # 'Район': lambda value: f.to_binary_equal(value, intervals.area(), to_float),
        # 'Расстояние до конца авт. Ост. По ходу движения': lambda value: f.to_binary_range(value, intervals.distance_to_bus_stop(), to_float),
        # 'Тип автоб остан (0 - без кармана, 1- карман)': lambda value: f.to_binary_equal(value, intervals.bus_stop_type(), to_float),
        # 'Тип перекрестка (т, у, х, 0, ж)': lambda value: f.to_binary_equal(value, intervals.intersection_type(), to_float),
        # #'Светофорное регулирование(0- нет, 1- есть)': lambda value: [value],
        # # 'КОЭФ  Фактическое (обеспечиваемое)  Кол. Прям.': lambda value: f.to_binary_equal(value, intervals.coefficient_number_of_lanes(), to_float),
        # # 'КОЭФ  Сужения прямого направления за 100 метров до рубежа контроля': lambda value: f.to_binary_range(value, intervals.taper_ratio_right_and_left(), to_float),
        # # 'Коэф левоповоротн': lambda value: f.to_binary_range(value, intervals.taper_ratio_right_and_left(), to_float),
        # # 'Коэф правоповорот': lambda value: f.to_binary_range(value, intervals.taper_ratio_right_and_left(), to_float),
        # # 'КОЭФ с уч лев, прав пол и Фактическое (обеспечиваемое)  Кол. Прям.': lambda value: f.to_binary_range(value, intervals.odds_all (), to_float),
       "0...200": lambda value: [value], "201...400": lambda value: [value], "401...600": lambda value: [value], "601...800": lambda value: [value], "801...1000": lambda value: [value],
 "1001...1200": lambda value: [value], "1201...1400": lambda value: [value], "1401...1600": lambda value: [value], "1601...1800": lambda value: [value], "1801...2000": lambda value: [value],
"2001...2200": lambda value: [value], "2201...2400": lambda value: [value], "2401...2600": lambda value: [value], "2601...2800": lambda value: [value], "2801...3000": lambda value: [value],
 "3001...3200": lambda value: [value], "3201...3400": lambda value: [value], "3401...3600": lambda value: [value], "3601...3800": lambda value: [value], "3801...4000": lambda value: [value],
"4001...4200": lambda value: [value], "4201...4400": lambda value: [value], "4401...4600": lambda value: [value], "4601...4800": lambda value: [value], "4801...5000": lambda value: [value], "5001...и_более": lambda value: [value]}