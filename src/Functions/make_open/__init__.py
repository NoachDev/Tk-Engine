import __main__, pathlib

class Main:
  def __init__(self, master, widget):
    widget.nametowidget("open_project").config(command = lambda: self.call_engine(widget, master))

  def call_engine(self, widget, master):
    self.path = pathlib.Path(__main__.filedialog.askdirectory())
    widget.grid_forget()
    master.call_fuction("engine").call_engine(self.path)
    

