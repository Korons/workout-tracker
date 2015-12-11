import os
import datetime
log = '' # <-- Where you want the info to be stored goes here
now = datetime.datetime.now()
print "-------------------------------------------------------\n\n Welcome to workout.py\n\n"
print "\n\n What will you be doing today? \n\n1) Lifting\n2) Running\n3) Situps\n4) Squats\n5) Pushups\n\n-------------------------------------------------------"
workout = raw_input()

if workout == "1":
	FreeorBench = raw_input("Free weights or bench presses: ")
	if FreeorBench == "bench":
		weight = raw_input("Enter weight of weights: ")
		goal = raw_input("Enter the number of reps you want to do: ")
		print "Go lift and return when done"
		started = now.strftime("%H:%M")
		raw_input("Press Enter when done")
		now2 = datetime.datetime.now()
		ended = now2.strftime("%H:%M")
		did = raw_input("Enter the number of reps you did: ")
		with open(log, "a") as myfile:
			myfile.write("workout type " + workout + FreeorBench + "\n")
			myfile.write("weight " + weight + "\n")
			myfile.write("goal " + goal + "\n")
			myfile.write("time started " + started + "\n")
			myfile.write("time ended " + ended + "\n")
			myfile.write("Number of reps done " + did + "\n")
	elif FreeorBench == "free":
		weight = raw_input("Enter weight of weights: ")
		goal = raw_input("Enter the number of reps you want to do: ")
		started = now.strftime("%H:%M")
		raw_input("Press Enter when done")
		now2 = datetime.datetime.now()
		ended = now2.strftime("%H:%M")
		did = raw_input("Enter the number of reps you did: ")
		with open(log, "a") as myfile:
			myfile.write("workout type " + workout + "\n")
			myfile.write("weight " + weight + "\n")
			myfile.write("goal " + goal + "\n")
			myfile.write("time started " + started + "\n")
			myfile.write("time ended " + ended + "\n")
			myfile.write("Number of reps done " + did + "\n")
elif workout == "2":
	goal = raw_input("How many you want to do: ")
	started = now.strftime("%H:%M")
	raw_input("Press Enter when done")
	did = raw_input("How far did you run: ")
	now2 = datetime.datetime.now()
	ended = now2.strftime("%H:%M")
	with open(log, "a") as myfile:
		myfile.write("goal " + goal + "\n")
		myfile.write("time started " + started + "\n")
		myfile.write("time ended " + ended + "\n")
		myfile.write("How far you ran " + did + "\n")
elif workout == "3":
	goal = raw_input("How many you want to do: ")
	started = now.strftime("%H:%M")
	raw_input("Press Enter when done")
	did = raw_input("How far did you run: ")
	now2 = datetime.datetime.now()
	ended = now2.strftime("%H:%M")
	with open(log, "a") as myfile:
		myfile.write("goal " + goal + "\n")
		myfile.write("time started " + started + "\n")
		myfile.write("time ended " + ended + "\n")
		myfile.write("How many you did " + did + "\n")
elif workout == "4":
	goal = raw_input("How many you want to do: ")
	started = now.strftime("%H:%M")
	raw_input("Press Enter when done")
	did = raw_input("How many did you do: ")
	now2 = datetime.datetime.now()
	ended = now2.strftime("%H:%M")
	with open(log, "a") as myfile:
		myfile.write("goal " + goal + "\n")
		myfile.write("time started " + started + "\n")
		myfile.write("time ended " + ended + "\n")
		myfile.write("How many you did " + did + "\n")
elif workout == "5":
	goal = raw_input("How many you want to do: ")
	started = now.strftime("%H:%M")
	raw_input("Press Enter when done")
	did = raw_input("How many did you do: ")
	now2 = datetime.datetime.now()
	ended = now2.strftime("%H:%M")
	with open(log, "a") as myfile:
		myfile.write("goal " + goal + "\n")
		myfile.write("time started " + started + "\n")
		myfile.write("time ended " + ended + "\n")
		myfile.write("How many you did " + did + "\n")
else:
	print "Command not found"
	sys.exit()
