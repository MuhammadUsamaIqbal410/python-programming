
# Problem No 04: Weriting a python program that copies the content of two files into 
# another file.


def copied_file(source, source2, merged):
    try:
        with open(source, "r") as file:
            content = file.read()
        with open(source2, "r") as file:
            content2 = file.read()
    except Exception as e:
        print(f"Error: {e}")
        

    try: 
        with open(merged, "w") as file:
            file.write(content)

    except Exception as e:
        print(f"Error: {e}")
        return
    
    try:
        with open(merged, "a") as file:
            file.write(content2)
    except Exception as e:
        print(f"Error: {e}")
        return
    
    print("File content has been copied successfully")

copied_file("new_file.txt", "new_file1.txt", "merged_file.txt")




    


    