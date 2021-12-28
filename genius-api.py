# import libraries
import requests
import json
import lyricsgenius
import os

# clear the console
# for linux terminal
if os.name == 'posix':
	clear = lambda: os.system('clear')
	clear()
#for windows cmd
elif os.name == 'nt':
	clear = lambda: os.system('cls')
	clear()

# export the color
class color:
   PURPLE = '\033[1;35;48m'
   CYAN = '\033[1;36;48m'
   BOLD = '\033[1;37;48m'
   BLUE = '\033[1;34;48m'
   GREEN = '\033[1;32;48m'
   YELLOW = '\033[1;33;48m'
   RED = '\033[1;31;48m'
   BLACK = '\033[1;30;48m'
   UNDERLINE = '\033[4;37;48m'
   END = '\033[1;37;0m'


# access to the api
base_url = 'https://api.genius.com'
client_access_token = ''
token = 'Bearer {}'.format(client_access_token)
headers = {'Authorization': token}
genius = lyricsgenius.Genius(client_access_token)

#######################################################START#########################################################
w = """
 ██████  ███████ ███    ██ ██ ██    ██ ███████      █████  ██████  ██ 
██       ██      ████   ██ ██ ██    ██ ██          ██   ██ ██   ██ ██ 
██   ███ █████   ██ ██  ██ ██ ██    ██ ███████     ███████ ██████  ██ 
██    ██ ██      ██  ██ ██ ██ ██    ██      ██     ██   ██ ██      ██ 
 ██████  ███████ ██   ████ ██  ██████  ███████     ██   ██ ██      ██ 
\n
"""
print(color.YELLOW + w + color.END)
print(color.YELLOW + 'By Cyclops789: github.com/Cyclops789' + color.END)
print(' ')
k = input(color.CYAN + "Artist's name: " + color.END)
g = input(color.CYAN + "Artist's ID, (type 'n' if you dont have one): " + color.END)
print(' ')
if g == 'n':
	# if you dont have artist's id, it will search for it
	def name_of_artist():
		artist_name = k.replace(" ", "-")

		path_search = 'search/'

		request_sch = '/'.join([base_url, path_search])
	
		params = {'q': artist_name}

		s = requests.get(request_sch, params=params, headers=headers)

		p_json = s.json()
		p_id = json.dumps(p_json['response']['hits'][0]['result']['primary_artist']['id'], indent=2)
		print(color.GREEN + k + "'s" + " ID is: " + color.RED + p_id + color.END)
		print(' ')

	name_of_artist()
	exit()
# check if variable g is a number 
elif g.isdigit():
	artist_id = g
	path_artist = 'artists/{}'.format(artist_id)

	request_id = '/'.join([base_url, path_artist])

	a = requests.get(request_id, headers=headers)

	p_json = a.json()

	p_name = json.dumps(p_json['response']['artist']['name'], indent=2)
	p_facebook = json.dumps(p_json['response']['artist']['facebook_name'], indent=2)
	p_instagram = json.dumps(p_json['response']['artist']['instagram_name'], indent=2)
	p_twitter = json.dumps(p_json['response']['artist']['twitter_name'], indent=2)
	p_followers_count = json.dumps(p_json['response']['artist']['followers_count'], indent=2)
	p_url = json.dumps(p_json['response']['artist']['url'], indent=2)
	p_bio = p_json['response']['artist']['description']['dom']['children'][0]['children']

	print(color.GREEN +'Name: '+ color.BLUE + p_name.replace('"', "") + color.END)
	for children in p_bio:
		print(color.GREEN +'Bio: '+ color.BLUE + children.replace('"', "") + color.END)

	print(color.GREEN +'Followers Count: '+ color.BLUE + p_followers_count.replace('"', "") + color.END)
	print(color.GREEN +'Instagram: '+ color.BLUE + p_instagram.replace('"', "") + color.END)
	print(color.GREEN +'Twitter: '+ color.BLUE + p_twitter.replace('"', "") + color.END)
	print(color.GREEN +'Facebook: '+ color.BLUE + p_facebook.replace('"', "") + color.END)
	print(color.GREEN +'Url: '+ color.BLUE + p_url.replace('"', "") + color.END)
	print(' ')
# if its not a number or 'n' then it will print this waring message
else:
	print(color.RED + 'That is not a number, please put the id!' + color.END)
	exit()
# get some of the artist's songs
def song_of_artist():
	artist_songs = g
	path_songs = 'artists/{}/songs'.format(artist_songs)

	request_songs = '/'.join([base_url, path_songs])
	so = requests.get(request_songs, headers=headers)

	p_json = so.json()
	p_songs = p_json['response']['songs']
	print(color.CYAN + "Songs: " + color.END)
	print(" ")
	for songs in p_songs:
		print(color.RED + songs['full_title'].replace('"', "") + color.END)
		print(' ')

song_of_artist()
print(' ')

f = input(color.PURPLE + 'Do you want to get the Lyrics of a song? [y/N]: ' + color.END)
print(' ')

def lyrics():
# this makes lyrics() function loop using while true
	while True:
		r = input(color.PURPLE + 'What is the name of the song?: ' + color.END)
		print(' ')
		artist = genius.search_artist(k, max_songs=0, sort="title")
		song = artist.song(r)
		d = (song.lyrics).replace("EmbedShare URLCopyEmbedCopy", "")
		print(color.CYAN + d + color.END)
		print(' ')
		l = input(color.PURPLE + "Do you want save these Lyrics in a text file? [y/N]: " + color.END)
		print(" ")
		if l == 'y':
			n = input(color.PURPLE + 'What do you want to name it?: ' + color.END)
			print(' ')
			ju = "{}.txt".format(n)
			f = open(ju, "w+")
			f.write(d)
			print(color.GREEN + 'Successfully save the lyrics ' + ju + color.END)
		b = input(color.PURPLE + 'Do you want to get the Lyrics of an other song? [y/N]: ' + color.END)
		if b == 'n':
			exit()
		elif b =='y':
			print(' ')
if f == 'y':
	lyrics()
else:
	exit()
#######################################################END#########################################################
