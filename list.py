team=['virat','dhoni','raina','rohit']
team.insert(4, 'dhawan')
print('list: ',team)
z=['python','java','c','html']
team.extend(z)
print(team)
print(len(team))
del team[0]
for x in team:
    print(x)
    if "virat" in team:
        print(" yes,'virat' is in team")
        team.clear()
        print(team)
        
        
