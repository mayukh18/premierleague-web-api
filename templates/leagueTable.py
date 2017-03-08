# formats the league table data into a structure. Pretty self explaining.
#
# For reference, the table can be scraped here on official site
#
##################################################
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# Url = "https://www.premierleague.com/tables"
# driver = webdriver.PhantomJS()
# driver.get(Url)
# html = driver.page_source
#
# tableObj = BeautifulSoup(html, "html5lib")
# table = tableObj.find("tbody",{"class":"tableBodyContainer"})
# print(table)
##################################################



class leagueTable:
    def __init__(self):
        self.container = {}
        clubstats = {
            'name': '',
            'played':0,
            'wins':0,
            'draws':0,
            'losses':0,
            'goals_for':0,
            'goals_against':0,
            'goal_difference':0,
            'points':0
        }
        self.table = [clubstats for i in xrange(0,19)]

    def addClub(self, position, name, played, wins, draws, losses, GF, GA, GD, points):
        self.table[position]['name'] = name
        self.table[position]['played'] = played
        self.table[position]['wins'] = wins
        self.table[position]['draws'] = draws
        self.table[position]['losses'] = losses
        self.table[position]['goals_for'] = GF
        self.table[position]['goals_against'] = GA
        self.table[position]['goal_difference'] = GD
        self.table[position]['points'] = points

    def get(self):
        self.container['table'] = self.table
        self.container['UCL_spots'] = [{'name':self.table[i]['name'],
                                        'played':self.table[i]['played'],
                                        'points':self.table[i]['points']} for i in (0,4)]
        self.container['relegation_spots'] = [{'name':self.table[i]['name'],
                                        'played':self.table[i]['played'],
                                        'points':self.table[i]['points']} for i in (17,20)]
        return self.container


