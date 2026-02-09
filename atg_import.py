from tkinter import *
from tkinter import filedialog
import tkSimpleDialog

class ATG_Import(tkSimpleDialog.Dialog):

    def body(self, master):

        self.option = StringVar(master)
        self.option.set("All")
        self.menu = OptionMenu(master, self.option, "Address", "Data", "Mask", "Control", "All", command=self.option_changed)
        self.menu.grid(row=0, sticky=E)

        self.file = StringVar(master)
        self.fileentry = Entry(master, textvariable=self.file)
        self.fileentry.grid(row=0, column=1)

        self.browse = Button(master, text='Browse...', command=self.browse_cb)
        self.browse.grid(row=0, column=2, padx=20)

        Label(master, text="(For 'All': select folder or leave blank for current/coe folder)", font=('Arial', 8)).grid(row=1, column=0, columnspan=3, pady=5)

        return self.menu

    def option_changed(self, value):
        """Update UI when option changes"""
        if value == "All":
            self.file.set("")    # Clear file path for "All" option

    def browse_cb(self):
        if self.option.get() == "All":
            # For "All" option, allow selecting a directory
            foldername = filedialog.askdirectory(title="Select folder containing .coe files (or cancel for default)")
            if foldername:
                self.file.set(foldername)
            else:
                self.file.set("")    # Empty means use default locations
        else:
            filename = filedialog.askopenfilename(defaultextension='.coe')
            self.file.set(filename)

    def apply(self):
        self.result = {'column': self.option.get().lower(), 'filename': self.file.get()}

if __name__ == '__main__':
    root = Tk()
    ATG_Import(root, 'File import')
    root.mainloop()

