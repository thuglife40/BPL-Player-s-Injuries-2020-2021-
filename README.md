# BPL-Player-s-Injuries-2020-2021-
This repository is a reupload of my project, which was initially posted here: https://github.com/mpara30/Player-injuries

The main idea of this study started from one of my favorite sports (football/soccer) and I decided to analyze if the number of injuries in the Premier League, for the 2020-2021 season, would have had a certain influence on the competing teams and, implicitly, on the positioning their final ranking. It started as a project for a MS university course assignment and, later, I continued to work on it as a final assignment for a Python course.

The main csv file was made up of data, taken from certain sites (https://www.football-lineups.com/tourn/FA_Premier_League_2020-2021/Table/; https://www.sporcle.com/games/easterbunny/football-club--by-abbreviations-/results; https://en.as.com/resultados/futbol/inglaterra/equipos/) that record such statistics, and organized by columns in this way:

TeamName = Premier League team names

Abbreviation = names abbreviation of these teams

PlayerNumbers = total number of players in the squad

InjuredPlayers = total number of injured players in the squad

Ankle = number of ankle injuries

Back = number of back injuries

Calf = number of calf injuries

COVID19 = number of players infected with COVID19 virus

Foot = number of foot injuries (everything related to their lower part)

Groin = number of groin injuries

Hamstring = number of hamstring injuries

Head = number of injuries in the cranial area

Knee = number of injuries in the knee area

Knock = number of injuries sustained as a result of simple blows

Muscles = number of injuries affecting all muscles in the body

Shoulder = number of injuries in shoulder area

Thigh = number of injuries in thigh area

OthCauses = number of injuries arising from other causes (diseases, lack of physical training etc.)

OthMembers = number of injuries in minor areas (abdomen, hip, hand, neck, etc.)

The python script was organized in the following points, to make it easier to implement the ideas related to this analysis:

I. Reading and editing the original file

II. Creating a Dataframe with the percentages of each type of injury, related to their total number, for each team

III. Creating a Dataframe for the total of each separate category

IV. Analyzing graphs

V. Creating the Dataframe with the new data and the ranking of the championship


I. Reading and editing the original file

I imported the csv file into python and I created a new column, called "InjuryNumbers", which contains the total number of injuries for each
team. I did this, because the number of injured players cannot coincide with the number of injuries in each team, because a player can be injured several times and suffer from the same type of injury or from different ones. The "InjuryNumbers" column was added to the 4th position in the table and then the data was saved in a new file ("Injuries_Updated.csv"). Furthermore, we have displayed the teams according to "Injury Numbers" and their decreasing values, to see if there is any difference compared to their positioning in the final ranking. I also wanted to see which categories of injuries are more pronounced in each team, so I built a stacked bar graph. Moreover, we have created a Series-type list, through which we can observe the important categories of injuries for each team.

II. Creating a Dataframe with the percentages of each type of injury, related to their total number, for each team

Next, I wanted to see what is the percentage of each injury, compared to their total number, for each team, so I created a function, which return these values in a matrix and allocate these values for each team. The new data was saved in "Percentages per teams.csv", and their 2-decimal approximate versions were saved in "Aprox. Percentages per teams.csv". To avoid certain variable recognition problems, I re-imported saved data from the last csv file and then I made 2 horizontal stacked bar graphs, to observe the percentages of each type of injury from all teams. The first graph projects only one bar, because it is built to display only one team, the abbreviation of that team being written from the input. The second graph projects separately all the teams and the injury percentages from each team.

III. Creating a Dataframe for the total of each separate category

Further, I imported the data from "Injuries_Updated.csv", I created a new row for each column, to display the total of their values, and I saved them in "Injuries_with_TOTAL.csv". Then, I wanted to see what is the percentage of each type of injury, compared to the total. For this, I copied from the previous dataframe only the row with the total, related to "InjuryNumbers", and the injury categories, then I created a new column, called "Percent", to save those percentages. In fact, I named "Categories" the column related to categories and I deleted the row related to "InjuryNumbers", in order to create a graph corresponding to these data.

IV. Analyzing graphs

Next, I built several graphs. In order to observe the percentages related to each category, compared to the total number of injuries, I created a bar-chart and a treemap. Taking into account the total number of injuries, depending on their types, I created a bar-chart for the values of each main type of injury in a team. Thus, I projected the values for the 'Ankle', 'Knock' and 'Thigh' categories, to see how much they vary depending on the team. I also built a heatmap graph for the correlation between injuries, along with another bar-chart, for the percentage of injured players. Moreover, in order to create the last mentioned graph, I created a column called "Player_Inj_Perc" in the original dataframe, in order to save those percentage values.

V. Creating the Dataframe with the new data and the ranking of the championship

Further, from the original Dataframe, I extracted the necessary columns and I made two descending sorts, applied according to "TeamName": the first one for "InjuryNumbers", where the column "Inj_Numb_Pos" was added with the positions of the teams according to this sort , and the second one for "Player_Inj_Perc", where a new column was created also for the positions of the teams, called "Player_Inj_Perc_Pos". Of course, those columns were saved in two different dataframe variables (the first one with the number of injuries, the second one for the percentage of injured players). Then, through a dictionary, I created a dataframe, which contains a part of the Premier League ranking for the 2020-2021 season. To this dataframe, I added the data from the other two recently created dataframes ("inj_numb_class" and "player_inj_perc_class"), to see if there is any connection between the number of injuries, the percentage of injured players and the final position of the teams at the end of the championship.
