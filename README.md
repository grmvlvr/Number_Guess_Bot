# Number_Guess_Bot

[Number Guess](https://t.me/Number_Guess100_bot) - это телеграм бот, который предоставляет пользователю возможность угадать загаданное ботом число от 1 до 100. У пользователя есть 3 попытки отгадать число.

## Установка/Запуск

Для успешной работы бота на вашем устройстве должна быть установлена библиотека pyTelegramBotAPI (telebot). Установить её можно командой в терминале:

```
pip install pyTelegramBotAPI
```

Далее, необходимо склонировать данный репозиторий при помощи команды ```clone```. После этого бота можно запускать напрямую из терминала командой ```python main.py```, находясь в директории с файлом ```main.py```, или через IDE (VS Code, Pycharm, IDLE и т.д.).

Альтернативно, можно при помощи модуля ```PyInstaller``` собрать исполняемый файл для запуска бота ```*.exe```. Для этого необходимо установить данный модуль, если он ещё не установлен, командой ```pip install pyinstaller```. После установки модуля нужно ввести в терминал ввести команду ```pyinstaller --onefile main.py```, которая создаст ```main.exe``` внутри директории ```dist```.

## Работа через Docker

Для запуска бота в Docker-контейнере необходимо в терминале перейти в директорию файлами бота, а затем собрать и запустить контейнер (при необходимости, можно модифицировать .Dockerfile):

```
docker build -t Number_Guess .
docker run --rm Number_Guess
```
