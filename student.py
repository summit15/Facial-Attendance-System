from tkinter import *
from tkinter import ttk 
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np


class Student:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #(1530 is width , 790 is height, +0 +0 is x axis and yaxis starting from top left corner )
        root.configure(bg='#B0E0E6')
        self.root.title("Face Recognition System")

        # *************variables******* 

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_rollno=StringVar()
        self.var_name=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_phoneno=StringVar()
        self.var_email=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_address=StringVar()
        self.var_section=StringVar()

        #first image
        img = Image.open(r"Face recognition\Image 1.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img=img.resize((490,200))  # ANTIALIAS converts high level image into low levels
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x=10,y=0,width=490,height=180)

        #second image
        img1 = Image.open(r"Face recognition\Image 2.jpg")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img1=img1.resize((490,200))  
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x=520,y=0,width=490,height=180)

        #third image
        img2 = Image.open(r"Face recognition\image_3.png")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img2=img2.resize((500,200)) 
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x=1030,y=0,width=490,height=180)

        #title name
        title_lbl = Label(self.root, text='Add/Modify Student Details',font=('times new roman',35,'bold'),fg='green')
        title_lbl.place(x=10,y=190,width=1510, height= 55)

        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=10,y=250,width=1510,height=620)

        #left label frame 
        left_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=5,width=725,height=530)

        #current course frame 
        curr_course_frame=LabelFrame(left_frame,bd=3,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        curr_course_frame.place(x=5,y=0,width=700,height=115)

        dep_label = Label(curr_course_frame,text="Department",font=("times new roman",12,"bold"),bg='white',bd=1)
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("Select Department","Computer","Civil","Mechanical","Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column = 1,padx=2,pady=10,sticky=W)

        space_label = Label(curr_course_frame,text="            ",font=("times new roman",12,"bold"),bd=1)
        space_label.grid(row=0,column=2,padx=10,sticky=W)

        #course label
        course_label = Label(curr_course_frame,text="Course",font=("times new roman",12,"bold"),bg='white',bd=1)
        course_label.grid(row=0,column=3,padx=10,sticky=W)

        course_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
        course_combo["values"]=("Select Course","CSE","IT","CSCE","CSSE")
        course_combo.current(0)
        course_combo.grid(row=0,column = 4,padx=2,pady=10,sticky=W)


        #Year Label
        year_label = Label(curr_course_frame,text="Year",font=("times new roman",12,"bold"),bg='white',bd=1)
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2024-25")
        year_combo.current(0)
        year_combo.grid(row=1,column = 1,padx=2,pady=10,sticky=W)

        #Semester Label
        semester_label = Label(curr_course_frame,text="Semester",font=("times new roman",12,"bold"),bg='white',bd=1)
        semester_label.grid(row=1,column=3,padx=10,sticky=W)

        semester_combo=ttk.Combobox(curr_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
        semester_combo["values"]=("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eighth")
        semester_combo.current(0)
        semester_combo.grid(row=1,column = 4,padx=2,pady=10,sticky=W)

        # Class Student frame 
        class_student_frame=LabelFrame(left_frame,bd=3,relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=120,width=700,height=385)

        #Roll Number
        rollnumber_label = Label(class_student_frame,text="Roll No",font=("times new roman",12,"bold"),bg='white',bd=1)
        rollnumber_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)
        
        rollnumber_entry=ttk.Entry(class_student_frame,textvariable=self.var_rollno,width=20,font=("times new roman",12,"bold"))
        rollnumber_entry.grid(row=0,column=1,padx=10,sticky=W)


        #Student Name
        student_name_label = Label(class_student_frame,text="Name",font=("times new roman",12,"bold"),bg='white',bd=1)
        student_name_label.grid(row=1,column=0,padx=10,pady=10,sticky=W)
        
        student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_name,width=30,font=("times new roman",12,"bold"))
        student_name_entry.grid(row=1,column=1,padx=10,sticky=W)

        #Section
        section_label = Label(class_student_frame,text="Section",font=("times new roman",12,"bold"),bg='white',bd=1)
        section_label.grid(row=2,column=0,padx=10,pady=10,sticky=W)
        
        section_entry=ttk.Entry(class_student_frame,textvariable=self.var_section,width=20,font=("times new roman",12,"bold"))
        section_entry.grid(row=2,column=1,padx=10,sticky=W)

        #Gender
        gender_label = Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg='white',bd=1)
        gender_label.grid(row=2,column=2,padx=10,pady=10,sticky=W)
        
        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=17,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column = 3,padx=10,pady=10,sticky=W)
        


        #kiit id
        Email_label = Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg='white',bd=1)
        Email_label.grid(row=3,column=0,padx=10,pady=10,sticky=W)
        
        Email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        Email_entry.grid(row=3,column=1,padx=10,sticky=W)

        dob_label = Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg='white',bd=1)
        dob_label.grid(row=3,column=2,padx=10,pady=10,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=3,column=3,padx=10,sticky=W)

        phone_label = Label(class_student_frame,text="Phone No",font=("times new roman",12,"bold"),bg='white',bd=1)
        phone_label.grid(row=4,column=0,padx=10,pady=10,sticky=W)
        
        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phoneno,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=4,column=1,padx=10,sticky=W)

        address_label = Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg='white',bd=1)
        address_label.grid(row=5,column=0,padx=10,pady=10,sticky=W)
        
        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=30,font=("times new roman",12,"bold"))
        address_entry.grid(row=5,column=1,padx=10,sticky=W)

        #radio Button
        self.var_radio1 = StringVar()

        sample_label = Label(class_student_frame,text="Take Photo Sample ",font=("times new roman",12,"bold"))
        sample_label.grid(row=6,column=0,padx=10,pady=10,sticky=W)
        radiobtn1 = ttk.Radiobutton(class_student_frame,text="Yes",value="Yes",variable=self.var_radio1)
        radiobtn1.grid(row=6,column=1)
        radiobtn2 = ttk.Radiobutton(class_student_frame,text="No",value="No",variable=self.var_radio1)
        radiobtn2.grid(row=6,column=2)


        #button frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=5,y=295,width = 680,height = 30)

        save_btn = Button(btn_frame,text="Save",command=self.add_data,width=18,font=('times new roman',12,"bold"),fg='white',bg='lightgreen')
        save_btn.grid(row=0,column=0)
        
        update_btn = Button(btn_frame,text="Update",command=self.update_data,width=18,font=('times new roman',12,"bold"),fg='white',bg='lightblue')
        update_btn.grid(row=0,column=1)

        delete_btn = Button(btn_frame,text="Delete",command=self.delete_data,width=18,font=('times new roman',12,"bold"),fg='white',bg='red')
        delete_btn.grid(row=0,column=2)

        reset_btn = Button(btn_frame,text="Reset",command=self.reset_data,width=18,font=('times new roman',12,"bold"),fg='white',bg='purple')
        reset_btn.grid(row=0,column=3)

        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=5,y=325,width = 680,height = 30)

        take_photo_btn = Button(btn_frame1,command=self.generate_dataset,text="Take Photo",width=37,font=('times new roman',12,"bold"),fg='white',bg='lightblue')
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn = Button(btn_frame1,text="Update Photo",width=37,font=('times new roman',12,"bold"),fg='white',bg='lightgreen')
        update_photo_btn.grid(row=0,column=1)








        #right label frame 
        right_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=5,width=725,height=530)

        search_frame=LabelFrame(right_frame,bd=3,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=5,width=700,height=120)

        search_label = Label(search_frame,text="Search By : ",font=("times new roman",12,"bold"),bg='white',bd=1)
        search_label.grid(row=0,column=0,padx=10,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),width=17,state="readonly")
        search_combo["values"]=("Select","Roll No","Name","Phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column = 1,padx=10,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=30,font=("times new roman",12,"bold"))
        search_entry.grid(row=1,column=0,padx=10,sticky=W)


        search_btn = Button(search_frame,text="Search",width=15,font=('times new roman',12,"bold"),fg='white',bg='lightgreen')
        search_btn.grid(row=1,column=1,padx=4)

        showAll_btn = Button(search_frame,text="Show All",width=15,font=('times new roman',12,"bold"),fg='white',bg='lightgreen')
        showAll_btn.grid(row=1,column=2,padx=4)

        table_frame=LabelFrame(right_frame,bd=3,relief=RIDGE)
        table_frame.place(x=5,y=130,width=700,height=350)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=('rollno','name','dep','course','section','email','year','semester','gender','dob','phoneno','address','photo'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text='Department')
        self.student_table.heading("rollno",text='Roll Number')
        self.student_table.heading("name",text='Name')
        self.student_table.heading("email",text='Email')
        self.student_table.heading("year",text='Year')
        self.student_table.heading("gender",text='Gender')
        self.student_table.heading("semester",text='Semester')
        self.student_table.heading("dob",text='DOB')
        self.student_table.heading("phoneno",text='Phone No')
        self.student_table.heading("course",text='Course')
        self.student_table.heading("section",text='Section')
        self.student_table.heading("address",text='Address')
        self.student_table.heading("photo",text='Photo Sample Status')
        self.student_table['show']='headings'

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column('rollno',width=100)
        self.student_table.column('dep',width=100)
        self.student_table.column('course',width=150)
        self.student_table.column('year',width=100)
        self.student_table.column('semester',width=100)
        self.student_table.column('section',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('photo',width=120)
        self.student_table.column('phoneno',width=100)
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # Function declaration

    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get()=="Select Course" or self.var_rollno=="":
            messagebox.showerror("Error","All fields are required to fill",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user="root",password='R00tpp123..Abc',database='face_recognition',auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_rollno.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_phoneno.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            
                                                                                                            
                                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details successfully added",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # *************Fetch Data******************

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user="root",password='R00tpp123..Abc',database='face_recognition',auth_plugin='mysql_native_password')
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #**************** get cursor function *****************

    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_rollno.set(data[0]),
        self.var_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_section.set(data[4]),
        self.var_email.set(data[5]),
        self.var_year.set(data[6]),
        self.var_semester.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_phoneno.set(data[10]),
        self.var_address.set(data[11]),
        self.var_radio1.set(data[12])

    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get()=="Select Course" or self.var_rollno=="":
            messagebox.showerror("Error","All fields are required to fill",parent=self.root)
        else:
            try:
                update_msg = messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if update_msg>0:
                    conn=mysql.connector.connect(host='localhost',user="root",password='R00tpp123..Abc',database='face_recognition',auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Name=%s,Department=%s,Course=%s,Section=%s,Email=%s,Year=%s,Semester=%s,Gender=%s,DOB=%s,Phoneno=%s,Address=%s,PhotoSample=%s where RollNo=%s" , (
                                                                                                            
                                                                                                            self.var_name.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_phoneno.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_rollno.get()
                                                                                                            
                                                                                                             
                                                                                                    ))
                else:
                    if not update_msg:
                        return 
                    
                messagebox.showinfo("Success","Student Details updated.",parent  = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Error occured due to {str(es)}",parent = self.root)

    # ************ DETELE RESET FUNCTION *************************
    def delete_data(self):
        if self.var_rollno.get()=="":
            messagebox.showerror("Error","Roll Number is required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Confirmation","Do you want to delete the data ? ",parent = self.root)
                if delete > 0:
                    conn=mysql.connector.connect(host='localhost',user="root",password='R00tpp123..Abc',database='face_recognition',auth_plugin='mysql_native_password')
                    my_cursor = conn.cursor()
                    sql = "delete from student where RollNo=%s"
                    val = (self.var_rollno.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                messagebox.showinfo("Success","Student Details Deleted.",parent  = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Error occured due to {str(es)}",parent = self.root)

    def reset_data(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_section.set("")
        self.var_email.set("")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_phoneno.set("")
        self.var_address.set("") 
        self.var_radio1.set("")


    # ---------------Generate dataset and take photo samples -------------#

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get()=="Select Course" or self.var_rollno=="":
            messagebox.showerror("Error","All fields are required to fill",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user="root",password='R00tpp123..Abc',database='face_recognition',auth_plugin='mysql_native_password')
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student")
                myresult = my_cursor.fetchall()
                id=0
                for x in myresult: 
                    id+=1
                my_cursor.execute("update student set Name=%s,Department=%s,Course=%s,Section=%s,Email=%s,Year=%s,Semester=%s,Gender=%s,DOB=%s,Phoneno=%s,Address=%s,PhotoSample=%s where RollNo=%s" , (
                                                                                                            
                                                                                                            self.var_name.get(),
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_course.get(),
                                                                                                            self.var_section.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_phoneno.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_radio1.get(),
                                                                                                            self.var_rollno.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # Load predefined data on face frontals from opencv 

                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                    #scaling factor = 1.3 , minimum neighbour = 5 by default

                    if len(faces) == 0:
                        return None

                    for (x,y,w,h) in faces:
                        if w<200 or h<200:
                            continue
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap = cv2.VideoCapture(0)
                img_id = 0
                sample_count = 0

                while True:
                    ret,my_frame = cap.read()
                    if not ret:
                        print("Failed to capture frame")
                        break
                    my_frame = cv2.cvtColor(my_frame, cv2.COLOR_BGR2GRAY)
                    my_frame = cv2.equalizeHist(my_frame)
                    my_frame = cv2.cvtColor(my_frame, cv2.COLOR_GRAY2BGR)
                    cropped_face= face_cropped(my_frame)

                    if cropped_face is not None:
                        img_id +=1
                        face = cv2.resize(cropped_face,(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                        if np.mean(face) < 10 or np.mean(face) > 300:
                            print("Skipped sample due to poor lighting.")
                            continue
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(10,30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)
                        cv2.imshow("Cropped a face",face)

                        sample_count +=1

                    if cv2.waitKey(1)==13 or sample_count == 100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Dataset generated successfully")


            except Exception as es:
                messagebox.showerror("Error",f"Error occured due to {str(es)}",parent = self.root)

  
                
            

                                                                                                            
                                                                                                             
                                                          
                


        













                
            

        


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()