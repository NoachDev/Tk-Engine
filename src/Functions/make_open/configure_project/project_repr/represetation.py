import threading

class Main:
  def __init__(self, master, widget):
    self.canvas     = widget.nametowidget("canvas")
    self.info_screen= list(set(master.call_fuction("structure")().get_info(r = {"px" : 100 , "py" : 100 , "sx" : 100 , "sy" : 100 }).values()))

    threading.Thread(target=self.config).start()
  
  def config(self):
    try:
      
      self.canvas.wait_visibility()

      self.x      = self.canvas.winfo_x()
      self.y      = self.canvas.winfo_y()

      self.w      = self.canvas.winfo_width()
      self.h      = self.canvas.winfo_height()


      self.width  = 600
      self.height = 20
      self.sp     = 10

      self.color  = "white"
      
      self.text = [0,0,0,0,0,0,0,0]
                                                            # (====================================) size(self.width. self.height)
      
      self.canvas.create_oval              (self.w/2-self.width/2-self.height/2    , 0, self.w/2-self.width/2+self.height/2  , self.height, fill = self.color, outline = self.color)
      self.canvas.create_oval              (self.w/2+self.width/2-self.height/2    , 0, self.w/2+self.width/2+self.height/2  , self.height, fill = self.color, outline = self.color)
      self.canvas.create_rectangle         (self.w/2-self.width/2                  , 0, self.w/2+self.width/2                , self.height, fill = self.color, outline = self.color)
      
                                                    # ax : 0 ay : 0 aw : 0 ah : 0 | rx : 0 ry : 0 rw : 0 rh : 0
      self.p      = self.canvas.create_text(self.w/2                      , self.height/2 , text = "|"              , anchor = "center" , tag = "|")

      self.ax     = self.canvas.create_text(self.canvas.bbox(self.p) [0] - self.sp , self.height/2 , text = f"ax : {self.text[0]}", anchor = "e"      , tag = "ax")
      self.ay     = self.canvas.create_text(self.canvas.bbox(self.ax)[0] - self.sp , self.height/2 , text = f"ay : {self.text[1]}", anchor = "e"      , tag = "ay")
      self.aw     = self.canvas.create_text(self.canvas.bbox(self.ay)[0] - self.sp , self.height/2 , text = f"aw : {self.text[2]}", anchor = "e"      , tag = "aw")
      self.ah     = self.canvas.create_text(self.canvas.bbox(self.aw)[0] - self.sp , self.height/2 , text = f"ah : {self.text[3]}", anchor = "e"      , tag = "ah")

      self.rx     = self.canvas.create_text(self.canvas.bbox(self.p) [2] + self.sp , self.height/2 , text = f"rx : {self.text[4]}", anchor = "w"      , tag = "rx")
      self.ry     = self.canvas.create_text(self.canvas.bbox(self.rx)[2] + self.sp , self.height/2 , text = f"ry : {self.text[5]}", anchor = "w"      , tag = "ry")
      self.rw     = self.canvas.create_text(self.canvas.bbox(self.ry)[2] + self.sp , self.height/2 , text = f"rw : {self.text[6]}", anchor = "w"      , tag = "rw")
      self.rh     = self.canvas.create_text(self.canvas.bbox(self.rw)[2] + self.sp , self.height/2 , text = f"rh : {self.text[7]}", anchor = "w"      , tag = "rh")

      self.rt     = self.canvas.create_rectangle(0, 0, 0, 0 , fill = "white"            )
      self.ln     = self.canvas.create_line     (0, 0, 0, 0 , fill = "black"            )
      self.lx     = self.canvas.create_text     (0, 0       , text = "X", anchor = "e"  )
      self.lm     = self.canvas.create_line     (0, 0, 0, 0 , fill = "black"            )

    except:
      pass

  def define(self, connect):
    tx = [0,0,0,0,0,0,0,0]

    for i in connect.values():
      
      k = i.get("type")
      v = i.get("val")

      if "x" in k:
        lv = 0
        m = self.info_screen[0]
      
      elif "y" in k:
        lv = 1
        m = self.info_screen[1]

      elif "w" in k:
        lv = 2
        m = self.info_screen[0]
      else:
        lv = 3
        m = self.info_screen[-1]

      if "a" in k:

        tx[lv]    = v
        tx[lv+4] = f"{float(v)/m*100:.2f}"

      else:
        tx[lv]    = int(float(v)*m/100)
        tx[lv+4]  = v

    self.text = tx
    
    self.canvas.itemconfigure("5" ,text = f"ax : {self.text[0]}")
    self.canvas.itemconfigure("6" ,text = f"ay : {self.text[1]}")
    self.canvas.itemconfigure("7" ,text = f"aw : {self.text[2]}")
    self.canvas.itemconfigure("8" ,text = f"ah : {self.text[3]}")

    self.canvas.itemconfigure("9" ,text = f"rx : {self.text[4]}")
    self.canvas.itemconfigure("10",text = f"ry : {self.text[5]}")
    self.canvas.itemconfigure("11",text = f"rw : {self.text[6]}")
    self.canvas.itemconfigure("12",text = f"rh : {self.text[7]}")

    self.resize(self.text[4:])
    
  def resize(self, cord):

    self.canvas.coords("5" , self.canvas.bbox(self.p) [0] - self.sp , self.height/2)
    self.canvas.coords("6" , self.canvas.bbox(self.ax)[0] - self.sp , self.height/2)
    self.canvas.coords("7" , self.canvas.bbox(self.ay)[0] - self.sp , self.height/2)
    self.canvas.coords("8" , self.canvas.bbox(self.aw)[0] - self.sp , self.height/2)
    
    self.canvas.coords("9" , self.canvas.bbox(self.p) [2] + self.sp , self.height/2)
    self.canvas.coords("10", self.canvas.bbox(self.rx)[2] + self.sp , self.height/2)
    self.canvas.coords("11", self.canvas.bbox(self.ry)[2] + self.sp , self.height/2)
    self.canvas.coords("12", self.canvas.bbox(self.rw)[2] + self.sp , self.height/2)


    self.width = (self.canvas.bbox(self.rh)[2] - self.canvas.bbox(self.ah)[0]) * 1.2
    
    self.canvas.coords("1", self.w/2-self.width/2-self.height/2    , 0, self.w/2-self.width/2+self.height/2  , self.height)
    self.canvas.coords("2", self.w/2+self.width/2-self.height/2    , 0, self.w/2+self.width/2+self.height/2  , self.height)
    self.canvas.coords("3", self.w/2-self.width/2                  , 0, self.w/2+self.width/2                , self.height)

    # self.rt     = self.canvas.create_rectangle(20                             , 25, self.w-20                         , self.h-20 , fill = "white")
    # self.ln     = self.canvas.create_line     (20                             , 45, self.w-20                         , 45        , fill = "black")
    # self.lx     = self.canvas.create_text     (self.w-20 - 5                  , 35, text = "X"                        ,             anchor = "e"  )
    # self.lm     = self.canvas.create_line     (self.canvas.bbox(self.lx)[0]-5 , 35, self.canvas.bbox(self.lx)[0] - 15 , 35        , fill = "black")
    
    cord[0] = float(cord[0])*self.w/100
    cord[1] = 25 + float(cord[1])*(self.h-25)/100
    cord[2] = float(cord[2])*self.w/100 + cord[0]
    cord[3] = 25 + float(cord[3])*(self.h-25)/100 + cord[1] - 25

    self.canvas.coords(self.rt, *cord)
    self.canvas.coords(self.ln, cord[0], cord[1]+20, cord[2], cord[1]+20)
    self.canvas.coords(self.lx, cord[2]-5, cord[1]+10)
    self.canvas.coords(self.lm, self.canvas.bbox(self.lx)[0]-5 , cord[1]+10, self.canvas.bbox(self.lx)[0] - 15 , cord[1]+10)