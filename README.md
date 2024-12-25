<table>
<tr>
    <th><h1 align="center"><a href="https://t.me/gen_secur_pass_bot">Telegram Generate Password Bot</a></h1>
</th>
    <th width="15%">

![img.png](qr_code_bot.png)

</th>
</tr>
</table>

<h1 align="center">

![img.png](pic_tg_generate.png)

</h1>

Во многих современных браузерах есть встроенная функция, которая предлагает безопасный пароль из заглавных и прописных 
букв, цифр и специальных символов при клике на поле для пароля.

Этот бот умеет больше, чем встроенные методы генерации пароля браузером:

* можно выбрать длину пароля до 20 символов; 
* включить или исключить из генерации заглавные и прописные буквы, цифры и специальные символы; 
* задать количество генерируемых паролей в одном сообщении за раз. 

После генерации паролей, не нужно выделять сообщение, а затем выделять пароль в сообщении, чтобы вставить его в поле 
при регистрации, Вы просто нажимаете на него для копирования.

### Доступные команды для пользователя:

* **/start** - _начать общение с ботом_
* **/author** - _узнать автора бота_
* **/pic** - _получить ссылку на аватар бота_
* **/description** - _получить описание бота_
* **/example_gen_pass** - _получить примеры команд с описанием и результаты_
* **/ver** - _получить версию бота_
  
**_Пароли не сохраняются, кроме Вашего чата с ботом. Какой пароль и где Вы его используете, 
знаете только Вы_.**

## :computer: Technology Stack

#### Computer language

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)

> **Python для Telegram** — это язык программирования, который используется для создания Telegram-ботов.
Бот, написанный на Python, отличается скоростью, безопасностью и стабильностью.

#### FrameWork

![Aiogram](https://img.shields.io/badge/-Aiogram-black?style=flat-square&logo=Aiogram)

> **Aiogram** — это асинхронная библиотека для языка программирования Python, основанная на Telegram Bot API.

#### Libs/Module

**configparser**

> **Configparser** предназначен для работы с файлами конфигурации, которые хранят настройки и параметры для приложений

Использовалась для парсинга файла конфигурации .ini, содержащего настройки к боту. 

Содержание файла:

```
; активность бота
[ACTIVE_BOT]
is_active_bot = 0

; tg_id владельца бота
[OWNER_TELEGRAM_BOT]
user_id = 1

; токен для подключения к боту
[KEY_INFO_BOT]
key = TELEGRAM BOT FATHER

; версия бота
[VERSION_BOT]
ver = x.x
```

_Версия бота будет изменяться_.

**_! ! ! Представлена только структура файла, данные изменены ! ! !_**

**sys**

> Модуль **sys** в Python предоставляет доступ к некоторым переменным и функциям, используемым или управляемым 
интерпретатором Python.

**os**

> Модуль **os** в Python позволяет работать с операционной системой компьютера прямо из кода Python. 
> 
> Он предлагает функции для управления файлами и каталогами, манипулирования процессами и контроля переменных среды.

Используется для проверки существования файла базы данных

**pprint**

> Модуль **pprint** в Python (pretty-print) предоставляет возможность форматировать вывод сложных структур данных, 
> таких как списки, кортежи, словари и вложенные комбинации этих типов.

Используется для отладки, вывод массивов в консоль, полученных из базы данных 

**asyncio**

> **Asyncio** — это модуль в стандартной библиотеке Python, который предоставляет инфраструктуру для написания 
> одновременного кода с использованием асинхронных операций ввода-вывода. 
> 
> Он позволяет эффективно обрабатывать многочисленные задачи ввода-вывода (например, сетевые операции или 
> чтение/запись из файлов) без необходимости создавать множество потоков или процессов.

Используется для отправки сообщений

**yaml**

> Для работы с **YAML** в Python используется библиотека PyYAML

Использовалось для шаблонов вопросов собеседнику

#### Data Bases

![SQLite](https://img.shields.io/badge/-SQLite-black?style=flat-square&logo=sqlite)

> **SQLite** — это система управления базами данных, написанная на языке C. 
> 
> Она не имеет сервера и хранит созданные базы данных в пределах одного локального компьютера.

#### VCS

![GitHub](https://img.shields.io/badge/-GitHub-black?style=flat-square&logo=github)

> **GitHub** — это веб-сервис для хостинга IT-проектов и их совместной разработки. 
> 
> Также его называют социальной сетью для разработчиков, так как в нём можно не только размещать код, но и общаться, 
> комментировать правки друг друга.

<hr>

<!-- START [S E C T I O N] Communication with me -->

## :link: Communication with Me

<h1 align="center">
  <a href="https://t.me/m/QidnFEAvNzBi">
      <!-- Telegram -->
      <img src="https://img.icons8.com/?size=100&id=Sz6lu91x9jqC&format=png&color=000000" alt="darkwood"/>
    </a>
</h1>

<!-- END [S E C T I O N] Communication with me -->

<hr>

<!-- START [S E C T I O N] count visits and date profile update -->

<p align="center">
    <a href="https://github.com/ma5t0d0nt-tg" target="_blank">
        <img src="https://img.shields.io/github/watchers/ma5t0d0nt-tg/Telegram_Generate_Password_Bot.svg"/>
    </a>
    <a href="https://github.com/ma5t0d0nt-tg" target="_blank">
        <img src="https://img.shields.io/github/stars/ma5t0d0nt-tg/Telegram_Generate_Password_Bot.svg"/>
    </a>
</p>

<p align="center">
    <a href="https://github.com/ma5t0d0nt-tg/Telegram_Generate_Password_Bot" target="_blank">
        <img src="https://img.shields.io/github/last-commit/ma5t0d0nt-tg/ma5t0d0nt-tg?label=Project%20Updated&style=flat-square">
    </a>
</p>

<!-- END [S E C T I O N] count visits and date profile update -->