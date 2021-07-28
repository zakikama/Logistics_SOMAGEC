from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('600x600')

min_w = 50 # Minimum width of the frame
max_w = 200 # Maximum width of the frame
cur_width = min_w # Increasing width of the frame
expanded = False # Check if it is completely exanded

def expand():
    global cur_width, expanded
    cur_width += 10 # Increase the width by 10
    rep = root.after(5,expand) # Repeat this func every 5 ms
    frame.config(width=cur_width) # Change the width to new increase width
    if cur_width >= max_w: # If width is greater than maximum width 
        expanded = True # Frame is expended
        root.after_cancel(rep) # Stop repeating the func
        fill()

def contract():
    global cur_width, expanded
    cur_width -= 10 # Reduce the width by 10 
    rep = root.after(5,contract) # Call this func every 5 ms
    frame.config(width=cur_width) # Change the width to new reduced width
    if cur_width <= min_w: # If it is back to normal width
        expanded = False # Frame is not expanded
        root.after_cancel(rep) # Stop repeating the func
        fill()

def fill():
    if expanded: # If the frame is exanded
        # Show a text, and remove the image
        home_b.config(text='Home',image='',font=(0,21))
        set_b.config(text='Settings',image='',font=(0,21))
        ring_b.config(text='Bell Icon',image='',font=(0,21))
    else:
        # Bring the image back
        home_b.config(image=home,font=(0,21))
        set_b.config(image=settings,font=(0,21))
        ring_b.config(image=ring,font=(0,21))

# Define the icons to be shown and resize it
home = ImageTk.PhotoImage(Image.open('/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/remorque.png').resize((40,40),Image.ANTIALIAS))
settings = ImageTk.PhotoImage(Image.open('/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/remorque.png').resize((40,40),Image.ANTIALIAS))
ring = ImageTk.PhotoImage(Image.open('/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/remorque.png').resize((40,40),Image.ANTIALIAS))

root.update() # For the width to get updated
frame = Frame(root,bg='orange',width=50,height=root.winfo_height())
frame.grid(row=0,column=0) 

# Make the buttons with the icons to be shown
home_b = Button(frame,image=home,bg='orange',relief='flat')
set_b = Button(frame,image=settings,bg='orange',relief='flat')
ring_b = Button(frame,image=ring,bg='orange',relief='flat')

# Put them on the frame
home_b.grid(row=0,column=0,pady=10)
set_b.grid(row=1,column=0,pady=50)
ring_b.grid(row=2,column=0)

# Bind to the frame, if entered or left
frame.bind('<Enter>',lambda e: expand())
frame.bind('<Leave>',lambda e: contract())

# So that it does not depend on the widgets inside the frame
frame.grid_propagate(False)

root.mainloop()