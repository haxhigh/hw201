from tkinter import *
window=Tk()
window.title('Simple Interest Calculator')
window.geometry("500x400")
window.configure(bg='grey')
   
def calculate_interest():
    p = float(principle.get())
    r = float(rate.get())
    t = float(time.get())
    i = (p*r*t)/100
    interest = round(i, 2)
    message=Label(result_frame,text="Interest on Rs."+str(p)+" at rate of interest "+str(r)+"% for "+str(t)+" years is Rs."+str(interest), bg = "grey", font=("Calibri", 12), width=55)
    message.place(x=100,y=40,anchor=CENTER)
    message.pack()

app_label=Label(window, text="SIMPLE INTEREST CALCULATOR", bg = "grey")
app_label.place(x=250, y=10,anchor=CENTER)

principle_label=Label(window, text="Principle in Rs", bg = "grey")
principle_label.place(x=100, y=100,anchor=CENTER)
principle=Entry(window, text="", width=22)
principle.place(x=300, y=100,anchor=CENTER)

rate_label=Label(window, text="Rate of Interest in %", bg = "grey")
rate_label.place(x=100, y=150,anchor=CENTER)
rate=Entry(window, text="", width=15)
rate.place(x=300, y=150,anchor=CENTER)

time_label=Label(window, text="Time in Yrs", bg = "grey")
time_label.place(x=100, y=200,anchor=CENTER)
time=Entry(window, text="", width=15)
time.place(x=300, y=200,anchor=CENTER)

calculate_button=Button(window,text="done",bg = "grey",command=calculate_interest)
calculate_button.place(x=100,y=250,anchor=CENTER)

result_frame = LabelFrame(window, bg = "grey")
result_frame.place(x=250,y=350,anchor=CENTER)

window.mainloop()