import tkinter as tk
import tkinter.font as tkf
import numpy as np


class GUI:

    def __init__(self, table):
        self.__pressed_button = None
        self.__selected_value = 0
        self.__table = table
        self.__buttons = np.empty((9, 9), dtype=object)
        self.__number_buttons = np.empty(10, dtype=object)

    def run(self):
        root = tk.Tk()
        root.geometry("500x620")
        root.config(bg='gray20')
        frame = tk.Frame(root, bg='snow', height=470, width=470)
        frame.place(x=15, y=15)
        font_basic = tkf.Font(family='System', size=40, weight=tkf.BOLD)
        for i in range(9):
            for j in range(9):
                self.__buttons[i][j] = tk.Button(frame,
                                                 text='',
                                                 bg='gray1',
                                                 bd=0,
                                                 fg='snow',
                                                 font=font_basic)
                self.__buttons[i][j].config(command=lambda
                    btn=self.__buttons[i][j], x=i, y=j:
                self.change_btn(btn, x, y))
                self.__buttons[i][j].place(height=50,
                                           width=50,
                                           x=i * 50 + int(i / 3) * 3 + 3 + i,
                                           y=j * 50 + int(j / 3) * 3 + 3 + j)
        for i in range(10):
            self.__number_buttons[i] = tk.Button(root,
                                                 text=i,
                                                 bg='gray1',
                                                 fg='snow',
                                                 font=font_basic)
            self.__number_buttons[i].config(command=lambda
                nr=i,
                btn=self.__number_buttons[i]:
            self.select_value(nr, btn))
            self.__number_buttons[i].place(height=45,
                                           width=45,
                                           x=21 + i + i * 45,
                                           y=500)
        solve_btn = tk.Button(root, text='solve',
                              bg='gray1',
                              fg='snow',
                              font=font_basic,
                              command=self.solver)
        solve_btn.place(height=50,
                        width=150,
                        x=20,
                        y=550)
        generate_btn = tk.Button(root, text='new',
                                 bg='gray1',
                                 fg='snow',
                                 font=font_basic,
                                 command=self.generate)
        generate_btn.place(height=50,
                           width=130,
                           x=185,
                           y=550)

        clear_btn = tk.Button(root, text='clear',
                                 bg='gray1',
                                 fg='snow',
                                 font=font_basic,
                                 command=self.clear)
        clear_btn.place(height=50,
                           width=150,
                           x=330,
                           y=550)
        root.mainloop()

    def change_btn(self, btn, x, y):
        if self.__pressed_button is not None:
            if self.__selected_value != 0:
                btn['text'] = self.__selected_value
            else:
                btn['text'] = ''
            try:
                self.__table[(x, y)] = self.__selected_value
            except ValueError as ve:
                if str(ve) == "Wrong value!":
                    if self.__table[(x, y)] == 0:
                        btn['text'] = ''
                    else:
                        btn['text'] = self.__table[(x, y)]

    def select_value(self, number, btn):
        if self.__pressed_button is None:
            self.__pressed_button = btn
        else:
            self.__pressed_button['relief'] = tk.RAISED
            self.__pressed_button = btn
        self.__pressed_button['relief'] = tk.SUNKEN
        self.__selected_value = number

    def init_table(self):
        for x in range(9):
            for y in range(9):
                if self.__buttons[x][y]['text'] != '':
                    self.__table[(x, y)] = self.__buttons[x][y]['text']
                else:
                    self.__table[(x, y)] = 0

    def update_buttons(self):
        for x in range(9):
            for y in range(9):
                if self.__table[(x, y)] == 0:
                    self.__buttons[x][y]['text'] = ''
                else:
                    self.__buttons[x][y]['text'] = self.__table[(x, y)]

    def generate(self):
        self.__table.clear()
        self.__table.generate(51)
        self.update_buttons()

    def clear(self):
        self.__table.clear()
        self.update_buttons()

    def solver(self):
        self.__table.solve()
        self.update_buttons()
