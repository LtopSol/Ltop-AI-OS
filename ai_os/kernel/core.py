import threading
import time
from queue import Queue

class Kernel:
    def __init__(self):
        self.processes = {}
        self.memory = {}
        self.event_queue = Queue()
        self.running = False

    def register_process(self, name, func):
        self.processes[name] = func
        print(f"[KERNEL] Агент {name} зарегистрирован.")

    def send_event(self, target, data):
        self.event_queue.put((target, data))

    def run(self):
        self.running = True
        print("[KERNEL] Система запущена.")
        while self.running:
            if not self.event_queue.empty():
                target, data = self.event_queue.get()
                if target in self.processes:
                    threading.Thread(target=self.processes[target], args=(data,)).start()
            time.sleep(0.1)

    def stop(self):
        self.running = False
        print("[KERNEL] Система остановлена.")
