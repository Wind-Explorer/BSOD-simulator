from tkinter import *
import os
os.system('taskkill -f -im explorer.exe')
root=Tk()
root.title("bsod")
root.configure(bg="#000083")
screenWidth=root.winfo_screenwidth()
screenHeight=root.winfo_screenheight()
root.attributes('-topmost', True)
screenResolution=("{}x{}".format(screenWidth, screenHeight))
root.geometry(screenResolution)
root.minsize(800, 600)
root.overrideredirect(1)
root.config(cursor="none")
pressed_f4 = False
def do_exit():
    global pressed_f4
    if pressed_f4:
        print('no')
        pressed_f4 = False
    else:
        close()
def alt_f4(event):
    global pressed_f4
    pressed_f4 = True
def close(*event):
    root.destroy()
    os.system("explorer.exe")
    exit()
root.bind('<Alt-F4>', alt_f4)
root.bind('<Control-Up>', close)
root.protocol("WM_DELETE_WINDOW",do_exit)
warnText=Label(root, text="***STOP: 0x000000D1 (0x00000000, 0xF73120AE, 0xC0000008, 0xC0000000)\n\nA problem has been detected and Windows has been shut down to prevent damage to your computer.\n\nDRIVER_IRQL_NOT_LESS_OR_EQUAL\n\nIf this is the first time you’ve seen this Stop error screen, restart your computer.\nIf this screen appears again, follow these steps:\n\nCheck to make sure any new hardware or software is properly installed.\nIf this is a new installation, ask your hardware or software manufacturer for any Windows updates you might need.\n\nIf problems continue, disable or remove any newly installed hardware or software. Disable BIOS\nmemory options such as caching or shadowing.\n\nIf you need to use Safe Mode to remove or disable components, restart your computer,\npress f8 to select Advanced Startup Options, and then select Safe Mode.\n\n*** WXYZ.SYS – Address F73120AE base at C00000000, DateStamp 36b072a3\n\nKernel Debugger Using: COM2 <Port 0x2f8, Baud Rate 19200>\nBeginning dump of physical memory\nPhysical memory dump complete. Contact your system administrator or technical support group.", font=('Consolas Bold', 17), fg="white", bg='#000083', justify=LEFT)
warnText.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()
