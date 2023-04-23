def Main():
    while True:
        user_input = input("Введите строку: ")
        if user_input == "":
            print("Пустые строки вводить нельзя!")
            continue
        else:
            break
    print("Вы ввели:", user_input)

if __name__=='__main__':
    Main()