from tkinter import *

window = Tk()

window.title("Calculator")
window.configure(bg='#808B96')
window.resizable(False, False)

# -- initialization
operator = ''
num1 = 0

standard_font = ('courier', '20')
button_color = '#566573'
font_color = '#FDFEFE'


def operation(n1, n2):

    if operator == '-':
        return n1 - n2

    elif operator == '+':
        return n1 + n2

    elif operator == '/':
        return n1 / n2

    elif operator == '*':
        return n1 * n2

    else:
        return n2


def insert(value):

    global operator, num1

    # get the current displayed string
    curr = result.cget('text')
    result.configure(text='')

    # remove the last number inserted
    if value == 'del':
        curr = curr.replace(curr[-1], '', 1)
        result.configure(text=curr)

    # toggle off negative sign
    elif value == 'neg':

        if float(curr) > 0:
            curr = '-' + curr;
            result.configure(text=curr)

        elif float(curr) < 0:
            curr = curr.replace('-', '')
            result.configure(text=curr)

    # clear the displayed string
    elif value == 'clr':
        curr = ''
        result.configure(text='')

    else:
        # appends the current string with additional numeral(s)
        if len(curr) < 10:

            if value.isdigit() or value == '.' and curr.find('.') < 0:
                curr = curr + value

            elif curr.find('.') >= 0:
                curr = curr

        result.configure(text=curr)

        # --- operators insertion
        # val == addtion
        if value == '+' and curr != '':
            num1 = float(curr)
            operator = '+'
            result.configure(text="")

        # val == subtraction
        elif value == '-' and curr != '':
            num1 = float(curr)
            operator = '-'
            result.configure(text="")

        # val == multiplication
        elif value == '*' and curr != '':
            num1 = float(curr)
            operator = '*'
            result.configure(text="")

        # val == division
        elif value == '/' and curr != '':
            num1 = float(curr)
            operator = '/'
            result.configure(text='')

        # val == equal
        elif value == '=' and curr != '':

            if operator == '':
                result.configure(text=curr)

            else:
                num2 = float(curr)
                ans = operation(num1, num2)
                ans = f'{ans:g}'
                result.configure(text=str(ans))
                operator = ''

        # --- end of operator insertion


result = Label(window, text="", height=2, width=12, bg='#808B96', font=standard_font, fg=font_color)
result.grid(column=0, columnspan=5, row=0, rowspan=2, sticky='nesw')

# -- first row
btn7 = Button(window, text="7", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('7'))
btn8 = Button(window, text="8", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('8'))
btn9 = Button(window, text="9", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('9'))
btn_pls = Button(window, text="+", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('+'))
btn_clear = Button(window, text="clr", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('clr'))

btn7.grid(column=0, row=3, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn8.grid(column=1, row=3, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn9.grid(column=2, row=3, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_pls.grid(column=3, row=3, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_clear.grid(column=4, row=3, padx=(2, 2), pady=(2, 2), sticky='nesw')
# -- end of first row

# -- second row
btn4 = Button(window, text="4", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('4'))
btn5 = Button(window, text="5", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('5'))
btn6 = Button(window, text="6", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('6'))
btn_min = Button(window, text="-", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('-'))
btn_del = Button(window, text="del", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('del'))

btn4.grid(column=0, row=4, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn5.grid(column=1, row=4, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn6.grid(column=2, row=4, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_min.grid(column=3, row=4, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_del.grid(column=4, row=4, padx=(2, 2), pady=(2, 2), sticky='nesw')
# -- end of second row

# -- third row
btn1 = Button(window, text="1", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('1'))
btn2 = Button(window, text="2", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('2'))
btn3 = Button(window, text="3", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('3'))
btn_mul = Button(window, text="*", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('*'))
btn_neg = Button(window, text="neg", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('neg'))

btn1.grid(column=0, row=5, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn2.grid(column=1, row=5, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn3.grid(column=2, row=5, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_mul.grid(column=3, row=5, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_neg.grid(column=4, row=5, padx=(2, 2), pady=(2, 2), sticky='nesw')
# -- end of third row

# -- forth row
btn0 = Button(window, text="0", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('0'))
btn_dot = Button(window, text=".", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('.'))
btn_equal = Button(window, text="=", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('='))
btn_div = Button(window, text="/", height=2, width=3, bd=0, font=standard_font, bg=button_color, fg=font_color, command=lambda: insert('/'))

btn0.grid(column=0, row=6, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_dot.grid(column=1, row=6, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_equal.grid(column=2, row=6, padx=(2, 2), pady=(2, 2), sticky='nesw')
btn_div.grid(column=3, row=6, padx=(2, 2), pady=(2, 2), sticky='nesw')
# -- end of third row

window.mainloop()

