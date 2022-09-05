from behave import *
from hamcrest import *
from Frobulator import Frobulator


@given(u'a sample text loaded into frobulator')
def step_impl(context):
    frobulator = getattr(context,'frobulator',None)
    if not frobulator:
        context.frobulator = Frobulator()
    context.frobulator.text = context.text



@when(u'we activate the frobulator')
def step_impl(context):
    context.frobulator.activate()


@then(u'we will find it similar to {language}')
def step_impl(context,language):
    assert_that(language,equal_to(context.frobulator.seems_like_language()))

