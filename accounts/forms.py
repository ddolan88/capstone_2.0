from .models import CustomUser
from django.contrib.auth.forms import(
    UserCreationForm,
    UserChangeForm,
)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'email_confirmation', 'password', 'password_confirmation')

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields= ('first_name', 'last_name', 'email', 'email_confirmation', 'password', 'password_confirmation')