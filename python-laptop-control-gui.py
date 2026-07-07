import tkinter as tk
import os
def restart():
    os.system("shutdown /r /t 1")
def shutdown():
    os.system("shutdown /s /t 1")
def cancel_shutdown():
    os.system("shutdown /a")
#Create GUI Window
root = tk.Tk()
root.title("Laptop Control ")
root.geometry("700x400")
root.config(bg="Grey")
#Heading
lb=tk.Label(root,text="Laptop Control Panel",font=("Arial", 24,"bold"))
lb.pack(pady=20)
#Shutdown Button
st_button=tk.Button(root,text="Shutdown",command=shutdown,font=("Arial", 20,))
st_button.pack(pady=20)
#Restart Button
rt_button=tk.Button(root,text="Restart",command=restart,font=("Arial", 20))
rt_button.pack(pady=20)
#Cancel Button
c_button=tk.Button(root,text="Cancel Shutdown",command=cancel_shutdown,font=("Arial", 20))
c_button.pack(pady=20)
root.mainloop()