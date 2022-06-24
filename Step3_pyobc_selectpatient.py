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

# select a ltem form the treeview
def selectItem(a):
    curItem = tree.focus()
    #print (tree.item(curItem))
    #print(tree.item(curItem).get('values'))
    if tree.item(curItem).get('values'):
        print(tree.item(curItem).get('values')[0])
        rowID=tree.item(curItem).get('values')[0]

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
            sql="select PatientID,Name,Insurance,PrimaryPhysician,\
                    CreditRating,HomePhone,HomeAdd_City,HomeAdd_State,\
                    HomeAdd_Zip from Patient where PatientID=?"
            #print(Platfrom)
            cursor = connection.cursor()
            cursor.execute(sql,rowID)

            rows=cursor.fetchall()
            print(rows[0])
            listrow=list(rows[0])
            ## display the data
            text2.set(listrow[1])
            text3.set(listrow[2])
            text4.set(listrow[3])
            text5.set(listrow[4])
            text6.set(listrow[5])
            text7.set(listrow[6])
            text8.set(listrow[7])
            text9.set(listrow[8])
            text10.set(listrow[0])
            
        # Close the connection to InterSystems IRIS
        if connectionstatus==1:
            connection.close
            print("disconnected")

# define function SearchButtonClick
def SearchButtonClick():
    #print("searching")
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
        # clear the pervious selection
        for item in tree.get_children():
            tree.delete(item)
        # clear the patient detail
            text2.set("")
            text3.set("")
            text4.set("")
            text5.set("")
            text6.set("")
            text7.set("")
            text8.set("")
            text9.set("")
            text10.set("")
        
        sql="select PatientID,Name,Insurance,PrimaryPhysician from Patient where Name like ?"
        PatientName=editbox1.get()+str('%')
        cursor = connection.cursor()
        cursor.execute(sql,PatientName)

        rows=cursor.fetchall()
        # loop through the rows
        for i in rows:
            #print(i)
            thislist=list(i)
            tree.insert('',tk.END, values=thislist)
        
    # Close the connection to InterSystems IRIS
    if connectionstatus==1:
        connection.close
        print("disconnected")

# define function UpdateButtonClick
def UpdateButtonClick():
    #print("Updated")
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
        PatientID=editbox10.get()
        Name=editbox2.get()
        Insurance=editbox3.get()
        PrimaryPhysician=editbox4.get()
        CreditRating=editbox5.get()
        HomePhone=editbox6.get()
        HomeAddCity=editbox7.get()
        HomeAddState=editbox8.get()
        HomeAddZip=editbox9.get()
        if PatientID:
            sql="update Patient set Name=?,Insurance=?,PrimaryPhysician=?,\
                    CreditRating=?,HomePhone=?,HomeAdd_City=?,HomeAdd_State=?,\
                    HomeAdd_Zip=? where PatientID=?"
            
            #print(PatientID)
            cursor = connection.cursor()
            cursor.execute(sql,Name,Insurance,PrimaryPhysician,CreditRating,HomePhone,HomeAddCity,HomeAddState,HomeAddZip,PatientID)
            connection.commit()

            tmsg.showinfo("Data","Updated")
            # clear the pervious selection
            for item in tree.get_children():
                tree.delete(item)
        else:
            print("No Patient ID")
        
    # Close the connection to InterSystems IRIS
    if connectionstatus==1:
        connection.close
        print("disconnected")
        
# define function ExportButtonClick
def ExportButtonClick():
    #print("Export")
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
        sql="select PatientID,Name,Insurance,PrimaryPhysician,CreditRating,HomePhone,HomeAdd_City,HomeAdd_State,HomeAdd_Zip from Patient where Name like ?"
        PatientName=editbox1.get()+str('%')
        cursor = connection.cursor()
        cursor.execute(sql,PatientName)
        str1='PatientID,Name,Insurance,PrimaryPhysician,CreditRating,HomePhone,HomeAdd_City,HomeAdd_State,HomeAdd_Zip\n'
        rows=cursor.fetchall()
        print(rows)
        # loop through the rows
        for i in rows:
            #print(i)
            #str1=str1+str(i)[1:-1]+"\n"
            thislist=list(i)
            for j in thislist:
                str1=str1+'\"'+str(j)+'\",'
            str1=str1+"\n"
        
        write_to_file("PatientExport.csv", str1)
        
    # Close the connection to InterSystems IRIS
    if connectionstatus==1:
        connection.close
        print("disconnected")

