import mysql.connector
import pandas as pd
from tkinter import ttk, messagebox
from tkinter import *
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600+0+0")
        self.root.title("Absent Students List")

        # Frame for Attendance Report Table
        self.frame = Frame(self.root)
        self.frame.pack(fill=BOTH, expand=1)

        # Table to display absent students
        self.AttendanceReportTable = ttk.Treeview(
            self.frame,
            columns=("rollno", "name", "dep", "attendance"),
            show="headings"
        )
        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.heading('rollno', text='Roll No')
        self.AttendanceReportTable.heading('name', text='Name')
        self.AttendanceReportTable.heading('dep', text='Department')
        self.AttendanceReportTable.heading('attendance', text='Attendance')

        # Column configurations
        self.AttendanceReportTable.column('rollno', width=100)
        self.AttendanceReportTable.column('name', width=150)
        self.AttendanceReportTable.column('dep', width=100)
        self.AttendanceReportTable.column('attendance', width=100)

        # Button to export absent students
        export_button = Button(self.root, text="Export Absent List", command=self.export_absent_list)
        export_button.pack(pady=10)

        # Button to send email to absent students
        email_button = Button(self.root, text="Send Email to Absent Students", command=self.send_email_to_absent)
        email_button.pack(pady=10)

        self.find_absent_students()

    def find_absent_students(self):
        try:
            # Connect to MySQL
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="R00tpp123..Abc",
                database="face_recognition",
                auth_plugin="mysql_native_password"
            )
            cursor = conn.cursor()

            # Fetch all students
            cursor.execute("SELECT RollNo, Name, Department, Email FROM student")
            all_students = cursor.fetchall()

            # Load attendance data from CSV
            csv_path = "attendance.csv"  # Path to the CSV file
            attendance_data = pd.read_csv(csv_path, header=None)
            attendance_data.columns = ['rollno', 'name', 'department', 'time', 'date', 'status']

            # Extract RollNos of present students
            present_rollnos = list(map(int, attendance_data["rollno"].tolist()))
            print(present_rollnos)

            # Identify absent students
            self.absent_students = [
                student for student in all_students
                if int(student[0]) not in present_rollnos
            ]
            print(self.absent_students)

            # Populate the AttendanceReportTable with absent students
            for student in self.absent_students:
                rollno, name, department = student[:3]
                self.AttendanceReportTable.insert(
                    "", 
                    END, 
                    values=(rollno, name, department, "Absent")
                )

            conn.close()

        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to database: {e}")
        except FileNotFoundError:
            messagebox.showerror("File Error", "Attendance CSV file not found!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def export_absent_list(self):
        try:
            # Specify the output file path
            output_file = "absent_students.csv"
            # Convert absent students to a DataFrame
            df = pd.DataFrame(self.absent_students, columns=["Roll No", "Name", "Department", "Email"])
            # Save the DataFrame to a CSV file
            df.to_csv(output_file, index=False)
            messagebox.showinfo("Export Success", f"Absent list exported successfully to {output_file}")
        except Exception as e:
            messagebox.showerror("Export Error", f"An error occurred while exporting: {e}")
    
    def send_email_to_absent(self):
        try:
            # Email sender credentials
            sender_email = "2abcabc@gmail.com"  # Replace with your email
            app_password = "xxxx xxxx xxxx xxxx"  # app_passwords not shared due to security reasons.

            # SMTP server configuration
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Set up the email server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, app_password)

            # Send an email to each absent student
            for student in self.absent_students:
                rollno, name, department, email = student
                subject = "Class Attendance Notification"
                body = f"Dear {name},\n\nYou missed today's class.\n\nBest regards,\nClass Administration\n\n\n\nThis is a System Generated Mail. Do not Reply!"

                # Create the email
                msg = MIMEMultipart()
                msg['From'] = sender_email
                msg['To'] = email
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))

                # Send the email
                server.sendmail(sender_email, email, msg.as_string())
                print(f"Email sent to {name} ({email})")

            server.quit()
            messagebox.showinfo("Email Success", "Emails sent successfully to absent students!")

        except smtplib.SMTPAuthenticationError:
            messagebox.showerror("Authentication Error", "Failed to authenticate the email. Please check your username and password.")
        except smtplib.SMTPException as e:
            messagebox.showerror("SMTP Error", f"An error occurred while sending emails: {e}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    app = Attendance(root)
    root.mainloop()
