#!/bin/env python
import tkinter as tk
import simon

window = tk.Tk()
window.title("Simon says")
for col in range(2):
	window.columnconfigure(col, weight=1, minsize=200)
for row in range(3):
	window.rowconfigure(row, weight=1, minsize=200)

frame = tk.Frame( master=window, relief=tk.RAISED,  borderwidth=1)
frame.grid(row=2, column=0, padx=10, pady=10)
message = tk.Label(master=frame, text="Press start to play")
message.pack()

def proceed():
	global user_sequence
	buttonS.config(state="disabled")
	if len(user_sequence)==0:
		message.config(text="(concentrate)")
	else:
		message.config(text="Good (now concentrate)")
	user_sequence = ""	
	simon.extend_sequence()
	
	for l in simon.sequence:
		sel = int(l,16)-10 
		original_color = buttons[sel].cget("bg")
		for fl in range(1):			
			buttons[sel].config(bg = 'white')
			buttons[sel].update()
			window.after(500, buttons[sel].config(bg = original_color))
			buttons[sel].update()
		window.after(100, buttons[sel].config(bg = original_color))
		buttons[sel].update()
	message.config(text="What did Simon say?")
		
def handle_S(event):
	if buttonS["state"]!="disabled":
		#for i in range(4): buttons[i]["state"]="normal"
		
		proceed()

frameS = tk.Frame( master=window, relief=tk.RAISED,  borderwidth=1)
frameS.grid(row=2, column=1, padx=5, pady=5)
buttonS = tk.Button(master=frameS, text="Start", width=10, height=7)
buttonS.bind("<Button-1>", handle_S)
buttonS.pack()

	
user_sequence = ""


letters = ("A", "red"), ("B", "green"), ("C", "cyan"), ("D", "yellow")
buttons = []

def handle_B(event,l_i):	
	global user_sequence 
	if buttonS["state"]=="disabled":
		user_sequence+=str(chr(65+l_i))
		if len(user_sequence) == len(simon.sequence):
			if simon.compare_sequence(user_sequence):
				proceed()
			else:			
				message.config(text="Game over! score="+str(len(user_sequence)-1))
				buttonS.config(state="normal")
				simon.clear_sequence()
				user_sequence = ""

for l_i in range(4):
	l = letters[l_i]
	frame = tk.Frame( master=window, relief=tk.RAISED,  borderwidth=1)
	frame.grid(row=int(l_i/2), column=l_i%2, padx=5, pady=5)
	button = tk.Button(master=frame, text=l[0], width=10, height=7, bg=l[1])
	
	button.bind("<Button-1>", lambda event, l_i=l_i: handle_B(event, l_i))
	button.pack()
	buttons.append(button)

user_sequence = ""

window.mainloop()
