import matplotlib.pyplot as plt
import csv 
import screeninfo

screen_info = screeninfo.get_monitors()[0]
width, height = screen_info.width, screen_info.height
fig = plt.figure(figsize=(width/200, height/200))

with open('./ucl_data/csv/goalkeeping.csv', 'r', encoding='utf-8') as keeperstats:
    reader = csv.DictReader(keeperstats)
    keepersMetMeerDan2Wedstrijden = []
    aantalWedstrijden = []
    gem_saves_per_match = []
    gem_goals_tegen_per_match = []
    cleansheets = []
    score = []
    keepers_met_club = []
    for i in reader:
        value = int(i['match_played'])
        if value > 2:
            gem_goal_tegen = round(int(i['conceded'])/value, 2)
            gem_goals_tegen_per_match.append(gem_goal_tegen)

            gem_saves = round(int(i['saved'])/value, 2)
            gem_saves_per_match.append(gem_saves)

            keepersMetMeerDan2Wedstrijden.append(i['player_name'])
            keeper_met_club = i['player_name'] + ' (' + i['club'] + ')'
            keepers_met_club.append(keeper_met_club)
            
            aantalWedstrijden.append(value)

            cleansheet = int(i['cleansheets'])
            cleansheets.append(cleansheet)

            score.append(round((gem_saves*2 + cleansheet *3 - gem_goal_tegen)/3, 2))
            
keepers = keepersMetMeerDan2Wedstrijden
keepers_met_club = keepers_met_club
matchen = aantalWedstrijden
gemiddeld_saves_per_match = gem_saves_per_match
gemiddeld_goals_tegen_per_match = gem_goals_tegen_per_match
cleansheets = cleansheets
score = score

sorted_keepers = [x for _,x in sorted(zip(score, keepers_met_club))]
sorted_score = sorted(score)

####### score per keeper #######
plt.barh(sorted_keepers, sorted_score, color='green')
plt.xlabel('score op 10')
plt.ylabel('keepers')
plt.title('score per keeper in de ucl')
plt.yticks(sorted_keepers, fontsize=6)
plt.xticks(range(0, 11, 1))
for i, aantal in enumerate(sorted_score):
    plt.text(aantal, i, str(aantal), fontsize=6)


####### gemiddeld aantal saves en goals tegen per match #######
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 6))

# #gemiddeld aantal saves
# ax1.barh(keepers, gemiddeld_saves_per_match, color='blue')
# ax1.set_xlabel('gemiddeld aantal saves per match')
# ax1.set_ylabel('keepers')
# ax1.set_title('gemiddeld aantal saves per match per keeper in de ucl')
# ax1.set_yticklabels(keepers, fontsize=6)
# ax1.set_xticks(range(0, 8, 1))
# for i, aantal in enumerate(gemiddeld_saves_per_match):
#     ax1.text(aantal, i, str(aantal), fontsize=6)


# #gemiddeld aantal goals tegen
# ax2.barh(keepers, gemiddeld_goals_tegen_per_match, color='red')
# ax2.set_xlabel('gemiddeld aantal goals tegen per match')
# ax2.set_ylabel('keepers')
# ax2.set_title('gemiddeld aantal goals tegen per match per keeper in de ucl')
# ax2.set_yticklabels(keepers, fontsize=6)
# ax2.set_xticks(range(0, 8, 1))
# for i, aantal in enumerate(gemiddeld_goals_tegen_per_match):
#     ax2.text(aantal, i, str(aantal), fontsize=6)

plt.show()