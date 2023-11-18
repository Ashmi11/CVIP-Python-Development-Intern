from tkinter import *

first_number=second_number=operator=None

# Function to display numbers on the screen
def get_digit(digit):
    current = result_display['text']
    new = current + str(digit)
    result_display.config(text=new)


#  Function to delete values on display
def  clear():
    result_display.config(text='')


# Function to be able to operate with decimal values
def get_decimal():
    current_display_value= result_display['text']
    if current_display_value.find(".")==-1:
        result_display.config(text='')
        result_display.config(text=str(current_display_value + "."))


#  Function to enable desired operation to be performed
def get_operator(op):
    global first_number,operator

    first_number = float(result_display['text'])
    operator = op
    result_display.config(text='')


#  Function to display final result on screen
def get_result():
    global first_number,second_number,operator

    second_number = float(result_display['text'])

    if operator == '+':
        result_display.config(text=str(first_number + second_number))
    elif operator == '-':
        result_display.config(text=str(first_number - second_number))
    elif operator == '*':
        result_display.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_display.config(text='Error')
        else:
            result_display.config(text=str(round(first_number / second_number, 2)))

# To create the basic GUI
root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

# To define how the output should be displayed
result_display = Label(root, text='', bg='black', fg='white')
result_display.grid(row=0, column=0, columnspan=5, pady=(50, 25), sticky='w')
result_display.config(font=('verdana', 30, 'bold'))


# Creation and styling of buttons

btn_clr = Button(root,text='C',bg='lavender',fg='dark red',width=5,height=2,command=lambda :clear())
btn_clr.grid(row=0,column=3,pady=(70,0))
btn_clr.config(font=('verdana',14))

btn7 = Button(root,text='7',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('verdana',14))

btn8 = Button(root,text='8',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('verdana',14))

btn9 = Button(root,text='9',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('verdana',14))

btn_div = Button(root,text='/',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_operator('/'))
btn_div.grid(row=1,column=3)
btn_div.config(font=('verdana',14))

btn4 = Button(root,text='4',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('verdana',14))

btn5 = Button(root,text='5',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('verdana',14))

btn6 = Button(root,text='6',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('verdana',14))

btn_prod = Button(root, text='*', bg='lavender',fg='dark red', width=5, height=2, command=lambda :get_operator('*'))
btn_prod.grid(row=2, column=3)
btn_prod.config(font=('verdana', 14))

btn1 = Button(root,text='1',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('verdana',14))

btn2 = Button(root,text='2',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('verdana',14))

btn3 = Button(root,text='3',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('verdana',14))

btn_sub = Button(root,text='-',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_operator('-'))
btn_sub.grid(row=3,column=3)
btn_sub.config(font=('verdana',14))

btn_dec = Button(root,text='.',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_decimal())
btn_dec.grid(row=4,column=0)
btn_dec.config(font=('verdana',14))

btn0 = Button(root,text='0',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('verdana',14))

btn_equals = Button(root,text='=',bg='lavender',fg='dark red',width=5,height=2,command=get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('verdana',14))

btn_add = Button(root,text='+',bg='lavender',fg='dark red',width=5,height=2,command=lambda :get_operator('+'))
btn_add.grid(row=4,column=3)
btn_add.config(font=('verdana',14))

root.mainloop()