from flask import Blueprint, render_template, request, redirect, url_for
from app.decorators import login_required
product_routes = Blueprint('product_routes', __name__)


products = []


@product_routes.route('/products')
@login_required
def index():
    return render_template('products/index.html', products=products)



@product_routes.route('/products/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
      
        new_product = {
            'id': len(products) + 1,
            'name': request.form['name'],
            'price': request.form['price']
        }
        products.append(new_product)
        return redirect(url_for('product_routes.index')) 
    return render_template('products/create.html')



@product_routes.route('/products/update/<int:product_id>', methods=['GET', 'POST'])
@login_required
def update(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    if not product:
        return "Product not found", 404
    if request.method == 'POST':
        product['name'] = request.form['name']
        product['price'] = request.form['price']
        return redirect(url_for('product_routes.index'))
    return render_template('products/update.html', product=product, product_id=product_id)




@product_routes.route('/products/delete/<int:product_id>', methods=['POST'])
@login_required
def delete(product_id):
    product = next((product for product in products if product['id'] == product_id), None)
    products.remove(product)
    for i, product in enumerate(products):
        product['id'] = i + 1  
    
    return redirect(url_for('product_routes.index')) 
