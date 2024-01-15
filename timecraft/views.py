from flask import Blueprint, render_template, url_for, request, session, flash, redirect
from .models import WatchCategory, Watch, Order, watch_category_association, orderdetails
from datetime import datetime
from .forms import CheckoutForm
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    featured = Watch.query.filter(Watch.featured == True).all()
    return render_template('index.html', featured = featured)

# Category pages
@bp.route('/<string:category_name>')
def watch_categories(category_name):
    watches = Watch.query.join(WatchCategory.watches).filter(WatchCategory.name == category_name).all()
    category = WatchCategory.query.filter(WatchCategory.name == category_name).first()
    return render_template('watchcategories.html', watches = watches, category = category)

# Search functionality
@bp.route('/search', methods=['POST'])
def search():
    search_query = request.form.get('search_query')
    watches = search_watches(search_query)
    return render_template('search.html', watches = watches)

def search_watches(query):
    return Watch.query.filter(Watch.name.ilike(f"%{query}%")).all()

# filter functionality
@bp.route('/<string:category_name>/filtered', methods=['POST'])
def filter(category_name):
    selected_brands = request.form.getlist('brand_filter')
    category_watches = Watch.query.join(WatchCategory.watches).filter(WatchCategory.name == category_name).all()
    category = WatchCategory.query.filter(WatchCategory.name == category_name).first()
    watches = [watch for watch in category_watches if watch.brand in selected_brands]
    return render_template('watchcategories.html', watches = watches, category = category)

# Product details pages
@bp.route('/<int:watch_id>')
def details(watch_id):
    watch = Watch.query.get(watch_id)
    return render_template('details.html', watch = watch)

# Referred to as "Cart" to the user
@bp.route('/order', methods=['POST','GET'])
def order():
    watch_id = request.values.get('watch_id')

    # retrieve order if there is one
    if 'order_id' in session.keys():
        order = Order.query.get(session['order_id'])
        # order will be None if order_id stale
    else:
        # there is no order
        order = None

    # create new order if needed
    if order is None:
        order = Order(status = False, firstname='', surname='', email='', phone='', address='', totalcost=0, date=datetime.now())
        try:
            db.session.add(order)
            db.session.commit()
            session['order_id'] = order.id
        except Exception as e:
            print(f'Failed at creating a new order: {e}')
            order = None
    
    # calcultate totalprice
    totalprice = 0
    
    if order is not None:
        for watch in order.watches:
            totalprice = totalprice + watch.price*watch.quantity
    
    # are we adding an item?
    if watch_id is not None and order is not None:
        watch = Watch.query.get(watch_id)
        if watch not in order.watches:
            try:
                order.watches.append(watch)
                db.session.commit()
            except Exception as e:
                print(f"Error adding item to cart: {str(e)}")
                db.session.rollback()  # Rollback the session to avoid leaving the database in an inconsistent state
                flash('There was an issue adding the item to your cart. Please try again.')
            return redirect(url_for('main.order'))
        else:
            try:
                watch.quantity += 1
                db.session.commit()
            except Exception as e:
                print(f"Error adding item to cart: {str(e)}")
                db.session.rollback()  # Rollback the session to avoid leaving the database in an inconsistent state
                flash('There was an issue adding the item to your cart. Please try again.')
            return redirect(url_for('main.order'))
    
    return render_template('order.html', order = order, totalprice = totalprice)


# Delete specific basket items
@bp.route('/deleteorderitem', methods=['POST'])
def deleteorderitem():
    id=request.form['id']
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
        watch_to_delete = Watch.query.get(id)
        try:
            watch_to_delete.quantity = 1
            order.watches.remove(watch_to_delete)
            db.session.commit()
            return redirect(url_for('main.order'))
        except:
            return 'Problem deleting item from order'
    return redirect(url_for('main.order'))


# Scrap basket
@bp.route('/deleteorder')
def deleteorder():
    if 'order_id' in session:
        order = Order.query.get(session['order_id'])
        for watch in order.watches:
            watch.quantity = 1
        db.session.commit()
        del session['order_id']
        flash('All items deleted')
    return redirect(url_for('main.index'))


@bp.route('/checkout', methods=['POST','GET'])
def checkout():
    form = CheckoutForm() 
    if 'order_id' in session:
        order = Order.query.get_or_404(session['order_id'])
       
        if form.validate_on_submit():
            order.status = True
            order.firstname = form.firstname.data
            order.surname = form.surname.data
            order.email = form.email.data
            order.phone = form.phone.data
            order.address = form.address.data
            totalcost = 0
            for watch in order.watches:
                totalcost = totalcost + watch.price
            order.totalcost = totalcost
            order.date = datetime.now()
            try:
                db.session.commit()
                del session['order_id']
                flash('Your order is complete. Thank you for choosing Timecraft.')
                return redirect(url_for('main.index'))
            except:
                return 'There was an issue completing your order'
    return render_template('checkout.html', form = form)