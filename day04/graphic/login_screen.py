# import tkinter        기본적으로 모듈을 불러올 때 사용
from tkinter import *   # 이렇게 설정을 하면 따로 tkinter를 쓰지 안아도 그냥 쓸수있다.
from tkinter import messagebox
# 함수 생성
    # 버튼을 눌렀을때 로그인 기능을 처리해야함
    # 특정한 기능은 하나의 함수로 만들어주면 된다.
    # 버튼을 눌렀을 때 처리하고 하는 기능 하나는 함수하나가 됨
    # 함수를 만드는 것을 함수를 정의한다라고 함
    # 기능을 프로그래머가 정의하기 때문에 우리는 이것을 함수를 정의한다라고 함

# 파이썬 문법을 이용해서 함수 정의

def login():
    # id 입력한 값, qw 입력한 값을 가지고 와야함
    # 원래 회원 가입을 할 때의 id/pw와 입력한 값을 비교해야함
    id2 = id_entry.get() # id_entry에 입력한 값을 get을 이용해서 가져오고 그것을 id2에 넣는다.
    print('입력한 id는', id2)
    # pw 입력한 값 가지고와서 프린트
    pw2 = pw_entry.get()
    print('입력한 pw는', pw2)
    # result
    # 원래의 id:root/pw:1234
    # 원래 정해진것과 입력한 id/pw가 동일한지 판별하는 프린트트
    if id2 == 'root' and pw2 == '1234':

        def result():
            result_num = number_entry.get()
            print('번호는', result_num)
            result_title = title_entry.get()
            print('제목은', result_title)
            result_body = body_entry.get()
            print('내용은', result_body)
            result_wri = writer_entry.get()
            print('작성자는', result_wri)

        print('로그인이 성공하셨습니다.')
        messagebox.showinfo('로그인 성공', '축하합니다.')
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
                    font=('궁서', 25), bg='pink', fg='black',
                    command=result
                    )
        b2.pack()

        w2.mainloop()
    else:
        print('로그인에 실패하셨습니다.')
        result = Label(w,
                       text='로그인에 실패하셨습니다.', font=('궁서', 20), fg='red'
                       )
        result.pack()


w = Tk()             # Tk 를 이용하기 위해서 변수로 지정
w.geometry('500x300')   # 띄울 화면의 크기를 결정


id = Label(w, text='사용자 ID 입력', font=('궁서',30))
        # 창에 글씨를 쓸 경우에 사용한다
        # text는 들어갈 내용, font는 글자체,크기(set) bg는 배경색, fg는 글자색
id.pack()
        # pack은 입력한 순서대로 올라간다
id_entry = Entry(w, font=('궁서',25), bg='black', fg='white')
        # Entry는 입력하는 란은 생성 Entry(어디로 올라갈지)
id_entry.pack()

pw = Label(w, text='사용자 PW 입력', font=('궁서',30))
pw.pack()
pw_entry = Entry(w, font=('궁서',25), bg='black', fg='white')
        # Entry는 입력하는 란은 생성 Entry(어디로 올라갈지)
pw_entry.pack()

b = Button(w,
           text='로그인처리', font=('궁서',30), bg='black', fg='white',
           command=login    # ()를 쓰지않고 함수만 쓴다.
           )
b.pack()

w.mainloop() # 계속해서 띄워져 있다 (맨 마지막에 써져있어야 함)