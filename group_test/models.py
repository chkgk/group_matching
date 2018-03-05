from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from pprint import pprint

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'group_test'
    players_per_group = None
    num_rounds = 1

    category_names = ['A', 'B', 'C', 'D', 'E']


class Subsession(BaseSubsession):
    def set_groups(self):

        # Create category lists
        cat_lists = dict.fromkeys(Constants.category_names)
        for element in cat_lists:
            cat_lists[element] = []

        # sort players into category lists by their choices
        for player in self.get_players():
            for cat_name in cat_lists:
                if player.category == cat_name:
                    cat_lists[cat_name].append(player)
                    
        # berechne anzahl nötiger Gruppen
        # für jede Gruppe gehe durch alle categorien
        # nimm jeweils einen spieler aus jeder cat, startend bei der ersten
        # wenn keine spieler mehr in der gruppe, nimm nächste gruppe, bis gruppe voll

        total_players = len(self.get_players())
        group_size = 5
        number_groups = int(total_players / group_size)


        group_list = []
        for group in range(number_groups):
            group_members = []
            while len(group_members) < group_size:
                for cat_name in cat_lists:
                    if cat_lists[cat_name]:
                        group_members.append(cat_lists[cat_name].pop())

                    if len(group_members) >= group_size:
                        break

                print(len(group_members))
            group_list.append(group_members)

        pprint(group_list)

        self.set_group_matrix(group_list)
        
        group_matrix = self.get_group_matrix()
        for group in group_matrix:
            for player in group:
                player.my_group_id = group_matrix.index(group) + 1

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    category = models.CharField(choices=Constants.category_names, label="Category?")
    my_group_id = models.IntegerField()