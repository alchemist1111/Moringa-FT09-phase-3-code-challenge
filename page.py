class Users:

    def _init_(self, username, password):
            self.username = username
            self.password = password


class Sign_up(Users):

      def _init_(self, username, email, password):
            super()._init_(self, username, password)
            self.email = email

      def input_email(self):
                          