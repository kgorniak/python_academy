from behave import *


@when("Select category and subcategory")
def step_impl(context):
    context.home_page.select_random_category()
    context.home_page.select_random_subcategory()


@then("Products appear")
def step_impl(context):
    assert context.home_page.get_visible_products()


@when("Select brand")
def step_impl(context):
    context.home_page.select_random_brand()
