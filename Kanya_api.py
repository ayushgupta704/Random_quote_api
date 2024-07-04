from tkinter import *
import requests

def press():
    data=requests.get(url="https://api.kanye.rest/")
    data.raise_for_status()
    data_response=data.json()
    data_response_quote=data_response["quote"]
    canvas.itemconfig(kanya_txt,text=data_response_quote)




windows=Tk()
windows.minsize(width=350,height=600)
windows.title("Kanya Scroll")




canvas=Canvas(width=300,height=440)
background_img=PhotoImage(file="background.png")
canvas.create_image(150,220,image=background_img)
kanya_txt=canvas.create_text(150,250,text="Kanya Quote show here.",width=200,fill="white",font=("cursive",30,"bold"))
canvas.pack()
#button img
kanya_img=PhotoImage(file="kanye.png")
kanye_button=Button(image=kanya_img,highlightthickness=0,command=press)
kanye_button.pack()

windows.mainloop()


















