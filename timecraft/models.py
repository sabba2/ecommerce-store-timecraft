from . import db

watch_category_association = db.Table(
    'watch_category_association',
    db.Column('category_id', db.Integer, db.ForeignKey('watch_categories.id')),
    db.Column('watch_id', db.Integer, db.ForeignKey('watches.id')),
    db.PrimaryKeyConstraint('category_id', 'watch_id')
)
class WatchCategory(db.Model):
    __tablename__='watch_categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}"

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('watch_id',db.Integer,db.ForeignKey('watches.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'watch_id') )

class Watch(db.Model):
    __tablename__='watches'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128),nullable=False)
    description = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    brand = db.Column(db.String(64), nullable=False)
    movement_type = db.Column(db.String(64), nullable=False) 
    dial_colour = db.Column(db.String(32), nullable=False)
    strap_type = db.Column(db.String(32), nullable=False)
    style = db.Column(db.String(32), nullable=False)
    material = db.Column(db.String(32), nullable=False)
    collection = db.Column(db.String(32), nullable=False)
    glass = db.Column(db.String(32), nullable=False)
    water_resistance = db.Column(db.String(32), nullable=False)
    featured = db.Column(db.Boolean, default=False)
    quantity = db.Column(db.Integer, default=1)
    # Watches can have 1 to many Watch Categories.
    categories = db.relationship('WatchCategory', secondary=watch_category_association, backref='watches')
    
    def __repr__(self):
        return f"Id: {self.id}, Name: {self.name}, Description: {self.description}, Image: {self.image}, Price: {self.price}, Brand: {self.brand}, Movement Type: {self.movement_type}, Dial Colour: {self.dial_colour}, Strap Type: {self.strap_type}, Style: {self.style}, Material: {self.material}, Collection: {self.collection}, Glass: {self.glass}, Water Resistance: {self.water_resistance}, Featured: {self.featured}, Categories: {self.categories}"


class Order(db.Model):
    __tablename__='orders'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, default=False)
    firstname = db.Column(db.String(64))
    surname = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address = db.Column(db.String(128))
    totalcost = db.Column(db.Float)
    date = db.Column(db.DateTime)
    watches = db.relationship("Watch", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        return f"id: {self.id}, Status: {self.status}, Firstname: {self.firstname}, Surname: {self.surname}, Email: {self.email}, Phone: {self.phone}, Address: {self.address}, Date: {self.date}, Watches: {self.watches}, Total Cost: {self.totalcost}"
