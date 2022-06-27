# IRIS-SQLCloud-connect-by-pyodbc-with-UI
IRIS SQLCloud connect by pyodbc with UI<br>

#### Hello everyone (maybe only me is reading),<br>

I am sorry to let you know that I am new to Python (and also IRIS) ...<br>
That's is the reason I satrted this mini project<br>
- to connect to IRIS by pyodbc
- to do the basic query by UI
- to learn how to write python (I am sorry I am no a good programmer)

The interesting thing is I found it is quite easy to write some simple UI by using the tkinter library of python <br>
<br>

#### In this mini project, it contained two parts <br>

- Deploy a table on the IRIS SQLCloud
  - Run a Create table query
  - Upload a .csv file
- Query the table by the UI wirtten by Python
  - Select 
  - Insert
  - Update
  - Export the selected rows to .csv file
<br>

About my code <br>
----------------------------------------------
In my code, I have written 3 .py file
- Step1_pyobc_configUI
- Step2_pyobc_uploadcsv
- Step3_pyobc_selectpatient

and there is one config file for storing the pyodbc connection configuration
- connetconf

and there is a csv file storing a set for sample patient data
- PatientData

<br>

Before running the code <br>
----------------------------------------------
1. Python 3.x should be installed (recommended python 3.4-3.7, if you would like to use the irienative library. I found the wheel file for 3.8-3.9 also, but 3.10... sorry may need to wait.)<
2. The following libraries are used, please include them by (py -m pip install )
  - import tkinter
  - import pyodbc
  - import ast
<br>

Running the code <by>
----------------------------------------------
To make it simple, I devied my code into three parts <br>
   
#### Step0. Deploy a cloud and get the connection information

![step0deployacloud](https://user-images.githubusercontent.com/107917928/175937086-2dc1b045-005e-40db-a42b-8793b7cee797.png)
  
#### Step1. Connection setting and testing

1. Input the connection information and click the save button to save the configuration <br>
2. You may click the Test Connection button to test the connection<br>

<br>

![step1py](https://user-images.githubusercontent.com/107917928/175937897-d6d69b6f-db77-4814-a9dd-63ce0d8fafdb.png)

#### Step2. Table creating and sample data uploading
 
1. Input the Name of the table you are going to create 
2. Click the Open button to import a .csv file
3. A Create table script will be generated, you may modify it before clicking the Create Table button to create
4. Click the Create Table button to create a table
5. Click the Upload Data button to upload data
  
<br>  
  
![step2py](https://user-images.githubusercontent.com/107917928/175935627-a3f561c3-16f8-4a22-b374-93f48bfdbb6f.png)
  
#### Step3. Data query, insert, modify and export

  

