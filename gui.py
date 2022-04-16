import tkinter as tk  
from tkinter import ttk

class HandleGui:
    
    def __init__(self):
        self.win = tk.Tk()  
        

    def takeTextUserInput(self):
        self.win.title("Enter OTP")# Label  
        
        otpCode = None
        def setOtp():
            otpCode = otp.get()
        
        lbl = ttk.Label(self.win, text = "Enter OTP:").grid(column = 0, row = 0)# Click event  
        otp = tk.StringVar()  
        nameEntered = ttk.Entry(self.win, width = 12, textvariable = otp).grid(column = 0, row = 2)# Button widget  
        button = ttk.Button(self.win, text = "submit", command = setOtp).grid(column = 0, row = 4)  
        self.win.mainloop()   
        return otpCode

if __name__ == "__main__":
    print(HandleGui().takeTextUserInput())