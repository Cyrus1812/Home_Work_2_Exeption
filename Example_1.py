# Реализуйте метод, который запрашивает у пользователя ввод дробного числа,
#  и возвращает введенное значение. Ввод текста вместо числа не должно приводить к падению приложения, 
#  вместо этого, необходимо повторно запросить у пользователя ввод данных.

def Main():
    print(get_float_input())

def get_float_input():
    while True:
        try:
            user_input = float(input("Введите дробное число: "))
            if float.is_integer(user_input) == False:
                return user_input
            else:
                print("Ошибка! Введите дробное число.")
        except ValueError:
            print("Ошибка! Введите дробное число.")

if __name__=='__main__':
    Main()