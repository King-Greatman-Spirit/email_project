# models.py (remove the entire file)

# from django.db import models
# from datetime import datetime

# def get_attachment_upload_path(instance, filename):
#     # Define the upload path for attachments
#     # Modify it according to your needs, such as using a subdirectory per user or email
#     return f'attachments/{filename}'

# class SentEmail(models.Model):
#     email_subject = models.CharField(max_length=100)
#     email_content = models.TextField(max_length=1000)
#     sent_datetime = models.DateTimeField(default=datetime.now)
#     created_date = models.DateTimeField(auto_now_add=True)
#     attachments = models.FileField(upload_to=get_attachment_upload_path, blank=True)

#     def __str__(self):
#         return self.email_subject
