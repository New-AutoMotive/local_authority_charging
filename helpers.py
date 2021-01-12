#import packages necessary for functions
import os

# Function to check for data folder and create if not there
def data_folder():
    print("Data checker will look for the data folder. If none is found then it will create it.")
    if os.path.basename(os.getcwd()) == 'local_authority_charging':
        dirname = 'Data'
        if not os.path.isdir(dirname):
            try:
                os.mkdir(dirname)
            except OSError:
                print("Creation of the Directory %s failed" % dirname)
        else:
            print("Successfully created the directory %s " % dirname)
    else:
        print("Directory %s already exists" % dirname)
    
#function to check for presence of particular dataset or other file
def data_checker(file_name):
    dirname = 'Data'
    data_folder_path = os.path.join(os.getcwd(), dirname)
    if file_name not in os.listdir(data_folder_path):
        print('Data not already in folder')
        return False
    else:
        print('Data has already been downloaded')
        return True
    