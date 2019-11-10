from behave import *


@given('we have behave installed')
def step_impl(context):
    pass


@when('we implement a test')
def step_impl(context):
    result = True is not False
    assert result


@then('behave will test it for us!')
def step_impl(context):
    pass
