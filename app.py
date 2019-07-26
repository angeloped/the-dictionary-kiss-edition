import json
try:
	import Tkinter as tk
	import ttk
except ImportError:  # Python 3
	import tkinter as tk
	import tkinter.ttk

class DICTIONARY:
	def __init__(self, top=None):
		'''This class configures and populates the toplevel window.
		top is the toplevel containing window.'''
		top.title("The Dictionary (KISS Edition)")
		top.resizable(False, False)
		top.attributes('-topmost',True)
		top.bind("<Escape>",lambda e:top.destroy())
		
		# Gets both half the screen width/height and window width/height
		x,y = 320,370
		positionRight = int(top.winfo_screenwidth()/2 - x/2)
		positionDown = int(top.winfo_screenheight()/2 - y/2)
		# Positions the window in the center of the page.
		top.geometry("{0}x{1}+{2}+{3}".format(x, y, positionRight, positionDown))
		
		# frames
		Frame1 = ttk.Frame(top)
		Frame1.pack(fill="both")
		Frame2 = ttk.Frame(top)
		Frame2.pack(fill="both")
		
		# search button
		Clickie = ttk.Button(Frame1, command=self.search, text="Search", width=8, )
		Clickie.pack(side="right")
		
		# search entry
		self.Entry1 = ttk.Entry(Frame1, text="", width=26)
		self.Entry1.pack(side="right")
		self.Entry1.focus()
		self.Entry1.bind("<Return>",lambda e:self.search())
		
		# label
		ttk.Label(Frame2, text="Definition:", justify="left").pack(fill="x")
		
		# definition text
		self.msg_box = tk.Text(Frame2, bg="gray", fg="black", highlightbackground="orange", highlightcolor="orange")
		#add scrollbar
		vsb = ttk.Scrollbar(Frame2, orient="vertical", command=self.msg_box.yview)
		vsb.pack(side='right', fill='y')
		self.msg_box.pack(side = "left", fill="both", expand=True)
		self.msg_box.configure(yscrollcommand=vsb.set)
	
	def search(self):
		with open('dictionary.json') as json_file:  
			data = json.load(json_file)
		
		try:
			result = data[self.Entry1.get()]
		except KeyError:
			result = "No results found."
		
		print(result)
		
		# data garbage collection
		del data
		
		# clear search entry
		self.Entry1.delete(0,"end")
		self.Entry1.insert(0,"")
		
		# return response
		self.msg_box.delete('1.0',"end")
		self.msg_box.insert("end", result)
		

root = tk.Tk()
DICTIONARY(root)
root.mainloop()