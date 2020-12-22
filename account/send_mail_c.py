from django.core.mail import send_mail

class AppSenEmail:
    def __init__(self, obj_email):
         self.obj_email = obj_email
    def send_m(self):
        try:
          message = ("<div><p><strong> Hola </strong>"+ self.obj_email['to'] + "</p>"+
                    " <p style='color:blue'>Esto es una prueba </p><p>" +
                      self.obj_email['activate_rul']+'</p></div>')
          
          send_mail(self.obj_email['subject'], message,
                    'miguelconsoro@gmail.com', [self.obj_email['to']],
                    fail_silently = False)

          return "Ok"
        except:
            return "Error"  
