import random
	
# Цифры (Обучающая выборка)
num0 = list('111101101101111')
num1 = list('001001001001001')
num2 = list('111001111100111')
num3 = list('111001111001111')
num4 = list('101101111001001')
num5 = list('111100111001111')
num6 = list('111100111101111')
num7 = list('111001001001001')
num8 = list('111101111101111')
num9 = list('111101111001111')
	
# Список всех вышеуказанных цифр
nums = [num0, num1, num2, num3, num4, num5, num6, num7, num8, num9]

	
# Инициализация весов сети
weights = []
for i in range(10):
	weights.append([0] * 15)

	
# Порог функции активации
bias = 7
# Является ли данное число 5
def proceed(number, N):
	# Рассчитываем взвешенную сумму
	net = 0
	for i in range(15):
	    net += int(number[i])*weights[N][i]
	
	# Превышен ли порог? (Да - сеть думает, что это 5. Нет - сеть думает, что это другая цифра)
	return net >= bias
	
	# Уменьшение значений весов, если сеть ошиблась и выдала 1
def decrease(number,N):
        for i in range(15):
                # Возбужденный ли вход
                if int(number[i]) == 1:
                        # Уменьшаем связанный с ним вес на единицу
                        weights[N][i] -= 1
	
	# Увеличение значений весов, если сеть ошиблась и выдала 0
def increase(number, N):
	for i in range(15):
	# Возбужденный ли вход
	     if int(number[i]) == 1:
	# Увеличиваем связанный с ним вес на единицу
	       weights[N][i] += 1

def Train():
        # Тренировка сети
        for j in range(10):
                for i in range(1000):
                        # Генерируем случайное число от 0 до 9
                        option = random.randint(0, 9)
                        # Если получилось НЕ число 5
                        if option != j:
                        # Если сеть выдала True/Да/1, то наказываем ее
                                if proceed(nums[option],j):
                                        decrease(nums[option],j)
                        # Если получилось число 5
                        else:
                                # Если сеть выдала False/Нет/0, то показываем, что эта цифра - то, что нам нужно
                                if not proceed(nums[option],j):
                                        increase(nums[option],j)
                        # Вывод значений весов
                        #print(weights)


Train()
stroka = input("Введите число в формате 111100111000111: ")

print("Разпознавание числа")
for i in range(10):
     print("Эта цифра похоже на %d: %s" % (i, proceed(stroka,i)))   

# Искаженные цифры, похожие на5 (Тестовая выборка)
num51 = list('111100111000111')
num52 = list('111100010001111')
num53 = list('111100011001111')
num54 = list('110100111001111')
num55 = list('110100111001011')
num56 = list('111100101001111')

