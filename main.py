totalMoney = 2000000
atmMoney = 5000000
cardPassword = 1111
telNumber = 0


def get50():
    '''
    This functions give money from ATM
    '''
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (50000 + (50000 * 0.01))
    atmMoney = atmMoney - (50000 + (50000 * 0.01))
    return totalMoney


def get100():
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (100000 + (100000 * 0.01))
    atmMoney = atmMoney - (100000 + (100000 * 0.01))
    return totalMoney


def get200():
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (200000 + (200000 * 0.01))
    atmMoney = atmMoney - (200000 + (200000 * 0.01))
    return totalMoney


def get300():
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (300000 + (300000 * 0.01))
    atmMoney = atmMoney - (300000 + (300000 * 0.01))
    return totalMoney


def get400():
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (400000 + (400000 * 0.01))
    atmMoney = atmMoney - (400000 + (400000 * 0.01))
    return totalMoney


def get500():
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (500000 + (500000 * 0.01))
    atmMoney = atmMoney - (500000 + (500000 * 0.01))
    return totalMoney


def getmore(money):
    global totalMoney
    global atmMoney
    totalMoney = totalMoney - (money + (money * 0.01))
    atmMoney = atmMoney - (money + (money * 0.01))
    return totalMoney


def addcash(inmoney):
    global totalMoney
    global atmMoney
    atmMoney += inmoney
    totalMoney += inmoney
    return totalMoney


