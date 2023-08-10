from django.db import models
import datetime

class Profile(models.Model): 
    profile_id = models.AutoField(primary_key=True)
    staff_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, unique=True)
    adhar_No = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    birth_date = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    role = models.CharField(max_length=50)
    responcebility = models.TextField()

    def __str__(self):
        return self.staff_name

class TimeSchedule(models.Model):
    SHIFT = (
        ('DAY','day'),
        ('HYBRID','hybrid'),
        ('NIGHT','night'), 
    )
    TIME_TABLE = (
        ('10AM-6PM','10AM-6PM'),
        ('3PM-11PM','3PM-11PM'),
        ('8PM-4AM','8PM-4AM')
    )
    shift = models.CharField(max_length=50 , choices=SHIFT,default='day')
    shift_timing = models.CharField(max_length=50 , choices=TIME_TABLE ,default='10AM-6PM')
    shift_change_date = models.DateField(auto_now_add=True)
    profile = models.ForeignKey(Profile ,related_name="staffschedule", on_delete=models.CASCADE)

    def __str__(self):
        return self.shift

class Performance(models.Model):  
    MONTH = (
        ('JANUARY','January'),
        ('FEBRUARY','February '),
        ('MARCH','March'),
        ('APRIL','April'),
        ('MAY','May '),
        ('JUNE','June '),
        ('JULY','July'),
        ('AUGEST','August'),
        ('SEPTEMBER','September'),
        ('OCTOBER','October'),
        ('NOVEMBER','November'),
        ('DECEMBER','December'),
    )
    def current_year():
         return datetime.date.today().year
    def year_choices():
         return [(r,r) for r in range(1984, datetime.date.today().year+1)]
    def current_month():
         return datetime.date.today().month
    
    description = models.TextField(max_length=500)
    year = models.IntegerField(('year'), choices=year_choices(), default=current_year)
    month = models.CharField(primary_key=True,  max_length=50 , choices=MONTH,default='January')
    profile = models.ForeignKey(Profile ,related_name="staffperformance", on_delete=models.CASCADE)

    def __str__(self):
        return self.month