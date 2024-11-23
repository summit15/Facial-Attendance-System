from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np




class Train:
    def __init__(self, root):
        self.root=root
        self.root.geometry("1530x790+0+0")  #(1530 is width , 790 is height, +0 +0 is x axis and yaxis starting from top left corner )
        root.configure(bg='#B0E0E6')
        self.root.title("Face Recognition System")


        #title name
        title_lbl = Label(self.root, text='Train Dataset',font=('times new roman',35,'bold'),fg='green')
        title_lbl.place(x=0,y=0,width=1530, height= 45)


        img_top = Image.open(r"facial.webp")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img_top=img_top.resize((1530,325)) 
        self.photoimg_top = ImageTk.PhotoImage(img_top)


        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=325)


        b1 = Button(self.root,command=self.train_photos, text="TRAIN DATA", cursor="hand2",font=('times new roman',20,'bold'),fg='white',bg='lightgreen')
        b1.place(x=600,y=385,width=300,height=50)


        img_bottom = Image.open(r"facial.webp")  # in python we have to convert backslash to forward slash , alternative method is writing r in front
        img_bottom=img_bottom.resize((1530,325))  
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)


        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x=0,y=440,width=1530,height=325)


    def train_photos(self):
        data_dir = ("data")
        path = [os.path.join(data_dir,file) for file  in os.listdir(data_dir)]
        faces=[]
        ids=[]


        for image in path:
            img=Image.open(image).convert('L')  #gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split('.')[1])


            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13


        ids=np.array(ids)


        ###########Training the classifier


        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Completed !!")




if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()