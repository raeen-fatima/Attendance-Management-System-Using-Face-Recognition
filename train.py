from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.config(bg="#f4f4f4")

        # Title Label
        title_lbl = Label(self.root, text="TRAIN DATA SET", font=("Arial", 35, "bold"), bg="#4CAF50", fg="white", anchor="w", padx=20)
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # Create a Frame for images and buttons to keep everything organized
        frame = Frame(self.root, bg="#f4f4f4")
        frame.place(x=0, y=60, width=1530, height=600)

        # Top Image Section
        img_top = Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\FACE2.png")
        img_top = img_top.resize((1530, 325), Image.ADAPTIVE)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_top = Label(frame, image=self.photoimg_top)
        f_lbl_top.grid(row=0, column=0, padx=20, pady=20)

        # Bottom Image Section
        img_bottom = Image.open(r"D:\Attendance-Management-System-Using-Face-Recognition\Data\FACE3.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ADAPTIVE)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl_bottom = Label(frame, image=self.photoimg_bottom)
        f_lbl_bottom.grid(row=1, column=0, padx=20, pady=20)

        # Button Section
        button_frame = Frame(self.root, bg="#4CAF50")
        button_frame.place(x=0, y=440, width=1530, height=100)

        b1_1 = Button(button_frame, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("Arial", 25, "bold"), bg="#FF5722", fg="white", relief=RAISED, bd=3, padx=20)
        b1_1.place(x=600, y=20, width=300, height=60)
        b1_1.bind("<Enter>", lambda e: b1_1.config(bg="#FF7043"))  # Hover effect
        b1_1.bind("<Leave>", lambda e: b1_1.config(bg="#FF5722"))

        # Progress Bar
        self.progress = ttk.Progressbar(button_frame, length=300, mode="indeterminate")
        self.progress.place(x=600, y=80)

        # Status Bar (optional)
        self.status_bar = Label(self.root, text="Ready", bd=1, relief=SUNKEN, anchor=W, font=("Arial", 10))
        self.status_bar.place(x=0, y=740, relwidth=1, height=20)

    def update_status(self, message):
        self.status_bar.config(text=message)
        self.root.update_idletasks()

    def train_classifier(self):
        self.update_status("Training started... Please wait.")

        data_dir = r"D:\Attendance-Management-System-Using-Face-Recognition\imgData"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        # Start the progress bar
        self.progress.start()

        for image in path:
            img = Image.open(image).convert('L')  # Convert image to grayscale
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)  # Optional: Display the image for training
            cv2.waitKey(1)  # Just wait a bit

        ids = np.array(ids)

        # Train Classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write(r"D:\Attendance-Management-System-Using-Face-Recognition\classifier.xml")
        cv2.destroyAllWindows()

        # Stop the progress bar
        self.progress.stop()

        # Update status and show completion message
        self.update_status("Training completed successfully.")
        messagebox.showinfo("Result", "Training dataset completed!!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
