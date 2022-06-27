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


Running the code <by>
----------------------------------------------
To make it simple, I devied my code into three parts <br>
  
#### Step1. Connection setting and testing

![step1py](https://user-images.githubusercontent.com/107917928/175935176-03f64c20-fef3-49ef-b338-2df903dae8e7.png)

#### Step2. Table creating and sample data uploading
  
![step2py](https://user-images.githubusercontent.com/107917928/175935627-a3f561c3-16f8-4a22-b374-93f48bfdbb6f.png)
  
#### Step3. Data query, insert, modify and export

  

