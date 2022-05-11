import pathlib, __main__

class Main:
  def __init__(self, master, widget):
    self.wid_path   = widget.nametowidget("path")
    self.wid_search = widget.nametowidget("search")
    self.wid_name   = widget.nametowidget("name")

    self.name       = ""
    self.path       = ""

    self.wid_path.bind("<Key-slash>", self.verify_path)
    self.wid_path.bind("<Key-backslash>", self.verify_path)

    self.wid_name.bind("<Key>", self.name_project)

    self.wid_search.config(command = self.search_path)

  def name_project(self, Event):
    self.name = self.wid_name.get() + Event.char

  def verify_path(self, Event):
    text = self.wid_path.get() + Event.char

    if not "/" in text[0] and not "\\" in text[2]:
      self.path = pathlib.Path(str(pathlib.Path(__main__.__file__).parent) + Event.char + text)
    else:
      self.path = pathlib.Path(text)

    if not self.path.is_dir():
      for i in [a for a in range(max(0, text[:-1].rfind(Event.char)), len(text))][::-1]:
        self.wid_path.delete(i)

  def search_path(self):
    self.path = __main__.filedialog.askdirectory()
    
    for i in self.wid_path.get():
      self.wid_path.delete(0)
    
    self.wid_path.insert(0, self.path)