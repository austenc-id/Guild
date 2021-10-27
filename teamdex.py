import sys

paths = ['X:\\dungeon-dex\\','X:\\dungeon-dex\\pokedex\\', 'X:\\dungeon-dex\\teamdex\\']
for path in paths:
  sys.path.append(path)
from pokedex import Pokedex
from data.models import team_models
from utilities.teamfiles import teamfiles

pokedex = Pokedex.build()
qualitydex = pokedex.pop()




memberlist = []
file = teamfiles.member.readfile()
for member in file:
  memberlist.append(member)
teamfiles.member.writefile(memberlist)

teamlist = []
file = teamfiles.team.readfile()
for team in file:
  teamlist.append(team)
addnew = input('add new team?\n')
if addnew == 'yes':
  team = team_models.model.Team.add(pokedex, qualitydex)
  team = team[0]
  memberlist = team[1]
  teamlist.append(team)
teamfiles.team.writefile(teamlist)

teamdex = []
for team in teamlist:
  team_members = []
  team_memberlist = []
  for team_member in team['members']:
    for member in memberlist:
      if team_member['name'] == member['name']:
        team_member = member
        team_members.append(team_member)
    team.update({'members': team_members})
    for pokemon in pokedex:
      for team_member in team['members']:
        if team_member['species'] == pokemon.species:
          team_member.update({'species': pokemon})
          team_member = team_models.model.Member(team_member)
          team_memberlist.append(team_member)
  team = team_models.model.Team(team['name'], team_memberlist)
  teamdex.append(team)