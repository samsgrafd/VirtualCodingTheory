import sys
import os
import subprocess
import fileinput
import tkinter as tk

class Settings(tk.Tk): 
   
        
        
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text="StartProfiler/SetRange", command=self.on_button)
        self.button.pack()
        self.entry.get()

    
    def on_button(self):
        file1 = "bridge.py"
        
        text = "        " + "globalrange =" +  self.entry.get() +"\r\n"
        
        globalrange( self, file1, 46, text)

        clicked(self)
        
    #lbl = Label(window, text="ProfileSearching")
 
    #lbl.grid(column=0, row=0)

    


    #txt = Entry(window,width=12)
    #txt.grid(column=0, row=2)


    



def globalrange(self, file_name, line_num, text):

    self.entry.pack()
    text = "        " + "globalrange =" + self.entry.get() +"\r\n"
    
  

    
    
    file1 = "bridge.py"
    
    line_num = 46
    lines = open(file1, 'r').readlines()
    lines[line_num] = text
    out = open(file1, 'w')
    out.writelines(lines)
    out.close()
    
def clicked(self):
 
    
    os.chdir("\Program_synthesis")
    #os.startfile("startprofiler.bat")
    print("start")
    #os.popen("cmd startprfiler.bat") 
    cmdCommand = "searchprofiler.bat"   #specify your cmd command
    process = subprocess.Popen(cmdCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    print("finished")
    
    #btn = tk.Button(self, text="Start", command=clicked)

 

app = Settings()
app.mainloop()
