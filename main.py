from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
from train import Train
from face_recognition import FaceRecognition
from attendance import Attendance
from devdetails import Developers
import os


class Face_recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")  # Full screen dimensions
        root.configure(bg='#F4F4F9')  # Neutral, light background for professionalism
        self.root.title("Face Recognition System")

        # Header Section
        title_lbl = Label(
            self.root,
            text='Face Recognition Attendance System',
            font=('Arial', 40, 'bold'),
            fg='#0F4C75',
            bg='#F4F4F9',
            anchor="w",
            padx=20
        )
        title_lbl.place(x=0, y=0, width=1530, height=80)

        # Top Borderline
        LineFrame = Frame(self.root, bg='#0F4C75', height=2)
        LineFrame.place(x=0, y=80, width=1530)

        # Top Images Section
        self.add_top_images()

        # Navigation Panel
        self.add_buttons()

    def add_top_images(self):
        # Display a modern image gallery on top
        image_paths = [
            r"Face recognition\Image 1.png",
            r"Face recognition\Image 2.jpg",
            r"Face recognition\image_3.png"
        ]
        x_positions = [10, 520, 1030]
        for i, path in enumerate(image_paths):
            img = Image.open(path).resize((490, 200), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            label = Label(self.root, image=photo_img, bg='#F4F4F9')
            label.image = photo_img  # Store reference to prevent garbage collection
            label.place(x=x_positions[i], y=90, width=490, height=200)

    def add_buttons(self):
        # Button Layout
        sections = [
            {"text": "Add Student Details", "image": r"Face recognition\add_student.png", "command": self.student_details},
            {"text": "Take Attendance", "image": r"Face recognition\attend.webp", "command": self.face_recognize},
            {"text": "Attendance List", "image": r"Face recognition\Attendance_2 (1).jpg", "command": self.attendance_list},
            {"text": "Train Data", "image": r"Face recognition\images.jpg", "command": self.train_photos},
            {"text": "Photos Database", "image": r"Face recognition\images (1).jpg", "command": self.open_img},
            {"text": "Developer Details", "image": r"Face recognition\developer.jpg", "command": self.dev_details},
        ]
        x_positions = [100, 600, 1100]
        y_positions = [320, 520]

        # Distribute Buttons in Rows
        for i, section in enumerate(sections):
            img = Image.open(section["image"]).resize((300, 100), Image.Resampling.LANCZOS)
            photo_img = ImageTk.PhotoImage(img)
            label = Label(self.root, image=photo_img, bg='#F4F4F9')
            label.image = photo_img  # Store reference
            label.place(x=x_positions[i % 3], y=y_positions[i // 3], width=300, height=100)

            button = Button(
                self.root,
                text=section["text"],
                command=section["command"],
                font=('Arial', 14, 'bold'),
                fg='white',
                bg='#0F4C75',
                cursor="hand2",
                relief=RAISED
            )
            button.place(x=x_positions[i % 3], y=y_positions[i // 3] + 110, width=300, height=40)

    def open_img(self):
        os.startfile(r"data")

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_photos(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_recognize(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)

    def attendance_list(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)
    def dev_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Developers(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_recognition_System(root)
    root.mainloop()