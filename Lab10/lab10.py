from pathlib import Path

from datetime import datetime
from cryptography.fernet import Fernet
# from programming_languages_labs.Lab9.Data import lab9_logs


class Logger:
    def __init__(self, file:str='Data/logs.txt', new_file:str='new'):
        self.file = file
        self.new_file = new_file
        if self.new_file:
            Path(self.file).write_text('')

        self.create_key()
        self.key = self.load_key()

        self.new_log('инициализация')


    def create_key(self):
        """Метод создает ключ key и записывает его в файл"""
        Path('Data/key').write_bytes(Fernet.generate_key())

    def load_key(self):
        """Метод возвращает ключ из файла key"""
        return Path('Data/key').read_bytes()

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
        data = Path(self.file).read_bytes()
        Path(self.file).write_bytes(Fernet(self.key).encrypt(data))


def decrypt(*args):
    match len(args):
        case 2:
            encrypt_file = args[0]
            decrypt_file = args[0]
            key = args[1]
        case 3:
            encrypt_file = args[0]
            decrypt_file = args[1]
            key = args[2]
        case _:
            print('Неправильное количество параметров')
            return

    encrypted_data = Path(encrypt_file).read_bytes()
    Path(decrypt_file).write_bytes(Fernet(key).decrypt(encrypted_data))
