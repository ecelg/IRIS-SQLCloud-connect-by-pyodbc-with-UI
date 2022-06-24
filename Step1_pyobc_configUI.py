## import the tkinter package for GUI
import tkinter as tk
#[1] import pyodbc package
# py -m pip install pyodbc
import pyodbc
# convert dictionary string to dictionary
# using ast.literal_eval()
import ast

# define function read config from file
def get_connection_info(file_name):
    str1=""
    # Open config file to get connection info
    file1=open(file_name,"r")
    str1=file1.readlines()
    file1.close
    return str1

# define function SaveButtonClick
import tkinter.messagebox as tmsg
def SaveButtonClick():
    connectionconfig.update({'hostname':editbox1.get(),'port':editbox2.get(), \
        'namespace':editbox3.get(),'login':editbox4.get(),'password':editbox5.get()})
    print(connectionconfig)
    file1=open("connetconf.txt","w")
    file1.write(str(connectionconfig))
    file1.close
    tmsg.showinfo("Config","Save")
    
# define function ConnectButtonClick
def ConnectButtonClick():
    hostname=editbox1.get()
    port=editbox2.get()
    namespace=editbox3.get()
    login=editbox4.get()
    password=editbox5.get()
    connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
        .format(driver, hostname, port, namespace, login, password)
    try:
        connection = pyodbc.connect(connection_string)
        conettionst="Able to connected to IRIS"
    except pyodbc.Error as ex:
        print("{c} is not working".format(c=connection_string))
        conettionst="Fail to connect!"
    text6.set(conettionst)
    connection.close

# define function CloseButtonClick
def CloseButtonClick():
    root.destroy()


#Retrieve connection information from configuration file
str1=get_connection_info("connetconf.txt")
connectionconfig=ast.literal_eval(str1[0])

hostname=connectionconfig['hostname']
port=connectionconfig['port']
namespace=connectionconfig['namespace']
login=connectionconfig['login']
password=connectionconfig['password']
driver="{InterSystems IRIS ODBC35}"
connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
        .format(driver, hostname, port, namespace, login, password)
conettionst=""


## define a window
root = tk.Tk()

## define the window size
root.geometry("600x150")
## define the title of the Windows
root.title("pyodbc config")

## add a label
label1=tk.Label(root,text="hostname")
label1.place(x=10,y=10)
## add an entry box
text1=tk.StringVar()
text1.set(hostname)
editbox1=tk.Entry(width=50,textvariable=text1)
editbox1.place(x=100,y=10)
## add a label
label2=tk.Label(root,text="port")
label2.place(x=10,y=30)
## add an entry box
text2=tk.StringVar()
text2.set(port)
editbox2=tk.Entry(width=50,textvariable=text2)
editbox2.place(x=100,y=30)
## add a label
label3=tk.Label(root,text="namespace")
label3.place(x=10,y=50)
## add an entry box
text3=tk.StringVar()
text3.set(namespace)
editbox3=tk.Entry(width=50,textvariable=text3)
editbox3.place(x=100,y=50)
## add a label
label4=tk.Label(root,text="login")
label4.place(x=10,y=70)
## add an entry box
text4=tk.StringVar()
text4.set(login)
editbox4=tk.Entry(width=50,textvariable=text4)
editbox4.place(x=100,y=70)
## add a label
label5=tk.Label(root,text="password")
label5.place(x=10,y=90)
## add an entry box
text5=tk.StringVar()
text5.set(password)
editbox5=tk.Entry(width=50,textvariable=text5)
editbox5.place(x=100,y=90)

## add a label
text6=tk.StringVar()
text6.set(conettionst)
label6=tk.Label(root,textvariable=text6)
label6.place(x=420,y=10)




## add a save button
button1=tk.Button(root, text="Save",width=8,command=SaveButtonClick)
button1.place(x=10,y=120)
## add a TestConnection button
button2=tk.Button(root, text="Test Connection",width=16,command=ConnectButtonClick)
button2.place(x=80,y=120)
## add a Close button
button4=tk.Button(root, text="Close",width=8,command=CloseButtonClick)
button4.place(x=220,y=120)

## display a window
root.mainloop()



