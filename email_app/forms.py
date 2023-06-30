# forms.py (remove the entire file)

# from django import forms
# from .models import SentEmail

# # Create your forms here.
# class EmailForm(forms.ModelForm):
#     class Meta:
#         model = SentEmail
#         fields = [
#             'email_subject',
#             'email_content'
#         ]
#     def __init__(self, *args, **kwargs):
#         super(EmailForm, self).__init__(*args, **kwargs)
#         self.fields['email_subject'].widget.attrs['placeholder'] = 'Enter Email Subject'
#         self.fields['email_content'].widget.attrs['placeholder'] = 'Enter Message'


#         self.fields['email_subject'].widget.attrs['class'] = 'gui-input'

#         self.fields['email_content'].widget.attrs['class'] = 'gui-textarea'
