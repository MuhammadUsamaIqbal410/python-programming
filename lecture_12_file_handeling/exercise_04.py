
# Problem No 04: Weriting a python program that copies the file content into 
# another file.


def copied_file(source, copied):
    try:
        with open(source, "r") as file:
            content = file.read()

            
    except Exception as e:
        print(f"Error: {e}")
        

    try: 
        with open(copied, "w") as file:
            file.write(content)

    except Exception as e:
        print(f"Error: {e}")
        return
    
    print("File content has been copied successfully")

copied_file("new_file.txt", "copied_file.txt")

    


    