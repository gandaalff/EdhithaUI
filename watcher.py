from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import time
import threading
import main_window as mw


class MyHandler(PatternMatchingEventHandler):
    patterns = ["*.JPG", "*.JPEG"]

    def process(self, event):
        import main_window
        print(event.src_path)
        name = event.src_path.split('\\')[::-1]
        print("image added is : ",name[0])
        main_window.image_list.append(name[0])

    def on_created(self, event):
        self.process(event)


def start_observe(path):

    observer = Observer()
    observer.schedule(MyHandler(), path=path)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

'''
def start():
    try:
        threading._start_new_thread(start_observe(mw.PATH),)
    except:
        print("Error in starting thread")
'''