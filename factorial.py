n = int(input("Введите число: ")) #Вводим инпут от пользователя
 
factorial = 1 #Определяем переменную факториал
while n > 1: #пока значение введённой пользователем переменной больше одного
    factorial *= n #умножаем предыдущее значение факториала на него
    n -= 1 #уменьшаем число на 1
print("Факториал этого числа:", factorial)

