import threading

a = 0  # try with 1 and two afterwards.


def test(x):
    global a
    if a == x:
        print("Hello from thread:", x)


threadOne = threading.Thread(target=test, args=(1,))
threadTwo = threading.Thread(target=test, args=(2,))


threadOne.start()
threadTwo.start()