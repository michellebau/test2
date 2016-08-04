start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a dull basement.
A sign is hanging from a doorknob: "You have one hour. Don't lose your head."
There is a staircase that parts into two directions.
'''


print(start)

done = False
print("Type 'up' to go up or 'down' to go down.")
user_input = input()
while not done:
	if user_input == "up":
		print("You decide to go up and walk up towards a cellar. Would you like to stay or leave?")
		done = True
		user_input = input()
		if user_input == "stay":
			print("So you have decided to stay and a pack of beavers drag you to coexist with them in their colony.")
			done = True
		elif user_input == "leave":
			print("You decide to leave and walk into the White Witch's Castle, you immediately freeze.")
			done = True
		else:
			print ("Please enter either 'stay' or 'leave.'")
			user_input = input()
	elif user_input == "down":
		print("You choose to go down and trip down a rabbit hole. Would you rather follow the white rabbit or the Queen of Hearts?")
		user_input = input()
		if user_input == "white rabbit":
			print("You lose him in a forrest, calmed by surrounding flora and fauna.")
		elif user_input == "Queen of Hearts":
			print("You are seized by her henchmen, and taken to a dungeon. You hear her scream, 'Off with her head!'")
		else:
			print ("Please enter either 'white rabbit' or 'Queen of Hearts.'")
			user_input = input()
	else:
		print ("Please enter either 'up' or 'down.'")
		user_input = input()