def validate(user_age, user_wght, user_rank_num):
    # check if user data is correct data type.

    if user_age > 0:
        print("valid Age")
    else:
        print("Invalid Age")
    if 0.0 < user_wght <= 1000.0:
        print("Valid weight")
    else:
        print("Invalid weight")
    if user_rank_num >= 0:
        print("Valid rank number")
    else:
        print("Invalid rank number")
