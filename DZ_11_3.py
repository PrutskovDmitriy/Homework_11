class Error:
    def __init__(self, ):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите число и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Введите только цифры")
                yon = input(f'Попробовать еще раз? Y/N ')

                if yon == 'Y' or yon == 'y':
                    print(try_except.my_input())
                elif yon == 'N' or yon == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error()
print(try_except.my_input())
