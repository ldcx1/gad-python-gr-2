import requests
from bs4 import BeautifulSoup

URL = 'https://lpf.ro/liga-1'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

stage_table = soup.find(class_='clasament_general white-shadow etape_meciuri')
#print(stage_table.prettify())

team_rows1 = stage_table.find_all(class_='echipa-etapa-1')
team_rows2 = stage_table.find_all(class_='echipa-etapa-2')

teams = []
for team1, team2 in zip(team_rows1, team_rows2):
    team_name1 = team1.find(class_='hiddenMobile').text.strip()
    team_name2 = team2.find(class_='hiddenMobile').text.strip()
    print(team_name1, " -- ", team_name2)
    teams.append([team_name1, team_name2])

print(teams)

