# fhand = open('text.txt')
# counts = {}
# for line in fhand:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# lst = []
# for key, value in counts.items():
#     newtup = (value, key)
#     lst.append(newtup)

# lst = sorted(lst, reverse=True)

# for value, key in lst[:10]:
#     print(key, value)

# print(sorted([(v, k) for k, v in counts.items()], reverse=True)[:10])

# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

fhand = open('mbox-short.txt')
hours = {}
for line in fhand:
    if line.startswith('From '):
        words = line.split()
        time = words[5]
        hour = time.split(':')[0]
        hours[hour] = hours.get(hour, 0) + 1

print(hours)
for hour, count in sorted(hours.items()):
    print(hour, count)