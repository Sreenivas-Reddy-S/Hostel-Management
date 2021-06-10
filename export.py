import tkinter as tk
from tkinter import StringVar,IntVar,ttk
from PIL import Image,ImageTk
import pymysql
FF_FONT=("action man",22)
F_FONT=("action man",14)
S_FONT=("tahoma",10)
hen=[]
class Application(tk.Tk):
    def __init__(self,*args):
        tk.Tk.__init__(self,*args)
        tk.Tk.wm_title(self,"VIT Hostel Room Allotment System")
        container=tk.Frame(self)
        container.pack(side="top",fill="both",expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0,weight=1)
        self.frames={}
        for fram in (loginpage,success,reg):
            frame=fram(container,self)
            self.frames[fram]=frame
            frame.grid(row=0,column=0,sticky="nsew")
        self.show_frame(loginpage)
        
    def show_frame(self,cont):
        frame=self.frames[cont]
        frame.tkraise()



    
class loginpage(tk.Frame):
    def __init__(self,parent,controller):
        loginid=StringVar()
        pid=StringVar()
        def loginfunc(lid,password):
            cur.execute("select s.studentID from student s,ainfo a where s.studentID=a.studentID and s.roomID is null order by a.year DESC,a.cgpa DESC;")
            ord=cur.fetchall()
            print('this is print',lid,ord[0]['studentID'])
            if(lid==ord[0]['studentID']):
                chance=1
            else:
                chance=0
            if(len(lid)>9 or len(lid)==0):
                popup=tk.Toplevel()
                popup.title("Caution")
                popup.geometry("200x200")
                popup.configure(background="#a1dbcd",bg="#aadbcd")
                inv=tk.Label(popup,text="INVALID REGISTRATION NUMBER")
                pic=Image.open('warn.png')
                ren=ImageTk.PhotoImage(pic)
                w=tk.Label(popup,image=ren)
                w.image=ren
                w.pack()
                inv.pack()
            cur.execute("select password from student where studentID='%s'"%(lid))
            psw=cur.fetchall()
            print(psw)
            if(psw[0]['password']==password and chance==1):
                controller.show_frame(reg)
            elif(psw[0]['password']!=password):
                ppopup=tk.Toplevel()
                ppopup.title("Caution")
                ppopup.geometry("250x250")
                pic=Image.open('ad.png')
                ren=ImageTk.PhotoImage(pic)
                w1=tk.Label(ppopup,image=ren)
                w1.image=ren
                w1.pack()
                inv=tk.Label(ppopup,text="INVALID PASSWORD",font=F_FONT)
                inv.pack(side=tk.TOP)
            elif(chance==0):
                ppopup=tk.Toplevel()
                ppopup.title("Caution")
                ppopup.geometry("250x250")
                pic=Image.open('ad.png')
                ren=ImageTk.PhotoImage(pic)
                w1=tk.Label(ppopup,image=ren)
                w1.image=ren
                w1.pack()
                inv=tk.Label(ppopup,text="WAIT FOR YOUR CHANCE",font=F_FONT)
                inv.pack(side=tk.TOP)
                inv1=tk.Label(ppopup,text="see the allotment order",font=F_FONT)
                inv1.pack(side=tk.TOP)
            print(lid)
            print(password)
        def aorder():
            popup1=tk.Tk()
            popup1.title("allotment order")
            popup1.geometry("300x150")
            sb=tk.Scrollbar(master=popup1)
            sb.pack(side=tk.RIGHT,fill=tk.Y)
            listbox=tk.Listbox(master=popup1)
            listbox.pack(side=tk.TOP)
            cur.execute("select s.studentID,a.cgpa,a.year from student s,ainfo a where s.studentID=a.studentID and s.roomID is null order by a.year DESC,a.cgpa DESC;")
            ord=cur.fetchall()
            #print(ord)
            listbox.insert(tk.END,('RegnNo','|','Year','|','CGPA'))
            for i in range(len(ord)):
                listbox.insert(tk.END,(ord[i]['studentID'],'-',ord[i]['year'],'-',ord[i]['cgpa']))
            listbox.config(yscrollcommand=sb.set)
            sb.config(command=listbox.yview)
            
        tk.Frame.__init__(self,parent)
        photo=tk.PhotoImage(file="vhm.png")
        w=tk.Label(self,image=photo)
        w.image=photo
        w.pack()
        label=tk.Label(self,text="LOGIN PAGE",font=F_FONT)
        label.pack(pady=10,padx=10)
        login=tk.Label(self,text="Login",font=F_FONT)
        lo_entry=tk.Entry(self,textvariable=loginid,width=10)
        pas=tk.Label(self,text="Password",font=F_FONT)
        pas_entry=tk.Entry(self,show='*',textvariable=pid)
        login.pack(side=tk.LEFT)
        lo_entry.pack(side=tk.LEFT)
        pas.pack(side=tk.LEFT)
        pas_entry.pack(side=tk.LEFT)
        logbutton=ttk.Button(self,text="Login",command=lambda:loginfunc(loginid.get(),pid.get()))
        logbutton.pack(pady=20,padx=20,side=tk.LEFT)
        button=ttk.Checkbutton(self,text="Allotment Order",command=lambda:aorder())
        button.pack(pady=20,padx=20)
        

        
