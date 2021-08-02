from os import chmod
import sqlite3
import tkinter as tk
import tkinter.ttk as ttk


class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        self.table = ttk.Treeview(self, show="headings")
        self.table.tag_configure('oddrow', background='#B0E7F4')
        self.table.tag_configure('evenrow', background='white')
        
        # self.table.tag_configure('odd', background='#458093',foreground="white")
        self.table["columns"] = headings
        self.table["displaycolumns"] = headings

        for head in headings:
            self.table.heading(head, text=head, anchor=tk.CENTER)
            self.table.column(head, anchor=tk.CENTER)
        a=0
        for row in rows:
            a+=1
            if (a % 2) == 0:
                self.table.insert('', tk.END, values=tuple(row),tags = ('evenrow',))
            else:
                self.table.insert('', tk.END, values=tuple(row),tags = ('oddrow',))

            
           

        scrolltabley = tk.Scrollbar(self, command=self.table.yview)
        scrolltablex = tk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.table.xview)
        self.table.configure(yscrollcommand=scrolltabley.set)
        self.table.configure(xscrollcommand=scrolltablex.set)
        scrolltabley.pack(side=tk.RIGHT, fill=tk.Y)
        scrolltablex.pack(side=tk.BOTTOM, fill=tk.X)
        # self.table.bind("<Double-1>", self.GetSelected)
        self.table.pack(expand=tk.YES, fill=tk.BOTH)

    def GetSelected(self):
        cd=[]
        curItem = self.table.focus()
        print(type(curItem))
        if not curItem :
            print("no item selected")
            return cd
        else:
            Item=self.table.item(curItem)
            cd=Item["values"]
            return cd
        
        

