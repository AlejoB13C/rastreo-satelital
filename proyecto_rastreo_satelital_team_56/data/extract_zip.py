import csv
import pathlib
from subprocess import call
from zipfile import ZipFile


def check_done(dones_file, data_name):
    """check if a file has been already processed

    if the file was processed, returns true to continue with the next file

    Args:
        dones_file (str): path to the file containing the extracted xlsx
        data_name (str): name of the file to be checked

    Returns:
        bool: if true avoids the file, else continue processing the xlsx to csv
    """
    with open(dones_file, "r+") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        
        if data_name in lines:
            print("Already done")
            return True
        
        file.write(data_name+"\n")
        
        return False


def csv_convert(data):
    data_name = data.filename
    if check_done("./done.txt", data_name):
        return
    
    zip.extract(data, DATA_RAW.as_posix())
            
    data_file = DATA_RAW.as_posix()+"/"+data_name # Extracted file path and name
    
    new_path = DATA_CSV.joinpath(*data_name.rstrip(".xlsx").split("/")) # Create the path for the sheets
    
    if not new_path.exists():
        new_path.mkdir(parents=True)
    
    call(["xlsx2csv", data_file, new_path.as_posix().replace(" ","_")+"/", "-a"])


    pathlib.Path(data_file).unlink()
    pathlib.Path(data_file.rsplit("/",1)[0]).rmdir()


def zip_iter(ZIP_FILE):
    with ZipFile(ZIP_FILE, "r") as zip:
        total_files = len(zip.namelist()) # Total files in the zip
        done_files = 1
        
        for data in zip.infolist():
            
            csv_convert(data)
            print(f"{done_files}/{total_files} working on: {data_name}")
            done_files += 1
            
            
            data_name = data.filename
            if check_done("./done.txt", data_name):
                continue
            zip.extract(data, DATA_RAW.as_posix())
                    
            data_file = DATA_RAW.as_posix()+"/"+data_name # Extracted file path and name
            
            new_path = DATA_CSV.joinpath(*data_name.rstrip(".xlsx").split("/")) # Create the path for the sheets
            if not new_path.exists():
                new_path.mkdir(parents=True)
            
            call(["xlsx2csv", data_file, new_path.as_posix().replace(" ","_")+"/", "-a"])

            
            pathlib.Path(data_file).unlink()
            pathlib.Path(data_file.rsplit("/",1)[0]).rmdir()


if __name__ == "__main__":
    
    CURRENT_DIR = pathlib.Path().resolve()
    DATA_RAW = CURRENT_DIR.parent.joinpath("data", "raw", "Historico Informes FTS Vehiculos 2021-2022") # Path where the zip is located
    DATA_CSV = CURRENT_DIR.parent.joinpath("data", "interm") # Destination Path
    ZIP_FILE = DATA_RAW.as_posix()+".zip" # Zip file name
    DOT_ENV = CURRENT_DIR.as_posix()+"/.env"