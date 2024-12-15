"""
Парсер скрипта для получения данных из конфигурационного файла
для управления ботом владельцем телеграмм-бота
"""

import configparser
import asyncio

conf = configparser.ConfigParser()
conf.read('config/config.ini')


def get_token() -> str:
    """
    Функция для получения токена из отдельного файла
    :return: dict токен для подключения к боту
    """
    return str(conf['KEY_INFO_BOT']['key'])


def get_owner_user_id() -> int:
    """
    Функция для получения user_id владельца
    :return: dict owner_user_id - идентификатор телеграмм аккаунта, прописанный в файле конфигурации
    """
    return int(conf['OWNER_TELEGRAM_BOT']['user_id'])


def get_status_bot() -> str:
    """
    Функция для получения статуса работы бота
    :return: dict: is_active_bot - текущий статус работы бота
    """
    return str(conf['ACTIVE_BOT']['is_active_bot'])


def set_active_bot() -> None:
    """
    Функция для включения работы телеграмм бота
    :return: dict
    """
    conf.set('ACTIVE_BOT', 'is_active_bot', '1')
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None


def set_inactive_bot() -> None:
    """
    Функция для отключения работы телеграмм бота
    :return: dict
    """
    conf.set('ACTIVE_BOT', 'is_active_bot', '0')
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None


def get_max_len() -> int:
    """
    Получение максимальной длины одного пароля
    :return: максимальная длина генерируемого пароля
    """
    return int(conf['PARAMETERS_MAX']['len'])


def get_max_size() -> int:
    """
    Получение максимального количества паролей за один запрос
    :return:
    """
    return int(conf['PARAMETERS_MAX']['size'])


def set_len(val: str) -> None:
    """
    Установка нового значения максимальной длины
    :param val: новое значение длины
    :return: None
    """
    conf.set('PARAMETERS_MAX', 'len', val)
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None


def set_size(val: str) -> None:
    """
        Установка нового значения максимального количества
        :param val: новое значение количества
        :return: None
        """
    conf.set('PARAMETERS_MAX', 'size', val)
    with open('config/config.ini', 'w') as configfile:
        conf.write(configfile)
    return None
