from django.shortcuts import render
from uc.models import UnderConstruction
from decouple import config
class UnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response
        print("One time Initialize")
        
    def __call__(self, request):
        if request.user.is_staff:
            return self.get_response(request)
        
        UC_key = config("MAINTENANCE_BYPASS_KEY") 
        if 'u' in request.GET and request.GET['u'] == UC_key:
            request.session['bypass_maintenance'] = True
            request.session.set_expiry(0)
            
            
        if request.session.get('bypass_maintenance',False):
            return self.get_response(request)
        try:
            uc = UnderConstruction.objects.first()
            context = {
                'uc_note':uc.uc_note,
                'uc_duration':uc.uc_duration
            }
            if uc and uc.is_under_construction:
                return render(request,'uc/underc.html',context)
        except:
            pass
        return self.get_response(request)
        
        
        
        # print("THis is before view")
        # response = render(request,'uc/underc.html')
        # print("this is after response")
        # return response
        