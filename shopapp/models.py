
import uuid
from django.db import models
 
class RegistrationModel(models.Model):
        user_name =  models.CharField(max_length=30)
        email = models.EmailField(max_length=50, unique=True)
        password = models.CharField(max_length=50)
    
        uid = models.UUIDField( primary_key=True,  default=uuid.uuid4,  editable=False )
        created_at = models.DateField(auto_now=True)
        updated_at = models.DateField(auto_now_add=True)
 
        def __str__(self):
            return self.user_name