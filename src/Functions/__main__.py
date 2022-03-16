import pathlib, json

class On_open:
  def __init__(self, __master__):
    import __main__

    self.json_file_configure = pathlib.Path(__file__).parents[1].joinpath("config.json")

    with open(self.json_file_configure, "r") as file:
      self.json_file_data    = json.load(file) 
    
    self.project = self.json_file_data["project"]

    if self.project == None:
      vars(__main__)["choose"].Init_open(__master__)