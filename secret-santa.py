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

		print('Giver:' + giver)
		print()
		for recipient, times in recipientTimes.items():
			print (recipient + ': ' + str(times) + ' times')

# Run Secret Santa assignment test
testAssignParticipants()
