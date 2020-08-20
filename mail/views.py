from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail,send_mass_mail,mail_admins,mail_managers
from viva import settings

                                                # Send  Single_Mail
# def mail(request):
#     mail = send_mail("Test-Subject", "Hello, How are you? this is text ", "shubhamupadhyay1014@gmail.com",["shubhamupadhyay1014@gmail.com"],
#                      fail_silently=False,html_message="<h2>Hello, how are you?</h2> this is html msg for Gmail")
#     if mail :
#         return render(request,'mail/mail.html',{"BASE_URL": settings.Base_url})
#     else:
#         raise Exception("Error")

                                                 # Send Mass Mail
def mass_mail(request):
    mail1 = ("Test-Subject", "Hello, How are you? this is text", "shubhamupadhyay1014@gmail.com",["shubhamupadhyay1014@gmail.com"],)

    mail2 = ("Test-Subject", "Hello, How are you? this is text", "shubhamupadhyay1014@gmail.com",["shubhamupadhyay10@yahoo.in"])

    mail = send_mass_mail([mail1,mail2],fail_silently=False)

    if mail:
        return render(request,'mail/mail.html',{"BASE_URL": settings.Base_url})
    else:
        raise Exception("Error")

                             # send 'mail_admins'   Note- Required some settings in main app
# def admins(request):
#     mail_admins('Error- Admins Message', 'we have found some Errors', fail_silently=False)
#     return render(request,'mail/mail.html',{"BASE_URL": settings.Base_url})


                          # send 'mail_managers'   Note- Same as 'mail_admins'
# def managers(request):
#     mail_managers('Error- Managers Message', 'we have found some Errors', fail_silently=False)
#     return render(request,'mail/mail.html',{"BASE_URL": settings.Base_url})