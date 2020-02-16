"""Решение подсмотрел, но логику понял не сразу. Пишу для закрепления"""
my_list = []
parameters = {'Название': '', 'Цена': '', 'Кол-во': '', 'Ед.изм.': ''}
analit = {'Название': [], 'Цена': [], 'Кол-во': [], 'Ед.изм.': []}
n = 0
while True:
    if input('Выход q, \n любая клавиша - продолжить').lower() == 'q':
        break
    n += 1
    for i in parameters.keys(): #неясно что подразумевается под i, это ключ или значение?
        inf = input('{}: '.format(i)) # Пока неясно, что я форматирую. Название ключа? Зачем?
        #parameters[i] = int(inf) if (i == 'Цена' or 'Кол-во') else inf #интересное оформление, но какаято ошибка в синтаксисе в конце строки
        if i == 'Цена' or 'Кол-во':
            parameters[i] = int(inf)
        #else:
        #    inf
        analit[i].append(parameters[i])
    my_list.append({n, parameters})
    print('Аналитика по товарам \n')
    for key, value in analit.items():
        print(key, value)