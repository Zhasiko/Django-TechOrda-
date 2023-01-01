import os
import sys

path = "C:/"
while True:
    command = input(f"{path}"+'>')
    list_of_ls = os.listdir(path)
    if command == "ls":
        for i in list_of_ls:
            print(i)
    elif command == "cd ..":
        list_of_path = path.split("/")
        path = ""
        if path != "C:/":
            list_of_path.remove(list_of_path[-2])
            list_of_path.remove(list_of_path[-1])
            for i in list_of_path:
                path += f"{i}/"
    elif command.startswith("cd"):
        a = command.split()
        if not a[1] in list_of_ls:
            print('No such directory')
        else:
            path += f"{a[1]}/"

#Creating dir and file
    elif command.startswith("mkdir"):
        a = command.split()
        os.mkdir(path+a[1])

    elif command.startswith("mkfile"):
        a = command.split()
        f = open(path+a[1], "x")

#Renaming directory or file
    elif command.startswith("rename"):
        a = command.split()
        os.rename(path+a[1], path+a[2])

#Removing dir or file
    elif command.startswith("remove"):
        a = command.split()
        try:
            os.rmdir(path+a[1])
        except:
            os.remove(path+a[1])

    elif command.startswith("open"):
        a = command.split()
        f = open(path+a[1])
        for line in f:
            print(line)
        f.close()

    elif command == "quit":
        sys.exit(0)
