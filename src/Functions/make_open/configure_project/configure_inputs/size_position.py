from functools import partial

class Main:
	def __init__(self, master, widget):
		self.master 				= master
		self.wid_children 	= widget.winfo_children()

		# ['width_height', 'box_size_w', 'box_size_h', 'ent_size_w', 'ent_size_h', 'place_x_y', 'box_place_x', 'box_place_y', 'ent_place_x', 'ent_place_y']
		self.name_children 	= [a.winfo_name() for a in self.wid_children]
		self.connect				= {}

		for e, b in zip([a for a in self.name_children if "ent_" in a], [a for a in self.name_children if "box_" in a]):
			btn = self.wid_children[self.name_children.index(b)]
			ent = self.wid_children[self.name_children.index(e)]

			self.connect[e] = {"type" : e[e.rfind("_"):].replace("_", "a"), "val" : 0}
			
			btn.configure(command = partial(self.rel_abs, btn, ent, e))
			ent.configure(validate = "key", validatecommand = (ent.register(self.numbers_int),'%S'))

			for i in [a for a in range(0, 9)] + ["Return", "BackSpace"]:
				ent.bind(f"<Key-{i}>", partial(self.update, ent, e))

	def update(self, wid, name, Event):
		tx 	= wid.get().replace("\r", "")
		
		if Event.keycode == 22:
			wid.delete(len(tx))
			tx = tx[:-1]
			
		else:
			tx 	+= Event.char

		if len(tx) >= 1:
			self.connect[name]["val"] = tx

			self.master.call_fuction("represetation").define(self.connect)
			
	def rel_abs(self, b, e, n):

		if "a" in b.cget("text"):
			t = b.cget("text").replace("a", "r")
			self.connect[n]["type"] = t
			
			b.config(text = t)
			e.config(validatecommand = (e.register(self.numbers_float),'%S'))

		else:
			t = b.cget("text").replace("r", "a")
			self.connect[n]["type"] = t

			e.config(validatecommand = (e.register(self.numbers_int),'%S'))
			b.config(text = t)

	def numbers_int(self, Event):
		if str(Event).isdigit():
			return True

		else:
			return False
	
	def numbers_float(self, Event):
		if str(Event).isdigit() or "." in str(Event):
			return True
		
		else:
			return False