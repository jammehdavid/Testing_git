from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"

printer = PrettyPrinter()

def get_links():
	data= get(BASE_URL + ALL_JSON).json()
	Links = data["links"]
	return Links

def get_scoreboard():
	scoreboard = get_links()["currentScoreboard"]
	games = get(BASE_URL + scoreboard).json()['games']

	for game in games:
		home_team = game["hTeam"]
		away_team = game['vTeam']
		clock = ['clock']
		period = game['period']
		print('---------------------------------------------------------')
		print(f"{home_team['triCode']} VS {away_team['triCode']}")
		print(f"{home_team['score']}-{away_team['score']}")
		print(f"{clock}-{period['current']}")

		print("---------------------------------------------------------")
		break 

def get_stats():
	stats = get_links()['leagueTeamStatsLeaders']
	teams= get(BASE_URL +stats).json()['league']['standard']['regularSeason']['teams']

	teams = list(filter(lambda x: x['name'] !='Team', teams))

	teams.sort(key=lambda x: x['ppg']['rank'])

	#Only uncomment the line below when the regular season start else you will have a value error. 
	#teams.sort(key=lambda x: int(x['ppg']['rank']))

	for i,team in enumerate(teams):
		name = team['name']
		nickname = team['nickname']
		ppg = team['ppg']
		print(f"{i +1}.{name} - {nickname} - {ppg}")

get_scoreboard()

get_stats()

print('The code worked')

print('It will work')
