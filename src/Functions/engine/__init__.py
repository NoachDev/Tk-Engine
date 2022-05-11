class Main:
  def __init__(self, master, widget):
    self.widget = widget

  def call_engine(self, project):
    self.project = project
    self.widget.grid(row = 0, column = 0, sticky = "nswe")
