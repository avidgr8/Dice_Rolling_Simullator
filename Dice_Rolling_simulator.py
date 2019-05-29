# import random
# print('This is dice rolling!')
# def rolldice():
#     print("The dice says : ", end="")
#     print(random.randrange(1,7))
# for i in range(0,20):
#     again=input('do you want to roll (y/n) ')
#     if(again=='y'):
#         rolldice()
#     elif(again=='n'):
#         print('thank you for playing')
#         break
#     else:
#         print('invalid input')
#         break


import tkinter as tk
import random

mainwindow=tk.Tk()
mainwindow.title('DICE ROLLING GAME')
label=tk.Label(mainwindow,text='This is dice rolling!')
label.pack()
label1=tk.Label(mainwindow,text='Do you want to roll (y/n) ')
label1.pack()
choice=tk.Entry(mainwindow)
choice.pack()

button=tk.Button(mainwindow,text='Roll',command=lambda: rolling())
button.pack()

def rolling():
    choicemade=choice.get()
    if (choicemade=='y'):
        rand=random.randrange(1,7)
        result.config(text='The rolled no. is : ' + str(rand))
    elif(choicemade=='n'):
        result.config(text='Thank you for playing')
    else:
        result.config(text='invalid input')

result=tk.Label(mainwindow, text="Choices you made in life!!")
result.pack()
mainwindow.mainloop()