class success(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        suc=tk.Label(self,text="SUCCESSFULLY REGISTERED",font=FF_FONT)
        suc.pack(side=tk.TOP)
        button=ttk.Button(self,text="Back to Login Page",command=lambda: controller.show_frame(loginpage))
        button.pack()
        
class reg(tk.Frame):
    def __init__(self,parent,controller):
        rno=IntVar()
        def availa(blo,ty,si):
            blo=blo.upper()
            ty=ty.upper()
            if ty=='AC':
                ty='A'
            elif ty=='NON AC':
                ty='N'
            cur.execute("select rno from room where block='%s' and Type='%s' and beds=%d and taken=0"%(blo,ty,si))
            res=cur.fetchall()
            print(res)
            l=tk.Label(self,text="The Following rooms are available",font=F_FONT)
            l.grid()
            tr=''
            for i in range(len(res)):
                tr=tr+'\n'+str(res[i]['rno'])
            l1=tk.Label(self,text=tr,font=F_FONT)
            l1.grid(row=18)
            cf=tk.PhotoImage(file='cb.png')
            cb=tk.Button(self,image=cf,command=lambda:(l.grid_forget(),l1.grid_forget(),cb.grid_forget(),rs()))
            cb.image=cf
            cb.grid(row=30,column=0,sticky='N',padx=10,pady=10)
        def rs():
            r1=tk.Label(self,text='enter the selected room number',font=F_FONT)
            r1.grid(row=24)
            r_ent=tk.Entry(self,textvariable=rno)
            r_ent.grid(row=26)
            cf=tk.PhotoImage(file='cb.png')
            cb=tk.Button(self,image=cf,command=lambda:(r1.grid_forget(),r_ent.grid_forget(),cb.grid_forget(),fin()))
            cb.image=cf
            cb.grid(row=30,sticky='S',padx=10,pady=10)
        def fin():
            
            entry=tk.Tk()
            entry.title("Enter Roommates")
            entry.geometry('150x300')
            cur.execute("select roomID,beds from room where rno=%d and block='%s'"%(rno.get(),blok.get()))
            res=cur.fetchall()
            ss=[]
            s=tk.Label(entry,text='enter details of roommates')
            s.pack()
            def com():
                global hen
                for j in range(0,res[0]['beds']):
                    hen.append(ss[j].get())
                    print(hen[j],res[0]['roomID'])
                for k in range(0,res[0]['beds']):
                    cur.execute("update student set roomID=%d where studentID='%s'"%(res[0]['roomID'],hen[k]))
                    conn.commit()
                cur.execute("update room set taken=1 where roomID=%d"%res[0]['roomID'])
                conn.commit()
                controller.show_frame(success)
                entry.destroy()
            for i in range(0,res[0]['beds']):              
                e=tk.Entry(entry)
                e.pack(padx=7,pady=7)
                ss.append(e)
            r=tk.Button(entry,text="Register",command=lambda:com())
            r.pack()
            
        t1=StringVar()
        blok=StringVar()
        capacity=IntVar()
        tk.Frame.__init__(self,parent)
        w=tk.Label(self,text="ROOM ALLOTMENT",font=F_FONT)
        w.grid(row=1,sticky='N',padx=250,pady=10)
        block=tk.Label(self,text="Block:",fg="#383239",bg="#a1dbcd")
        b_ent=tk.Entry(self,textvariable=blok)
        typ=tk.Label(self,text="Type:",fg="#383239",bg="#a1dbcd")
        t_ent=tk.Entry(self,textvariable=t1)
        size=tk.Label(self,text="Beds:",fg="#383239",bg="#a1dbcd")
        s_ent=tk.Entry(self,textvariable=capacity)
        block.grid(row=4,sticky='N',padx=10,pady=10)
        b_ent.grid(row=6,sticky='N',padx=10,pady=10)
        typ.grid(row=8,sticky='N',padx=10,pady=10)
        t_ent.grid(row=10,sticky='N',padx=10,pady=10)
        size.grid(row=12,sticky='N',padx=10,pady=10)
        s_ent.grid(row=14)
        avail=ttk.Button(self,text="Check Availability",command=lambda: availa(blok.get(),t1.get(),capacity.get()))
        avail.grid(row=16,sticky='N',padx=10,pady=10)        



conn=pymysql.connect(host='localhost',user='root',password='',db='hostel')
cur=conn.cursor(pymysql.cursors.DictCursor)

conn.commit()
app= Application()
app.mainloop()
