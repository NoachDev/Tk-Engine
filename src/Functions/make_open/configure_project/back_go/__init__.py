import pathlib

class Main:
  def __init__(self, master, widget):
    self.widget                       = widget

    self.widget.nametowidget("back") .config(command = self.widget.master.grid_forget    )
    self.widget.nametowidget("go")   .config(command = lambda : self.create_path(master) )

  def request_info(self, master):
    return {"path": master.call_fuction("project").path, "coords" : master.call_fuction("represetation").text, "name" :  master.call_fuction("project").name}

  def validate_info(self, info):
    if info["path"] != "" and info["name"] != "" and float(info["coords"][6]) > 0 and float(info["coords"][7]) > 0:
      return True
    else:
      return False

  def create_path(self, master):
    info = self.request_info(master)

    if self.validate_info(info) == True:
      info["path"] = pathlib.Path(info["path"]).joinpath(str(info["name"]))
      info["path"].mkdir()

      functions = info["path"].joinpath("Function")
      functions.mkdir()
      functions = functions.joinpath("__main__.py")
      functions.touch()

      with open(functions, "w") as file:
        file.writelines([
          "from tkinter import *\n"       ,
          "import Tk_functions\n\n"       ,
          "class App():\n"                ,
          "\tdef __init__(self):\n"       ,
          "\t\tsuper().__init__()\n"      ,
          "\t\tTk_functions.widgets_config.widgets_load.Modify_widgets(self)\n",
          "\t\tself.mainloop()\n"         ,
          "if __name__ == '__main__':\n"  ,
          "\tApp()\n\n"
        ])

      pages     = info["path"].joinpath("Pages")
      pages.mkdir()
      pages     = pages.joinpath("__init__.wd")
      pages.touch() 

      with open(pages, "w") as file:

        file.writelines([
          "<|\n"                          ,
          "\ttk_name\t:\t__master__\n\n"    ,
          "\t{|\n"                        ,
          "\t\tbg\t:\tgray23\n"             ,
          "\t|}\n\n"                      ,
          "\t[|\n"                        ,
          f"\t\ttitle\t:\t{str(info['name'])}\n" ,
          "\t|]\n\n"                      ,
          "\t(|\n"                        ,
          "\t\tstructure\t:\tmaster : #/__master__/ , r : {" + f"px : {info['coords'][4]} , py : {info['coords'][5]} , sx : {info['coords'][6]} , sy : {info['coords'][7]}" + "}\n",
          "\t|)\n\n"                      ,
          "|>\n\n"
          ])
      
      self.widget.master.master.grid_forget()
      master.call_fuction("engine").call_engine(info["path"])