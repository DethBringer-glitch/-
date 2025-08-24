import time
import threading

.001.left(char='s')(char='e')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()

    def start_clicking(self):

    def stop_clicking(self):


    def exit(self):
        self.stop_clicking()

    def run(self):
        while self.program_run:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)
            time.sleep(0.1)


()(delay, button)
thread.start()


def on_press(key):
    if key:
        if thread.running:
            thread.stop_clicking()
        else:
            thread.start_clicking()
    elif key:
        thread.exit()
        listener.stop()


with as listener:
    listener.join()