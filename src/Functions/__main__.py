from tkinter import filedialog
from tkinter import *
import Tk_functions

class App(Tk):
  def __init__(self):
    super().__init__()

    Tk_functions.widgets_config.widgets_load.Modify_widgets(self)

    self.mainloop()

if __name__ == "__main__":
  App()