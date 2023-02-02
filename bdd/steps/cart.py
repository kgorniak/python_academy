from behave import *


@when("I navigate to cart")
def step_impl(context):
    context.cart_page.navigate_to_cart()


@then("I see empty cart")
def step_impl(context):
    assert context.cart_page.check_if_empty_cart()


@when("I add {number_of_items} items of {item_name} to the cart")
def step_impl(context, number_of_items, item_name):
    context.products_page.search_product(item_name)
    context.products_page.go_to_view_product()
    context.view_product_page.set_number_of_items_and_add_to_cart(number_of_items)


@step("I proceed to checkout")
def step_impl(context):
    context.cart_page.proceed_to_checkout()


@then("I see login modal")
def step_impl(context):
    context.cart_page.check_if_login_modal_visible()


@then("I calculate value of cart")
def step_impl(context):
    """Calculate if sum of items equals total sum of cart"""
    assert sum(context.checkout_page.get_items_prices()) == context.checkout_page.get_total_price()
