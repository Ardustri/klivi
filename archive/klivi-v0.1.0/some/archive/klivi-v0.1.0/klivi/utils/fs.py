import os

def write_file(filename, content, mode="w"):
    file = open(filename, mode)
    file.write(content)
    file.close()
    return file


def read_file(filename, mode="r"):
    file = open(filename, mode)
    file_content = file.read()
    file.close()
    return file_content


def exist(name):
    if os.path.exists(name):
        return True
    else:
        return False


def mkdir(folder_name):
    if exist(folder_name):
        print("The folder is already exist")
    else:
        os.mkdir(folder_name)


def rmdir(folder_name):
    if exist(folder_name):
        os.rmdir(folder_name)
    else:
        print("The folder does not exist")
