# Androidn APK Malware detecting using Machine Learning 
cse545-project-1_3-machine_learning

## Course Project's Problem 1's Part -3 : Detecting whether an Android APK is malicious or not using Python scikit. 

**Steps to for development environment:Ubuntu**


**Install Python**
  sudo apt update 
  sudo apt install python3


**Install scikit**
  sudo apt install python3-pip
  pip3 install -U scikit-learn

**
Install JupyterLab**
  pip install jupyterlab


**Download and install Anaconda**
  https://www.anaconda.com/products/distribution#Downloads
  64-Bit (x86) Installer (737 MB)



**Install pandas**
  pip3 install pandas

**APKtool**
  Download from https://ibotpeaches.github.io/Apktool/
  Copy APKTool to /usr/local/bin
  sudo cp apktool.jar /usr/local/bin
  sudo cp apktool /usr/local/bin
  Set execute permission to APKtool
  cd /usr/local/bin
  chmod a+x apktool



**Java**
_  Install_
    sudo apt-get install default-jdk

_
  Uninstall_
    sudo apt-get purge --auto-remove openjdk*


**Install PyCharm**
  sudo snap install pycharm-professional --classic


**Install LibreOffice**
  sudo snap install libreoffice
  
 --------------------------------------------------------------------------------------------<br>
 Extracting APKs
Open folder ‘Modules/APK_Extraction’.
Copy APKs to be extracted to the folder ‘APKs_to_be_extracted’.
Open terminal (in the folder ‘APK_Extraction’) 
Run in Terminal
bash Extract_XML_from_APK


New folder ‘Extracted_XML_Files_of_APKs’ will contain AndroidManifest.xml files of the APKs.


Extracting Permissions from AndroidManifest.xml files
Open folder ‘Modules/XML_to_CSV’.
Copy XML files to folders:
benign
Malware
Run Python file ‘XML_to_CSV-Converter.py’’
4 CSV files will be generated:
Benign-permissions
Benign-permissions_and_receiver
Malware-permissions
Malware-permissions_and_receiver


Permission 
Only contains permissions requested by the APK


Permissions_and_receiver
Contain permissions and broadcast receiving intents.


Generating CSV for ML
Open MS Excel file ‘All_Permissions.xlsx’.
Copy contents of each file to the corresponding sheet in this Excel file.
Permissions_only
Permissions_and_receiver
Ensure to mark the 1st column cell value as ‘benign’ or ‘malware’.
Save Excel file. 


EDIT GREEN Cells only. 


Save the 2 sheets as CSV with following names:
Permissions_only.csv
Permissions_and_receiver.csv


Close main Excel after saving 1 CSV file. 


Remove empty rows at end of CSV files.
Each CSV file has formulas to hold 1500 APK entries/rows.


CSV Format Issue
This is done because ‘Permissions_and_receiver.csv’ shows an error in formatting when training the model.
Take a copy of ‘Permissions_and_receiver.csv’.
Rename copy as ‘Permissions_and_receiver-Original.csv’.
Open ‘Permissions-only.csv’.
CTRL + A.
Open ‘Permissions_and_receiver.csv’
CTRL + A
DEL
Paste on Cell A1 (copied items from Permissions_only.csv).
Copy the first 3 columns from ‘Permissions_and_receiver-Original.csv’.
Paste on Cell A1 of ‘Permissions_and_receiver.csv’
Save the files.
Ensure files are saved in the folder ‘resources’




Making Prediction
Run Python file ‘Android_Malware.py’
It has 4 methods:
Training_models_initialize
    Specify ML training learning models here.


Get_prediction_for_training_data_after_training
Returns a matrix with accuracy score based on training data.


Get_prediction_for_input_after_training
Returns prediction for input. 



