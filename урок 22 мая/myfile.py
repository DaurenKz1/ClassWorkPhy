salary_user_input = input("Введите зарплату за месяц: ")
kredit_user_input = input("Введите сумму кредита за месяц: ")
nalogi_user_input = input("Введите сумму налогов: ")

try:
    salary = float(salary_user_input)
    kredit = float(kredit_user_input)
    nalogi = float(nalogi_user_input)
except ValueError:
    print("Введите числа!")
else:
    money = float(salary - kredit - nalogi )
    print("Осталось: ", money)