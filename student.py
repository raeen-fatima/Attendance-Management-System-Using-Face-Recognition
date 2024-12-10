from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Using geometry for window size
        self.root.title("Face Recognition System")

        # <<<<<<<<<<<<<< Variables >>>>>>>>>>>>>>>>>>>>
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

    # First Image 
        img=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\f1.jpg")
        img=img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        # Second image
        img1=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\f2.webp")
        img1=img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        # Third image 
        img2=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\f3.jpg")
        img2=img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        # Background img
        img5=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\background.jpg")
        img5=img5.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        bg_img=Label(self.root,image=self.photoimg5)
        bg_img.place(x=0,y=130,width=1530,height=710)

         # Add a title label to the Background image
        title_lbl=Label(bg_img, text="STUDENT ATTENDANCE SYSTEM ", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame= Frame(bg_img, bd = 2,bg = "white")
        main_frame.place(x =10, y =55, width= 1505, height= 620)

        # Left side frame
        Left_frame = LabelFrame(main_frame, bd = 2,bg = "white", relief = RIDGE, text = "Student Details", font = ("times roman", 12, "bold"))
        Left_frame.place(x = 10, y = 10, width= 760, height =580)

        img_left=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Left-image.jpg")
        img_left=img_left.resize((745,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=745,height=130)

        # Corrent Course Infomation
        Current_Course_frame = LabelFrame(Left_frame, bd = 2,bg = "white", relief = RIDGE, text = "Current Course Infomation", font = ("times roman", 12, "bold"))
        Current_Course_frame.place(x = 5, y = 135, width= 745, height =115)

        # Department
        dep_lebal = Label(Current_Course_frame, text =" Department", font = ("times roman", 12, "bold",), bg= "white")
        dep_lebal.grid(row=0, column=0, padx= 10)

        dep_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_dep, font = ("times roman", 12, "bold"), state = "readonly",width=20)
        dep_combo["values"] = ("Select Department","Engineering and Technology", "Management and Business Studies", "Biotechnology", "Law", "Psychology and Behavioral Sciences", "Architecture and Planning", "Communication and Journalism", "Fashion and Design", "Fine Arts", "Medical and Allied Health Sciences", "Liberal Arts", "Languages", "Hospitality and Tourism", "Economics", "Environmental Sciences", "Data Science and Artificial Intelligence")
        dep_combo.current(0)
        dep_combo.grid(row=0, column= 1, padx=2, pady= 10)

        # Course
        course_label=Label(Current_Course_frame, text= "Course", font= ("times new roman", 13, "bold",), bg="white")
        course_label.grid(row=0, column=2, padx= 10, sticky=W)

        course_label = ttk.Combobox(Current_Course_frame, textvariable=self.var_course, font = ("times roman", 12, "bold"), state = "readonly",width=20)
        course_label["values"] = ("Select Course", "FE", "SE", "TE", "BE")
        course_label.current(0)
        course_label.grid(row=0, column= 3, padx=2, pady= 10, sticky=W)

        # Year
        year_label=Label(Current_Course_frame, text= "Year", font= ("times new roman", 13, "bold",), bg="white")
        year_label.grid(row=1, column=0, padx= 10, sticky=W)

        year_label = ttk.Combobox(Current_Course_frame, textvariable=self.var_year, font = ("times roman", 12, "bold"), state = "readonly",width=20)
        year_label["values"] = ("Select Year", "2020-21", "2021-22", "2022-23", "2023-24")
        year_label.current(0)
        year_label.grid(row=1, column= 1, padx=2, pady= 10, sticky=W)

        # Samester
        sem_label_label=Label(Current_Course_frame, text= "Semestar", font= ("times new roman", 13, "bold",), bg="white")
        sem_label_label.grid(row=1, column=2, padx= 10, sticky=W)

        sem_label = ttk.Combobox(Current_Course_frame, textvariable=self.var_semester,font = ("times roman", 12, "bold"), state = "readonly",width=20)
        sem_label["values"] = ("Select Semester", "Semester-1", "Semester-2")
        sem_label.current(0)
        sem_label.grid(row=1, column= 3, padx=2, pady= 10, sticky=W)

        # Student Class Infomation
        student_class_frame = LabelFrame(Left_frame, bd = 2,bg = "white", relief = RIDGE, text = "Student Class Infomation", font = ("times roman", 12, "bold"))
        student_class_frame.place(x = 5, y = 250, width= 745, height =300)

        # Student Id
        studentId_label=Label(student_class_frame, text= "Student ID :", font= ("times new roman", 13, "bold",), bg="white")
        studentId_label.grid(row=0, column=0, padx= 10, sticky=W)

        studentId_entry = ttk.Entry(student_class_frame, textvariable=self.var_std_id, width=20, font= ("times new roman", 13, "bold"))
        studentId_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student Name
        studentName_label=Label(student_class_frame, text= "Student Name :", font= ("times new roman", 13, "bold",), bg="white")
        studentName_label.grid(row=0, column=2, padx= 10, sticky=W)

        studentName_entry = ttk.Entry(student_class_frame, textvariable=self.var_std_name, width=20, font= ("times new roman", 13, "bold"))
        studentName_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        #class Division
        classDivision_label=Label(student_class_frame, text= "Class Division :", font= ("times new roman", 13, "bold",), bg="white")
        classDivision_label.grid(row=1, column=0, padx= 10, sticky=W)

        Div_comboBox_label = ttk.Combobox(student_class_frame, textvariable=self.var_div, font = ("times roman", 12), state = "readonly",width=18)
        Div_comboBox_label["values"] = ("Select","A", "B", "C")
        Div_comboBox_label.current(0)
        Div_comboBox_label.grid(row=1, column= 1, padx=7, pady= 5, sticky=W)

        # Roll No.
        rollNo_label=Label(student_class_frame, text= "Roll Number :", font= ("times new roman", 13, "bold",), bg="white")
        rollNo_label.grid(row=1, column=2, padx= 10, sticky=W)

        rollNo_entry = ttk.Entry(student_class_frame, textvariable=self.var_roll, width=20, font= ("times new roman", 13, "bold"))
        rollNo_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label=Label(student_class_frame, text= "Gender :", font= ("times new roman", 13, "bold",), bg="white")
        gender_label.grid(row=2, column=0, padx= 10, sticky=W)

        gender_comboBox_label = ttk.Combobox(student_class_frame, textvariable=self.var_gender, font = ("times roman", 12), state = "readonly",width=18)
        gender_comboBox_label["values"] = ("Select Gender","Male", "Female", "Other")
        gender_comboBox_label.current(0)
        gender_comboBox_label.grid(row=2, column= 1, padx=7, pady= 5, sticky=W)

        # Date of Birth
        DOB_label=Label(student_class_frame, text= "DOB :", font= ("times new roman", 13, "bold",), bg="white")
        DOB_label.grid(row=2, column=2, padx= 10, sticky=W)

        DOB_entry = ttk.Entry(student_class_frame, textvariable=self.var_dob, width=20, font= ("times new roman", 13, "bold"))
        DOB_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        email_label=Label(student_class_frame, text= "E-Mail :", font= ("times new roman", 13, "bold",), bg="white")
        email_label.grid(row=3, column=0, padx= 10, sticky=W)

        email_entry = ttk.Entry(student_class_frame, textvariable=self.var_email, width=20, font= ("times new roman", 13, "bold"))
        email_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone
        phoneNumber_label=Label(student_class_frame, text= "Phone Number :", font= ("times new roman", 13, "bold",), bg="white")
        phoneNumber_label.grid(row=3, column=2, padx= 10, sticky=W)

        phoneNumber_entry = ttk.Entry(student_class_frame, textvariable=self.var_phone, width=20, font= ("times new roman", 13, "bold"))
        phoneNumber_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        # Address
        address_label=Label(student_class_frame, text= "Address :", font= ("times new roman", 13, "bold",), bg="white")
        address_label.grid(row=4, column=0, padx= 10, sticky=W)

        address_entry = ttk.Entry(student_class_frame, textvariable=self.var_address, width=20, font= ("times new roman", 13, "bold"))
        address_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Teacher Name 
        teacherName_label=Label(student_class_frame, text= "Teacher Name :", font= ("times new roman", 13, "bold",), bg="white")
        teacherName_label.grid(row=4, column=2, padx= 10, sticky=W)

        teacherName_entry = ttk.Entry(student_class_frame, textvariable=self.var_teacher, width=20, font= ("times new roman", 13, "bold"))
        teacherName_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        #Radio Buttons 
        self.var_radio1=StringVar()
        radioButtons1= ttk.Radiobutton(student_class_frame,variable=self.var_radio1, text="Take Photo Sample", value="Yes")
        radioButtons1.grid(row=6, column=0)

        radioButtons2= ttk.Radiobutton(student_class_frame,variable=self.var_radio1, text="No Photo Sample", value="No")
        radioButtons2.grid(row=6, column=1)

        # Buttons Frame
        btn_frame= Frame(student_class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x = 10, y=200, width=715, height=35)

        save_btn = Button(btn_frame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_btn.grid(row=0, column=1)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=0, column=2)

        delete_btn = Button(btn_frame, text="Delete",  command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        delete_btn.grid(row=0, column=3)

        # take photo grid
        btn_frame1= Frame(student_class_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x = 10, y=235, width=715, height=35)

        take_photo_btn = Button(btn_frame1, text="Take Photo", command=self.generate_dataset, width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0, column=2)

        update_photo_btn = Button(btn_frame1, text="Update Photo", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0, column=3)


         # Right side frame
        Right_frame = LabelFrame(main_frame, bd = 2,bg = "white", relief = RIDGE, text = "Student Details", font = ("times roman", 12, "bold"))
        Right_frame.place(x = 780, y = 10, width= 690, height =580)

        right=Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\right image.jpg")
        right=right.resize((677,130),Image.Resampling.LANCZOS)
        self.right=ImageTk.PhotoImage(right)

        f_lbl=Label(Right_frame,image=self.right)
        f_lbl.place(x=5,y=0,width=677,height=130)

        # <<<<<<<<<<<<< Search System >>>>>>>>>>>>>>>>>>>>>
        search_system_frame = LabelFrame(Right_frame, bd = 2,bg = "white", relief = RIDGE, text = "Search By Information", font = ("times roman", 12, "bold"))
        search_system_frame.place(x = 5, y = 135, width= 677, height =70)

        search_label=Label(search_system_frame, text= "Search By", font= ("times new roman", 13, "bold",), bg="white")
        search_label.grid(row=0, column=0, padx= 10, sticky=W)

        search_combo = ttk.Combobox(search_system_frame, font = ("times roman", 10, "bold"), state = "readonly",width=15)
        search_combo["values"] = ("Select ", "Student_Id", "Phone_Number","Roll_Number")
        search_combo.current(0)
        search_combo.grid(row=0, column= 1, padx=2, pady= 10, sticky=W)

        search_entry = ttk.Entry(search_system_frame, width=15, font= ("times new roman", 13, "bold"))
        search_entry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        search_btn = Button(search_system_frame, text="Search", width=14, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0, column=3, padx=4)

        showAll_btn = Button(search_system_frame, text="Show All", width=14, font=("times new roman", 10, "bold"), bg="blue", fg="white")
        showAll_btn.grid( row=0, column=4, padx=4)

        # <<<<<<<<<<<<<<<< Table Frame >>>>>>>>>>>>>>>>>
        table_frame =Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=677, height=350)

        scroll_x =ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll","gender", "dob","email", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student_Id")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll_Number")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhoneSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


 # <<<<<<<<<<<<<<<<<<Function for Decration>>>>>>>>>>>>>>>>>>>>
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error", "All Fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host ="localhost", username="root", password="Ritesh@Database02", database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute(
    "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (
        self.var_dep.get(),
        self.var_course.get(),
        self.var_year.get(),
        self.var_semester.get(),
        self.var_std_id.get(),
        self.var_std_name.get(),
        self.var_div.get(),
        self.var_roll.get(),
        self.var_gender.get(),
        self.var_dob.get(),
        self.var_email.get(),
        self.var_phone.get(),
        self.var_address.get(),
        self.var_teacher.get(),
        self.var_radio1.get()
    )
)

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success", "Student details has been added Successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f" Due to :{str(es)}",parent=self.root)

    # <<<<<<<<<<<< Fetch Data >>>>>>>>>>>>>>>>>
    def fetch_data(self):
        conn = mysql.connector.connect(host ="localhost", username="root", password="Ritesh@Database02", database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()

    # <<<<<<<<<<<<< Get cursor >>>>>>>>>>>>>>>
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
        
    # <<<<<<<<<<<Update Function>>>>>>>>>>>>
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update?", parent=self.root)
                if update:
                    conn = mysql.connector.connect(host="localhost", username="root", password="Ritesh@Database02", database="face_recognizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute(
                        """UPDATE student SET Name=%s, Dep=%s, Course=%s, Year=%s, Semester=%s, Division=%s, Roll=%s, Gender=%s, 
                        Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s WHERE Student_id=%s""",
                        (
                            self.var_std_name.get(),
                            self.var_dep.get(),
                            self.var_course.get(),
                            self.var_year.get(),
                            self.var_semester.get(),
                            self.var_div.get(),
                            self.var_roll.get(),
                            self.var_gender.get(),
                            self.var_dob.get(),
                            self.var_email.get(),
                            self.var_phone.get(),
                            self.var_address.get(),
                            self.var_teacher.get(),
                            self.var_radio1.get(),
                            self.var_std_id.get()
                        )
                    )
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
                else:
                    if not update:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    # Delete Function

    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error", "Student id must be required", parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page", "Do you want to delete this?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host ="localhost", username="root", password="Ritesh@Database02", database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where student_id=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f" Due to :{str(es)}",parent=self.root)

    # delete function

    def reset_data(self):
            self.var_dep.set("Select Department"),
            self.var_course.set("Select Course"),
            self.var_year.set("Select Year"),
            self.var_semester.set("Select Semester"),
            self.var_std_id.set(""),
            self.var_std_name.set(""),
            self.var_div.set("Select Division"),
            self.var_roll.set(""),
            self.var_gender.set("Select Gender"),
            self.var_dob.set(""),
            self.var_email.set(""),
            self.var_phone.set(""),
            self.var_address.set(""),
            self.var_teacher.set(""),
            self.var_radio1.set("")

    
    # <<<<<<<<<<<<<<<<<<Generate Data set take photo sample>>>>>>>>>>>>>>>>>>>>>>>
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester" or self.var_std_id.get()=="" or self.var_std_name.get()=="" or self.var_div.get()=="" or self.var_roll.get()=="" or self.var_gender.get()=="" or self.var_dob.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_address.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                
                conn = mysql.connector.connect(user='root', password='Ritesh@Database02',host='localhost',database='face_recognizer',port=3306)
                mycursor = conn.cursor()
                mycursor.execute("select * from student")
                myreslut = mycursor.fetchall()
                id=0
                for x in myreslut:
                    id+=1

                mycursor.execute("update student set Dep=%s, Course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s,Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s,PhotoSample=%s WHERE Student_id=%s",( 
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()==id+1   
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # <<<<<<<<<<<<< Load Predefind data on frontals from opencv>>>>>>>>>>>>>>>>
                
                # face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                face_classifier = cv2.CascadeClassifier(r"D:\Attendance-Management-System-Using-Face-Recognition\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #Scaling Factor = 1.3
                    #Minimum Neigver=5

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame), (450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path=r"D:\Attendance-Management-System-Using-Face-Recognition\imgData/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Capture Picture", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!")

            except Exception as es:
                messagebox.showerror("Error", f" Due to :{str(es)}",parent=self.root)

                    

     

if __name__ == "__main__":
        root = Tk() 
        obj = Student(root)
        root.mainloop()