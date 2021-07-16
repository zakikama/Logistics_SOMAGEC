def Formulaire_MRemorque(Remorque):
    root1 = tk.Toplevel(root)
    root1.title("Modifier Remorque")
    image = Image.open(
        '/Users/ikama/Desktop/Logistics_SOMAGEC/DATABASE/Form.png')

    # Reszie the image using resize() method
    resize_image = image.resize((500, 750))

    def triangleClicked(eventorigin):
        global x, y
        x = eventorigin.x
        y = eventorigin.y
        if ((418 <= x <= 427 and 683 <= y <= 716) or (418 <= x <= 452 and 709 <= y <= 716) or (427 <= x <= 452 and 683 <= y <= 709)):
            print("CLICK")
            edit()

    def enter_Tapped(event):
        print("enter")
        edit()

    def edit():

        modifier_Remorque(designationRemorque_entry.get(), typeRemorque_entry.get(
        ), ptcRemorque_entry.get(), ptvRemorque_entry.get(), immatriculationRemorque_entry.get())

        messagebox.showinfo("showinfo", "modification de " +
                            designationRemorque_entry.get()+" Reussis ")

    root1.img = ImageTk.PhotoImage(resize_image)
    global designationRemorque
    global typeRemorque
    global ptcRemorque
    global ptvRemorque
    global immatriculationRemorque

    global designationRemorque_entry
    global typeRemorque_entry
    global immatriculationRemorque_entry
    global ptcRemorque_entry
    global ptvRemorque_entry

    designationRemorque = StringVar()
    typeRemorque = StringVar()
    immatriculationRemorque = StringVar()
    ptcRemorque = StringVar()
    ptvRemorque = StringVar()

    canvas = Canvas(
        root1,
        width=500,
        height=1000,
        bg="#2d5b6b",
        bd=0,
        highlightthickness=0
    )

    canvas.pack(fill='both', expand=True)

    canvas.create_image(
        0,
        0,
        image=root1.img,
        anchor="nw"

    )
    if Remorque != []:
        canvas.create_text(
        80,
        190,
        text='Immatriculation :',
        font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Type:',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            340,
            text='PTC(kg) :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            390,
            text='PTV(kg) :',
            font=('HIND Light', 20),
        )
        immatriculationRemorque_entry = Entry(
            root1, textvariable=immatriculationRemorque)
        immatriculationRemorque_entry.insert(END,Remorque[2])
        immatriculationRemorque_entry.config(highlightbackground='#eeeeee',
                                            foreground="#ff6815", background='#eeeeee')
        immatriculationRemorque_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=immatriculationRemorque_entry,
        )
        designationRemorque_entry = Entry(root1, textvariable=designationRemorque)
        designationRemorque_entry.insert(END,Remorque[1])
        designationRemorque_entry.config(highlightbackground='#eeeeee',
                                        foreground="#ff6815", background='#eeeeee')
        designationRemorque_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationRemorque_entry,
        )
        typeRemorque_entry = Entry(root1, textvariable=typeRemorque)
        typeRemorque_entry.insert(END,Remorque[3])
        typeRemorque_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        typeRemorque_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=typeRemorque_entry,
        )

        ptcRemorque_entry = Entry(root1, textvariable=ptcRemorque)
        ptcRemorque_entry.insert(END,Remorque[4])
        ptcRemorque_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        ptcRemorque_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=ptcRemorque_entry,
        )
        ptvRemorque_entry = Entry(root1, textvariable=ptvRemorque)
        ptvRemorque_entry.insert(END,Remorque[5])
        ptvRemorque_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        ptvRemorque_entry_canvas = canvas.create_window(
            200,
            370,
            anchor="nw",
            window=ptvRemorque_entry,
        )
        
    else:

        canvas.create_text(
        80,
        190,
        text='Immatriculation :',
        font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            240,
            text='Libellé :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            290,
            text='Type:',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            340,
            text='PTC(kg) :',
            font=('HIND Light', 20),
        )
        canvas.create_text(
            80,
            390,
            text='PTV(kg) :',
            font=('HIND Light', 20),
        )
        immatriculationRemorque_entry = Entry(
            root1, textvariable=immatriculationRemorque)
        immatriculationRemorque_entry.config(highlightbackground='#eeeeee',
                                            foreground="#ff6815", background='#eeeeee')
        immatriculationRemorque_entry_canvas = canvas.create_window(
            200,
            170,
            anchor="nw",
            window=immatriculationRemorque_entry,
        )
        designationRemorque_entry = Entry(root1, textvariable=designationRemorque)
        designationRemorque_entry.config(highlightbackground='#eeeeee',
                                        foreground="#ff6815", background='#eeeeee')
        designationRemorque_entry_canvas = canvas.create_window(
            200,
            220,
            anchor="nw",
            window=designationRemorque_entry,
        )
        typeRemorque_entry = Entry(root1, textvariable=typeRemorque)
        typeRemorque_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        typeRemorque_entry_canvas = canvas.create_window(
            200,
            270,
            anchor="nw",
            window=typeRemorque_entry,
        )

        ptcRemorque_entry = Entry(root1, textvariable=ptcRemorque)
        ptcRemorque_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        ptcRemorque_entry_canvas = canvas.create_window(
            200,
            320,
            anchor="nw",
            window=ptcRemorque_entry,
        )
        ptvRemorque_entry = Entry(root1, textvariable=ptvRemorque)
        ptvRemorque_entry.config(highlightbackground='#eeeeee',
                                foreground="#ff6815", background='#eeeeee')
        ptvRemorque_entry_canvas = canvas.create_window(
            200,
            370,
            anchor="nw",
            window=ptvRemorque_entry,
        )
        
    root1.bind("<Button 1>", triangleClicked)
    root1.bind("<Return>", enter_Tapped)
    root1.bind('<KP_Enter>', enter_Tapped)
    root1.resizable(0, 0)
    root1.mainloop()