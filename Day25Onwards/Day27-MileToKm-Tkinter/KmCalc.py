import tkinter
import math
window = tkinter.Tk()
window.minsize(height=200,width=300)
text_box = tkinter.Entry()
text_box.grid(row = 0, column= 1)

miles_label = tkinter.Label(text="Miles")
miles_label.grid(row= 0,column=2)

equals_label = tkinter.Label(text="is Equal to")
equals_label.grid(row=1,column=0)

result= tkinter.Label()
result.grid(row=1,column=1)

km_label = tkinter.Label(text="km")
km_label.grid(row=1,column=2)

def calculation():
    mile = text_box.get()
    result.config(text=math.floor(int(mile)*1.6))

calc_button = tkinter.Button(text="Calculate",command=calculation)
calc_button.grid(row=2,column=1)
window.mainloop()