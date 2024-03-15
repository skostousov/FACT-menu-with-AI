import submenus
import queue
import threading
print("commited from clone")
q = queue.Queue()

def worker():
  while True:
    if q.empty():
      pass
    else:
      item = q.get()
      item()
      q.task_done()


threading.Thread(target=worker, daemon=True).start()
menu = submenus.MainMenu(q, "Main Menu")
menu.run()
