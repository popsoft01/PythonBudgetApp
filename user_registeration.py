class user_registration:
    def __init__(self, user_email, user_username, user_password):
        self.user_email = user_email
        self.user_username = user_username
        self.user_password = user_password
        self.user_detail = {}

    def set_username(self, username):
        self.user_username = username

    def set_user_password(self, password):
        self.user_password = password

    def set_user_email(self, user_email):
        self.user_email = user_email

    def get_username(self):
        return self.user_username

    def get_user_password(self):
        return self.user_password

    def get_user_email(self):
        return self.user_email

    def get_user_details(self):
        return self.user_detail

    # def registration(self, new_email, new_username, new_password):
    #     if new_email == self.user_email and new_username == self.user_username and new_password == self.user_password:
    #         self.user_detail[new_username] = user_registration
    #         return self.user_detail
    #
    #
    # def login(self, username, user_password):
    #     if username == user_registration.registration()
    #


# def login(user_email, username, user_password):
#     user_detail = registration(user_email, username, user_password)
#     if user_detail == login()


p1 = user_registration("sasdddddd", "qweerrrr", "yuuiiiii")
p1.registration("sasdddddd", "qweerrrr", "yuuiiiii")
