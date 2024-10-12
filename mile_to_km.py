from tkinter import *

window = Tk()
window.minsize(width=300,height=150)
window.config(padx=40, pady=40)
window.title("Mile to KM Converter")

input = Entry(width=10)
input.grid(row=0,column=1)

def clicked():
    entry_mile = float(input.get())  # Değeri float olarak alıyoruz
    converted_mile = entry_mile * 1.6
    km.config(text=f"{converted_mile:.2f}")  
    

miles_label = Label(text="Miles" , font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to" , font=("Arial", 12, "bold"))
is_equal_label.grid(row=1, column=0)

km = Label(text="0", font=("Arial" , 12, "italic"))
km.grid(row=1,column=1)

text_km_label = Label(text="Km" , font=("Arial", 12, "bold"))
text_km_label.grid(row=1, column=2)

convert_button = Button(text="Convert", command=clicked)
convert_button.grid(row=2, column=1)









window.mainloop()