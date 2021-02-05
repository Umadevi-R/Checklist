from tkinter import *
root=Tk()
root.title('Your Checklist')
root.iconbitmap('check.ico')
root.geometry('400x400')
root.resizable(0,0)

#define fonts and colors
fonts=('Times New Roman',12)
root_color='#6c1cbc'
bt_color='#e2cff4'
root.config(bg=root_color)

#functions
def addItem():
    list_box.insert(END,list_entry.get())
    list_entry.delete(0,END)
def removeItem():
    list_box.delete(ANCHOR)
def clearList():
    list_box.delete(0,END)
    try:
        with open('store.txt','w') as f:
            f.truncate()
            f.close()
    except:
        return
def saveList():
    with open('store.txt','w') as f:
        tup=list_box.get(0,END)
        for item in tup:
            if item.endswith('\n'):
                f.write(item)
            else:
                f.write(item+'\n')
        f.close()
def openList():
    try:
        with open('store.txt','r') as f:
            for line in f:
                list_box.insert(END,line)
    except:
        return

#layout
#frames
inp=Frame(root,bg=root_color)
out=Frame(root,bg=root_color)
buttonF=Frame(root,bg=root_color)
inp.pack()
out.pack()
buttonF.pack()

#inp frame
list_entry=Entry(inp,width=35,borderwidth=3,font=fonts)
add_button=Button(inp,text='Add item',borderwidth=2,font=fonts,bg=bt_color,command=addItem)
list_entry.grid(row=0,column=0,padx=5,pady=5)
add_button.grid(row=0,column=1,padx=5,pady=5,ipadx=5)

#out frame
sb=Scrollbar(out)
list_box=Listbox(out,width=45,height=15,borderwidth=3,font=fonts,yscrollcommand=sb.set)
sb.config(command=list_box.yview)
list_box.grid(row=0,column=0)
sb.grid(row=0,column=1,sticky='NS')

#buttonF frame
remove_button=Button(buttonF,text='Remove item',borderwidth=2,font=fonts,bg=bt_color,command=removeItem)
clear_button=Button(buttonF,text='Clear List',borderwidth=2,font=fonts,bg=bt_color,command=clearList)
save_button=Button(buttonF,text='Save List',borderwidth=2,font=fonts,bg=bt_color,command=saveList)
quit_button=Button(buttonF,text='Quit',command=root.destroy,borderwidth=2,font=fonts,bg=bt_color)
remove_button.grid(row=0,column=0,padx=2,pady=10)
clear_button.grid(row=0,column=1,padx=2,pady=10,ipadx=10)
save_button.grid(row=0,column=2,padx=2,pady=10,ipadx=10)
quit_button.grid(row=0,column=3,padx=2,pady=10,ipadx=25)

openList()

root.mainloop()
