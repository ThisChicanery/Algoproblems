def tournamentWinner(competiotors, results):
    d = {}

    for i in range(len(competiotors)):
        if results[i] == 0:

            d[competiotors[i][1]] = d.get(competiotors[i][1],0) + 3

        else:
            d[competiotors[i][0]] = d.get(competiotors[i][0],0) + 3
    
    winner = max(d, key=d.get)

    return winner


x = [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
y = [0, 0, 1]

    
print(tournamentWinner(x, y))