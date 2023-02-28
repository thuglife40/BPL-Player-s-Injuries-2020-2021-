# Import packages
import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
import squarify as sq

# I. Reading and editing the original file

# 1.1. Read the file
pd.set_option('display.max_columns', None)
injury = pd.read_csv("Injuries Databases.csv", index_col=False)
print(injury, sep="\n")

# 1.2. Add the 'InjuryNumbers' column
injuries_list = ["Ankle", "Back", "Calf", "COVID19", "Foot", "Groin", "Hamstring", "Head", "Knee", "Knock",
                "Muscles", "Shoulder", "Thigh", "OthCauses", "OthMembers"]
sum_injuries = injury[injuries_list].sum(axis = 1)
injury.insert(4, 'InjuryNumbers', sum_injuries)
print(injury)
injury.to_csv("Injuries_Updated.csv", index=False)

# 1.3. Decreasing sort of the teams for each InjuryNumbers
print((injury[['TeamName', 'InjuryNumbers']].copy()).sort_values(by = ['InjuryNumbers'], ascending=False))

# 1.4. Create a Stacked bar graph for teams
culori_stack = ['darkorange', 'royalblue', 'silver', 'red', 'forestgreen', 'chocolate', 'violet', 'aqua',
                'gold', 'tomato', 'springgreen', 'darkkhaki', 'skyblue', 'pink', 'steelblue']
injury.plot(x='Abbreviation', y = injuries_list, color = culori_stack, kind='bar', stacked=True,
            title='Grafic Stacked Bar al tipurilor de accidentari, pentru fiecare echipa')
plt.legend(loc = 'best', frameon = False, ncol = 2)
plt.yticks(np.arange(0, 70, 5))
plt.show()

# 1.5. Sort the types of injuries for each time
acc_dframe = injury.drop(injury.columns[[0, 2, 3, 4]], axis=1).copy().set_index('Abbreviation')
inj_lst = [[z for z,p in sorted(zip(acc_dframe.columns.values.tolist(), x), key=lambda y: y[1], reverse=True)]
      for x in acc_dframe.apply(lambda x : x.rank(),1).values.tolist()]
print(pd.Series(data=inj_lst,index=acc_dframe.index))

# II. Creating a Dataframe with the percentages of each type of injury, related to their total number, for each team

# 2.1. The function which calculate the percentages
def c_proc():

    valori = []
    for i in range(len(injury)):
        _v = []
        for (j, k) in zip(injuries_list, range(len(injuries_list))):
            f_proc = float((injury[j][i] / injury["InjuryNumbers"][i]) * 100)
            _v.append(f_proc)
        valori.append(_v)

    return np.array(valori)

proc_echipe = c_proc()
print(proc_echipe)

# 2.2. Save the values in a tables
p_echipe = pd.DataFrame(data=proc_echipe, index=injury["Abbreviation"], columns=injuries_list)
print(p_echipe)
p_echipe.to_csv("Percentages per teams.csv")

# 2.3. Convert the values to 2 decimals and save them in other table
print(p_echipe.applymap('{:.2f}'.format).astype(float))
(p_echipe.applymap('{:.2f}'.format).astype(float)).to_csv("Aprox. Percentages per teams.csv")

# 2.4. Import data from the new dataframe
perc_teams = pd.read_csv("Aprox. Percentages per teams.csv", index_col=False)
print(perc_teams)

# 2.5. Create an horizontal stacked bar graph for a team
echipa_graf = perc_teams[perc_teams['Abbreviation'] == input("Choose the team by its Abbreviation: ")]
single_graf = echipa_graf.plot(x='Abbreviation', y= injuries_list, color = culori_stack, kind = 'barh',
             stacked=True, width=.03, figsize=(6, 5),  alpha = .85)
for c in single_graf.containers:
    single_graf.bar_label(c, labels = [f'{w:.2f}' if (w := v.get_width()) > 0 else '' for v in c],
                          fontsize=7, label_type='center')
