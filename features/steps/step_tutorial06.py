from behave import *
from hamcrest import *
from test_util import NamedNumber
from Model import Model


@given(u'a set of specific users')
def step_impl(context):
    model = getattr(context, 'model', None)
    if not model:
        context.model = Model()
    for row in context.table:
        context.model.add_users(row['name'], department=row['department'])


@when(u'we count the number of people in each department')
def step_impl(context):
    context.model.count_persons_per_dept()


@then(u'we will find {count} people in "{department}"')
def step_impl(context, count, department):
    count_ = NamedNumber.from_string(count)
    assert_that(count_, equal_to(context.model.get_head_count(department=department)))


@then(u'we will find one person in "{department}"')
def step_impl(context, department):
    assert_that(1, equal_to(context.model.get_head_count(department=department)))
