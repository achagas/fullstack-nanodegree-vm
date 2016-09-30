from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

meuRestaurant = Restaurant(name = "Lanche do Castelao")
session.add(meuRestaurant)
session.commit()
session.query(Restaurant).all()

xsalada = MenuItem(name = "X-Salada", description = "Carne, ovo, verdura, presunto de peru e queijo no pao de forma", course = "Entrada", price = "R$8.00", restaurant = meuRestaurant)
session.add(xsalada)
session.commit()
session.query(MenuItem).all()


items = session.query(MenuItem).all()
for item in items:
	print item.name


veggieBurgers = session.query(MenuItem).filter_by(name = 'Verggie Burger')
for verggieBurger in veggieBurgers:
	print verggieBurger.id
	print verggieBurger.price
	print verggieBurger.restaurant.name
	print "\n"
