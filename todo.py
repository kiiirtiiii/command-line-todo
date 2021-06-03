print("-------------------------------------------")
print("MANAGE ALL YOUR TASKS AND BE MORE ORGANIZED")
print("-------------------------------------------")
print()
print('type "help" to know the commands')

start = 1

def help():
	print("Usage :-")

	print('add "todo item"	# Add a new todo')
	print('ls		# Show remaining todos')
	print('del "NUMBER"	# Delete a todo')
	print('done "NUMBER"	# Complete a todo')
	print('help		# Show usage')
	print('report		# Statistics')
	print('close 		# Close the application')

def report():
	f = open("Pending.txt", "r")
	f1 = open("Completed.txt", "r")
	
	print("Pending : ",len(f.readlines()), end=" ")
	print("Completed : ",len(f1.readlines()))

	f.close()
	f1.close()

def add(x):
	y = x[4::]
	f = open("Pending.txt", "a")
	f.write(y+"\n")
	f.close()
	print("Added todo: "+y)

def ls():
	f = open("Pending.txt", "r")
	k = f.readlines()
	for i in range(len(k)-1, -1, -1):
		print("["+str(i+1)+"] "+k[i])
	f.close()

def delete(x):
	msg = "check"
	take = 'nothing'

	try:
		item = int(x)
	except:
		msg = "** Not a valid command **"

	if msg[0]=='*':
		pass
	
	else:
		f = open("Pending.txt", "r")
		k = f.readlines()

		try:
			take = k.pop(item-1)
			f.close()
		
			f2 = open("Pending.txt", "w")
			for i in k:
				f2.write(i)
			f2.close()
			
			msg = "Deleted todo #"+x
		
		except:
			msg = "Error: todo #"+x+" does not exist. Nothing deleted."
			f.close()

	return([msg, take])
				
def done(x):
	p = delete(x)
	
	if p[0][0]=='E':
		msg = "Error: todo #"+x+" does not exist."
	
	elif p[0][0]=='*':
		msg = p[0]

	else:
		f1 = open("Completed.txt", "a")
		f1.write(p[1])
		f1.close()

		msg = "Maked todo #"+x+" as done"

	print(msg)

while start:
	print()
	x = input()

	if x=="help":
		help()

	elif x=="report":
		report()

	elif x[0:4]=="add ":
		add(x)

	elif x=="ls":
		ls()
		
	elif x[0:5]=="done ":
		done(x[5::])

	elif x[0:4]=="del ":
		result = delete(x[4::])
		print(result[0])

	elif x=="close":
		print('Are you sure, you want to close the application?\nPress "enter" to confirm\nPress "any key" to decline')
		decide = input()
		if len(decide)>0:
			pass
		else:
			start = 0

	else:
		print("** Not a valid command **")