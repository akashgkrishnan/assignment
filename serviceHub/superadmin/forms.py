from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'email', 'password1','password2', 'groups' ]:
            self.fields[fieldname].help_text = None
            
    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2', 'groups' ]
