import numpy as np
while True:
    try:
        cr_num = int(input("Введите кол-во критериев: "))
        break
    except ValueError:
        print('Неверное значение')
s_matr = np.eye(cr_num)#Создаём 1-ную матрицу
#Заполняем матрицу коэффициентами сравнений
a = 1   #счётчик для пропуска уже заполненных значений
for i in range(a, cr_num+1):
    for j in range(a+1, cr_num+1):
        while True:
            try:
                #Заполняем каждый элемент строки матрицы
                s_matr[i-1][j-1] = round(float(input('Введите сравнение К{0}-К{1}:'.format(i, j))), 3)
                break
            except ValueError:
                print('Неверное значение')
        # Заполняем ячейки для обратного отношения (К1-К2 -> К2-К1)
        s_matr[j-1][i-1] = round(s_matr[i-1][j-1]**(-1), 2)
    a += 1
# Создаём список сумм строки
comp_list = [round(sum(j),2) for j in s_matr]
out_list = [round(n/sum(comp_list), 2) for n in comp_list]
if (sum(out_list)) != 1.0:
    index = out_list.index(max(out_list))
    k = (sum(out_list)) - 1.0
    out_list[index] -= k
print('Весовые коэффициенты')
for ind in out_list:
    print(ind, end=' ')

