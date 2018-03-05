from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class CatWahl(Page):
    form_model = 'player'
    form_fields = ['category']


class MyWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.subsession.set_groups()

class Ergebnis(Page):
    pass

page_sequence = [
    CatWahl,
    MyWaitPage,
    Ergebnis
]
