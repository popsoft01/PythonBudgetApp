class user:
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

    def __str__(self):
        return user
