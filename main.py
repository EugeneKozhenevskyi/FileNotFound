def file_not_found():
    try:
        file = open("name_for_homework.txt", "r")
        read_file = file.read()
        file.close()
        print("File is ready for reading: ", read_file)
    except FileNotFoundError:
        print("Error: No such file exists")


file_not_found()
