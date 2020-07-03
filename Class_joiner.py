#Program for Joining Zoom Classes

import webbrowser
import subprocess
import pyautogui
import time
import psutil
import datetime
import socket

def lec_no():
    current_time = datetime.datetime.today().strftime("%H:%M:%S")
    #print(current_time)
    if current_time <= "10:15:00" and current_time >= "09:55:00":
        return 1
    elif current_time <= "10:45:00" and current_time >= "10:30:00":
        return 2
    elif current_time <= "11:20:00" and current_time >= "11:05:00":
        return 3
    elif current_time <= "11:55:00" and current_time >= "11:40:00":
        return 4
    elif current_time <= "12:35:00" and current_time >= "12:15:00":
        return 5
    else:
        return "Timming is not correct"

def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                process_handles=proc.num_handles()
                if process_handles >900:
                    if process_handles >=1150:
                        return True
                    elif process_handles <= 1150 and process_handles >=980:
                        proc.terminate()
                        return False
                    else:
                        return False
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False
def run_again():
    print("\n\nDo You want to run this script again: ")
    print("Press Y for yes and N for No")
    response=input()
    if response.lower()=="y":
        join_in_class()
    print("\n.\n.\nClass joined")
    input()
    quit()
def join_in_class():  
    days = {"Monday" : {2 : ["OS","3753284740" , "12345"], 3 : ["Maths","7888484402","343927"], 4 : ["SE","859-964-4525","813135"], 5 : ["OT","9520868049","754986"]},
    "Tuesday" : {1 : ["Maths","7888484402","343927"], 2 : ["SE","859-964-4525","813135"], 3 : ["OT","9520868049","754986"], 5 : ["OS","3753284740" , "12345"]},
    "Wednesday" : {1 : ["SE","8599644525","813135"], 2 : ["OT","9520868049","754986"], 3 : ["OS","3753284740" , "12345"], 5 : ["Maths","7888484402","343927"]},
    "Thursday": {1 : ["Maths","7888484402","343927"], 2 : ["SE","859-964-4525","813135"], 3 : ["OT","9520868049","754986"], 4 : ["OS","3753284740" , "12345"]},
    "Friday" : {2 : ["Maths","7888484402","343927"], 3 : ["SE","859-964-4525","813135"], 4 : ["OT","9520868049","754986"], 5 : ["OS","3753284740" , "12345"]}}
#    print(days.keys())
    day=datetime.datetime.today().strftime("%A")


    while is_connected()==False:
        print("wating for internet access.....")
        time.sleep(2)
    lec=lec_no()
    if lec=="Timming is not correct":
        print(lec)
        input()
        quit()
    elif lec in days[day].keys():
        print("We are about to join a class so, please stop whatever u were doing and let the script do its work")
        time.sleep(5)
        while checkIfProcessRunning('zoom'):
            print("waiting for class get over")
            print(".......")
            time.sleep(9)
        print("\n.\n.\n.\n.\n.\nNow we'll join into next class")
        pyautogui.hotkey("win","d")
        # if len(days[day][lec]) == 1:
        #     print("Its",days[day][lec][0],"class and you are about to join in")
        #     website = "https://classroom.google.com/u/1/c/MTY1NzU0ODA1ODFa"
        #     webbrowser.open_new(website)
        #     time.sleep(3)
        #     pyautogui.click(1716,296)
        #     time.sleep(12)
        #     pyautogui.hotkey("ctrl","f")
        #     time.sleep(2)
        #     pyautogui.typewrite("https://us04web.zoom.us/j/")
        #     pyautogui.typewrite(["esc"])
        #     pyautogui.typewrite(["enter"])
        #     time.sleep(6)
        #     pyautogui.typewrite(["left"])
        #     pyautogui.typewrite(["enter"])
        #     pyautogui.hotkey("ctrl","w")
        #     time.sleep(1)
        #     pyautogui.hotkey("ctrl","w")
        #     run_again()
        print("Its",days[day][lec][0],"class and you are about to join in")
        subprocess.Popen([r'C:\Users\akash\AppData\Roaming\Zoom\bin\Zoom.exe'])
        time.sleep(4)
        pyautogui.hotkey("shift","tab")
        pyautogui.typewrite(["tab"])
        pyautogui.typewrite(["enter"])
        time.sleep(6)
        pyautogui.typewrite(days[day][lec][1])
        pyautogui.typewrite(["enter"])
        time.sleep(6)
        if len(days[day][lec])>2:
            pyautogui.typewrite(days[day][lec][2])
            pyautogui.typewrite(["enter"])
        run_again()
    else:
        print("Its a CG lecture")
        input()
join_in_class()