import os

def rename_files():
    #(1) get file names from a floder
    # r stands for rawpack, and it tells Python, take this string as it is, and don't interprrt it any other way
    file_list = os.listdir(r"..\\resource\Sec")
    #get current working directory
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    #change working directory
    os.chdir(r"..\\resource\Sec")
    #(2) for each file, rename file
    for file_name in file_list:
        print("change "+file_name+" to "+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    print("finished")
    os.chdir(saved_path)
rename_files()
