import submenus
import queue
import threading

q = queue.Queue()

print("hello")
def worker():
  while True:
    if q.empty():
      pass
    else:
      item = q.get()
      item()
      q.task_done()


threading.Thread(target=worker, daemon=True).start()
menu = submenus.MainMenu(q, "main menu")
menu.run()
