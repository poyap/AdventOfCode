with open('2.txt' , 'r') as f:
    total_score = 0
    correspond_words = {
        'A': 'rock',
        'X': 'lose',
        'Y': 'draw',
        'B': 'paper',
        'Z': 'win',
        'C': 'scissor',
        }
    wins_stat = {
        'rock' : ['scissor', 1],
        'paper': ['rock', 2],
        'scissor': ['paper', 3],
    }
    for round in f.readlines():
        component, you = round.split()
        component = correspond_words[component]
        you = correspond_words[you]
        if you == 'draw':
            you = component
            total_score += int(wins_stat[you][-1]) + 3
        elif you == 'lose':
            you = wins_stat[component][0]
            total_score += int(wins_stat[you][-1]) 
        else:
            you = wins_stat[wins_stat[component][0]][0]
            total_score += int(wins_stat[you][-1]) + 6
    print(total_score)
        

# A rock, B paper, C scissors
# X rock, Y paper , Z scissors 
