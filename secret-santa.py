from random import shuffle

def getRecipients(participants):
	"""
	Get a list of Secret Santa recipients

	Args:
		participants - list of participants in random order

	Returns:
		list of gift recipients, the random participant list rotated once
	"""
	recipients = participants.copy()
	firstPerson = recipients.pop(0)
	recipients.append(firstPerson)
	return recipients

def assignParticipants(participants):
	"""
	Assign a set of Secret Santa participants their gift recipients

	Args:
		participants - list of Secret Santa participants

	Returns:
		map of individuals to who their Secret Santa recipient is
	"""
	participantsList = participants.copy()

	shuffle(participantsList)

	recipients = getRecipients(participantsList)
	assignments = dict(zip(participantsList, recipients))

	return (assignments)


def testAssignParticipants():
	"""
	Tests assigning participants for a secret santa and displays
	how frequently individuals would have each other individual
	as a recipient
	"""
	def createFrequencyMap(participants):
		"""
		Creates a map of participant to how many times each other person received
		a gift from them.
		"""
		frequencyMap = {}
		for participant in participants:
			recipientList = participants.copy()
			recipientList.remove(participant)

			frequencyMap[participant] = {}
			for recipient in recipientList:
				frequencyMap[participant][recipient] = 0
		return frequencyMap

	participants = ['Albert', 'Becky', 'Chad', 'Diane', 'Eliza']

	frequencyMap = createFrequencyMap(participants)

	# Assign Secret Santas for test list 10000 times and increment each persons'
	# recipient frequency map each time
	for x in range(0, 10000):
		secretSanta = assignParticipants(participants)
		for giver, recipient in secretSanta.items():
			frequencyMap[giver][recipient] += 1

	# Print frequency map results
	#
	# If everything works as intended, there should be a relatively even
	# distribution of givers and the number of times they had each other person
	# as their recipient.
	for giver, recipientTimes in frequencyMap.items():
		print('#######################')

		print(f'Giver: {giver}')
		print()
		for recipient, times in recipientTimes.items():
			print (f'{recipient}: {str(times)} times')


def initSecretSanta(): 
	"""
	Start the Secret Santa tool with basic menu
	"""
	options = {
		'1': 'Generate Secret Santas by giving names',
		'2': 'Generate Secret Santas from file',
		'3': 'Run distribution test'
	}

	print('Welecome to Truly Secret Santa! Please type a number for one of the following options:')
	for num, option in options.items():
		print(f'{num}: {option}')
	selection = input('Please select an option: ')

	while (selection is not None and selection not in options.keys()):
		selection = input('Invalid selection, please select an option from above: ')

	if selection == '1':
		results = assignParticipants(giveNames())
		writeResultFiles(results)

	elif selection == '2':
		results = assignParticipants(giveFile())
		writeResultFiles(results)

	elif selection == '3':
		# Run Secret Santa assignment test
		testAssignParticipants()

def giveNames():
	"""
	Collect Secret Santa participant names one at a time via user input

	Returns:
		A list of Secret Santa participants
	"""
	participants = []
	print('Please enter participant names one at a time, then enter 25 when complete')
	nameInput = input()
	while (nameInput is not None and nameInput != '25'):
		participants.append(nameInput)
		nameInput = input()
	return participants

def giveFile():
	"""
	Collect Secret Santa participant names one at a time via user input

	Returns:
		A list of Secret Santa participants
	"""
	fileName = input('Please enter the name of a file to read from: ')
	while (fileName is None or fileName is ''):
		fileName = input('Invalid, please enter a valid filename: ')
	try:
		with open(fileName, 'r') as f:
			fileContents = f.readlines()
		participants = [line.strip() for line in fileContents]
	except FileNotFoundError:
		print(f'Error: could not find file {fileName}')
		exit(1)
	return participants

def writeResultFiles(resultsMap):
	"""
	Write the Secret Santa results to text files.
	
	A text file will be generated for each participant, and the file
	will be named after that participant. Each person's text file will
	tell them who their gift recipient is. An organizer key with all
	the Secret Santas is created as well.

	Args:
		resultsMap - dictionary of participants paired with their gift recipient
	"""
	with open('organizer-key.txt', 'w') as key:
		key.write('Organizer Key:\n')
		for giver, recipient in resultsMap.items():
			with open(f'{giver}.txt', 'w') as f:
				f.write(f'Hello {giver}! You will be Secret Santa for {recipient}')
			key.write(f'{giver} will give a gift to {recipient}\n')



initSecretSanta()