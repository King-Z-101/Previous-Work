def check_it_out(car, fav_car):
    if car.lower().strip() == fav_car.lower().strip():
        print("It looks like you still love the", fav_car + "!")
    else:
        print("You've changed your mind! You used to love the " + fav_car + "!")


