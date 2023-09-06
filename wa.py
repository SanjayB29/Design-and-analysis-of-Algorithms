# import time 
# import pywhatkit
# import pyautogui
# from pynput.keyboard import Key, Controller

# keyboard = Controller()


# def send_whatsapp_message(msg: str):
#     try:
#         pywhatkit.sendwhatmsg_instantly(
#             phone_no="+91 7358989333", 
#             message=msg,
#             tab_close=True
#         )
#         time.sleep(3)
#         pyautogui.click()
#         time.sleep(2)
#         keyboard.press(Key.enter)
#         keyboard.release(Key.enter)
#         print("Message sent!")
#     except Exception as e:
#         print(str(e))


# if __name__ == "__main__":
#     send_whatsapp_message(msg="jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")


import time
import pywhatkit
import pyautogui
from pynput.keyboard import Key, Controller
from datetime import datetime, timedelta

keyboard = Controller()


def send_whatsapp_message_at_time(msg: str, phone_number: str, scheduled_time: datetime):
    try:
        # Calculate the time difference from now to the scheduled time
        time_diff = scheduled_time - datetime.now()
        
        # Convert the time difference to seconds
        time_diff_seconds = time_diff.total_seconds()

        # Wait until it's time to send the message
        time.sleep(time_diff_seconds)

        # Send the message using pywhatkit
        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone_number, 
            message=msg,
            tab_close=True
        )
        
        # Wait for the WhatsApp Web page to load
        time.sleep(3)
        
        # Click to focus the message input field
        pyautogui.click()
        
        # Simulate pressing Enter to send the message
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        print("Message sent!")
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    # Define the scheduled time (24-hour format)
    scheduled_time = datetime.now() + timedelta(hours=0.02)  # Schedule for 1 hour from now
    
    # Call the function to send the message at the scheduled time
    send_whatsapp_message_at_time(
        msg="poda punda",
        phone_number="+91 6383425519",
        scheduled_time=scheduled_time
    )