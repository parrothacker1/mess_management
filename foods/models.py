from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=255)
    mess = models.CharField(max_length=255)
    reg_no = models.CharField(unique = True , max_length=255)

    def get_details(self):
        return { "name":self.name,"mess":self.mess,"reg_no":self.reg_no}
