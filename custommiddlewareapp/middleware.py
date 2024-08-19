from typing import Any
from django.http import HttpResponseForbidden
from datetime import date,datetime
from custommiddlewareapp.models import PublicHoliday



class MaintainMiddleware:
    def __init__(self,get_response): # constructor will execute in (firstTime or restart server)
        self.get_response = get_response # get_response => reponsible for move from middleware to another
    
    def __call__(self,request): # call method => Execute it's code before access view 
        # if self.is_public_holiday():
        #     return HttpResponseForbidden('Site is not accessiable in the public holiday')
        
        # if self.is_weekend():
        #     return HttpResponseForbidden('Site is not accessiable in the WeekEnd')
        
        if self.is_maintenance_time():
            return HttpResponseForbidden('Site is  maintenance, Try Again After period of time')
        
        #! two lines of code below is important to continue next middleware in out project 
        #! Code Before Two line exceute before access view
        respone = self.get_response(request) 
        return respone
        #! code After Two line exceute After access view
        
    
    # def is_public_holiday(self):
    #     today = datetime.now().date()
    #     return PublicHoliday.objects.filter(date=today).exists() #  exists() => return boolean variable
    
    # def is_weekend(self):
    #     today = datetime.now().date().weekday()
    #     return today in [0,1]
    
    def is_maintenance_time(self):
        currentTime = datetime.now().hour
        return (currentTime >= 17 and currentTime <= 20) # 17 => 5PM 20=> 8PM