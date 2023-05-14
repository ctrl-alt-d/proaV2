from crispy_forms.helper import FormHelper
from allauth.account.forms import LoginForm
from crispy_forms.layout import Layout, HTML
from crispy_forms.bootstrap import PrependedText
from django.utils.html import mark_safe


class UserLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields["login"].label = ""
        self.fields["password"].label = ""
        self.helper.form_show_labels = False
        self.helper.form_tag = False
        self.helper.layout = Layout(
            PrependedText(
                field='login',
                text=mark_safe('<i class="fa fa-solid fa-user"></i>')),
            PrependedText(
                field='password',
                text=mark_safe('<i class="fa fa-key"></i>')),
        )