# define function ClearButtonClick
def ClearButtonClick():
    print("clearing")
    # clear the pervious selection
    for item in tree.get_children():
        tree.delete(item)
    # clear the patient detail
    text1.set("")
    text2.set("")
    text3.set("")
    text4.set("")
    text5.set("")
    text6.set("")
    text7.set("")
    text8.set("")
    text9.set("")
    text10.set("")
    
# define function InsertButtonClick
def InsertButtonClick():
    print("Inserting")
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
        PatientID=editbox10.get()
        Name=editbox2.get()
        Insurance=editbox3.get()
        PrimaryPhysician=editbox4.get()
        CreditRating=editbox5.get()
        HomePhone=editbox6.get()
        HomeAddCity=editbox7.get()
        HomeAddState=editbox8.get()
        HomeAddZip=editbox9.get()
        if PatientID:
            sql="update Patient set Name=?,Insurance=?,PrimaryPhysician=?,\
                    CreditRating=?,HomePhone=?,HomeAdd_City=?,HomeAdd_State=?,\
                    HomeAdd_Zip=? where PatientID=?"
        
            #print(PatientID)
            cursor = connection.cursor()
            cursor.execute(sql,Name,Insurance,PrimaryPhysician,CreditRating,HomePhone,HomeAddCity,HomeAddState,HomeAddZip,PatientID)
            connection.commit()

            tmsg.showinfo("Data","Data of  "+Name+" Updated")
            # clear the pervious selection
            for item in tree.get_children():
                tree.delete(item)
        else:
            print("No Patient ID going to insert")
            sql="select MAX(PatientID) from Patient"
            cursor = connection.cursor()
            cursor.execute(sql)
            rows=cursor.fetchall()
            #print(rows[0])
            thislist=list(rows[0])
            PatientID=thislist[0]+1
            print(PatientID)
            
            sql="INSERT INTO Patient (PatientID,Name,Insurance,PrimaryPhysician,CreditRating,HomePhone,HomeAdd_City,HomeAdd_State,HomeAdd_Zip)\
            VALUES (?,?,?,?,?,?,?,?,?)"
            cursor = connection.cursor()
            cursor.execute(sql,PatientID,Name,Insurance,PrimaryPhysician,CreditRating,HomePhone,HomeAddCity,HomeAddState,HomeAddZip)
            connection.commit()

            tmsg.showinfo("Data","Data of  "+Name+" Inserted")
            ClearButtonClick()
    # Close the connection to InterSystems IRIS
    if connectionstatus==1:
        connection.close
        print("disconnected")
    
# Retrieve connection information from configuration file
str1=get_connection_info("connetconf.txt")
connectionconfig=ast.literal_eval(str1[0])
"""
hostname=connectionconfig['hostname']
port=connectionconfig['port']
namespace=connectionconfig['namespace']
login=connectionconfig['login']
password=connectionconfig['password']
"""
driver="{InterSystems IRIS ODBC35}"
connection_string = 'DRIVER={};SERVER={};PORT={};DATABASE={};UID={};PWD={}' \
                    .format(driver, connectionconfig['hostname'], connectionconfig['port']\
                    , connectionconfig['namespace'], connectionconfig['login'], connectionconfig['password'])

## define a window
root = tk.Tk()
## define the window size
#root.geometry("800x350")
root.geometry("1200x350")
## define the title of the Windows
root.title("pyodbc SQL query")

## add a label
label1=tk.Label(root,text="Patient Name")
label1.place(x=10,y=10)
## add an entry box
text1=tk.StringVar()
text1.set("")
editbox1=tk.Entry(width=40,textvariable=text1)
editbox1.place(x=100,y=10)
## add a Search button
button1=tk.Button(root, text="Search",width=8,command=SearchButtonClick)
button1.place(x=400,y=10)
## add a Close button
button1=tk.Button(root, text="Close",width=8,command=root.destroy)
button1.place(x=480,y=10)


