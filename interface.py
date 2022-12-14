from tkinter import *
from tkinter import ttk
from phrases import *
from voiceBot import *
from osnova import *
from skills import *


#делаем окно интерфейса
root = Tk()
root.geometry('450x350')
root.configure(bg='gray22')
root.title('GS_sevase')

#делаем флаги для изменения скорости речи бота                                 #НИХЕРА НЕ СЛУШАЕТСЯ С МНОГОПОТОКОМ
rad1 = Radiobutton(root, text='Стандарт', value=0, command=scoreStndart)
rad2 = Radiobutton(root, text='Медленно', value=1, command=scoreSlow)
rad3 = Radiobutton(root, text='Быстро', value=2, command=scoreFast)
rad1.grid(column=0, row=0) #гридовка
rad2.grid(column=1, row=0)
rad3.grid(column=2, row=0)

menu = Menu(root)
new_item = Menu(menu)
new_item.add_command(label='Новый')
new_item.add_separator()
new_item.add_command(label='Изменить')
menu.add_cascade(label='Файл', menu=new_item)
root.config(menu=menu)


def start(): #вкл бота

    main()

def off(): #откл бота
    offBot()


btnStart = Button(root, text='Начать', command=start)
btnStart.configure(bd=1, font=('Castellar', 25), bg='gray')
btnStart.place(x=155, y=160, height=50, width=150)

btnOff = Button(root, text='Отключить', command=off)
btnOff.configure(bd=1, font=('Castellar', 25), bg='gray')
btnOff.place(x=140, y=260, height=50, width=180)

root.mainloop()