single_graf.set_xlabel('Procente (%)', fontsize = 10)
single_graf.set_title("Procentaj al accidentarilor, raportat la numarul lor total, pentru fiecare echipa")
plt.legend(loc = 'best', ncol = 2)
plt.show()

# 2.6. Create an horizontal stacked bar graph for all teams
multiple_graf = perc_teams.plot(x='Abbreviation', y= injuries_list, color = culori_stack, kind = 'barh',
             stacked=True, width=.8, mark_right = True, alpha = .8)
for c in multiple_graf.containers:
    multiple_graf.bar_label(c, labels = [f'{w:.2f}' if (w := v.get_width()) > 0 else '' for v in c],
                            fontsize=6.5, label_type='center')
multiple_graf.set_xlabel('Procente (%)')
multiple_graf.set_title("Procentaj al accidentarilor, raportat la numarul lor total, pentru fiecare echipa")
plt.legend(bbox_to_anchor=(1, 1), loc='upper left',  ncol = 1)
plt.show()

# III. Creating a Dataframe for the total of each separate category

# 3.1. Calculate the total for numeric columns Calcul total pentru coloanele numerice
new_injury = pd.read_csv("Injuries_Updated.csv")
print(new_injury.select_dtypes(np.number).sum().rename('TOTAL').sort_values(ascending=False))

# 3.2. Add TOTAL values as a new row in the dataframe
new_injury.loc[len(new_injury.index)] = new_injury.select_dtypes(np.number).sum()
new_injury = new_injury.rename(index = {new_injury.index[20]:"TOTAL"})
print(new_injury)
new_injury.to_csv("Injuries_with_TOTAL.csv", index=False)

# 3.3. Create dataframe with the total of each category
new_injury = new_injury.drop(new_injury.iloc[:, 0:4], axis=1).copy().astype(int)
new_injury_total = new_injury.loc["TOTAL"].reset_index()
new_injury_total = new_injury_total.rename(columns={new_injury_total.columns[0]:'Categories'}).reset_index(drop=True)
new_injury_total['Percent'] = (new_injury_total['TOTAL']/new_injury_total.iloc[0, 1]*100).map('{:.2f}'.format).astype(float)
new_injury_total = new_injury_total.drop(0, axis = 0)
print(new_injury_total)

# IV. Analyzing graphs

# 4.1. Create graphs to show the percentages of each category related to the total number of injuries

# 4.1.1. Bar Chart graph
x = new_injury_total['Categories']
y = new_injury_total['Percent']
plt.yticks(np.arange(0, y.max(), 2.5))
for bar in plt.bar(x, height = y, width=.5, color=culori_stack):
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .2, yval)
plt.xticks(rotation=45, horizontalalignment='right', fontweight='light', fontsize=10)
plt.title("Procentajul tipurilor de accidentari, raportat la numarul lor total")
plt.show()

# 4.1.2. Treemap graph
lbl_tree = [f'{el[0]} = {el[1]}%' for el in zip(new_injury_total['Categories'], new_injury_total['Percent'])]
plt.figure(figsize=(12,8), dpi= 80)
sq.plot(sizes = new_injury_total['Percent'], label = lbl_tree, color = culori_stack, alpha=.7)
plt.title('Grafic Treemap pentru afisarea procentelor de accidentari, raportat la total', fontsize = 14)
plt.axis('off')
plt.show()

# 4.2. Barchart graph for values of important types of injuries from a team
injury.plot.bar(x = 'Abbreviation', y = ['Ankle','Knock','Thigh'],
                title = 'Bar Chart al categoriilor principale de accidentari')
plt.yticks(np.arange(0, 31, 2))
plt.show()

# 4.3. Heatmap graph for the correlation between injuries
sb.heatmap(injury.corr().loc['Ankle':'OthMembers', 'Ankle':'OthMembers'], cmap='coolwarm', annot=True).\
    set(title = 'Corelograma a accidentarilor')
