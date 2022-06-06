from tkinter import *
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import os
import pyttsx3

time.clock = time.time

#Making a object of the Chatbot class and training it to give the answer
bot=ChatBot('Tom')
trainer=ListTrainer(bot)

for files in os.listdir('data/hindi/'):
    data=open('data/hindi/'+files,'r',encoding='utf-8').readlines()
    trainer.train(data)

def botreply():
    question=questionfield.get()
    question=question.capitalize()
    answer=bot.get_response(question)
    textarea.insert(END,'You: '+question+'\n\n')
    textarea.insert(END,'Tom: '+str(answer)+'\n\n')
    pyttsx3.speak(answer)
    questionfield.delete(0,END)

root=Tk()
root.geometry("550x570+100+30")
root.title("Talking ChatBot")
root.config(bg='aquamarine')

botpic=PhotoImage(file='pic.png')
botpiclabel=Label(root,image=botpic,bg='white')
botpiclabel.pack(side=TOP,pady=15)

centerFrame=Frame(root)
centerFrame.pack()

scroll=Scrollbar(centerFrame)
scroll.pack(side=RIGHT)

textarea=Text(centerFrame,font=('times new roman',20,'bold'),height=10,relief=SUNKEN,yscrollcommand=scroll.set,wrap='word')
textarea.pack(side=LEFT)
scroll.config(command=textarea.yview)

questionfield=Entry(root,font=('arial',23,'bold'),relief=SUNKEN)
questionfield.pack(pady=15,fill=X)

askimage=PhotoImage(file='ask.png')
askbutton=Button(root,image=askimage,bg='white',command=botreply)
askbutton.pack()

#Giving The ask button Function to the Enter button in keyboard.
def click(event):
    askbutton.invoke()

root.bind('<Return>',click)

root.mainloop()