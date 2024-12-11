from flask import Blueprint, render_template, request, redirect, url_for
from app.decorators import login_required 
category_routes = Blueprint('category_routes', __name__)

categories = []

@category_routes.route('/categories')
@login_required

def index():
    return render_template('categories/index.html', categories=categories)


@category_routes.route('/categories/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        new_category = {
            'id': len(categories) + 1,
            'name': request.form['name']
        }
        categories.append(new_category)
        return redirect(url_for('category_routes.index'))
    return render_template('categories/create.html')


@category_routes.route('/categories/update/<int:category_id>', methods=['GET', 'POST'])
@login_required
def update(category_id):
    category = next((category for category in categories if category['id'] == category_id), None)
    if not category:
        return "Category not found", 404
    if request.method == 'POST':
        category['name'] = request.form['name']
        return redirect(url_for('category_routes.index'))
    return render_template('categories/update.html', category=category, category_id=category_id)


@category_routes.route('/categories/delete/<int:category_id>', methods=['POST'])
@login_required
def delete(category_id):
    category = next((category for category in categories if category['id'] == category_id), None)
    categories.remove(category)
    for i, category in enumerate(categories):
        category['id'] = i + 1  
    return redirect(url_for('category_routes.index'))
