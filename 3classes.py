classes = [3, 5, 6]
sum = 0
for class1 in classes: # для переменой класс1, которая тут же объявляется, в списке classes
    sum += class1 // 2 + class1 % 2 #каждый проход добавляем сумму, делённую на 2 нацело + что осталось
print (sum)