from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from attendance import Attendance
from absentlist import Attendance


class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.configure(bg='#B0E0E6')
        self.root.title("Face Recognition Attendance System")

        # Title
        title_lbl = Label(self.root, text='Face Recognition Attendance System', font=('Arial', 40, 'bold'),
                          bg='#4682B4', fg='white')
        title_lbl.place(x=0, y=0, width=1530, height=60)

        # Frame for Buttons
        button_frame = Frame(self.root, bg='#4682B4')
        button_frame.place(x=450, y=250, width=630, height=300)

        # Face Recognition Button
        face_btn = Button(button_frame, command=self.face_recog, text="Recognize Face", cursor="hand2",
                          font=('Arial', 20, 'bold'), fg='white', bg='#5F9EA0', activebackground='#20B2AA',
                          activeforeground='white')
        face_btn.place(x=130, y=50, width=400, height=60)

        # Attendance Button
        absent_btn = Button(button_frame, command=self.view_absent, text="Absent List", cursor="hand2",
                                 font=('Arial', 20, 'bold'), fg='white', bg='#5F9EA0', activebackground='#20B2AA',
                                 activeforeground='white')
        absent_btn.place(x=130, y=150, width=400, height=60)



    def view_attend(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def view_absent(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def mark_attendance(self, roll, name, department):
        file_path = "attendance.csv"
        now = datetime.now()
        date_str = now.strftime("%d/%m/%Y")
        time_str = now.strftime("%H:%M:%S")

        # Use a set for efficient duplicate detection
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write("Roll,Name,Department,Time,Date,Status\n")

        with open(file_path, "r+") as f:
            records = f.readlines()
            recorded_entries = {line.split(",")[0].strip() for line in records[1:]}

            if roll not in recorded_entries:
                f.writelines(f"{roll},{name},{department},{time_str},{date_str},Present\n")

    def face_recog(self):
        def draw_boundary(img, classifier, clf, scaleFactor=1.1, minNeighbors=10):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img, scaleFactor, minNeighbors)
            coord = []

            for (x, y, w, h) in features:
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int((100 * (1 - predict / 300)))

                conn = None
                try:
                    conn = mysql.connector.connect(
                        host='localhost',
                        user="root",
                        password='R00tpp123..Abc',
                        database='face_recognition',
                        auth_plugin='mysql_native_password'
                    )
                    cursor = conn.cursor()

                    cursor.execute("SELECT Name, Department, RollNo FROM student WHERE RollNo = %s", (str(id),))
                    result = cursor.fetchone()

                    if result:
                        name, department, rollno = result
                    else:
                        name, department, rollno = "Unknown", "Unknown", "Unknown"

                    if confidence > 77:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        cv2.putText(img, f"Roll: {rollno}", (x, y - 55), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Name: {name}", (x, y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        cv2.putText(img, f"Dept: {department}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                        self.mark_attendance(rollno, name, department)
                    else:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

                    coord.append((x, y, w, h))
                except mysql.connector.Error as e:
                    messagebox.showerror("Database Error", f"Error: {str(e)}")
                finally:
                    if conn:
                        conn.close()
            return coord

        def recognize(img, clf, face_cascade):
            return draw_boundary(img, face_cascade, clf)

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            if not ret:
                print("Error capturing video.")
                break
            recognize(img, clf, face_cascade)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
