print('``````````````` type "help" to know the commands ```````````````')

start = 1


def help():
	print("Usage :-")

	print('add "todo item"	# Add a new todo')
	print('ls		# Show remaining todos')
	print('del Number	# Delete a todo')
	print('done Number	# Complete a todo')
	print('help		# Show usage')
	print('report		# Statistics')
	print('close 		# Application will be closed')

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
	f = open("Pending.txt", "r")
	k = f.readlines()
	p = k.pop(int(x[4::])-1)
	f.close()
	
	f2 = open("Pending.txt", "w")
	for i in k:
		f2.write(i)
	f2.close()

	return p

def done(x):
	p = delete(x)
	
	f1 = open("Completed.txt", "a")
	f1.write(p)
	f1.close()

	print("Maked todo #"+x[5::]+" as done")



while start:
	print()
	x = input()

	if x=="help":
		help()

	elif x=="report":
		report()

	elif x[0:3]=="add":
		add(x)

	elif x=="ls":
		ls()
		
	elif x[0:4]=="done":
		done(x)

	elif x[0:3]=="del":
		p = delete(x)
		print("Deleted todo #"+x[4::])

	elif x=="close":
		print("``````````````` Application is closing ```````````````")
		start = 0
