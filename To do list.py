import tkinter

r=tkinter.Tk()
r.title("TO DO LIST")
r.config(bg="darkgreen")
r.geometry("400x500")

up=False

def update():
    outputvar.set("")

                                   
def addlistbar():
    global up
    if inputvar.get()=="":                                      
            outputvar.set("Input bar is empty")

    else:   
        if up==True:                                                    
            selected=lb.curselection()                                  
            if selected and inputvar.get() not in lb.get(0,"end"):     
                lb.delete(selected[0])                                  
                lb.insert(selected[0],inputvar.get())                   
                up=False                                                
                outputvar.set("Task updated successfully")
            
            else:                                                       
                up=False
                addlistbar()                                          
            
        
        else:                                                        
            l=lb.get(0,"end")                                           
            if inputvar.get() not in l:                                 
                lb.insert("end",inputvar.get())
                outputvar.set("Task added successfully")
            else:                                                     
                outputvar.set("Task already exist")
        
    inputvar.set("")                                        

    lb.selection_clear(0,"end")                                   
    r.after(1500,update)

                                           
def updatelistbar():
    global up
    l=lb.get(0,"end")                                                            
    if not l:                                                      
        outputvar.set("list is empty")
        
    else:                                                          
        selected=lb.curselection()                                  
        if selected:                                                
            
            inputvar.set(lb.get(selected[0]))
            up=True
            
            
        else:
            outputvar.set("No Task selected")
    r.after(1500,update)


                                  
def deletelistitem():
    s=lb.get(0,"end")                                                                    
    if not s:                                                       
        outputvar.set("List is Empty")
    else:                                                           
        selected=lb.curselection()                                                           
        if selected:                                                
            lb.delete(selected[0])
            outputvar.set("Deleted successfully")  
        else:
            outputvar.set("No Task selected")                      

    r.after(1500,update)

                           
def click(event):
    if event.widget.cget("text")=="CREATE":                                 
            addlistbar()
            
    elif event.widget.cget("text")=="UPDATE":                               
        updatelistbar()

    else:
        deletelistitem()                                                    


Heading=tkinter.Label(r,text="TO DO LIST",fg="white",bg="pink",font=("Arial",20,"italic","bold"),pady=15)
Heading.pack()

                                             
f1=tkinter.Frame(r)
f1.pack(fill="x",pady=5)
sb=tkinter.Scrollbar(f1)                                                                    
sb.pack(side="right",fill="y")

lb=tkinter.Listbox(f1,height=5,width=50,yscrollcommand=sb.set)                              
lb.pack(fill="x")
sb.config(command=lb.yview)                                                                 

                                             
f2=tkinter.Frame(r,bg="Brown")
f2.pack()

inputvar=tkinter.StringVar()                                                                                 
inputlabel=tkinter.Label(f2,text="Input Task",bg="darkgreen",fg="white",font=("Ariel",13),padx=10)       
inputlabel.grid(row=0,column=0)
inputentry=tkinter.Entry(f2,font=("Ariel",15,"bold"),textvariable=inputvar)                                  # Entry widget inputvar connect with it
inputentry.grid(row=0,column=1,pady=5)

outputvar=tkinter.StringVar()                                                                                # string variable for output 
outputentry=tkinter.Entry(f2,state="readonly",width=25,justify="center",bg="black",fg="darkgrey",font=("Ariel",10,"bold"),textvariable=outputvar) # Entry widget ioutputvar connect with it
outputentry.grid(row=1,column=1)

                                         # frame for button
f3=tkinter.Frame(r,bg="Red")
f3.pack(pady=50)

#B
button=tkinter.Button(f3,text="CREATE",width=20,fg="white",bg="grey",padx=10)                               # create button to add new item
button.grid(row=0,column=0,pady=10)
button.bind("<Button-1>",click)
#B
button=tkinter.Button(f3,text="UPDATE",width=20,fg="white",bg="grey",padx=10)                               # update button to update current item
button.grid(row=2,column=0,pady=10)
button.bind("<Button-1>",click)
#B
button=tkinter.Button(f3,text="DELETE",width=20,fg="white",bg="grey",padx=10)                               # delete button to delete item from list
button.grid(row=3,column=0,pady=10)
button.bind("<Button-1>",click)
#B
button=tkinter.Button(f3,text="QUIT",width=20,fg="white",bg="red",padx=10,command=quit)                     # quit button to close the program
button.grid(row=4,column=0,pady=10)


r.mainloop()