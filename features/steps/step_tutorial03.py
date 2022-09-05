from behave import *
from blender import Blender
from hamcrest import *


@given(u'I put "{thing}" in a blender')
def step_impl(context, thing):
    context.blender = Blender()
    context.blender.add(thing)


@when(u'I switch on blender')
def step_impl(context):
    context.blender.switch_on()


@then(u'it should turn into "{other_thing}"')
def step_impl(context, other_thing):
    assert_that(context.blender.result, equal_to(other_thing))
