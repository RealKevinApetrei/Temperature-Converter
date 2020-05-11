# This code is poorly set out.

# ============================================================================
# ============================================================================
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# ============================================================================
# ============================================================================

from tkinter import *
import sys


def back_button():
    main.destroy()
    sys.exit()


def back_button2():
    screen2.destroy()
    main_program()


def back_button3():
    screen3.destroy()
    main_program()


def close_error1():
    screen4.destroy()


def close_error2():
    screen5.destroy()


def invalid_value1():
    global screen4
    screen4 = Toplevel(screen2)
    screen4.title("Error has Occured.")
    screen4.geometry("250x150")
    screen4.resizable(False, False)


    Label(screen4, text="Something went wrong...", bg="grey", width="250", height="2").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="Enter number values only!").pack()
    Label(screen4, text="").pack()
    Button(screen4, text="OK", command=close_error1).pack()


def invalid_value2():
    global screen5
    screen5 = Toplevel(screen3)
    screen5.title("Error has Occured.")
    screen5.geometry("250x150")
    screen5.resizable(False, False)

    Label(screen5, text="Something went wrong...", bg="grey", width="250", height="2").pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Enter number values only!").pack()
    Label(screen5, text="").pack()
    Button(screen5, text="OK", command=close_error2).pack()


def convert_c_to_f():
        try:
            celsius_input = int(celsius_val.get())

            fahrenheit_result = (celsius_input * 1.6) + 32
            fahrenheit_result_round = round(fahrenheit_result)

            Label(screen2,  text=str(fahrenheit_result_round) + " Degrees Fahrenheit", bg="grey", height="2").pack()
        except:
            invalid_value1()

        celsius_entry.delete(0, END)


def c_to_f():
    main.destroy()

    global screen2
    screen2 = Tk()
    screen2.title("Convert Celsius to Fahrenheit")
    screen2.geometry("500x500")
    screen2.resizable(False, False)

    global celsius_entry
    global celsius_val
    celsius_val = StringVar()

    Button(screen2, text="> Back <", command=back_button2).place(x=430, y=460)

    Label(screen2, text="Convert Celsius to Fahrenheit", bg="grey", width="500", height="2").pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Enter a Temperature (Celsius):").pack()
    celsius_entry = Entry(screen2, textvariable=celsius_val)
    celsius_entry.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Convert", command=convert_c_to_f).pack()
    Label(screen2, text="").pack()


def convert_f_to_c():
    try:
        fahrenheit_input = fahrenheit_val.get()
        celsius_result = (fahrenheit_input - 32) * 0.5556
        celsius_result_round = round(celsius_result)

        Label(screen3, text=str(celsius_result_round) + " Degrees Celsius", bg="grey", height="2").pack()
    except:
        invalid_value2()

    fahrenheit_entry.delete(0, END)


def f_to_c():
    main.destroy()

    global screen3
    screen3 = Tk()
    screen3.title("Convert Fahrenheit to Celsius")
    screen3.geometry("500x500")
    screen3.resizable(False, False)

    global fahrenheit_entry
    global fahrenheit_val
    fahrenheit_val = IntVar()

    Button(screen3, text="> Back <", command=back_button3).place(x=430, y=460)

    Label(screen3, text="Convert Fahrenheit to Celsius", bg="grey", width="500", height="2").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Enter a Temperature (Fahrenheit):").pack()
    fahrenheit_entry = Entry(screen3, textvariable=fahrenheit_val)
    fahrenheit_entry.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Convert", command=convert_f_to_c).pack()
    Label(screen3, text="").pack()


def main_program():
    global main
    main = Tk()
    main.title("Temperature Converter")
    main.geometry("500x500")
    main.resizable(False, False)

    Button(text="> Exit <", command=back_button).place(x=430, y=460)

    Label(text="Temperature Converter", bg="grey", width="500", height="2").pack()
    Label(text="").pack()

    Button(text="Convert Celsius to Fahrenheit", width="250", height="2", command=c_to_f).pack()
    Label(text="").pack()
    Button(text="Convert Fahrenheit to Celsius", width="250", height="2", command=f_to_c).pack()

    main.mainloop()


main_program()

# ============================================================================
# ============================================================================
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# Made by: https://github.com/OzonePrograms/
# ============================================================================
# ============================================================================

# Thanks for using!
