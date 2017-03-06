# a minimalistic approach to the api that serves the lineup div in the match page
# a lot of things are left out from that api response like birth info of players
# usual positions of players etc.
#
# For reference, the original api response in the website
#
##################################################
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import json
# import pprint
#
# pp = pprint.PrettyPrinter(indent=4)
# matchUrl = "https://www.premierleague.com/match/14274"
#
# driver = webdriver.PhantomJS()
# driver.get(matchUrl)
# html = driver.page_source
# matchObj = BeautifulSoup(html, "html5lib")
# comm = matchObj.find("div",{"class":"mcTabsContainer"})
# match_data = json.loads(comm['data-fixture'])
# pp.pprint(match_data['teamLists'])
#
##################################################

class teamList:
    def __init__(self, teamName='', teamId = ''):
        self.team = {}
        self.starting_eleven = []
        self.substitutes = []
        self.formation = {}
        self.teamId = teamId
        if teamName != '':
            self.teamName = teamName
        else:
            raise AttributeError("team name can't be blank")

    def addPlayer(self, name, id, shirtNumber, matchPosition, captain = False, sub = False):
        player = {}
        player['name'] = name
        player['id'] = id
        player['shirtNumber'] = shirtNumber
        player['matchPosition'] = matchPosition
        player['captain'] = captain

        if sub == False and len(self.starting_eleven)<11:
            self.starting_eleven.append(player)
        else:
            self.substitutes.append(player)
        return

    def addFormation(self, label, players):
        self.formation['label'] = label
        self.formation['players'] = players
        return

    def get(self):
        self.team['teamName'] = self.teamName
        self.team['teamId'] = self.teamId
        self.team['formation'] = self.formation
        self.team['starting_eleven'] = self.starting_eleven
        self.team['substitutes'] = self.substitutes
        return self.team

