user_detail = {}


def registration(new_email, new_username, new_password):
    if len(new_email) >= 10 and len(new_username) >= 5 and len(new_password):
        user_detail[new_email] = new_email
        print(user_detail)
        # return (f"Registration successful \n your registration details are {new_email},"
        #         f" {new_password}, and {new_password}")

# def login(user_email, username, user_password):
#     user_detail = registration(user_email, username, user_password)
#     if user_detail == login()
