
# подключение к хостингу timeweb

#     (.venv) D:\Rabota_2025\deadlinetaskbot_02_25 git:[main]
# >>> ssh root@31.130.150.56
#     root@31.130.150.56's password: (пароль берем на хостинге для root и вводим по одной цифре)


# Создайте директорию для нового бота:
# В командной строке сервера создайте новую директорию для Вашего бота.
# Это поможет организовать файлы и избежать путаницы.

#           >>>  mkdir ~/deadlinetaskbot_02_25
#           >>>  cd ~/deadlinetaskbot_02_25

# Комбинация клавиш Ctrl + D:
# Нажмите Ctrl и D одновременно. Это также завершит сессию и выйдет из SSH.

# Подключение к хостингу и клонирование чатбота в него из папки на компе

#            >>> scp -r D:/Rabota_2025/deadlinetaskbot_02_25 root@31.130.150.56:~/deadlinetaskbot_02_25

# Перейдите в директорию с вашим проектом:
# После подключения выполните:

#            >>> cd ~/deadlinetaskbot_02_25

# Убедитесь, что у Вас установлен Python и pip на сервере. Если pip не установлен, возможно, Вам нужно будет установить его с помощью команды:

#            >>> sudo apt-get install python3-pip