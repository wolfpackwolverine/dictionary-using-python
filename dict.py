from tkinter import *
from tkinter.font import Font
import json
#from difflib import get_close_matches
dict={}
f=open("dictionary.json","r")
s=f.read()
dict=json.loads(s)
f.close()

def lookup():
    word=entry.get()
    word=word.upper()
    if word in dict.keys():
        answer.delete(1.0,END)
        answer.insert(INSERT,dict[word])
    else:
        answer.delete(1.0,END)
        answer.insert(INSERT,'Word Not Found')
root= Tk()
root.title("Dictionary")
mainframe=Frame(root)

my_font = Font(size=36,weight='bold')
one=Label(root,text='Dictionary',font=my_font,bg='skyblue')
one.pack(fill=X)

mainframe.pack(side=TOP)

topframe= LabelFrame(root,text='Input',padx=5,pady=5,bg='skyblue')

entry=Entry(topframe,width=55)
entry.pack(side=LEFT)
button=Button(topframe,text="search",command=lookup)
button.pack()

topframe.pack(side=TOP)

bottomframe=Frame(root,bg='skyblue')

scroll=Scrollbar(bottomframe)
scroll.pack(side=RIGHT,fill=Y)
answer=Text(bottomframe,width=46,height=17,yscrollcommand=scroll.set,wrap=WORD)
scroll.config(command=answer.yview)
answer.pack(side=LEFT)

bottomframe.pack()
root.geometry("400x400")
root.mainloop()
