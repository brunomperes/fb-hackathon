import random
users_list = ["Adam", "Bruno", "Iva", "Terry", "Misha", "Lisa", "Joe"];

def give_pairs(user_list):
    randomized = random.sample(users_list, len(users_list))
    first_user = randomized[0]
    previous_user = first_user
    for user in randomized[1:]:
        yield previous_user, user
        previous_user = user
    yield previous_user, first_user
print [i for i in give_pairs(users_list)]

