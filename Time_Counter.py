import tkinter as tk


class Application:
    people_number = int
    time = int
    names = []

    def __init__(self, root):

        self.marc_n_people = tk.Label(root, text='Numero de participantes', bg='DeepSkyBlue2',
                                      font=('Baskerville Old Face', 14))
        self.marc_n_people.pack()
        self.n_people_box = tk.Entry(root)
        self.n_people_box.pack()
        self.button_accept = tk.Button(root, text="Aceptar", command=lambda: self.accept(self.n_people_box, root), relief="groove", borderwidth=5)
        self.button_accept.pack()

    def accept(self, n_people_box, root):
        try:
            self.people_number = int(n_people_box.get())  # Obtenemos el número de la StringVar
        except ValueError:  # Si lo ingresado no es un entero
            pass
        else:  # Si lo ingresado es un entero
            self.marc_n_people.destroy()
            self.n_people_box.destroy()
            self.button_accept.destroy()
            self.add_time(root)

    def add_time(self, root):
        self.time_marc = tk.Label(root, text='Tiempo en segundos para cada persona', bg='DeepSkyBlue2', font=('Baskerville Old Face', 14))
        self.time_marc.pack()
        self.time_box = tk.Entry(root)
        self.time_box.pack()
        self.button_accept_time = tk.Button(root, text="Aceptar", command=lambda: self.accept_time(self.time_box, root), relief="groove", borderwidth=5)
        self.button_accept_time.pack()

    def accept_time(self, time_box, root):
        try:
            self.time = int(time_box.get())  # Obtenemos el número de la StringVar
        except ValueError:  # Si lo ingresado no es un entero
            pass
        else:  # Si lo ingresado es un entero
            self.time_marc.destroy()
            self.time_box.destroy()
            self.button_accept_time.destroy()
            self.button_accept_time = tk.Button(root, text="Comenzar", command=lambda: self.counter(root), relief="raised", borderwidth=5)
            self.button_accept_time.pack()

    def refresh_counter(self, root):
        self.second += 1

        self.time_count.config(text=f"Segundo - {self.second}, Ronda {self.round + 1}", bg='DeepSkyBlue2', font=('Baskerville Old Face', 26))

        if self.second >= self.time:
            self.round += 1
            if self.round == self.people_number:
                root.after_cancel(self.loop)
                self.time_count.config(text='SE ACABO EL TIEMPO', bg='DeepSkyBlue2', font=('Baskerville Old Face', 16))
                root.after(2000, self.close_counter, root)

            else:
                self.second = 0
                root.after(1000, self.refresh_counter, root)
        else:
            root.after(1000, self.refresh_counter, root)

    def close_counter(self, root):
        self.time_count.destroy()
        self.button_accept_time.destroy()
        self.button_again = tk.Button(root, text="Comenzar", command=lambda: self.reset_app(root))
        self.button_again.pack()


    def counter(self, root):
        self.button_accept_time.destroy()
        self.round = 0
        self.time_count = tk.Label(root, text='COMENZAMOS!!', bg='DeepSkyBlue2', font=('Baskerville Old Face', 26))
        self.time_count.pack(side=tk.BOTTOM)
        self.second = 0
        self.loop = root.after(1000, self.refresh_counter, root)

    def reset_app(self, root):
        self.button_again.destroy()
        Application(root)


if __name__ == '__main__':
    app = tk.Tk()
    app.title('Contador Debates')
    app.iconbitmap(r"C:/Users/toore/PycharmProjects/contadorDebates/ii.ico")

    app.geometry("320x150")
    app.config(bg='DeepSkyBlue2')
    app.marc = tk.Label(app, text='Contador de tiempos para debates', bg='DeepSkyBlue2', font=('Baskerville Old Face', 14))
    app.marc.pack()
    window = Application(app)
    app.mainloop()
