from execute import *

def MenuList():
    print("1 - Выполнить скалярный запрос\n" +
          "2 - Выполнить запрос с несколькими соединениями (JOIN)\n" +
          "3 - Выполнить запрос с ОТВ(CTE) и оконными функциями\n" +
          "4 - Выполнить запрос к метаданным\n" +
          "5 - Вызвать скалярную функцию (написанную в третьей лабораторной работе)\n" +
          "6 - Вызвать многооператорную или табличную функцию (написанную в третьей" +
            "лабораторной работе)\n" +
          "7 - Вызвать хранимую процедуру (написанную в третьей лабораторной работе\n" +
          "8 - Вызвать системную функцию или процедуру\n" +
          "9 - Создать таблицу в базе данных, соответствующую тематике БД\n" +
          "10 - Выполнить вставку данных в созданную таблицу с использованием" +
            " инструкции INSERT или COPY\n" +
          "0 - Выход\n")
    
def Menu(cur, con):

    Tasks = [Task1, Task2, Task3, Task4, Task5, Task6, Task7, Task8, Task9, Task10]
    while True:
        MenuList()
        option = int(input("Choose the option from menu list: "))
        if not option:
            break
        elif option == 7 or option == 9 or option == 10:
            Tasks[option - 1](cur, con)
        else:
            Tasks[option - 1](cur)
    
    
