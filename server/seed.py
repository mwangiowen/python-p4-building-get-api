# app/seed.py

from faker import Faker
from app.models import db, Bakery, BakedGood

fake = Faker()

with db.app.app_context():
    Bakery.query.delete()
    BakedGood.query.delete()

    bakeries = [Bakery(name=fake.company()) for _ in range(5)]
    db.session.add_all(bakeries)

    baked_goods = []
    for bakery in bakeries:
        for _ in range(3):
            baked_good = BakedGood(
                name=fake.word(), price=fake.random.uniform(1, 20), bakery=bakery
            )
            baked_goods.append(baked_good)

    db.session.add_all(baked_goods)
    db.session.commit()
