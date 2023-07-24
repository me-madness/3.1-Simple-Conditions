firstCompetition = int(input())
secondCompetition = int(input())
thirtCompetition = int(input())

minutes = 0
seconds = firstCompetition + secondCompetition + thirtCompetition

if seconds > 60:
    minutes += 1
    seconds = seconds - 60
if seconds > 60:
    minutes += 1
    seconds = seconds - 60    
if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')
        