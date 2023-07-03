'''
Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
'''
'''''
scorecard = []
for _ in range(int(input('How many student: '))):
    name = input('Input names: ')
    score = float(input('Input score: '))
    scorecard.append([name, score])
scorecard.sort(key=lambda x: x[1])
names = []
lowest_score = scorecard[0][1]
second_lowest = 0
for i in range(len(scorecard)):
    if scorecard[i][1] > lowest_score and second_lowest == 0:
        second_lowest = scorecard[i][1]
    elif second_lowest != 0 and scorecard[i][1] == second_lowest:
        names.append(scorecard[i][0])

names.sort()

for name in names:
    print(name)
'''
score_list = []
for _ in range(int(input('How many student: '))):
        name = input('Input names: ')
        score = float(input('Input score: '))

        score_list.append([name, score])

second_highest = sorted(set([score for name,score in score_list]))[1]
print('\n'.join(sorted([name for name, score in score_list if score == second_highest])))
