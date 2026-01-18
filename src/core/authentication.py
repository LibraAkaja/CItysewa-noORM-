from src.accounts.tables import User

class Backend:
    """
    Custom authentication backend.
    settings.AUTHENTICATION_BACKENDS should point to this class.
    """

    def authenticate(self, request, email=None, password=None, **kwargs):        
        if email is None or password is None:
            return
               
        try:
            user = User().get(email=email)
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
            
        except Exception as e:
            print(f"Error: {e}")
            return
        
    def user_can_authenticate(self, user):
        """
            An inactive user can`t authenticate.
        """
        return getattr(user, "is_active", True)







