'''Записываем значения в диапазоне'''
def to_binary_range(value, ranges, to_float):
    str = ''
    for range in ranges:
        if range[0] <= value <= range[1]:
            str += '1'
        else:
            str += '0'
    if to_float:
        return array_str_to_float(str)

    return str

 # Интервалы направления ветра (градусы)
# [[337.6, 360 + 0, 22.5], # С
# [22.6, 67.5], # СВ
# [67.6, 112.5], # В
# [112.6, 157.5],  # ЮВ
# [157.6, 202.5],  # Ю
# [202.6, 247.5],  # ЮЗ
# [247.6, 292.5],  # З
# [292.6, 337.5]] # СЗ
def direction_wind_to_matrix(float): # Направление ветра
    matrix = {
        'С': 0,
        'СВ': 0,
        'В': 0,
        'ЮВ': 0,
        'Ю': 0,
        'ЮЗ': 0,
        'З': 0,
        'СЗ': 0
    }
    if 22.5 >= float >= 0:
        matrix['С'] = 1
    elif 67.5 >= float > 22.5:
        matrix['СВ'] = 1
    elif 112.5 >= float > 67.5:
        matrix['В'] = 1
    elif 157.5 >= float > 112.5:
        matrix['ЮВ'] = 1
    elif 202.5 >= float > 157.5:
        matrix['Ю'] = 1
    elif 247.5 >= float > 202.5:
        matrix['ЮЗ'] = 1
    elif 292.5 >= float > 247.5:
        matrix['З'] = 1
    elif 337.5 >= float > 292.5:
        matrix['СЗ'] = 1
    elif float > 337.5:
        matrix['С'] = 1
    else:
        print('no direction value')
    return matrix.values()


def to_binary_equal(value, states, to_float):
    """Записываем значения равные"""
    str = ''
    for state in states:
        if (value == state).all():
            str += '1'

        else:
            str += '0'
    if to_float:
        return array_str_to_float(str)

    return str


def array_str_to_float(str):
    return [float(x) for x in str]
