import numpy as np
import timeit

#light
print("\n#1", end ="\n\n\n")
fname="train_vector_1.csv" #имя файла ввода
my_array = np.loadtxt(fname) #считывае данных в массив
print(type(my_array)) #вывод типа данных

print("\n#2", end ="\n\n\n")
def mean(a): #рассчёт среднего 
  return sum(a) / len(a) #сумма элементов на длину массива

my_list = my_array.tolist() # преобразование к list

#print(np.mean(my_array)) #Стандартная функция для сравнения полученных значений
print(mean(my_array)) #Примените ее к подгруженному массиву 
print(mean(my_list)) #Примените функцию к списку 

#время исполнения
#используется глобальная области видимости
#stmt - вызов функции с нужным параметром (list or np)

time_np = timeit.timeit(stmt="mean(my_array)", number=1000, globals=globals()) 
#время исполнения np
time_list = timeit.timeit(stmt="mean(my_list)", number=1000, globals=globals()) 
#время исполнения list
print(time_list - time_np) #разница времен для 1000 (number) вызовов

print("\n#3", end ="\n\n\n")
#iris.csv
fname="iris.csv" #имя файла ввода
my_2d_array = np.loadtxt(fname, #имя файла
skiprows=1, #первую строку игнорируем
usecols=(1, 2, 3, 4), #берем 4 колонки
delimiter = "," #знак разделитель
) #считывае данных в массив

#print(my_2d_array) #полученный массив из файла
print(np.sum(my_2d_array, axis = 0)) #axis = 0 сумма элементов по столбцам

print("\n#4", end ="\n\n\n")
arr = np.random.randint(11, 40, (3,3), int)
print(arr) #np массив 3 на 3 с числами от 11 до 40
print(arr[np.where(arr < 20)]) #элементы меньше 20, используется фильтрация
print(np.sum(arr)) #сумма всех элементов

print("\n\#5", end ="\n\n\n")

dtype = [('name', 'S10'), ('age', int), ('marks', float)] 
#Типы данных
values = [('Arthur', 18, 4.1), ('Lancelot', 19, 3.8), ('Merlin', 17, 3.8)] 
#значения у каждого студента

students = np.array(values, dtype=dtype) 
#Создание массива студентов
print(np.sort(students, order=['marks', 'age'])) 
#сортировка по средненему баллу, затем по возрасту

#Pro
print("Pro", end="\n")
print("\n#1", end="\n\n\n\n")
fname="iris.csv" #имя файла ввода
my_array = np.loadtxt(fname, #имя файла
skiprows=1, #первую строку игнорируем
usecols=(1, 2, 3, 4), #берем 4 колонки
delimiter = "," #знак разделитель
) #считывае данных в массив

my_generated_array = np.random.sample(my_array.shape) 
#генерация массива со случайными числами, размерности считанного массива 

print(my_generated_array.shape, my_array.shape)
#вывод размерностей получившегося массива и исходного

print("\n#2", end="\n\n\n\n")
mult = my_generated_array * my_array #поэлементное умножение
print(mult)
c = np.concatenate((my_generated_array, my_array), axis=1) #склейка по строкам axis = 1
#print(c) #склееный массив
#print(c.shape)
print(np.split(c, 3)) #делим на 3 равные части

print("\n#3", end="\n\n\n\n")

print(my_array[ np.logical_and( my_array > 3 , my_array < 5 )])
#Построим логическую матрицу со следующим условием: m>3 and m<5, в Numpy нельзя напрямую записать такое условие, поэтому воспользуемся функцией logical_and()

print("\n#4", end="\n\n\n\n")
array_3d = np.random.randint(15, 37, (2, 3, 4), int) #создание 3х мерного массива (размерность - 3ий параметр, диапазон значений от 1 параметр до 2го параметра, последний параметр - тип значений)
print(array_3d)

print("\n#5", end="\n\n\n\n")
b = np.full_like(array_3d.astype(str), 'medium') #заполняем массив В значениями medium
b[array_3d < 20] = 'small' #если меньше 20 значение перезаписываем туда значение 'Small'
b[array_3d > 30] = 'large' #если больше 30 значение перезаписываем туда значение 'Large'
print(b) #результат

print("\n#6", end="\n\n\n\n")
array6 = np.random.randint(0, 5, (10)) #одномерный массив значений от 0 до 5
# можно использовать array6 = np.random.sample(10)                                    

print(array6) #получившийся массив
print(np.sum(array6[2:7])) 
#сумма c 3 (2, т.к. нумерация с нуля) по 7 (не вкл правую границу) элемент, используя срез
print(array6[-1]**2 + array6[-2]**2) #отрицательные индексы - последний -1, предпоследний -2