import os
from tkinter import *
import subprocess
import time
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def setap():
    command = '[Environment]::SetEnvironmentVariable("Path", $env:Path + ";'+__location__+'", "Machine")'"
    print(command)
    f= open("usr.config","w+")
    f.close() 
    abcd = '%SYSTEMROOT%\System32\WindowsPowerShell\\v1.0\powershell.exe -Command '+command
    print(abcd)
    process = subprocess.Popen(abcd, shell = True,stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            line = str(output.strip().decode('ansi'))
            print(line)
    time.sleep(1)
    frm.destroy()
    nms.grid(row =2,column = 2)



rt = Tk()
rt.geometry('400x180')
rt.resizable(False, False)
rt.title('Setup')
frm = Frame(rt)
frm.grid(row = 3, column =2)
tp = Label(rt, text = "                                            ").grid(row =0,column =0)
bs = Label(rt, text = "                                            ").grid(row =0,column =2)
msg = Message(rt, text = "      Made by      \nSanjib Kumar Sen\n   Dept of CSE, BRAC University").grid(row =1,column =1, columnspan =3)
mid = Button(frm, text = "Intsall", command =setap).grid(row =3, column =2)
fs = Label(rt, text = "                                            ").grid(row =2,column =2)
nms = Label(rt, text = "Installation Complete")

rt.mainloop()
