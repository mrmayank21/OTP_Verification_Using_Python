#import necessary Libraries
from tkinter import *
from tkinter import messagebox
import random
import smtplib

#Code for pushing time limit
def timer():
    global temp_otp,email_var,otp,response
    if temp_otp != otp or response != "ok":
        window.title("OTP Verification------Verification Failed")
        messagebox.showerror("Verification Failed","Time Out----You need to Resend OTP")
        window.title("OTP Verification App")
        otp_var.set("")
        otp = None

#Code for sending the email via gmail
def send_otp():
    global email_var,otp,timer_id
    #generating 6-digit otp
    otp = str(random.randint(100000,1000000))
    send_otp_btn.config(text="Resend OTP")

    #Kindly provide a valid emailid and its password for send email for verification
    sender_email_address = "example@gmail.com"
    sender_email_password = "your password"
    
    
    try:
        message = f"Your OTP for verification is {otp}"
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(sender_email_address,sender_email_password)
        server.sendmail(sender_email_address,email_var.get(),message)
        server.quit()
        window.title("OTP Verification------OTP Sent")
        window.after_cancel(timer_id)
        timer_id = window.after(60000,timer)
    except:
        messagebox.showerror("Sent Failed","Message can't be sent")
        email_var.set("")

#Method to verify through otp
def verify_otp():
    global email_var,otp_var,otp,response,temp_otp
    temp_otp = otp_var.get()
    if otp_var.get()==otp:
        response = messagebox.showinfo("OTP Verification","OTP VERIFIED : Click on 'OK' for Confirmation") 
        window.title("OTP Verification------OTP Verified")
        if response == "ok":
            email_var.set("")
            otp_var.set("")
    else:
        window.title("OTP Verification------OTP Verification")
        messagebox.showerror("OTP Verification","OTP NOT VERIFIED: Resend the otp for verification")
        otp_var.set("")
        otp = None

#Initializing window
window = Tk()
window.title("OTP Verification")
window.geometry("600x500")
window.resizable(False,False)
window.iconbitmap("App-icon.ico")
window.config(bg="lightgray")

#Label for GUI title
Label(window,text="VERIFY YOUR EMAIL USING OTP",font=("timesnewroman",17,"bold","underline"),bg="Black",fg="white",relief=RAISED).place(x=110,y=30)

#frame for all widgets
frame = Frame(window,bg="lavender",height=400,width=500,relief=RAISED,highlightbackground="silver",highlightthickness=5)
frame.place(x=50,y=70)

#Label for email 
Label(frame,text="Enter Your Email ID:-",bg="seashell",fg="black",font=("timesnewroman",12,"bold"),relief=FLAT).place(x=10,y=20)

#Variable for accepting email address of the user
email_var = StringVar()

#Entry for email
Entry(frame,textvariable=email_var,font=("timesnewroman",12),bg="seashell",fg="black",relief=RAISED).place(x=200,y=20)

#timer_id
timer_id  = window.after(60000,quit)

#Label for OTP
Label(frame,text="Enter OTP Received:-",bg="seashell",fg="black",font=("timesnewroman",12,"bold"),relief=FLAT).place(x=10,y=200)

#variable for accepting 6-digit otp number from the user
otp_var = StringVar()

#Entry for otp
Entry(frame,textvariable=otp_var,font=("timesnewroman",12),bg="seashell",fg="black",relief=RAISED,width=18).place(x=200,y=200)

#Variable for storing 6-digit otp
otp = None
#Variable to store the response after verification
response = None
temp_otp = None

#Button for verify OTP
Button(frame,text="Verify OTP",fg="Black",bg="lawngreen",font=("timesnewroman",12,"bold"),relief=RAISED,command=verify_otp).place(x=120,y=270)

#Button to send OTP
send_otp_btn = Button(frame,text="Send OTP",fg="Black",bg="red",font=("timesnewroman",12,"bold"),relief=RAISED,command=send_otp).place(x=120,y=90)

window.mainloop()