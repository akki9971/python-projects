print("\n[+] there are two options:  addition of data and retrieve previous data ")         # user manual
choice = int(input("press  0 to add  or    1 to view your data: "))
print("\n[+] there are three persons avalable:  'akki', 'harry', 'sumer'   but you can create your own")     # user manual
person = input("type name of person: ")

def crnt_date_time():         # function to get curent date and time
    from datetime import datetime
    return datetime.now()

def view_data(name, filetype):  # handy function to get available data
    try:
        with open(f"data_logs/{name}.{filetype}.txt".format(name, filetype), "r+") as f:
            x = f.read()
            if len(x)!=0:
                print(x)
            else:
                print(f"[-] please add some {filetype} data to view".format(filetype))
    except:
        with open(f"data_logs/{name}.{filetype}.txt".format(name, filetype), "a") as f:
            f.write("")

def add_data(name, filetype):   # handy function to add data  { name:  'person name' ,  filetype:  'choice for food and exercise'}
    data = input(f"enter your {filetype} to add: ".format(filetype))
    with open(f"data_logs/{name}.{filetype}.txt".format(name, filetype), "a") as file:
        file.write(f"{crnt_date_time().date()} {crnt_date_time().hour}:{crnt_date_time().minute}  ->  {data}\n".format(crnt_date_time(), data))
        print(f"😊  your {filetype} added successfully".format(filetype))


if choice:                      # this is to view available data
    print("[+] what you want to see ? 'food' or 'exercise'  ")      # user manual
    file_choice = int(input("press  0 for 'exercise'   and 1 for 'food':  "))
    if file_choice:
        view_data(person, "diet")
    else:
        view_data(person, "exercise")
else:                           # this is to add data
    print("[+] what you want to add 'food' or 'exercise'  ")        # user manual
    addition_choice = int(input("press 0 for 'exercise'   and   1 for 'food' :  "))
    if addition_choice:
        add_data(person, "diet")
    else:
        add_data(person, "exercise")