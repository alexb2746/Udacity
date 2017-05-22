import webbrowser
import time

count = 0

print("The Program started at: " + time.ctime())

while (count < 3):
    time.sleep(5)
    webbrowser.open("http://youtube.com")
    count = count + 1
