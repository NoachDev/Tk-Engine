from tkinter import *
import Tk_functions, choose, sys

sys.path.append(".")

import src.Functions.__main__ as Func

class App(Tk):
  def __init__(self, ):
    super().__init__()

    Func.On_open(self)

    Load_Page(self)
    self.mainloop()

if __name__ == "__main__":

  Load_Page = lambda __master__: Tk_functions.widgets_config.widgets_load.Main(__master__)
  
  App()