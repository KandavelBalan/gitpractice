spotify = ['SVK','WSR','Vocal oli','Cheemsrajah']
hotel = ['chaminar','eam','mdb','ya.mohi']
tourist_spot = ['munnar','Wayanad','coorg','pondy']

print(spotify)
print(hotel)
print(tourist_spot)

#methods

# spotify.append("OmCreem")
# print(F'after append: {spotify}')

# spotify.insert(3,'VUP')
# print(f'after insert: {spotify}')

# spotify.remove('VUP')
# print(f'after removing: {spotify}')

# spotify.pop()
# print(f'after pop: {spotify}')

# spotify.reverse()
# print(f'after removing: {spotify}')

print(f'index postion of eam: {hotel.count('eam')}')

# # list slicing

# print(f'first 2 tour places: {tourist_spot[:2]}')

# print(f'latest 2 tour places: {tourist_spot[-2:]}')

# print(f'first 2 tour places: {tourist_spot[1:3]}')

# for rest in hotel:
    # print(f'briyani spots: {rest}')

for podcast in spotify:
    print(f'podcast name: {podcast}')

if 'Wayanad' in tourist_spot:
    print(True)

for i,place in enumerate(tourist_spot):
    print(f'{i}: {place}')