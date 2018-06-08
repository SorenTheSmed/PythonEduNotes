import threading
import time


def worker():
    time.sleep(5)
    print("I am a Thread, I want to sleep NOW!")
    time.sleep(5)
    print("Oh my, oh my, I just woke up.")


my_thread = threading.Thread(target=worker)

my_thread.start()
print("hello")
