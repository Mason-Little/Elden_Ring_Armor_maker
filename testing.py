from alive_progress import alive_bar
import time

with alive_bar(1000, force_tty=True) as bar:
    for i in range(1000):
        time.sleep(.00001)
        if i and i % 300 == 0:
            print('cool!')
        bar()
