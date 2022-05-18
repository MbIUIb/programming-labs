from  tkinter import *
from tkinter import messagebox

# Закрытие окна, не завершая работу программы
# self.window.destroy()
class Window:
    def __init__(self, width=600, height=300, title='Lab 11', resizable=(False, False)):
        self.window = Tk()
        self.window.title(title)
        self.window.iconbitmap('Data\\img.ico')
        # определение формата окна и его положения
        self.window.geometry(f'{width}x{height}+450+200')
        self.window.resizable(resizable[0], resizable[1])


    def run(self):
        self.draw_widgets()
        self.window.mainloop()


    def grab_focus(self):
        """Полностью захватывает фокус на текущем окне, до его закрытия"""
        # захват всех происходящих событий текущим окном
        self.window.grab_set()
        # захват фокуса
        self.window.focus_set()
        # предотвращение влияния на сторонние окна Tk до закрытия текущего
        self.window.wait_window()


    def draw_widgets(self):
        """Метод отрисовывает виджеты основного окна"""
        Label(self.window, text='Приветствуем вас в Lab 11!', font='Consolas 20').pack(anchor=N, pady=30)

        Button(self.window, width=15, height=2, text='Войти', font=('Consolas', 20, 'bold'), bd=8,
                            command=self.create_EntrWin).pack(anchor=CENTER, pady=5)
        Button(self.window, width=20, height=2, text='Зарегестрироваться', font=('Consolas', 8),
                            command=self.create_RegWin).pack(anchor=CENTER)


    def create_RegWin(self, width=400, height=200, type='Регистрация', title='Регистрация в Lab 11', resizable=(False, False)):
        """Метод создает окно регистрации нового пользователя"""
        LoginWindow(self.window, width, height, type, title, resizable)


    def create_EntrWin(self, width=400, height=200, type='Вход', title='Вход в Lab 11', resizable=(False, False)):
        """Метод создает окно входа"""
        LoginWindow(self.window, width, height, type, title, resizable)


class LoginWindow(Window):
    """Экземпляр класса является окном авторизации(регистрация/вход)"""

    def __init__(self, parent, width=300, height=200, type='Регистрация', title='Регистрация', resizable=(False, False)):
        self.window = Toplevel(parent)

        self.type = type
        if self.type == 'Регистрация':
            self.button_text = 'Зарегистрироваться'
            self.window.title(f'{self.type} в Lab 11')
        elif type == 'Вход':
            self.button_text = 'Войти'
            self.window.title(f'{self.type} в Lab 11')

        self.window.iconbitmap('Data\\img.ico')
        # определение формата окна и положения курсора
        self.window.geometry(f'{width}x{height}+550+200')
        self.window.resizable(resizable[0], resizable[1])

        self.login = Entry(self.window)
        self.password = Entry(self.window, show='*')

        self.draw_widgets()
        self.grab_focus()


    def draw_widgets(self):
        """Метод отрисовывает все виджеты"""
        Label(self.window, text=self.type, font='Consolas 20').grid(row=0, column=1, sticky=W+E, padx=10, pady=5)

        # логин
        Label(self.window, text='Login:', font='Consolas 9').grid(row=1, column=0, sticky=W, padx=10, pady=5)
        self.login.grid(row=1, column=1, sticky=W+E)
        # пароль
        Label(self.window, text='Password:', font='Consolas 9').grid(row=2, column=0, sticky=W, padx=10, pady=5)
        self.password.grid(row=2, column=1, sticky=W+E)


        # кнопки
        Button(self.window, width=20, height=1, text=self.button_text, font=('Consolas', 14, 'bold'), bd=8,
                            command=self.log).grid(row=3, column=1, sticky=W, padx=10, pady=20)


    def log(self):
        """Метод получает данные из полей ввода"""
        login = self.login.get()
        password = self.password.get()

        if self.type == 'Регистрация':
            # регистрация пользвателя.......
            #
            #

            messagebox.showinfo('Регистрация', f'Пользлватель {login} успешно зарегистрирован!')
        elif self.type == 'Вход':
            #вход пользователя.......
            #
            #

            # messagebox.showinfo('Вход', f'Пользлватель {login} успешно вошел!')
            pass
        self.window.destroy()




if __name__ == '__main__':
    win = Window()
    win.run()
