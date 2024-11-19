from app.models import db, Restaurant, environment, SCHEMA
from sqlalchemy.sql import text

def seed_restaurants():
    nikita_burger = Restaurant(
      owner_id=1,
      name="In-n-Out",
      address="32060 Union Landing Blvd, Union City, CA 94587",
      phone_number="8007861000",
      cuisine="American",
      description="Classic burger chain serving customizable burgers, hand-cut fries & shakes.",
      hours_of_operation="Monday-Friday: 9AM-11:59PM",
      delivery_radius=6,
      cover_image="https://res.cloudinary.com/djuzk5um3/image/upload/v1732042422/in_n_out_cover_image_ofsr26.webp")

    menards = Restaurant(
    owner_id=1,
    name="Menards",
    address="4550 Busy Street",
    phone_number="1234567890",
    cuisine="Hardware",
    description="Ever since Joe was a young sigma Ohioan, he dreamt of owning a Menards. Now you can shop at his franchise location, why not get some nails and plywood for lunch? Wash it down with a crowbar", hours_of_operation="Sunday-Saturday: 8AM-9PM",
    delivery_radius=25,
    cover_image="https://www.cincinnati.com/gcdn/presto/2020/10/01/NREC/b047431f-4184-462f-a239-e2e41926a077-RC_menards_open_announcement_Brimfield_5018.jpg"
    )

    mcdonalds = Restaurant(
        owner_id=2,
        name="McDonalds",
        address="123 That Street",
        phone_number="3049737978",
        cuisine="McDonald's",
        description="You can get food here sometimes you can even get an ice cream. Sometimes the ice manchine broke. We get what we get in this life. McDonald's: I'm mcdonalding it.",
        hours_of_operation="24h",
        delivery_radius=15,
        cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715960913/WuberEats/McDonalds/cover-image_oukkc3.jpg"
    )

    chick_fil_a = Restaurant(
    owner_id=2,
    name="Chick-fil-A",
    address="3290 Atlantic Avenue",
    phone_number="5621234567",
    cuisine="American",
    description="Enjoy delicious, freshly prepared chicken sandwiches, nuggets, and waffle fries. Known for exceptional service and quality, Chick-fil-A offers a variety of tasty options for a satisfying meal.",
    hours_of_operation="Monday-Saturday: 7AM-11PM",
    delivery_radius=2,
    cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715960849/WuberEats/Chick%20Fil%20A/cover-image_iuevu9.jpg"
    )

    taco_bell = Restaurant(
    owner_id=1,
    name="Taco Bell",
    address="2430 Carson St",
    phone_number="3239071358",
    cuisine="Mexican",
    description="Savor bold flavors with a variety of tacos, burritos, and quesadillas. Taco Bell delivers crave-worthy Mexican-inspired fast food with customizable options for every taste.", hours_of_operation="Sunday-Saturday: 8AM-9PM",
    delivery_radius=3,
    cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715961040/WuberEats/Taco%20Bell/cover-image_fck6bi.jpg"
    )

    burger_king = Restaurant(
    owner_id=4,
    name="Burger King",
    address="2955 North Bellflower Boulevard",
    phone_number="5623046642",
    cuisine="American",
    description="Indulge in flame-grilled burgers, crispy fries, and a variety of tasty sides. Enjoy the iconic Whopper, chicken sandwiches, and refreshing drinks.",
    hours_of_operation="Sunday-Saturday: 6:30AM-10:30PM",
    delivery_radius=1,
    cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715979869/WuberEats/Burger%20King/cover_ayhz5o.jpg"
    )

    shake_shack = Restaurant(
    owner_id=2,
    name="Shake Shack",
    address="6440 Pacific Coast Hwy",
    phone_number="3234561234",
    cuisine="American",
    description="Treat yourself to premium burgers, crinkle-cut fries, and hand-spun shakes. Shake Shack is known for its high-quality ingredients, mouthwatering flavors, and a menu that features both classic favorites and unique creations.",
    hours_of_operation="Sunday-Saturday: 11AM-2AM",
    delivery_radius=1,
    cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715960974/WuberEats/Shake%20Shack/cover-image_b4hnug.jpg"
    )

    wing_stop = Restaurant(
    owner_id=4,
    name="Wing Stop",
    address="2018 Carson St",
    phone_number="3231564398",
    cuisine="American",
    description="Enjoy flavorful, freshly made chicken wings in a variety of mouthwatering sauces and seasonings. Perfect for satisfying your wing cravings.",
    hours_of_operation="Sunday-Saturday: 10AM-1AM",
    delivery_radius=3,
    cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715979741/WuberEats/Wing%20Stop/cover-image_oeg0k5.jpg"
    )

    angry_fish = Restaurant(
    owner_id=3,
    name="Angry Fish",
    address="16250 14th St",
    phone_number="3234561234",
    cuisine="Japanese",
    description="Experience fresh, high-quality sushi and sashimi with a creative twist.",
    hours_of_operation="Sunday-Saturday: 1PM-11PM",
    delivery_radius=2,
    cover_image="https://res.cloudinary.com/djqcfdrbm/image/upload/v1715979707/WuberEats/Angry%20Fish/cover-image_hjx91u.jpg"
    )

    db.session.add(nikita_burger)
    db.session.add(menards)
    db.session.add(mcdonalds)
    db.session.add(chick_fil_a)
    db.session.add(taco_bell)
    db.session.add(burger_king)
    db.session.add(shake_shack)
    db.session.add(wing_stop)
    db.session.add(angry_fish)
    db.session.commit()

def undo_restaurants():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.restaurant RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM restaurant"))

    db.session.commit()
