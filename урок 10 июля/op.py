config = {}

with open('sm.ini') as file_config:
    config_list = file_config.readlines()

for value in config_list:
    result = value.strip().split('=')
    key = result[0]
    if result[1] == 'yes':
        value = True
    else:
        value = result[1]

    if result[1].isdigit():
        result[1]
    config[key] = value

print(config)

#['host ', ' localhost\n']
#['port', '5001\n']
#['allow_guest', 'yes\n']
#['timeout', '35\n']
#['db_address ', ' 192.168.2.34\n']
#['db_port', '9003\n']
#['db_user', 'Ali\n']
#['db_pass', '1@#$TGBhu\n']
