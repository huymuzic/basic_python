# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

try:
    fhandle = open("mbox-short.txt")
except FileNotFoundError:
    print("File not found.")
    exit()

senders = {}

for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        sender = words[1]
        senders[sender] = senders.get(sender, 0) + 1

fhandle.close()

max_sender = None
max_count = None

for sender, count in senders.items():
    if max_count is None or count > max_count:
        max_sender = sender
        max_count = count

print(max_sender, max_count)