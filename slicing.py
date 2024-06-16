# slicing = create a substring by extracting elements from another string 
#           indexing[] or slice()
#           [start:stop:step]
#           start: inclusive, end: exclusive

name = "Huy Music"

firstname = name[:3]
lastname = name[4:]
reversedname = name[::-1]

print(firstname)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7, -4)

print(website1[slice])
print(website2[slice])