#Braden Leach
#Febuary 3 2025
#Dictonary Evidence


#---Dictonary---#
fav_artists = {
            'Bruno Mars':'Die for you',
            'Imagine Dragons':'Beliver',
            'Chase Atlantic': 'Swim',
            'Jorge Herrans': 'Remember Them',
            'The Weekend':'Star boy',
            'Arctic Monkey':'I wanna be yours'
}

#-Print-#
print(f'{fav_artists}\n')

#--Update--#
fav_artists.update({'Lady Gaga':'Judas'})

#-Print-#
print(fav_artists)


#---Loop Dict---#
#-keys-#
for key in fav_artists.keys(): 
    print(f'{key}\n')
#-values-#
for value in fav_artists.values():
    print(f'{value}\n')
#-Pair-#
for items in fav_artists.items():
    print(f'{items}\n')