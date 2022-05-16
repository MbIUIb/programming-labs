import time
from datetime import datetime
from cryptography.fernet import Fernet
import os


class Logger:
    def __init__(self, file:str='logs.txt', encryption_mode:bool=False):
        self.file = file
        # очистка файла
        with open(self.file, 'w') as f:
            pass

        self.encryption_mode = encryption_mode
        self.create_key()
        self.key = self.load_key()

        self.new_log('инициализация')


    def create_key(self):
        """Метод создает ключ key и записывает его в файл"""
        key = Fernet.generate_key()
        with open('key', 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        """Метод возвращает ключ из файла key"""
        return open('key', 'rb').read()


    def date_of_log(self):
        return str(datetime.now())[:-7]

    def new_log(self, event):
        # формат логов:     дата время - [событие]
        time_now = self.date_of_log()
        log = f'{time_now} - [{event}]\n'

        with open(self.file, 'a', encoding='utf-8') as file:
            file.write(log)


    def encrypt(self):
        """Метод перезаписывает в файл данные в зашифрованном виде"""
        f = Fernet(self.key)

        with open(self.file, 'rb') as file:
            data = file.read()

        encrypted_data = f.encrypt(data)

        with open(self.file, 'wb') as file:
            file.write(encrypted_data)


def decrypt(*args):
    if len(args) == 2:
        encrypt_file = args[0]
        decrypt_file = args[0]
        key = args[1]
    elif len(args) == 3:
        encrypt_file = args[0]
        decrypt_file = args[1]
        key = args[2]
    else:
        print('Неправильное количество параметров')
        return None

    f = Fernet(key)
    with open(encrypt_file, 'rb') as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)


    with open(decrypt_file, 'wb') as file:
        file.write(decrypted_data)


if __name__ == '__main__':
    a = Logger(encryption_mode=True)
    a.new_log('event')

    a.encrypt()
    decrypt('logs.txt', 'decryptlogs', a.key)
