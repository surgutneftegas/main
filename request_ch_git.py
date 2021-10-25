#!/usr/bin/env python3
import os
print(f'Введите путь до директории:')
path = input()
print(f'Поиск модифицированных файлов будет выполненен в директории: {path}')
cd_path = "cd " + path
bash_command = [cd_path, "git status"]
result_os = os.popen(' && '.join(bash_command)).read()
is_change = False
for result in result_os.split('\n'):
    if result.find('modified') != -1:
        prepare_result = result.replace('\tmodified:   ', '')
        print(prepare_result)
