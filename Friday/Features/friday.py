from bardapi import BardCookies
import datetime
import pyttsx3

#add text-to-speech initialization
friday = pyttsx3.init()

#cookies updation
import pyperclip
import pyautogui
import webbrowser
from time import sleep
import json
import keyboard

def CookieScrapper():
    webbrowser.open("https://bard.google.com")
    sleep(4)
    pyautogui.click(x=1739, y=79)
    sleep(1)
    pyautogui.click(x=1509, y=284)
    sleep(2)
    pyautogui.click(x=1404, y=109)
    sleep(1)
    pyautogui.click(x=1778, y=0)
    sleep(1)
    keyboard.press_and_release('ctrl + w')

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        pass

    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")

    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    SIDValue = next((item for item in json_data if item["name"] == SID), None)
    TSValue = next((item for item in json_data if item["name"] == TS), None)
    CCValue = next((item for item in json_data if item["name"] == CC), None)

    if SIDValue is not None:
        SIDValue = SIDValue["value"]
    else:
        print(f"{SIDValue} not found in the JSON data.")

    if TSValue is not None:
        TSValue = TSValue["value"]
    else:
        print(f"{TSValue} not found in the JSON data.")

    if CCValue is not None:
        CCValue = CCValue["value"]
    else:
        print(f"{CCValue} not found in the JSON data.")

    cookie_dict = {
        "__Secure-1PSID": SIDValue ,
        "__Secure-1PSIDTS": TSValue,
        "__Secure-1PSIDCC": CCValue,
    }

    return cookie_dict

cookie_dict = CookieScrapper()

bard = BardCookies(cookie_dict=cookie_dict)


# Text Modification Function -
def split_and_save_paragraphs(data, filename):
    paragraphs = data.split('\n\n')
    with open(filename, 'w') as file:
        file.write(data)
    data = paragraphs[:2]
    separator = ', '
    joined_string = separator.join(data)
    return joined_string

print("\nHi! How can I help you today?")

# Get the user's choice
while True:
    choice = input("\n1.Chat\n2.Image detection\n3.Youtube Search\n4.Exit the Program\nEnter your choice: ")

    # Use an if-else statement to make a decision
    if choice == "1":

        # Chatbot
        Question = input("\nEnter The Query : ")
        RealQuestion = str(Question)
        results = bard.get_answer(RealQuestion)['content']
        current_datetime = datetime.datetime.now()
        formatted_time = current_datetime.strftime("%H%M%S")
        filenamedate = str(formatted_time) + str(".txt")
        filenamedate = "Brain\\DataBase\\" + filenamedate
        print(split_and_save_paragraphs("\n" + results, filename=filenamedate))
        friday.say(split_and_save_paragraphs("\n" + results, filename=filenamedate))
        friday.runAndWait()
            

    elif choice == "2":

        # Image Detection
        imagename = str(input("\nEnter The Image Name : "))
        image = open(imagename,'rb').read()
        bard = BardCookies(cookie_dict=cookie_dict)
        results = bard.ask_about_image('what is in the image?',image=image)['content']
        current_datetime = datetime.datetime.now()
        formatted_time = current_datetime.strftime("%H%M%S")
        filenamedate = str(formatted_time) + str(".txt")
        filenamedate = "Brain\\DataBase\\" + filenamedate
        print(split_and_save_paragraphs("\n" + results, filename=filenamedate))
        friday.say(split_and_save_paragraphs("\n" + results, filename=filenamedate))
        friday.runAndWait()

    elif choice == "3":
        query = str(input("\nEnter the topic : "))
        webbrowser.open("https://www.youtube.com/results?search_query=" + query)


    elif choice == "4":
        print("Thank you, Goodbye!")
        friday.say("Thank you, Goodbye!")
        friday.runAndWait()
        break
        
    else:
        print("Invalid choice.")