# Add a Treeview widget
tree = ttk.Treeview(root,column=("c1","c2", "c3","c4"), show='headings')
tree.column("#1", anchor=tk.CENTER,width=10)
tree.heading("#1", text="ID")
tree.column("#2", anchor=tk.CENTER,width=120)
tree.heading("#2", text="Name")
tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Insurance")
tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="PrimaryPhysician")
# add a button trigger for row selection
tree.bind('<ButtonRelease-1>', selectItem)       
tree.place(x=10,y=50,width=730,height=250)
 
# Constructing horizontal scrollbar with treeview
horscrlbar = ttk.Scrollbar(root,orient ="horizontal",command = tree.xview)
# Calling pack method w.r.to horizontal scrollbar
horscrlbar.place(x=10,y=320,width=730)
# Configuring treeview
tree.configure(xscrollcommand = horscrlbar.set)
# Constructing vertical scrollbar with treeview
verscrlbar = ttk.Scrollbar(root,orient ="vertical",command = tree.yview)
# Calling pack method w.r.to horizontal scrollbar
verscrlbar.place(x=760,y=50,height=250)
# Configuring treeview
tree.configure(yscrollcommand = verscrlbar.set)


## add a label
label2=tk.Label(root,text="Name")
label2.place(x=810,y=10)
## add an entry box
text2=tk.StringVar()
text2.set("")
editbox2=tk.Entry(width=40,textvariable=text2)
editbox2.place(x=890,y=10)
## add a label
label2=tk.Label(root,text="Insurance")
label2.place(x=810,y=40)
## add an entry box
text3=tk.StringVar()
text3.set("")
editbox3=tk.Entry(width=40,textvariable=text3)
editbox3.place(x=890,y=40)
## add a label
label4=tk.Label(root,text="P. Physician")
label4.place(x=810,y=60)
## add an entry box
text4=tk.StringVar()
text4.set("")
editbox4=tk.Entry(width=40,textvariable=text4)
editbox4.place(x=890,y=60)
## add a label
label5=tk.Label(root,text="CreditRating")
label5.place(x=810,y=80)
## add an entry box
text5=tk.StringVar()
text5.set("")
editbox5=tk.Entry(width=40,textvariable=text5)
editbox5.place(x=890,y=80)
## add a label
label6=tk.Label(root,text="HomePhone")
label6.place(x=810,y=110)
## add an entry box
text6=tk.StringVar()
text6.set("")
editbox6=tk.Entry(width=40,textvariable=text6)
editbox6.place(x=890,y=110)
## add a label
label7A=tk.Label(root,text="Address")
label7A.place(x=810,y=140)
## add a label
label7=tk.Label(root,text="City")
label7.place(x=810,y=160)
## add an entry box
text7=tk.StringVar()
text7.set("")
editbox7=tk.Entry(width=40,textvariable=text7)
editbox7.place(x=890,y=160)
## add a label
label8=tk.Label(root,text="State")
label8.place(x=810,y=180)
## add an entry box
text8=tk.StringVar()
text8.set("")
editbox8=tk.Entry(width=40,textvariable=text8)
editbox8.place(x=890,y=180)
## add a label
label9=tk.Label(root,text="Zip")
label9.place(x=810,y=200)
## add an entry box
text9=tk.StringVar()
text9.set("")
editbox9=tk.Entry(width=40,textvariable=text9)
editbox9.place(x=890,y=200)
## add a label
label10=tk.Label(root,text="Patient ID")
label10.place(x=810,y=230)
## add an entry box
text10=tk.StringVar()
text10.set("")
#editbox10=tk.Entry(width=40,textvariable=text10, state="readonly")
editbox10=tk.Entry(width=40,textvariable=text10)
editbox10.place(x=890,y=230)

## add a Update button
button1=tk.Button(root, text="Update",width=8,command=UpdateButtonClick)
button1.place(x=810,y=300)
## add a Export button
button1=tk.Button(root, text="Export CSV",width=8,command=ExportButtonClick)
button1.place(x=890,y=300)
## add a Clear button
button1=tk.Button(root, text="Clear",width=8,command=ClearButtonClick)
button1.place(x=970,y=300)
## add a Inesrt button
button1=tk.Button(root, text="Insert",width=8,command=InsertButtonClick)
button1.place(x=1050,y=300)

root.mainloop()


