from core.forms import *

class ChangePasswordForm():
    old_password = forms.PasswordField()
    new_password = form.PasswordField()
    confirm_new_password = forms.PasswordField()

class ChangeEmailAddress():
    password = forms.PasswordField()
    email = forms.PasswordField()
