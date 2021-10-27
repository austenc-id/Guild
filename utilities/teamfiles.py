class teamfiles:
  class team:
    def readfile():
        import json
        file = open('X:\\dungeon-dex\\data\\teams.json')
        file = file.read()
        file = json.loads(file)
        file.sort(key=lambda team: team['name'])
        return file
    def writefile(teamlist):
        import json
        teamlist.sort(key=lambda team: team['name'])
        teamlist = json.dumps(teamlist)
        file = open('X:\\dungeon-dex\\data\\teams.json', 'w')
        file.write(teamlist)
  class member:
    def readfile():
        import json
        file = open('X:\\dungeon-dex\\data\\members.json')
        file = file.read()
        file = json.loads(file)
        file.sort(key=lambda member: member['name'])
        return file
    def writefile(memberlist):
        import json
        memberlist.sort(key=lambda member: member['name'])
        memberlist = json.dumps(memberlist)
        file = open('X:\\dungeon-dex\\data\\members.json', 'w')
        file.write(memberlist)