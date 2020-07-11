#importar as bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import DataBaser

#criar janela
jan = Tk()
jan.title("DP Systems - Login Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.attributes("-alpha",0.9)

#colocando icone
#jan.iconbitmap(defaut ="icons/LogoIcon.ico") - tem que estar na pasta e no formato bitmap



#====carregando img===
logo = PhotoImage(file="icons/1.png")
 

#=====Widgets=====
LeftFrame = Frame(jan, width=200, height=300, bg="white",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=25, y=100)

#Usuario
UserLabel = Label(RightFrame, text="Username:", font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=150,y=110)

#Senha
PassLabel = Label(RightFrame, text="Password:",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=5,y=150)

PassEntry = ttk.Entry(RightFrame, width=30,show="*")
PassEntry.place(x=140,y=160)

def Login():
    User = UserEntry.get()
    Pass = PassEntry.get()

    DataBaser.cursor.execute("""
    SELECT * FROM Users
    WHERE(User = ? and Password = ?)
    """,(User,Pass))
    print("Selecionou")
    VerifyLogin = DataBaser.cursor.fetchone()
    try:
        if(User in VerifyLogin and Pass in VerifyLogin):
            messagebox.showinfo(title="Login Info", message="Acesso Confirmado.Bem Vindo!!")
    except:
        messagebox.showinfo(title="Login Info",message="Acesso Negado!! Verifique se esta cadastrado no sistema.")

#Botoes
LoginButton = ttk.Button(RightFrame, text="Login", width=30, command=Login)
LoginButton.place(x=100,y=225)

def Register():
    #removendo widgets de login
    LoginButton.place(x=5000)
    RegisterButton.place(x=5000)
    #inserindo widgets de cadastro
    NomeLabel = Label(RightFrame, text="Name:",font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="white")
    NomeLabel.place(x=5,y=5)

    NomeEntry = ttk.Entry(RightFrame,width=39)
    NomeEntry.place(x=100,y=16)

    EmailLabel = Label(RightFrame, text="Email:",font=("Century Gothic",20),bg="MIDNIGHTBLUE", fg="white")
    EmailLabel.place(x=5,y=55)

    EmailEntry = ttk.Entry(RightFrame,width=39)
    EmailEntry.place(x=100,y=66)

    #criar os botoes de cadastrar
    def RegisterToDataBase():
        Name = NomeEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Pass = PassEntry.get()

        if(Name == "" and Email == "" and User == "" and Pass ==""):
            messagebox.showerror(title="Register Error",message="Preencha TODOS os campos!!")
        else:
            DataBaser.cursor.execute("""
            INSERT INTO Users(Name,Email,User,Password) VALUES(?,?,?,?)
            """,(Name,Email,User,Pass))
            DataBaser.conn.commit()
            messagebox.showinfo(title="Register Info", message="Register Sucessfull")

    Register = ttk.Button(RightFrame,text="Register",width=30,command=RegisterToDataBase)
    Register.place(x=100,y=225)

    def BackToLogin():
        #removendo widgets de cadastro
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Register.place(x=5000)
        Back.place(x=5000)
        #trazendo os widgets de login
        LoginButton.place(x=100)
        RegisterButton.place(x=125)


    Back = ttk.Button(RightFrame,text="Back",width=20,command=BackToLogin)
    Back.place(x=125,y=260)



RegisterButton = ttk.Button(RightFrame, text="Register", width=20,command=Register)
RegisterButton.place(x=125,y=260)




 


jan.mainloop()