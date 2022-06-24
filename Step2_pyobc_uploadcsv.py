## import the tkinter package for GUI
from tkinter import *
from tkinter import ttk
import tkinter as tk
## [1] import pyodbc package
## py -m pip install pyodbc
import pyodbc
# convert dictionary string to dictionary
# using ast.literal_eval()
import ast
import tkinter.messagebox as tmsg
# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

# read config from file
def get_connection_info(file_name):
    str1=""
    # Open config file to get connection info
    file1=open(file_name,"r")
    str1=file1.readlines()
    file1.close
    return str1

# write string to file
def write_to_file(file_name, datastr):
    str1=""
    # Open file to write data into it
    file1=open(file_name,"w")
    file1.write(str(datastr))
    file1.close
    tmsg.showinfo("Export","Exported to "+file_name)

# This function will be used to open
# file in read mode and only csv files
# will be opened
def open_file():
    file = askopenfile(mode ='r', filetypes =[('Python Files', '*.csv')])
    if file is not None:
        content = file.read()
        editbox8.delete('1.0', END)
        editbox8.insert(INSERT,content)
        #print(content)
        thelist=list(content.split('\n'))
        #print(thelist[0])
        sqlstr="CREATE TABLE "+editbox4.get()+"("
        row1list=list(thelist[0].split(','))
        for i in row1list:
            sqlstr=sqlstr+str(i)+" varchar(255),"
        sqlstr=sqlstr[:-1]+")"
        text5.set(sqlstr)

# define function CreateTableButtonClick
def CreateTableButtonClick():
    print("CreateTable")
    sql=editbox5.get()
    if sql:
        connectionstatus=0
        # Create connection to InterSystems IRIS
        try:
            connection = pyodbc.connect(connection_string)
            print("{c} is working".format(c=connection_string))
            connectionstatus=1
        except pyodbc.Error as ex:
            print("{c} is not working".format(c=connection_string))
            connectionstatus=0

        # Created the table
        if connectionstatus==1:
            print(sql)
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            tmsg.showinfo("Message","Table "+editbox4.get()+" is created")
            
        # Close the connection to InterSystems IRIS
        if connectionstatus==1:
            connection.close
            print("disconnected")
    else:
        tmsg.showinfo("Message","Please input SQL")

# define function UploadDataButtonClick
def UploadDataButtonClick():
    print("Uploading")
    connectionstatus=0
    # Create connection to InterSystems IRIS
    try:
        connection = pyodbc.connect(connection_string)
        print("{c} is working".format(c=connection_string))
        connectionstatus=1
    except pyodbc.Error as ex:
        print("{c} is not working".format(c=connection_string))
        connectionstatus=0

    # select the tiems
    if connectionstatus==1:
        data1=editbox8.get('1.0', END)
        if data1!="\n":
            thelist=list(data1.split('\n'))
            row0=thelist.pop(0)
            sql="INSERT INTO "+editbox4.get()+"("+str(row0)+") VALUES ("
            #print(sql)
            counter=1
            for i in thelist:
                b=str(i).replace("'",'"')
                b="'"+b.replace(',',"','")+"'"
                b=b.replace('\r','')
                b=b.replace('\n','')
                if b=="":
                    pass
                #print(b)
                sqli=sql+b+")"
                print(sqli)
                cursor=connection.cursor()
                cursor.execute(sqli)
                connection.commit()
                print(str(counter)+". Inserted :"+b)
                counter=counter+1
            tmsg.showinfo("Message","Data Uploaded")
        else:
            tmsg.showinfo("Message","No data")
        
    # Close the connection to InterSystems IRIS
    if connectionstatus==1:
        connection.close
        print("disconnected")
        
# Retrieve connection information from configuration file
str1=get_connection_info("connetconf.txt")
connectionconfig=ast.literal_eval(str1[0])
driver="{InterSystems IRIS ODBC35}"
connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
                    .format(driver, connectionconfig['hostname'], connectionconfig['port']\
                    , connectionconfig['namespace'], connectionconfig['login'], connectionconfig['password'])
# define a string to store the content of a csv file
content=str("")

## define a window
root = tk.Tk()
## define the window size
root.geometry("800x350")
## define the title of the Windows
root.title("pyodbc SQL query")

## add a label
label2=tk.Label(root,text="Select a .csv file to import")
label2.place(x=10,y=70)
## add a button
button2=tk.Button(root, text ="Open", command = lambda:open_file())
button2.place(x=180,y=70, width=100)
## add a label
label3=tk.Label(root,text="Create a table")
label3.place(x=10,y=10)
## add a label
label4=tk.Label(root,text="Table Name")
label4.place(x=10,y=40)
## add an entry box
text4=tk.StringVar()
text4.set("Patient")
editbox4=tk.Entry(width=40,textvariable=text4)
editbox4.place(x=180,y=40)
## add a label
label5=tk.Label(root,text="SQL (Create Table)")
label5.place(x=10,y=100)
## add an entry box
text5=tk.StringVar()
text5.set("")
editbox5=tk.Entry(width=40,textvariable=text5)
editbox5.place(x=180,y=100,width=600)
## add a button
button5=tk.Button(root, text ="Create Table", command =CreateTableButtonClick)
button5.place(x=180,y=130, width=100)
## add a label
label6=tk.Label(root,text="Upload the data to Table")
label6.place(x=10,y=160)
## add a button
button7=tk.Button(root, text ="Upload Data", command =UploadDataButtonClick)
button7.place(x=180,y=160, width=100)
## add a label
label8=tk.Label(root,text="Data")
label8.place(x=10,y=190)
## add an entry box
editbox8=Text(root,width=95,height=4)
editbox8.place(x=10,y=220)


## add a Close button
button1=tk.Button(root, text="Close",width=8,command=root.destroy)
button1.place(x=10,y=300)


root.mainloop()


