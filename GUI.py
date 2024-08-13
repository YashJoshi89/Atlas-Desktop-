from tkinter import *
from PIL import Image, ImageTk
import speech_to_text
import action
import weather




# Create the main window
root = Tk()
root.title("Yash")
root.geometry("550x675")
root.resizable(False, False)
root.config(background="Olive")
#ask function implementation


def ask():
    user_val= speech_to_text.speech_to_text()
    bot_val= action.Action(user_val)
    text.insert(END,'USER---->'+user_val+"\n")
    if bot_val != None:
        text.insert(END,"BOT <---"+str(bot_val)+"\n")
    if bot_val == "ok sir":
        root.destroy()

def send():
    send = entry.get()
    bot =action.Action(send)
    text.insert(END,'USER---->'+send+"\n")
    if bot != None:
        text.insert(END,"BOT <---"+str(bot)+"\n")
    if bot == "ok sir":
        root.destroy()


def del_text():
    text.delete('1.0',"end")


# Create a frame
frame = LabelFrame(root, padx=100, borderwidth=3, relief="raised", background="Olive")
frame.grid(row=0, column=1, padx=55, pady=10)

# Add a text label to the frame
text_label = Label(frame, text="AI Assistant", background="yellow")
text_label.grid(row=0, column=0, padx=20, pady=10)

# Open and resize the image
image_path = "Image/yash.png"  # Ensure this path is correct
try:
    image = Image.open(image_path)
    image = image.resize((200, 200))  # Resize as needed
    image1 = ImageTk.PhotoImage(image)
except Exception as e:
    print(f"Error loading image: {e}")

# Add the image label to the frame
image_label = Label(frame, image=image1)
image_label.grid(row=1, column=0, pady=20)

#adding textwidget
text =Text(root,font=('courier 10 bold'),bg ="yellow")
text.grid(row =2,column=0)
text.place(x=70,y=375,width=375,height = 100)

#entry widget
entry = Entry(root, justify= CENTER)
entry.place(x=70,y=500,width=375,height=30)

#button1
Button1 = Button(root,text="ASK",bg="yellow",pady= 10,padx = 35,borderwidth= 3,relief=SOLID,command=ask)
Button1.place(x=70,y=570)

#button2
Button2 = Button(root,text="DELETE",bg="yellow",pady= 10,padx = 35,borderwidth= 3,relief=SOLID,command=del_text)
Button2.place(x=225,y=570)

#button3
Button3 = Button(root,text="SEND",bg="yellow",pady= 10,padx = 35,borderwidth= 3,relief=SOLID,command=send)
Button3.place(x=400,y=570)


# Run the Tkinter main loop
root.mainloop()
