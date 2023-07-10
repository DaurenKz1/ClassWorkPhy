import ini

config = ini.parse('config.ini')
print("Наша конфигурация: ")
print(config)

user_resp = input("Хотите изменить ключ? (yes/no):  ")

if user_resp == "yes":
    user_sec = input("В какой секции? ")
    if user_sec in config:
        user_key = input("Какой ключ? ")
        if user_key in config[user_sec]:
            user_in = input("На что хотите заменить?")
            if user_in.isdigit():
             config[user_sec][user_key] = int(user_in)
            else:
              config[user_sec][user_key] = user_in
            print(config)
    else:
        print("Не существует данной секции")
