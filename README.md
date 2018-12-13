# truly-secret-santa

A Python utility for secretly assigning a group of people their Secret Santa gift recipients (without the organizer even knowing)!

As of now, just has the basic secret santa assignment working and a test to make sure recipients are distributed evenly

To-Do List:
- Allow user to pass in a file with a list of participants to then assign secret santas
- Write each giver's recipient out to a file with the giver's name. This way, organizer generates the files and then sends each person the file with their name, and they'll know who to get a gift for
- Write whole mapping to file in case organizer needs to look up anything
- Add more options to client: allow organizer to pass in list of participants, or type them one-by-one, run test set, have better messaging for user
- Maybe create separate script to extract a recipient's secret santa from the mapping (so again organizer won't know 100%)
- Setup and usage instructions in README