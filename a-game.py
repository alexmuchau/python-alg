# teams = [['a', 20, 7, 5, 3, 3], ['b', 10, 7, 5, 3, 2],
#          ['c', 4, 4, 6, 3, 3], ['d', 20, 7, 5, 3, 2],
#          ['E', 22, 4, 6, 3, 3], ['F', 23, 7, 5, 3, 2]]
teams = []
isExistT1 = False
isExistT2 = False

# getting info
for match in range(6):
    print('PARTIDA NUMERO {}'.format(match + 1))
    nameT1 = str(input('Em um modelo Time1 x Time2, quem foi o Time1? '))
    nameT2 = str(input('Quem foi o Time2? '))
    print('')

    golsT1 = int(input('Quantos gols o time {} fez? '.format(nameT1)))
    golsT2 = int(input('Quantos gols o time {} fez? '.format(nameT2)))
    print('')

    yellowCardsT1 = int(
        input('Quantos cartões amarelo o time {} teve? '.format(nameT1)))
    yellowCardsT2 = int(
        input('Quantos cartões amarelo o time {} teve? '.format(nameT2)))
    print('')

    redCardsT1 = int(
        input('Quantos cartões vermelho o time {} teve? '.format(nameT1)))
    redCardsT2 = int(
        input('Quantos cartões vermelho o time {} teve? '.format(nameT2)))
    print('')

    againstGolsT1 = golsT2
    againstGolsT2 = golsT1

    if(golsT1 > golsT2):
        pointsT1 = 3
        pointsT2 = 0
    else:
        if(golsT2 > golsT1):
            pointsT1 = 0
            pointsT2 = 3
        else:
            pointsT1 = 1
            pointsT2 = 1

    team1 = [nameT1, pointsT1, golsT1,
             againstGolsT1, yellowCardsT1, redCardsT1]
    team2 = [nameT2, pointsT2, golsT2,
             againstGolsT2, yellowCardsT2, redCardsT2]

    teamsLength = len(teams)
    if(teamsLength >= 1):
        for i in range(teamsLength):
            contT1 = teams[i].count(nameT1)
            contT2 = teams[i].count(nameT2)

            if(contT1 == 1):
                isExistT1 = True
                indexT1 = i
            if(contT2 == 1):
                isExistT2 = True
                indexT2 = i

        if(isExistT1 == True):
            for i in range(6):
                if(i >= 1):
                    changedItem = team1[i]
                    changedItem = changedItem + teams[indexT1][i]

                    teams[indexT1][i] = changedItem
        else:
            teams += [team1]

        if(isExistT2 == True):
            for i in range(6):
                if(i >= 1):
                    changedItem = team2[i]
                    changedItem = changedItem + teams[indexT2][i]

                    teams[indexT2][i] = changedItem
        else:
            teams += [team2]
    else:
        teams += [team1] + [team2]

    print('')
    print('')


# filtering the table
teamsLength = len(teams)
ranked = []
rankLength = 1
criterionType = 1

print(teams)
print("")

for i in range(teamsLength):
    if(i == 0):
        ranked = [teams[0]]
    else:
        for rank in range(rankLength):
            if(teams[i][1] > ranked[rank][1]):
                ranked.insert(rank, teams[i])
                break
            else:
                if(rank == rankLength - 1):
                    if(teams[i][1] < ranked[rank][1]):
                        ranked.append(teams[i])

                if(teams[i][criterionType] == ranked[rank][criterionType]):
                    for criterionType in range(7):
                        criterionType = criterionType + 1
                        if(criterionType < 4):
                            # print(criterionType)
                            if(teams[i][criterionType] > ranked[rank][criterionType]):
                                ranked.insert(rank, teams[i])
                                break
                            else:
                                if(rank == rankLength - 1):
                                    if(teams[i][criterionType] < ranked[rank][criterionType]):
                                        ranked.append(teams[i])
                                        break
                        else:
                            # print(criterionType)
                            if(teams[i][criterionType] < ranked[rank][criterionType]):
                                ranked.insert(rank, teams[i])
                                break
                            else:
                                if(rank == rankLength - 1):
                                    if(teams[i][criterionType] > ranked[rank][criterionType]):
                                        ranked.append(teams[i])
                                        break
                    break

    rankLength = len(ranked)

print('================SEM RANK=============================')
print(" | TIME  |  P  |  G  |  GC  |  YC  |  RC  |")
for lines in range(teamsLength):
    print(" | ", teams[lines][0], " | ", teams[lines][1], " | ", teams[lines][2],
          " | ", teams[lines][3], " | ", teams[lines][4], " | ", teams[lines][5], )

print("")
print('================RANK=============================')
print(" | TIME  |  P  |  G  |  GC  |  YC  |  RC  |")
for lines in range(teamsLength):
    print(" | ", ranked[lines][0], " | ", ranked[lines][1], " | ", ranked[lines][2],
          " | ", ranked[lines][3], " | ", ranked[lines][4], " | ", ranked[lines][5], )

winner = ranked[0]

print("")
print("O GRANDE VENCEDOR FOI O TIME",
      winner[0], "!! COM SEUS", winner[1], "PONTOS!! PARABENS")

# print(ranked)
# print("")
# print(teams)
