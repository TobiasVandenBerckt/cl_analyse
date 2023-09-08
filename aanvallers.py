import matplotlib.pyplot as plt
import pandas as pd
import screeninfo

screen_info = screeninfo.get_monitors()[0]
width, height = screen_info.width, screen_info.height
fig = plt.figure(figsize=(width/200, height/200))

df_schoten = pd.read_csv('./ucl_data/csv/attempts.csv')
df_goals = pd.read_csv('./ucl_data/csv/goals.csv')
df_goals_en_attempts = pd.merge(df_schoten, df_goals, on='player_name')

df = df_goals_en_attempts.head()

spelers_met_meer_dan_2_wedstrijden = (df_goals_en_attempts['position_x'] == 'Forward') & (df_goals_en_attempts['match_played_y']> 2)
clubs = df_goals_en_attempts[spelers_met_meer_dan_2_wedstrijden]['club_x']
goals = df_goals_en_attempts[spelers_met_meer_dan_2_wedstrijden]['goals']
total_attempts = df_goals_en_attempts[spelers_met_meer_dan_2_wedstrijden]['total_attempts']
on_target = df_goals_en_attempts[spelers_met_meer_dan_2_wedstrijden]['on_target']
aanvallers_met_club = df_goals_en_attempts[spelers_met_meer_dan_2_wedstrijden]['player_name'] + ' (' + clubs + ')'

aanvallers_list = aanvallers_met_club.tolist()
goals_list = goals.tolist()
totaal_aantal_schoten_list = total_attempts.tolist()
on_target_list = on_target.tolist()

score = round((goals / total_attempts + goals / total_attempts + on_target / total_attempts) / 3, 2)

percentage_on_target = round(goals/on_target * 100, 2)
percentage_on_target_list = percentage_on_target.tolist()
percentage_total_attempts = round(goals/total_attempts * 100, 2)
percentage_total_attempts_list = percentage_total_attempts.tolist()
score_list = score.tolist()

sorted_aanvallers_on_target = [x for _,x in sorted(zip(percentage_on_target_list, aanvallers_list))]
sorted_percentage_on_target = sorted(percentage_on_target_list)

sorted_aanvallers_total_attempts = [x for _,x in sorted(zip(percentage_total_attempts_list, aanvallers_list))]
sorted_percentage_total_attempts = sorted(percentage_total_attempts_list)

sorted_data = sorted(zip(aanvallers_list, goals_list, totaal_aantal_schoten_list, on_target_list), key=lambda x: x[2])
sorted_aanvallers_list, sorted_goals_list, sorted_totaal_aantal_schoten_list, sorted_on_target_list = zip(*sorted_data)

sorted_aanvallers_score_list = [x for _,x in sorted(zip(score_list, aanvallers_list))]
sorted_score = sorted(score_list)

####### grafiek van percentage goals per schots on target per speler in de ucl #######
# plt.barh(sorted_aanvallers_on_target, sorted_percentage_on_target, color='green')
# plt.xlabel('percentage op 100')
# plt.ylabel('aanvallers')
# plt.title('percentage goals per schots on target per speler in de ucl')
# plt.yticks(sorted_aanvallers_on_target, fontsize=6)
# plt.xticks(range(0, 101, 10))
# for i, aantal in enumerate(sorted_percentage_on_target):
#     plt.text(aantal, i, str(aantal), fontsize=6)

####### overzicht van alle schoten #######
# y_pos = range(len(sorted_aanvallers_list))
# plt.barh(y_pos, sorted_totaal_aantal_schoten_list, color='orange')
# plt.barh(y_pos, sorted_on_target_list, color='red')
# plt.barh(y_pos, sorted_goals_list, color='blue')

# plt.yticks(y_pos, sorted_aanvallers_list, fontsize=6)
# plt.xlabel('aantal')
# plt.ylabel('aanvallers')
# plt.title('overzicht van alle schoten per speler')
# for i, aantal in enumerate(sorted_totaal_aantal_schoten_list):
#     plt.text(aantal, i, str(aantal), fontsize=6)
# plt.legend(['totaal aantal schoten', 'schoten on target', 'goals'], loc='lower right')

####### grafiek van de coeffient per aanvaller in de ucl #######
plt.barh(sorted_aanvallers_score_list, sorted_score, color='green')
plt.xlabel('score')
plt.ylabel('aanvallers')
plt.title('score per aanvaller in de ucl')
plt.yticks(sorted_aanvallers_score_list, fontsize=6)
plt.xticks(range(0, 2, 10))
for i, aantal in enumerate(sorted_score):
    plt.text(aantal, i, str(aantal), fontsize=6)
plt.show()