plt.xticks(rotation=40, ha="right")
plt.show()

# 4.4. Barchart graph for the percentages of injured players

# 4.4.1. Add a new column in the dataframe which contains the calculated percentage of injured players
injury['Player_Inj_Perc'] = ((injury['InjuredPlayers'] / injury['PlayerNumbers']) * 100)\
    .map('{:.2f}'.format).astype(float)
print(injury)

# 4.4.2. Create the graph
x = injury['Abbreviation']
y = injury['Player_Inj_Perc']
culori_echipe = ['red', 'maroon', 'dodgerblue', 'indianred', 'mediumblue',
                 'cornflowerblue', 'blue', 'gainsboro', 'gold', 'mediumpurple',
                 'crimson', 'deepskyblue', 'red', 'black', 'indianred',
                 'mistyrose', 'navy', 'yellowgreen', 'maroon', 'darkorange']
plt.yticks(np.arange(0, y.max(), 10))
for bar in plt.bar(x, height = y, width=.7, color=culori_echipe):
    yval = bar.get_height()
    plt.text(bar.get_x(), yval + .5, yval)
plt.title("Procentajul jucatorilor accidentati, in functie de echipa")
plt.show()

# V. Creating the Dataframe with the new data and the ranking of the championship

# 5.1. Create the teams ranking based on injury numbers
inj_numb_class = (injury[['TeamName', 'InjuryNumbers']].copy()).\
    sort_values(by = ['InjuryNumbers'], ascending=False).reset_index(drop=True)
inj_numb_class['Inj_Numb_Pos'] = [i for i in range(1, 21)]
print(inj_numb_class)

# 5.2. Create the teams ranking based on the percentages of injured players
player_inj_perc_class = (injury[['TeamName', 'Player_Inj_Perc']].copy()).\
    sort_values(by = ['Player_Inj_Perc'], ascending=False).reset_index(drop=True)
player_inj_perc_class['Player_Inj_Perc_Pos'] = [i for i in range(1, 21)]
print(player_inj_perc_class)

# 5.3. Create the dataframe of final ranking
BPL_data = {
    'Clas_Pos':[i for i in range(1, 21)],
    'TeamName': ['Manchester City', 'Manchester United', 'Liverpool', 'Chelsea', 'Leicester City',
                 'West Ham United', 'Tottenham Hotspur', 'Arsenal', 'Leeds United', 'Everton',
                 'Aston Villa', 'Newcastle United', 'Wolverhampton Wanderers', 'Crystal Palace',
                 'Southampton', 'Brighton & Hove Albion', 'Burnley', 'Fulham',
                 'West Bromwich Albion', 'Sheffield United'],
    'Points':[86, 74, 69, 67, 66, 65, 62, 61, 59, 59, 55, 45, 45, 44, 43, 41, 39, 28, 26, 23],
    'Win':[27, 21, 20, 19, 20, 19, 18, 18, 18, 17, 16, 12, 12, 12, 12, 9, 10, 5, 5, 7],
    'Draw':[5, 11, 9, 10, 6, 8, 8, 7, 5, 8, 7, 9, 9, 8, 7, 14, 9, 13, 11, 2],
    'Lose':[6, 6, 9, 9, 12, 11, 12, 13, 15, 13, 15, 17, 17, 18, 19, 15, 19, 20, 22, 29],
    'Gls_Dif':[+51, +29, +26, +22, +18, +15, +23, +16, +8, -1, +9, -16,
               -16, -25, -21, -6, -22, -26, -41, -43]
}
BPL_class = pd.DataFrame(BPL_data)
print(BPL_class)

# 5.4. Create the final dataframe using merge and save it as csv
tabel_final = pd.merge(pd.merge(BPL_class, inj_numb_class, on = 'TeamName'),
                       player_inj_perc_class, on = 'TeamName')
print(tabel_final)
tabel_final.to_csv('BPL_Ranking.csv', index=False)
