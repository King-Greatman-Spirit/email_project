import csv
import os
from email.mime.image import MIMEImage
from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from email.utils import formataddr

def send_email(request):
    """
    View function to send emails to recipients.

    This function retrieves the email subject and content from the form submission,
    reads the recipient email addresses from a CSV file, and sends personalized emails
    to each recipient. It also attaches files and images from the form submission and
    the static folder.

    :param request: The HTTP request object.
    :return: The HTTP response or redirect.
    """
    
    # Handling the form submission
    if request.method == 'POST':
        # Retrieve email subject and content from the form submission
        email_subject = request.POST.get('email_subject')
        email_content = request.POST.get('email_content')

        # Set the masked sender email and name
        masked_sender_email = settings.MASKED_SENDER_EMAIL
        sender_name = 'WEBSTACKA GROUP'
        sender_email = formataddr((sender_name, masked_sender_email))

        # Set the email template and context
        email_template = 'emails/email_template.html'
        context = {'email_subject': email_subject, 'email_content': email_content}
        html_message = render_to_string(email_template, context)
        plain_message = strip_tags(html_message)

        # Get the attached files from the form submission
        attachments = request.FILES.getlist('email_attachment')

        # Read recipient email addresses from a CSV file
        csv_path = os.path.join(settings.BASE_DIR, 'templates', 'includes', 'address.csv')

        with open(csv_path, 'r') as csv_file:
            reader = csv.reader(csv_file)
            
            # Loop through each recipient email address
            for row in reader:
                recipient_email = row[0]
                
                # Create a new EmailMultiAlternatives object for each recipient
                email = EmailMultiAlternatives(
                    email_subject,
                    plain_message,
                    sender_email,
                    [recipient_email],
                )
                email.attach_alternative(html_message, 'text/html')

                # Attach files from the form submission
                for attachment in attachments:
                    email.attach(attachment.name, attachment.read(), attachment.content_type)

                # Attach multiple images from the static folder with Content IDs (CIDs)
                image_folder = os.path.join(settings.STATIC_ROOT, 'images')
                image_files = os.listdir(image_folder)
                
                # Loop through each image file in the static folder
                for image_file in image_files:
                    image_path = os.path.join(image_folder, image_file)
                    with open(image_path, 'rb') as image_file:
                        image_payload = image_file.read()
                    
                    image_filename = os.path.basename(image_path)
                    
                    # Attach the image file to the email message
                    email.attach(image_filename, image_payload)

                # Send the email to the recipient
                email.send()

        messages.success(request, 'Thank you! Your emails have been sent successfully!')
        return redirect('send_email')

    return render(request, 'emails/email_form.html')
