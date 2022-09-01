from behave import *
from hamcrest import *


class NinjaFight(object):
    def __init__(self, with_ninja_level=None):
        self.with_ninja_level = with_ninja_level
        self.opponent = None

    def decision(self):

        assert self.with_ninja_level is not None
        assert self.opponent is not None

        if self.opponent == 'Chuck Norris':
            return 'run for life'
        if 'black-belt' in self.with_ninja_level:
            return 'engage the opponent'
        else:
            return 'run for life'


@given(u'the ninja has a {achievement}')
def step_ninja_has(context, achievement):
    context.ninja_fight = NinjaFight(achievement)


@when(u'attacked by a {opponent_role}')
def step_attacked_by_a(context, opponent_role):
    context.ninja_fight.opponent = opponent_role


@when(u'attached by {opponent}')
def step_attacked(context, opponent):
    context.ninja_fight.opponent = opponent


@then(u'the ninja should {decision}')
def step_decision(context, decision):
    assert_that(decision, equal_to(context.ninja_fight.decision()))
