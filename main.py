from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from help import Helpsupport
from attendance import Attendance
from Developer import Developer


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Background image  
        img_bg = Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\background blur.jpg")
        img_bg = img_bg.resize((1530, 790), Image.Resampling.LANCZOS)
        self.photo_bg = ImageTk.PhotoImage(img_bg)

        bg_label = Label(self.root, image=self.photo_bg)
        bg_label.place(x=0, y=0, width=1530, height=790)

        # Title Label
        title_lbl = Label(
            bg_label,
            text="FACE RECOGNITION ATTENDANCE SYSTEM",
            font=("Segoe UI", 30, "bold"),
            bg="#002147",  # Dark Blue Background
            fg="white",
            pady=10,
        )
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # Create a frame for the buttons
        main_frame = Frame(bg_label, bd=2, bg="white", relief=RIDGE)
        main_frame.place(x=100, y=100, width=1300, height=600)

        # Button configuration
        def create_button(image_path, text, x, y, command=None):
            img = Image.open(image_path)
            img = img.resize((150, 150), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            btn_img = Button(
                main_frame,
                image=photo,
                command=command,
                cursor="hand2",
                bg="white",
                bd=0,
                activebackground="white",
            )
            btn_img.image = photo
            btn_img.place(x=x, y=y, width=150, height=150)

            btn_txt = Button(
                main_frame,
                text=text,
                command=command,
                font=("Segoe UI", 12, "bold"),
                bg="#002147",
                fg="white",
                cursor="hand2",
                bd=0,
                activebackground="#003366",
                activeforeground="white",
            )
            btn_txt.place(x=x, y=y + 160, width=150, height=40)

        # Adding buttons
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Student details.jpg", "Student Details", 50, 50, command=self.student_deatils)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\face Detector.png", "Face Detector", 250, 50, command=self.face_data)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Attendace.jpg", "Attendance", 450, 50, command=self.attendance_data)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\help.png", "Help", 650, 50, command=self.help_data)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Train Data.png", "Train Data", 850, 50, command=self.train_data)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Photos.jpg", "Photos", 1050, 50, command=self.open_img)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Developer.jpg", "Developer", 50, 280, command=self.developer_data)
        create_button(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Exit.jpg", "Exit", 250, 280, command=self.root.destroy)

    def open_img(self):
        os.startfile(r"D:\Attendance-Management-System-Using-Face-Recognition\imgData")


        # <<<<<<<<<<<<<<<<<<<<<< Function Button >>>>>>>>>>>>>>>
    def student_deatils(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)
    
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
