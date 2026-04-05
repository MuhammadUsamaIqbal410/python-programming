
# Problem No 06: Create a logging system where every time the program runs,
# it appends a new log entry with a timestamp into a log file.

import datetime

def Log_entry(Log_file,log_message):
    try:    
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(Log_file, "a") as file:
            file.write(f"\n{log_message} [{current_time}]")
            print(f"Log entery {log_message} and timestamp {current_time} has"\
                " been added successfully")

    except Exception as e:
        print(f"Error: {e}")
        return
    
Log_entry("new_file.txt", "A new meassage has been added to the file")


    
