from tkinter import*
from PIL import Image,ImageTk
import webbrowser


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x700+0+0")
        self.root.title("HELP AND SUPPORT")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\support-banner2.png")
        img=img.resize((1530,120),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=120)

        # backgorund image 
        bg1=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\help_background-blur.jpg")
        bg1=bg1.resize((1530,768),Image.Resampling.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=768)


        # student button 1
        std_img_btn=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\help_linkedin.png")
        std_img_btn=std_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.linkdin,image=self.std_img1,cursor="hand2")
        std_b1.place(x=250,y=200,width=150,height=150)

        std_b1_1 = Button(bg_img,command=self.linkdin,text="LinkdIn",cursor="hand2",font=("tahoma",15,"bold"),bg="teal",fg="white")
        std_b1_1.place(x=250,y=350,width=150,height=35)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\help_github.png")
        det_img_btn=det_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.github,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=480,y=200,width=150,height=150)

        det_b1_1 = Button(bg_img,command=self.github,text="GitHub",cursor="hand2",font=("tahoma",15,"bold"),bg="teal",fg="white")
        det_b1_1.place(x=480,y=350,width=150,height=35)

         # Attendance System  button 3
        att_img_btn=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\help_instagram.png")
        att_img_btn=att_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.Instagram,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=710,y=200,width=150,height=150)

        att_b1_1 = Button(bg_img,command=self.Instagram,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="teal",fg="white")
        att_b1_1.place(x=710,y=350,width=150,height=35)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\help_gmail.png")
        hlp_img_btn=hlp_img_btn.resize((150,150),Image.Resampling.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=940,y=200,width=150,height=150)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="teal",fg="white")
        hlp_b1_1.place(x=940,y=350,width=150,height=35)


        # create function for button 
    
    
    def linkdin(self):
        self.new = 1
        self.url = "https://www.linkedin.com/in/ritesh-ray-682056319/"
        webbrowser.open(self.url,new=self.new)
    
    def github(self):
        self.new = 1
        self.url = "https://www.github.com/Thatcoderboy01"
        webbrowser.open(self.url,new=self.new)
    
    def Instagram(self):
        self.new = 1
        self.url = "https://www.instagram.com/7befikra"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com/riteshray0711@gmail.com"
        webbrowser.open(self.url,new=self.new)






if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()