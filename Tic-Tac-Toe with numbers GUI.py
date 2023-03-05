from tkinter import *
import tkinter.messagebox
'''
Program: Tic Tac Toe Game
author: Omar Adel
Date: 3 March 2022
Virsion: 1.4
'''

table = Tk()
table.title("Tic-Tac-Toe with numbers")

click = True
count = 0
unavailable_num = []

btn1 = IntVar()
btn2 = IntVar()
btn3 = IntVar()
btn4 = IntVar()
btn5 = IntVar()
btn6 = IntVar()
btn7 = IntVar()
btn8 = IntVar()
btn9 = IntVar()
selected_num = StringVar()

#set board play
def play():
    button1 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#90caf9", fg="#90caf9", textvariable=btn1, command=lambda:press(1,0,0))
    button1.grid(row=0,column=0)

    button2 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#90caf9", fg='#90caf9', textvariable=btn2, command=lambda:press(2,0,1))
    button2.grid(row=0,column=1)

    button3 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#90caf9", fg='#90caf9', textvariable=btn3, command=lambda:press(3,0,2))
    button3.grid(row=0,column=2)

    button4 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#42a5f5", fg='#42a5f5', textvariable=btn4, command=lambda:press(4,1,0))
    button4.grid(row=1,column=0)

    button5 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#42a5f5", fg='#42a5f5', textvariable=btn5, command=lambda:press(5,1,1))
    button5.grid(row=1,column=1)

    button6 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#42a5f5", fg='#42a5f5', textvariable=btn6, command=lambda:press(6,1,2))
    button6.grid(row=1,column=2)

    button7 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#1565c0", fg='#1565c0', textvariable=btn7, command=lambda:press(7,2,0))
    button7.grid(row=2,column=0)

    button8 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#1565c0", fg='#1565c0', textvariable=btn8, command=lambda:press(8,2,1))
    button8.grid(row=2,column=1)

    button9 = Button(table, height=8, width=18, relief='ridge', bd=1, bg="#1565c0", fg='#1565c0', textvariable=btn9, command=lambda:press(9,2,2))
    button9.grid(row=2,column=2)

    ask_user = Label(table, text = f"Enter the number then click place u want:\ndelete num after select\nplayer1 [1,3,5,7,9], player2 [0,2,4,6,8]", height=3, font=("futura-bold",15))
    ask_user.grid(row=0,column=3)

    num_input = Entry(table, width=1, font=("futura-bold",40), textvariable=selected_num)
    num_input.grid(row=1,column=3)

    btn = Button(table, text="Enter number", width=17, height=2, font=('futura-bold',12), bg='#ff5722', relief='ridge', bd=3, command=lambda:press )
    btn.grid(row=2,column=3)

# mange the press and appare
def press(num,r,c):
    global click, count
    entered_num = selected_num.get()
    
    if click == True:
        if entered_num in ['1','3','5','7','9']:
            unavailable(entered_num,num,r,c)
            
            if num == 1 or num == 2 or num == 3:
                bgc = '#90caf9'
            elif num == 4 or num == 5 or num ==6:
                bgc = '#42a5f5'
            else:
                bgc = '#1565c0'
            
            number = Label(table, text=selected_num.get(), bg=bgc, font=("Blond",40), fg="#e53935")
            number.grid(row=r,column=c)
            
            if num == 1:
                btn1.set(entered_num)
            elif num == 2:
                btn2.set(entered_num)
            elif num == 3:
                btn3.set(entered_num)
            elif num == 4:
                btn4.set(entered_num)
            elif num == 5:
                btn5.set(entered_num)
            elif num == 6:
                btn6.set(entered_num)
            elif num == 7:
                btn7.set(entered_num)
            elif num == 8:
                btn8.set(entered_num)
            else:
                btn9.set(entered_num)
            count += 1
            click = False
            check_winner1()
        else:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player1: Soory !!! select your number only")
    else:
        if entered_num in ['0','2','4','6','8']:
            unavailable(entered_num,num,r,c)
           
            if num == 1 or num == 2 or num == 3:
                bgc = '#90caf9'
            elif num == 4 or num == 5 or num ==6:
                bgc = '#42a5f5'
            else:
                bgc = '#1565c0'
           
            number = Label(table, text=selected_num.get(), bg=bgc, font=("Blond",40), fg="#388e3c")
            number.grid(row=r,column=c)
            
            if num == 1:
                btn1.set(entered_num)
            elif num == 2:
                btn2.set(entered_num)
            elif num == 3:
                btn3.set(entered_num)
            elif num == 4:
                btn4.set(entered_num)
            elif num == 5:
                btn5.set(entered_num)
            elif num == 6:
                btn6.set(entered_num)
            elif num == 7:
                btn7.set(entered_num)
            elif num == 8:
                btn8.set(entered_num)
            else:
                btn9.set(entered_num)
            count += 1
            click = True
            check_winner2()
        else:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player2: Soory !!! select your number only")

# check if player1 win or draw
def check_winner1():
    global click, count

    try:
        if (int(btn1.get()) + int(btn2.get()) + int(btn3.get()) == 15 or int(btn4.get()) + int(btn5.get()) + int(btn6.get()) == 15 or
        int(btn7.get()) + int(btn8.get()) + int(btn9.get()) == 15 or int(btn1.get()) + int(btn4.get()) + int(btn7.get()) == 15 or
        int(btn2.get()) + int(btn5.get()) + int(btn8.get()) == 15 or int(btn3.get()) + int(btn6.get()) + int(btn9.get()) == 15 or
        int(btn1.get()) + int(btn5.get()) + int(btn9.get()) == 15 or int(btn3.get()) + int(btn5.get()) + int(btn7.get()) == 15):
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player1 Win !!!")
            click =True
            count = 0
            clear()
            play()
        elif count == 9:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Draw !!!")
            click = True
            count = 0
            clear()
            play()
    except ValueError:
        pass

# check if player 2 win or draw
def check_winner2():
    global click, count

    try:
        if (int(btn1.get()) + int(btn2.get()) + int(btn3.get()) == 15 or int(btn4.get()) + int(btn5.get()) + int(btn6.get()) == 15 or
        int(btn7.get()) + int(btn8.get()) + int(btn9.get()) == 15 or int(btn1.get()) + int(btn4.get()) + int(btn7.get()) == 15 or
        int(btn2.get()) + int(btn5.get()) + int(btn8.get()) == 15 or int(btn3.get()) + int(btn6.get()) + int(btn9.get()) == 15 or
        int(btn1.get()) + int(btn5.get()) + int(btn9.get()) == 15 or int(btn3.get()) + int(btn5.get()) + int(btn7.get()) == 15):
        
            tkinter.messagebox.showinfo("Tic Tac Toe", "Player2 Win !!!")
            click =True
            count = 0
            clear()
            play()
        elif count == 9:
            tkinter.messagebox.showinfo("Tic Tac Toe", "Draw !!!")
            click = True
            count = 0
            clear()
            play()
    except ValueError:
        pass

# protect put number twice
def unavailable(snum,num,r,c):
    if snum in unavailable_num:
        tkinter.messagebox.showinfo("Tic Tac Toe", 'Sorry!! this num has been selected !!!')
        selected_num.set('')
        press(num,r,c)
    else:
        unavailable_num.append(snum)

# delete all and prepare game to new tern
def clear():
    global unavailable_num
    btn1.set(0)
    btn2.set(0)
    btn3.set(0)
    btn4.set(0)
    btn5.set(0)
    btn6.set(0)
    btn7.set(0)
    btn8.set(0)
    btn9.set(0)
    unavailable_num = []

play()

table.mainloop()