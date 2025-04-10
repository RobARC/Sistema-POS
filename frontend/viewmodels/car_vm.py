import streamlit as st


def init_cart():
    if 'cart' not in st.session_state:
        st.session_state['cart'] = {}  # id_producto: {"producto": {}, "cantidad": 0}


def add_to_cart(product):
    init_cart()
    pid = product["id"]
    if pid in st.session_state['cart']:
        st.session_state['cart'][pid]["cantidad"] += 1
    else:
        st.session_state['cart'][pid] = {"producto": product, "cantidad": 1}


def remove_from_cart(product_id):
    if product_id in st.session_state['cart']:
        del st.session_state['cart'][product_id]

def update_quantity(product_id, quantity):
    if product_id in st.session_state['cart']:
        if quantity > 0:
            st.session_state['cart'][product_id]["cantidad"] = quantity
        else:
            remove_from_cart(product_id)

def calculate_totals():
    subtotal = 0
    total_items = 0
    for item in st.session_state['cart'].values():
        price = item["producto"]["price"]
        qty = item["cantidad"]
        subtotal += price * qty
        total_items += qty
    return subtotal, total_items

def calculate_points(subtotal):
    return int(subtotal // 10)  # 1 punto por cada 10 de compra

def apply_discount(points_to_redeem, point_value=0.5):
    """Aplica descuento usando puntos. Cada punto vale `point_value`."""
    discount = points_to_redeem * point_value
    return discount
