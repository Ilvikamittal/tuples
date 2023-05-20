from tkinter import*
import random
root=Tk()

root.title("tuples")
root.geometry("700x700")
root.configure(background="red")

Months=("January","Febuaray","March","April","May","June","July","Augest","September","October","November","December")  
Profit=(3400,4000,2060,5080,7480,6789,4690,7430,8020,8760,5420,4680)

months=Label(root,text=Months)
months.place(relx=0.5,rely=0.1,anchor=CENTER)

profit=Label(root,text=Profit)
profit.place(relx=0.5,rely=0.2,anchor=CENTER)

max_profit=Label(root)
max_profit.place(relx=0.5,rely=0.4,anchor=CENTER)

min_profit=Label(root)
min_profit.place(relx=0.5,rely=0.6,anchor=CENTER)

def max_profit():
    max_p=max(Profit)
    max_index=Profit.index(max_p)
    
    max_m=Months[max_index]
    print("The maximum profit is "+str(max_p)+" Which was recorded in the month of "+str(max_m))

btn_1=Button(root,text="Show maximum profits",command=max_profit)
btn_1.place(relx=0.5,rely=0.3,anchor=CENTER)

def min_profit():
    min_p=min(Profit)
    min_index=Profit.index(min_p)
    
    min_m=Months[min_index]
    print("The minimum profit is "+str(min_p)+"Which was recorded in the month of "+str(min_m))

btn_2=Button(root,text="Show minimum profit",command=min_profit)
btn_2.place(relx=0.5,rely=0.5,anchor=CENTER)



root.mainloop()


