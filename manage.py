from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from App.main import app, db

from App.controllers import (
    create_user,
    create_customer,
    create_product,
    create_admin,
    get_all_products,
    get_product_by_name
)

manager = Manager(app)
migrate = Migrate(app, db)

#add migrate command
manager.add_command('db', MigrateCommand)

#add initDB command
@manager.command
def initDB():
    db.create_all(app=app)
    print('database initialized!')

@manager.command
def users():
    #newUser = create_user("1101", "Kim", "Jones","kim@email.com", "kimpass")
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1200","Mary", "White","mary@email.com","mary")
    #print(newUser.toDict())
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1300","Michael", "Doe","michael@email.com","michael")
    #newCustomer = create_customer(newUser)

    #newUser = create_user("1400","Caleb", "Danvers","Caleb@email.com","caleb")
    #newAdmin = create_admin(newUser,"Pharmacist")

    #newUser = create_user("1500","Pogue", "Perry","pogue@email.com","pogue")
    #newAdmin = create_admin(newUser,"Pharmacist")

    newUser = create_user("1600","Reid", "Garwin","reid@email.com","reid")
    newAdmin = create_admin(newUser,"Cashier")

    newUser = create_user("1700","Tyler", "Simms","tyler@email.com","tyler")
    newCustomer = create_customer(newUser)

    print(newCustomer.toDict())
    print(newAdmin.toDict())

@manager.command
def products():
    #newProd = create_product("Advil","Pain Reliever","",2)
    #newProd = create_product("Panadol","Pain Reliever","",2)
    #newProd = create_product("Tylenol","Pain Reliever","",5)
    #products = get_all_products()
    product = get_product_by_name("Advil")
    print(product)

if __name__ == "__main__":
    manager.run()