def ruMenu():
    operation = int(input('''    1. Получить наличные           4. Подключить SMS информирование
    2. Пополнить баланс            5. Проверить баланс
    3. Изменить пароль             0. Выход
    ---> '''))
    while operation < 0 or operation > 5:
        print('Выбрана неправильная операция')
        print('-----------------------------')
        return ruMenu()
    if operation == 1:
        # Get money from ATM
        i = int(input('''    1. 50,000               4. 300,000 
    2. 100,000              5. 400,000 
    3. 200,000              6. 500,000 
    7. Другая сумма
    ---> '''))
        while i > 7 or i < 0:
            print('Выбрана неправильная операция')
            i = int(input('Введите заново номера операции\n---> '))
        if i == 1:
            if totalMoney >= 50000 + (50000 * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', get50(), 'сум')
                print('--------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()
        elif i == 2:
            if totalMoney >= 100000 + (100000 * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', get100(), 'сум')
                print('----------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()
        elif i == 3:
            if totalMoney >= 200000 + (200000 * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', get200(), 'сум')
                print('----------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()
        elif i == 4:
            if totalMoney >= 300000 + (300000 * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', get300(), 'сум')
                print('----------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()
        elif i == 5:
            if totalMoney >= 400000 + (400000 * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', get400(), 'сум')
                print('-----------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()
        elif i == 6:
            if totalMoney >= 500000 + (500000 * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', get500(), 'сум')
                print('-----------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()
        elif i == 7:
            money = int(input('Введите сумму\n---> '))
            if atmMoney < money + (money * 0.01):
                print("Недостаточно средств в банкомате!")
                print('-----------------------------')
                return ruMenu()
            elif totalMoney >= money + (money * 0.01) and atmMoney >= money + (money * 0.01):
                print('Операция выполнена успешно!\n На вашей карточке осталось', getmore(), 'сум')
                print('-----------------------------------------------------------------------------------')
                return ruMenu()
            else:
                print("Недостаточно средств!")
                print('---------------------------------------------')
                return ruMenu()

    elif operation == 2:
        inmoney = int(input("Введите сумму пополнения карты\n---> "))
        print("Операция выполнена успешно!")
        print(f"На вашей карте теперь {addcash(inmoney)} сум")
        print("-----------------------------------------------------")
        return ruMenu()

    elif operation == 3:
        global cardPassword
        cardPassword = int(input("Введите новый пароль\n---> "))
        print("--------------------------------------------------------------")
        return main()

    elif operation == 4:
        global telNumber
        if telNumber == 0:
            telNumber = int(input("Введите номер для подключения SMS информирования\n---> "))
            print("--------------------------------------------------------------")
            return ruMenu()
        else:
            print(f"К телефон номеру подключено SMS информирование\n---> {telNumber}")
            telNumber = int(input("Введите новый телефон номер для подключения SMS информирования\n---> "))
            print("--------------------------------------------------------------")
            return ruMenu()

    elif operation == 5:
        print(f"На вашей карте {totalMoney} сумов")
        print("-----------------------------------------------")
        return ruMenu()

    else:
        return main()


def enMenu():
    operation = int(input('''    1. Get Cash                 4. Connect SMS notification
    2. Fill the balance         5. Check balance
    3. Reset password           0. Exit
    ---> '''))
    while operation < 0 or operation > 5:
        print('Wrong operation was chosen')
        print('--------------------------')
        return enMenu()

    if operation == 1:
        # Get money from ATM
        i = int(input('''    1. 50,000               4. 300,000 
    2. 100,000              5. 400,000 
    3. 200,000              6. 500,000 
    7. Another amount
    ---> '''))
        while i > 7 or i < 0:
            print('Wrong operation was chosen')
            i = int(input('Entel correct operation number\n---> '))
        if i == 1:
            if totalMoney >= 50000 + (50000 * 0.01):
                print('Operation was ended successfuly!\n', get50(), 'sums left in your credit card')
                print('--------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()
        elif i == 2:
            if totalMoney >= 100000 + (100000 * 0.01):
                print('Operation was ended successfuly!\n', get100(), 'sums left in your credit card')
                print('----------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()
        elif i == 3:
            if totalMoney >= 200000 + (200000 * 0.01):
                print('Operation was ended successfuly!\n', get200(), 'sums left in your credit card')
                print('----------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()
        elif i == 4:
            if totalMoney >= 300000 + (300000 * 0.01):
                print('Operation was ended successfuly!\n', get300(), 'sums left in your credit card')
                print('----------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()
        elif i == 5:
            if totalMoney >= 400000 + (400000 * 0.01):
                print('Operation was ended successfuly!\n', get400(), 'sums left in your credit card')
                print('-----------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()
        elif i == 6:
            if totalMoney >= 500000 + (500000 * 0.01):
                print('Operation was ended successfuly!\n', get500(), 'sums left in your credit card')
                print('-----------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()
        elif i == 7:
            money = int(input('Enter the amount of money\n---> '))
            if atmMoney < money + (money * 0.01):
                print("There is no anough money ATM!")
                print('-----------------------------')
                return enMenu()
            elif totalMoney >= money + (money * 0.01) and atmMoney >= money + (money * 0.01):
                print('Operation was ended successfuly!\n', getmore(money), 'sums left in your credit card')
                print('-----------------------------------------------------------------------------------')
                return enMenu()
            else:
                print("There is no anough money in your credit card!")
                print('---------------------------------------------')
                return enMenu()

    elif operation == 2:
        inmoney = int(input("Enter the amount of money you want to put in your credit card\n---> "))
        print("Operation was ended successfuly!")
        print(f"There is {addcash(inmoney)} sums in your credit card")
        print("-----------------------------------------------------")
        return enMenu()

    elif operation == 3:
        global cardPassword
        cardPassword = int(input("Enter new password\n---> "))
        print("--------------------------------------------------------------")
        return main()

    elif operation == 4:
        global telNumber
        if telNumber == 0:
            telNumber = int(input("Enter the number to connect SMS notification\n---> "))
            print("--------------------------------------------------------------")
            return enMenu()
        else:
            print(f"Telefon number connected to SMS notification\n---> {telNumber}")
            telNumber = int(input("Enter new telefon number to connect SMS notificarion\n---> "))
            print("--------------------------------------------------------------")
            return enMenu()

    elif operation == 5:
        print(f"There is {totalMoney} sums in your credit card")
        print("-----------------------------------------------")
        return enMenu()

    else:
        return main()


def uzMenu():
    '''
    This function enters to the menu with uzbek language
    '''
    operation = int(input('''    1. Naqd pul yechish                 4. SMS xabarnomani ulash
    2. Kartani to'ldirish               5. Balansni bilish
    3. Passwordni almashtirish          0. Exit
    ---> '''))
    while operation < 0 or operation > 5:
        print('Amal raqami notogri!')
        print('--------------------')
        return uzMenu()

    if operation == 1:
        # Get money from ATM
        i = int(input('''    1. 50,000               4. 300,000 
    2. 100,000              5. 400,000 
    3. 200,000              6. 500,000 
    7. Boshqa summa
    ---> '''))
        while i > 7 or i < 0:
            print('Bunday amal mavjud emas!')
            i = int(input('Togri amal raqamini kiriting: '))
        if i == 1:
            if totalMoney >= 50000 + (50000 * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', get50(), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()
        elif i == 2:
            if totalMoney >= 100000 + (100000 * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', get100(), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()
        elif i == 3:
            if totalMoney >= 200000 + (200000 * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', get200(), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()
        elif i == 4:
            if totalMoney >= 300000 + (300000 * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', get300(), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()
        elif i == 5:
            if totalMoney >= 400000 + (400000 * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', get400(), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()
        elif i == 6:
            if totalMoney >= 500000 + (500000 * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', get500(), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()
        elif i == 7:
            money = int(input('Summani kiriting: '))
            if atmMoney < money + (money * 0.01):
                print("Bankomatda mablag' yetarli emas!")
                print('--------------------------------')
                return uzMenu()
            elif totalMoney >= money + (money * 0.01) and atmMoney >= money + (money * 0.01):
                print('Operatsiya muvaffaqiatli bajarildi!\n', 'Kartada', getmore(money), 'sum qoldi')
                print('-------------------------------------------------------------------------')
                return uzMenu()
            else:
                print("Kartada mablag' yetarli emas!")
                print('-----------------------------')
                return uzMenu()

    elif operation == 2:
        inmoney = int(input("Kartani to'ldirmoqchi bolgan summangizni kiriting\n---> "))
        print("Operatsiya muvaffaqiyatli bajarildi!")
        print(f"Kartada {addcash(inmoney)} so'm bor")
        print("-----------------------------")
        return uzMenu()

    elif operation == 3:
        global cardPassword
        cardPassword = int(input("Yangi passwordni kiriting\n---> "))
        return main()

    elif operation == 4:
        global telNumber
        if telNumber == 0:
            telNumber = int(input("SMS xabarnomani ulash uchun telefon raqamni kiriting\n---> "))
            return uzMenu()
        else:
            print(f"Hozirgi sms xabarnomaga ulangan telefon raqam\n---> {telNumber}")
            telNumber = int(input("SMS xabarnomani ulash uchun yangi telefon raqamni kiriting\n---> "))
            return uzMenu()

    elif operation == 5:
        print(f"Kartada hozir {totalMoney} so'm pul bor")
        print("---------------------------------------")
        return uzMenu()

    else:
        return main()


def passwordCheck(password):
    if cardPassword == password:
        return True
    else:
        return False


def main():
    '''
    Main menu to choose the interface language
    '''
    til = int(input('''Tilni tanlang:
1. O'zbek
2. Русский язык
3. English
---> '''))
    print(til)

    if til == 1:
        '''
        Password checking for Uzbek
        '''
        print("O'zbek tili tanlandi")
        n = 3
        while n > 0:
            password = int(input("Parolni kiriting: "))
            if passwordCheck(password) == True:
                return uzMenu()
            else:
                print("Parol hato kiritildi!")
                print("---------------------")
                n -= 1
        if n == 0:
            print("Karta bloklandi!")
            print("----------------")
            return main()

    elif til == 2:
        '''
        Password checking for Russian
        '''
        print("Выбран русский язык")
        n = 3
        while n > 0:
            password = int(input("Введите пароль: "))
            if passwordCheck(password) == True:
                return ruMenu()
                break
            else:
                print("Пароль введён неверно!")
                print("---------------------")
                n -= 1
        if n == 0:
            print("Карта заблокирована!")
            print("--------------------")
            return main()

    elif til == 3:
        '''
        Password checking fo English
        '''
        print("English language was choosen")
        n = 3
        while n > 0:
            password = int(input("Enter the password: "))
            if passwordCheck(password) == True:
                return enMenu()
            else:
                print("Password is incorect!")
                print("---------------------")
                n -= 1
        if n == 0:
            print("Credit card was blocked!")
            print("--------------------")
            return main()

    else:
        print("Siz mavjud bo'lmagan tilni tanladingiz")
        print("--------------------------------------")
        return main()


if __name__ == "__main__":
    main()