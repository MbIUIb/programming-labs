from tkinter import *
from tkinter import messagebox
from database import Database
import hashlib


class Window:
    def __init__(self, width=600, height=300, title='Lab 11', resizable=(False, False)):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap('Data/img.ico')
        # определение формата окна и его положения
        self.window.geometry(f'{width}x{height}+450+200')
        self.window.resizable(*resizable)

        self.db = Database()

    def __del__(self):
        self.db.close()


    def run(self):
        self.draw_widgets()
        self.window.mainloop()

    def close_window(self):
        self.window.destroy()

    def grab_focus(self):
        """Полностью захватывает фокус на текущем окне, до его закрытия"""
        # захват всех происходящих событий текущим окном
        self.window.grab_set()
        # захват фокуса
        self.window.focus_set()
        # предотвращение влияния на сторонние окна Tk до закрытия текущего
        self.window.wait_window()


class BeginWindow(Window):
    """Экземпляр класса является окном, содержащим приветствие и кнопки для входи и регистрации"""
    def draw_widgets(self):
        """Метод отрисовывает виджеты основного окна"""
        Label(self.window, text='Приветствуем вас в Lab 11!', font='Consolas 20').pack(anchor=N, pady=30)

        Button(self.window, width=15, height=2, text='Войти', font=('Consolas', 20, 'bold'), bd=8,
                            command=self.create_EntrWin).pack(anchor=CENTER, pady=5)
        Button(self.window, width=20, height=2, text='Зарегестрироваться', font=('Consolas', 8),
                            command=self.create_RegWin).pack(anchor=CENTER)

    def create_RegWin(self, width=400, height=200, type='Регистрация', title='Регистрация в Lab 11', resizable=(False, False)):
        LoginWindow(self.window, width, height, type, title, resizable)

    def create_EntrWin(self, width=400, height=200, type='Вход', title='Вход в Lab 11', resizable=(False, False)):
        LoginWindow(self.window, width, height, type, title, resizable)


class MainWindow(Window):
    """Экземпляр класса является окном, содержащим информацию о пользователе"""
    def __init__(self, login):
        super().__init__()
        self.login = login
        self.user_id = self.db.get_id(self.login)
        self.draw_widgets()

    def draw_widgets(self):
        Label(self.window, text='Приветствуем вас в Lab 11!', font='Consolas 20').grid(row=0, column=0, columnspan=2,
                                                                                       sticky=W+E, padx=100, pady=30)
        # логин
        Label(self.window, text='Login:', font='Consolas 20').grid(row=1, column=0, sticky=W+E, padx=10, pady=5)
        Label(self.window, text=self.login, font='Consolas 20').grid(row=1, column=1, sticky=W)
        # id
        Label(self.window, text='ID:', font='Consolas 20').grid(row=2, column=0, sticky=W+E, padx=10, pady=5)
        Label(self.window, text=self.user_id, font='Consolas 20').grid(row=2, column=1, sticky=W)
        # кнопки
        Button(self.window, width=20, height=2, text='Удалить аккаунт', bd=4, font=('Consolas', 8, 'bold'),
                            command=self.del_user).grid(row=3, column=1, sticky=E, padx=10, pady=30)

    def del_user(self):
        self.db.del_user(self.user_id)
        self.db.commit()
        self.close_window()
        messagebox.showinfo('Удаление', f'Пользователь {self.login} удален!')


class LoginWindow(BeginWindow):
    """Экземпляр класса является окном егистрации/входа)"""
    def __init__(self, parent, width=300, height=200, type=None, title='Регистрация', resizable=(False, False)):
        self.window = Toplevel(parent)

        self.type = type
        if self.type != None:
            match self.type:
                case 'Регистрация':
                    self.button_text = 'Зарегистрироваться'
                    self.window.title(f'{self.type} в Lab 11')
                case 'Вход':
                    self.button_text = 'Войти'
                    self.window.title(f'{self.type} в Lab 11')
            self.login = Entry(self.window)

        self.window.iconbitmap('Data/img.ico')
        # определение формата окна и положения курсора
        self.window.geometry(f'{width}x{height}+550+200')
        self.window.resizable(*resizable)

        self.password = Entry(self.window, show='*')

        self.db = Database()

        self.draw_widgets(self.type)
        self.grab_focus()

    def draw_widgets(self, type):
        """Метод отрисовывает все виджеты"""
        Label(self.window, text=self.type, font='Consolas 20').grid(row=0, column=1, sticky=W+E, padx=10, pady=5)

        match type:
            case 'Регистрация' | 'Вход':
                # логин
                Label(self.window, text='Login:', font='Consolas 9').grid(row=1, column=0, sticky=W, padx=10, pady=5)
                self.login.grid(row=1, column=1, sticky=W+E)

        # пароль
        Label(self.window, text='Password:', font='Consolas 9').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        self.password.grid(row=2, column=1, sticky=W+E)

        # кнопки
        Button(self.window, width=20, height=1, text=self.button_text, font=('Consolas', 14, 'bold'), bd=8,
                            command=self.log).grid(row=3, column=1, sticky=W, padx=10, pady=20)

    def user_registration(self, login, password_hash):
        if self.db.new_user(login, password_hash):
            self.db.commit()

            self.window.destroy()
            messagebox.showinfo('Регистрация', f'Пользователь {login} успешно зарегистрирован!')
        else:
            messagebox.showerror('Ошибка', f'Пользователь {login} уже существует, попробуйте другой login.')

    def user_entrance(self, login, password, password_hash):
        status = self.db.authentication(login, password_hash)
        self.db.commit()

        match status:
            case 'successful':
                self.close_window()

                self.create_MainWindow(login)

                # messagebox.showinfo('Вход', f'Вы успешно вошли!\n\nВаш логин: {login}\nВаш id: {self.db.get_id(login)}')
            case 'login error':
                messagebox.showerror('Ошибка', f'Пользователя {login} не существует. Зарегистрируйтесь перед тем, как войти.')
                self.window.destroy()
            case 'password error':
                messagebox.showerror('Ошибка', f'Неверный пароль, попробуйте еще раз.')

    def log(self):
        """
        Метод создает окно регистрации/входа, получает данные из полей ввода, сравнивает с данными из базы данных и
        вызывает окно с дополнительной информацией в зависимости от случая
        """

        login = self.login.get()
        password = self.password.get()
        password_hash = hashlib.sha512(password.encode()).hexdigest()

        match self.type:
            case 'Регистрация':
                self.user_registration(login, password_hash)
            case 'Вход':
                self.user_entrance(login, password, password_hash)

    def create_MainWindow(self, login):
        MainWindow(login)
