from kernel.core import Kernel
from kernel.memory import Memory
from agents.echo import echo_agent
from agents.memory_agent import memory_agent
import threading
import time

if __name__ == "__main__":
    memory = Memory()
    kernel = Kernel()

    kernel.register_process("echo", echo_agent)
    kernel.register_process("memory", lambda data: memory_agent((memory, *data)))

    threading.Thread(target=kernel.run, daemon=True).start()

    kernel.send_event("echo", "Hello in AI-OS!")
    kernel.send_event("memory", ("goal", "Set"))
    kernel.send_event("echo", f"В памяти: {memory.all()}")

    time.sleep(2)
    kernel.stop()
