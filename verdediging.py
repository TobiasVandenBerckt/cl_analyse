import matplotlib.pyplot as plt
import pandas as pd
import screeninfo

screen_info = screeninfo.get_monitors()[0]
width, height = screen_info.width, screen_info.height
fig = plt.figure(figsize=(width/200, height/200))

df_defending = pd.read_csv('./ucl_data/csv/defending.csv')

df = df_defending.head()

spelers_met_meer_dan_4_wedstrijden = (df_defending['position'] == 'Defender') & (df_defending['match_played']> 4)
clubs = df_defending[spelers_met_meer_dan_4_wedstrijden]['club']
tackles_won = df_defending[spelers_met_meer_dan_4_wedstrijden]['t_won']
balls_recovered = df_defending[spelers_met_meer_dan_4_wedstrijden]['balls_recoverd']
clearences = df_defending[spelers_met_meer_dan_4_wedstrijden]['clearance_attempted']
verdedigers_met_club = df_defending[spelers_met_meer_dan_4_wedstrijden]['player_name'] + ' (' + clubs + ')'

score = round(((3 * tackles_won) + (2 * balls_recovered) + clearences) / 3, 2)

verdedigers_list = verdedigers_met_club.tolist()
tackles_won_list = tackles_won.tolist()
balls_recovered_list = balls_recovered.tolist()
clearances_list = clearences.tolist()
score_list = score.tolist()

sorted_verdedigers_list = [x for _,x in sorted(zip(score_list, verdedigers_list))]
sorted_score = sorted(score_list)

#enkel de 70 beste verdedigers (anders is het niet leesbaar)
sorted_verdedigers_list_70 = sorted_verdedigers_list[-70:]
sorted_score_70 = sorted_score[-70:]

####### grafiek van de coeffient per verdediger in de ucl #######
plt.barh(sorted_verdedigers_list_70, sorted_score_70, color='green')
plt.xlabel('score')
plt.ylabel('verdedigers')
plt.title('score per verdediger in de ucl')
plt.yticks(sorted_verdedigers_list_70, fontsize=6)
plt.xticks(range(0, 2, 10))
for i, aantal in enumerate(sorted_score_70):
    plt.text(aantal, i, str(aantal), fontsize=6)
plt.show()
