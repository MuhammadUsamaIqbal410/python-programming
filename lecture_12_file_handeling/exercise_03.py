
# Problem No 03: Writing apython program that reads the content of the file,
# reverse the content and save it another file

def reverse_file_content(new_file, another_file):
    
    try:
        with open(new_file, "r")as file:
            cont = file.read()
        reversed_cont = cont[::-1]

    except Exception as e:
        print(f"Error: {e}")
        return


    try:
        with open(another_file, "w")as file:
            file.write(reversed_cont)

    except Exception as e:
        print(f"Error: {e}")
        return

    print("content has been reversed and written successfully")

reverse_file_content("new_file.txt", "another_file.txt")
