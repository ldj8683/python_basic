from tkinter import *
from tkinter import messagebox

def result():
    result_num = number_entry.get()
    print('번호는', result_num)
    result_title = title_entry.get()
    print('제목은', result_title)
    result_body = body_entry.get()
    print('내용은', result_body)
    result_wri = writer_entry.get()
    print('작성자는', result_wri)


w2 = Tk()
w2.geometry('500x400')

number = Label(w2, text='번호', font=('궁서', 25))
number.pack()
number_entry = Entry(w2, font=('궁서', 25), bg='black', fg='white')
number_entry.pack()

title = Label(w2, text='제목', font=('궁서', 25))
title.pack()
title_entry = Entry(w2, font=('궁서', 25), bg='black', fg='white')
title_entry.pack()

body = Label(w2, text='내용', font=('궁서', 25))
body.pack()
body_entry = Entry(w2, font=('궁서', 25), bg='black', fg='white')
body_entry.pack()

writer = Label(w2, text='작성자', font=('궁서', 25))
writer.pack()
writer_entry = Entry(w2, font=('궁서', 25), bg='black', fg='white')
writer_entry.pack()

b2 = Button(w2, text='글쓰기 완료',
           font=('궁서', 25), bg='black', fg='white',
           command=result
           )
b2.pack()

w2.mainloop()