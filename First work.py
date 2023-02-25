import tkinter
from math_statistics import average, median, find_min, find_max


def calculate():
    numbers = list(map(float, entry.get().split()))
    label2['text'] = f'Arithmetic average: {average(numbers)}'
    label3['text'] = f'Median: {median(numbers)}'
    label4['text'] = f'Max value: {find_max(numbers)}'
    label5['text'] = f'Min value: {find_min(numbers)}'


window = tkinter.Tk()
window.geometry('270x400')
window.title('Work with array')
window.resizable(False, False)

label_1 = tkinter.Label(text='Good day!', font=('Aria', 20), width=15, fg='Purple')
label_1.pack()

entry = tkinter.Entry(font=('Times New Roman', 15), width=200, bg='white')
entry.pack()

button = tkinter.Button(text='Calculate', font=('Black Colibria', 12), activeforeground='Green', command=calculate)
button.pack()

label2 = tkinter.Label(text='Arithmetic average: ', font=('Times New Roman', 12), fg='Green')
label2.place(x=10, y=100)
label3 = tkinter.Label(text='Median: ', font=('Times New Roman', 12), fg='Green')
label3.place(x=10, y=120)
label4 = tkinter.Label(text='Max value: ', font=('Times New Roman', 12), fg='Green')
label4.place(x=10, y=140)
label5 = tkinter.Label(text='Min value: ', font=('Times New Roman', 12), fg='Green')
label5.place(x=10, y=160)
window.mainloop()
