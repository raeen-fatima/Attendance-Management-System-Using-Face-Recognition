from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x700+0+0")
        self.root.title("DEVELOPER")

        # Link Section
        def open_link():
            import webbrowser
            webbrowser.open("https://www.linkedin.com/in/ritesh-ray-682056319") 

        # Header Image
        img = Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\Developerzx.png")
        img = img.resize((1530, 120), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1530, height=120)

        # Background Image
        bg1 = Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\BackgroundDeveloper.jpg")
        bg1 = bg1.resize((1530, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1530, height=768)

        # Developer Frame
        developer_frame = Frame(root, bg="white", bd=2, relief="ridge")
        developer_frame.place(relx=0.5, rely=0.5, anchor="center", width=600, height=300)

        # Photo Label with Image
        try:
            image_path = r"D:\Attendance-Management-System-Using-Face-Recognition\Data\mypic.jpg"
            image = Image.open(image_path)
            image = image.resize((120, 160))
            photo = ImageTk.PhotoImage(image)

            photo_label = Label(developer_frame, image=photo, bg="white")
            photo_label.image = photo  # इमेज को रिफ्रेंस रखना जरूरी है
            photo_label.place(x=0, y=0, width=200, height=200)

            # Photo Button
            developer_button = Button(developer_frame, text="RITESH RAY", font=("Arial", 10, "bold"),
                                       bg="#4CAF50", fg="white", command=open_link)
            developer_button.place(x=40, y=170, width=120, height=20)

        except Exception as e:
            print("Error loading image:", e)
            photo_label = Label(developer_frame, text="Photo Placeholder", bg="white", font=("Arial", 10, "italic"))
            photo_label.place(x=20, y=20, width=120, height=160)

        # Developer Info Frame
        info_frame = Frame(developer_frame, bg="white")
        info_frame.place(x=200, y=20, width=360, height=250)

        Label(info_frame, text="Developer", font=("Arial", 12, "bold"), bg="white").grid(row=0, column=0, sticky="w", pady=5)
        Label(info_frame, text="Name: ", font=("Arial", 10, "bold"), bg="white").grid(row=1, column=0, sticky="w")
        Label(info_frame, text="Ritesh Ray", font=("Arial", 10), bg="white").grid(row=1, column=1, sticky="w")

        Label(info_frame, text="Course: ", font=("Arial", 10, "bold"), bg="white").grid(row=2, column=0, sticky="w")
        Label(info_frame, text="BCA With Cloud & Security", font=("Arial", 10), bg="white").grid(row=2, column=1, sticky="w")

        Label(info_frame, text="Collage: ", font=("Arial", 10, "bold"), bg="white").grid(row=3, column=0, sticky="w")
        Label(info_frame, text="Amity University Noida", font=("Arial", 10), bg="white").grid(row=3, column=1, sticky="w")

        Label(info_frame, text="Phone No: ", font=("Arial", 10, "bold"), bg="white").grid(row=4, column=0, sticky="w")
        Label(info_frame, text="+91 80818 70481", font=("Arial", 10), bg="white").grid(row=4, column=1, sticky="w")

        Label(info_frame, text="Email: ", font=("Arial", 10, "bold"), bg="white").grid(row=5, column=0, sticky="w")
        Label(info_frame, text="riteshray0711@gmail.com", font=("Arial", 10), bg="white").grid(row=5, column=1, sticky="w")

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
