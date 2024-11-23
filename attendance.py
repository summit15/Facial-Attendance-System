from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]


class Attendance:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #(1530 is width , 790 is height, +0 +0 is x axis and yaxis starting from top left corner )
        root.configure(bg='#B0E0E6')
        self.root.title("Face Recognition System")



        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_dep=StringVar()
        self.var_date=StringVar()
        self.var_time=StringVar()
        self.var_attend=StringVar()

    

    #first image
        img = Image.open(r"Face recognition\Image 1.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img=img.resize((490,200))  # ANTIALIAS converts high level image into low levels
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=10,y=0,width=490,height=180)

        #second image
        img1 = Image.open(r"Face recognition\Image 2.jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img1=img1.resize((490,200))  # ANTIALIAS converts high level image into low levels
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=520,y=0,width=490,height=180)

        #third image
        img2 = Image.open(r"Face recognition\image_3.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img2=img2.resize((500,200))  # ANTIALIAS converts high level image into low levels
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=1030,y=0,width=490,height=180)

        #title name
        title_lbl = Label(self.root, text='Student Attendance List',font=('times new roman',35,'bold'),fg='green')
        title_lbl.place(x=10,y=190,width=1510, height= 55)

        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=10,y=250,width=1510,height=620)

        #left label frame 
        left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=725,height=530)

        attendance_update_frame=LabelFrame(left_frame,bd=3,relief=RIDGE,text="Update Attendance",font=("times new roman",12,"bold"))
        attendance_update_frame.place(x=5,y=0,width=700,height=500)

        #Roll Number
        rollnumber_label = Label(attendance_update_frame,text="Roll No",font=("times new roman",12,"bold"),bg='white',bd=1)
        rollnumber_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        rollnumber_entry=ttk.Entry(attendance_update_frame,textvariable=self.var_rollno,width=20,font=("times new roman",12,"bold"))
        rollnumber_entry.grid(row=0,column=1,padx=10,sticky=W)


        #Student Name
        student_name_label = Label(attendance_update_frame,text="Name",font=("times new roman",12,"bold"),bg='white',bd=1)
        student_name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        student_name_entry=ttk.Entry(attendance_update_frame,textvariable=self.var_name,width=30,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,sticky=W)

        dep_label = Label(attendance_update_frame,text="Department",font=("times new roman",12,"bold"),bg='white',bd=1)
        dep_label.grid(row=1,column=2,padx=10,sticky=W)

        dep_combo=ttk.Combobox(attendance_update_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=1,column = 3,padx=2,pady=10,sticky=W)

        #Date Time label
        date_label = Label(attendance_update_frame,text="Date",font=("times new roman",12,"bold"),bg='white',bd=1)
        date_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        date_entry=ttk.Entry(attendance_update_frame,textvariable=self.var_date,width=30,font=("times new roman",12,"bold"))
        date_entry.grid(row=2,column=1,padx=10,sticky=W)


        time_label = Label(attendance_update_frame,text="Time",font=("times new roman",12,"bold"),bg='white',bd=1)
        time_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        time_entry=ttk.Entry(attendance_update_frame,textvariable=self.var_time,width=20,font=("times new roman",12,"bold"))
        time_entry.grid(row=2,column=3,padx=0,sticky=W)

        #Attendance Label
        attendance_label = Label(attendance_update_frame,text="Attendance",font=("times new roman",12,"bold"),bg='white',bd=1)
        attendance_label.grid(row=3,column=0,padx=10,sticky=W)

        attendance_combo=ttk.Combobox(attendance_update_frame,textvariable=self.var_attend,font=("times new roman",12,"bold"),width=17,state="readonly")
        attendance_combo["values"]=("Select Attendance","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.grid(row=3,column = 1,padx=2,pady=10,sticky=W)

        #button frame
        btn_frame = Frame(attendance_update_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=400,width = 680,height = 30)

        import_btn = Button(btn_frame,text="Import csv",command=self.import_csv,width=18,font=('times new roman',12,"bold"),fg='white',bg='lightgreen')
        import_btn.grid(row=0,column=0,padx=1)
        
        export_btn = Button(btn_frame,text="Export csv",command=self.export_csv,width=18,font=('times new roman',12,"bold"),fg='white',bg='lightblue')
        export_btn.grid(row=0,column=1,padx=1)

        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=18,font=('times new roman',12,"bold"),fg='white',bg='red')
        update_btn.grid(row=0,column=2,padx=1)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_attendance,width=18,font=('times new roman',12,"bold"),fg='white',bg='purple')
        reset_btn.grid(row=0,column=3,padx=1)

        

        

        right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Attendnace Details",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=5,width=725,height=530)

        table_frame=LabelFrame(right_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=10,width=700,height=500)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=('rollno','name','dep','date','time','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        
        self.AttendanceReportTable.heading("rollno",text='Roll Number')
        self.AttendanceReportTable.heading("name",text='Name')
        self.AttendanceReportTable.heading("dep",text='Department')
        self.AttendanceReportTable.heading("date",text='Date')
        self.AttendanceReportTable.heading("time",text='Time')
        self.AttendanceReportTable.heading("attendance",text='Attendance')
        
        self.AttendanceReportTable['show']='headings'

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.column('rollno',width=100)
        self.AttendanceReportTable.column('dep',width=100)
        self.AttendanceReportTable.column('date',width=150)
        self.AttendanceReportTable.column('time',width=100)
        self.AttendanceReportTable.column('attendance',width=100)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)
            
    def import_csv(self):
        global mydata
        mydata.clear()
        fin = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open csv file",filetypes=[("CSV File","*.csv"),("All File","*.*")],parent=self.root)
        with open(fin) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)


    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Empty","No data found to export",parent=self.root)
                return False
            fin = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open csv file",filetypes=[("CSV File","*.csv"),("All File","*.*")],parent=self.root)
            with open(fin,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","File saved successfully")

        except Exception as e:
            messagebox.showerror("Error",f"Due to {str(e)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        data = content["values"]

        self.var_rollno.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_date.set(data[3]),
        self.var_time.set(data[4]),
        self.var_attend.set(data[5])



    def update_data(self):
        pass


    def reset_attendance(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_dep.set("Select Department")
        self.var_date.set("")
        self.var_time.set("")
        self.var_attend.set("Select Attendance")

    

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()