# IRIS-SQLCloud-connect-by-pyodbc-with-UI
IRIS SQLCloud connect by pyodbc with UI<br>

Hello everyone (maybe only me is reading),<br>
<br>
I am sorry to let you know that I am new to Python (and also IRIS) ...<br>
That's is the reason I satrted this mini project<br>
- to connect to IRIS by pyodbc
- to do the basic query by UI
- to learn how to write python (I am sorry I am no a good programmer)
<br>
The interesting thing is I found it is quite easy to write some simple UI by using the tkinter library of python
<br>
<br><br>
In this mini project, it contained two parts<br>
- Deploy a table on the IRIS SQLCloud
  - Run a Create table query
  - Upload a .csv file
- Query the table by the UI wirtten by Python
  - Select 
  - Insert
  - Update
  - Export the selected rows to .csv file
<br><br>
About my code
----------------
In my code, I have written 3 .py file
- Step1_pyobc_configUI
- Step2_pyobc_uploadcsv
- Step3_pyobc_selectpatient
and there is one config file for storing the pyodbc connection configuration
- connetconf
and there is a csv file storing a set for sample patient data
- PatientData
<br><br>
Before running the code
-------------------
1. Python 3.x should be installed (recommended python 3.4-3.7, if you would like to use the irienative library. I found the wheel file for 3.8-3.9 also, but 3.10... sorry may need to wait.)

Step1 <br>
----------------------------------------------
Run the "Step1_pyobc_configUI" to input the parameter and save<br>
<br>
Step2 <br>
----------------------------------------------
Create a table and uloaded the data <br>
You may do it from the IRIS SQLCloud interface <br>
Or you may run the "Step2_pyobc_uploadcsv" to do the upload (howevere , I found some bugs here T__T") <br>
<br>
Step3 <br>
----------------------------------------------
Run the "Step3_pyobc_selectpatient" to have fun ^___^ <br>
