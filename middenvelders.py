import matplotlib.pyplot as plt
import pandas as pd
import screeninfo

############################not enough data to make a graph

#screen info
screen_info = screeninfo.get_monitors()[0]
width, height = screen_info.width, screen_info.height
fig = plt.figure(figsize=(width/200, height/200))

#reading csv files
df_distributon = pd.read_csv('./ucl_data/csv/distributon.csv')
df_key_stats = pd.read_csv('./ucl_data/csv/key_stats.csv')
df_midfielders = pd.merge(df_distributon, df_key_stats, on='player_name')

#checks if the merge works and shows the 5 first rows
# df = df_midfielders.head()
# print(df)

#getting data from csv files
midfielders_with_more_than_2_games= (df_midfielders['position_x'] == 'Midfielder') & (df_midfielders['match_played_y']> 2)
clubs = df_midfielders[midfielders_with_more_than_2_games]['club_x']
passes_completed = df_midfielders[midfielders_with_more_than_2_games]['pass_completed']
passes_attempted = df_midfielders[midfielders_with_more_than_2_games]['pass_attempted']
pass_accuracy = df_midfielders[midfielders_with_more_than_2_games]['pass_accuracy']
crosses_completed = df_midfielders[midfielders_with_more_than_2_games]['cross_complted']
crosses_attempted = df_midfielders[midfielders_with_more_than_2_games]['cross_attempted']
midfielers_clubs = df_midfielders[midfielders_with_more_than_2_games]['player_name'] + ' (' + clubs + ')'

#making a list of the data
midfielders_clubs_list = midfielers_clubs.tolist()
passes_completed_list = passes_completed.tolist()
passes_attempted_list = passes_attempted.tolist()
pass_accuracy_list = pass_accuracy.tolist()
crosses_completed_list = crosses_completed.tolist()
crosses_attempted_list = crosses_attempted.tolist()


