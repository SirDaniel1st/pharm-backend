from flask import Blueprint, redirect, render_template, request, abort, jsonify
from flask_jwt import jwt_required, current_identity
from flask_cors import CORS
import json

order_views = Blueprint('order_views', __name__, template_folder='../templates')

from App.controllers import (
    get_user,
    create_cust_order,
    get_orders,
    get_orders_by_user,
    get_product_by_slug,
    create_order_product,
    get_order_by_id,
    update_order_by_id,
    add_order_products,
)

# get all orders
@order_views.route('/orders', methods=["GET"])
@jwt_required()
def display_orders():
    orderList = get_orders()
    return jsonify(orderList)

# get user orders
@order_views.route('/user-orders', methods=["GET"])
@jwt_required()
def display_user_orders():
    orderList = get_orders_by_user(current_identity.email)
    return jsonify(orderList)

# create order
@order_views.route('/create-order', methods=["POST"])
@jwt_required()
def create_order():
    item_count = request.json.get('item_count')
    order_total = request.json.get('order_total')
    status = request.json.get('status')
    customer = get_user(current_identity.email) #parent
    newOrder = create_cust_order(customer, item_count, order_total, status) #association

    cart = request.json.get('cart') #call get product by slug for list of products
    orderProductList = []
    for product in cart:
        slug = product["slug"]
        #find product by slug and add to list of products
        productObj = get_product_by_slug(slug)
        newOrderProduct = create_order_product(newOrder, productObj)
        orderProductList.append(newOrderProduct)

    add_order_products(newOrder, orderProductList)
    response = jsonify(newOrder.toDict())
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

# get specific order by ID
@order_views.route('/order', methods=["GET"])
def get_order():
    order_id = request.args.get("id")
    order = get_order_by_id(order_id)
    return jsonify(order.toDict())

# update order status endpoint
@order_views.route('/update-order', methods=["PUT"])
@jwt_required()
def update_order():
    order_id = request.json.get("id")
    status = request.json.get("status")
    order = update_order_by_id(order_id, status)
    return jsonify(order.toDict())


