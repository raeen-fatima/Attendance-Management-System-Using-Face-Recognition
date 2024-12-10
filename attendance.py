from sys import path
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime
import csv
from tkinter import filedialog


#Global variable for importCsv Function 

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0") 
        self.root.title("Attendance Record")


         #-----------Variables-------------------
        self.var_id=StringVar()
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_time=StringVar()
        self.var_date=StringVar()
        self.var_attendance=StringVar()

         
        # This part is image labels setting start 
        # first header image  
        img=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\FACE1.jpg")
        img=img.resize((1530,710),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=800,height=200)

        img1=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\FACE1.jpg")
        img1=img1.resize((1530,710),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg1)
        f_lb1.place(x=800,y=0,width=800,height=200)

        # backgorund image 
        bg1=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Left-image.jpg")
        bg1=bg1.resize((1530,710),Image.ADAPTIVE)
        self.photobg1=ImageTk.PhotoImage(bg1)  

         # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=200,width=1530,height=710)


        #title section
        title_lb1 = Label(bg_img,text="ATTENDANCE DETAILS",font=("verdana",20,"bold"),bg="navyblue",fg="white")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        #========================Section Creating==================================

        # Creating Frame 
        main_frame = Frame(bg_img,bd=2,bg="white") #bd mean border 
        main_frame.place(x=20,y=55,width=1480,height=600)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("verdana",12,"bold"),fg="navyblue")
        left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Left-image.jpg")
        img_left=img_left.resize((700,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=10,y=10,width=700,height=130)

        left_inside_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=10,y= 140,width= 700,height=400)
        
        # ==================================Text boxes and Combo Boxes====================

        #Student id
        attendanceID_label = Label(left_inside_frame,text="AttendenceID :" ,font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendanceID_label.grid(row=0,column=0,padx=5,pady=5,sticky=W)

        attendanceID_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_id, font=("verdana",12,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=5,pady=5,sticky=W)

        #Student Roll
        student_roll_label = Label(left_inside_frame,text="Roll Number :",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_roll_label.grid(row=0,column=2,padx=5,pady=5,sticky=W)

        student_roll_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_roll, font=("verdana",12,"bold"))
        student_roll_entry.grid(row=0,column=3,padx=5,pady=5,sticky=W)

        #Student Name
        student_name_label = Label(left_inside_frame,text="Name :",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_name_label.grid(row=1,column=0,padx=5,pady=5,sticky=W)

        student_name_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_name, font=("verdana",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=5,pady=5,sticky=W)

        #Student Deparment
        student_dep_label = Label(left_inside_frame,text="Department :",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        student_dep_label.grid(row=1,column=2,padx=5,pady=5,sticky=W)

        student_dep_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_dep, font=("verdana",12,"bold"))
        student_dep_entry.grid(row=1,column=3,padx=5,pady=5,sticky=W)

        # Time
        time_label = Label(left_inside_frame,text="Time :",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        time_label.grid(row=2,column=0,padx=5,pady=5,sticky=W)

        time_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_time, font=("verdana",12,"bold"))
        time_entry.grid(row=2,column=1,padx=5,pady=5,sticky=W)

        # Date
        date_label = Label(left_inside_frame,text="Date :",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        date_label.grid(row=2,column=2,padx=5,pady=5,sticky=W)

        date_entry = ttk.Entry(left_inside_frame, width=15, textvariable=self.var_date, font=("verdana",12,"bold"))
        date_entry.grid(row=2,column=3,padx=5,pady=5,sticky=W)

        # Attendance Status
        attendance_status_label = Label(left_inside_frame,text="Attendance Status :",font=("verdana",12,"bold"),fg="navyblue",bg="white")
        attendance_status_label.grid(row=3,column=0,padx=5,pady=5,sticky=W)

        attendance_combo=ttk.Combobox(left_inside_frame, width=13, textvariable=self.var_attendance,font=("verdana",12),state="readonly")
        attendance_combo["values"]=("Select", "Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column=1,padx=5,pady=5,sticky=W)

        #     # =========================button section========================

        #Button Frame
        btn_frame = Frame(left_inside_frame,bg="white",relief=RIDGE)
        btn_frame.place(x=30,y=300,width=650,height=40)

        #Improt button
        save_btn=Button(btn_frame,text="Import CSV", command=self.importCsv, width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        save_btn.grid(row=0,column=0,padx=6,pady=10,sticky=W)

        #Exprot button
        update_btn=Button(btn_frame,text="Export CSV", command=self.exportCsv,width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        update_btn.grid(row=0,column=1,padx=6,pady=8,sticky=W)

        #Update button                    ###*****command=self.action add hoga
        del_btn=Button(btn_frame,text="Update",width=12,font=("verdana",12,"bold"),fg="white",bg="navyblue")
        del_btn.grid(row=0,column=2,padx=6,pady=10,sticky=W)

        #reset button
        reset_btn=Button(btn_frame,text="Reset",width=12, command=self.reset_data, font=("verdana",12,"bold"),fg="white",bg="navyblue")
        reset_btn.grid(row=0,column=3,padx=6,pady=10,sticky=W)

        # Right side frame
        Right_frame = LabelFrame(main_frame, bd = 2,bg = "white", relief = RIDGE, text = "Attendance Details", font = ("times roman", 12, "bold"))
        Right_frame.place(x = 760, y = 10, width= 705, height =580)

        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=10,y=5,width=680,height=490)

         #scroll bar 
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

    #    #create table 
        self.attendanceReport = ttk.Treeview(table_frame,column=("ID","Roll_No", "Name","Time","Date","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendanceReport.xview)
        scroll_y.config(command=self.attendanceReport.yview)

        self.attendanceReport.heading("ID",text="ID")
        self.attendanceReport.heading("Roll_No",text="Roll")
        self.attendanceReport.heading("Name",text="Name")
        self.attendanceReport.heading("Time",text="Time")
        self.attendanceReport.heading("Date",text="Date")
        self.attendanceReport.heading("Attendance",text="Attendance")
        self.attendanceReport["show"]="headings"


        # Set Width of Colums 
        self.attendanceReport.column("ID",width=30)
        self.attendanceReport.column("Roll_No",width=70)
        self.attendanceReport.column("Name",width=100)
        self.attendanceReport.column("Time",width=75)
        self.attendanceReport.column("Date",width=80)
        self.attendanceReport.column("Attendance",width=120)
        
        self.attendanceReport.pack(fill=BOTH,expand=1)
        self.attendanceReport.bind("<ButtonRelease>",self.get_cursor_left)



        # # # =========================Fetch Data Import data ===============

    def fetchData(self,rows):
        
        self.attendanceReport.delete(*self.attendanceReport.get_children())
        for i in rows:
            self.attendanceReport.insert("",END,values=i)
            print(i)
        
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
        self.fetchData(mydata)

        # # #==================Experot CSV=============
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Successfuly","Your data is exported!")
        except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root)    

         # # #=============Cursur Function for CSV========================

    def get_cursor_left(self,event=""):
        cursor_focus = self.attendanceReport.focus()
        content = self.attendanceReport.item(cursor_focus)
        data = content["values"]

        self.var_id.set(data[0]),
        self.var_roll.set(data[1]),
        self.var_name.set(data[2]),
        self.var_time.set(data[3]),
        self.var_date.set(data[4]),
        self.var_attendance.set(data[5])
        self.var_dep.set(data[6]),

# # #============================Reset Data======================
    def reset_data(self):
        self.var_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance.set("Status")



      

if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()