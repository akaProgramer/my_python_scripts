#Program for performing specific tasks on startup of System

import webbrowser
import os
import datetime
import socket
import time


day = datetime.datetime.today().strftime("%A")
current_time = datetime.datetime.today().strftime("%H:%M:%S")

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

while is_connected()==False:
        print("waiting for internet access.....")
        time.sleep(2)

def time_table_generator():
    buffer=[]
    i=False
    fopen=open("time_table.txt","r")
    lines=fopen.readlines()
    for line in lines:
        if line.startswith(day):
            i=True
        if i==True:
            buffer.append(line)
            if line.startswith("5."):
                i=False
    f2open=open("Today's_time_table.txt","w")
    f2open.writelines(buffer)
    fopen.close()
    f2open.close()
    os.system("Today's_time_table.txt")


def tasks_to_do():
    # website_1 = "www.google.com"
    # webbrowser.open_new(website_1)
    if (day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday") and (current_time <= "23:30:00" and current_time >= "09:30:00"):
        website_2="https://web.whatsapp.com/"
        webbrowser.open_new_tab(website_2)
        website_3 = "https://classroom.google.com/u/1/c/MTY1NzU0ODA1ODFa"
        webbrowser.open_new_tab(website_3)
        time_table_generator()
    else:
        print("Timming is not correct")
        input()
tasks_to_do()



