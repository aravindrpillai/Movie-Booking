from rest_framework.decorators import api_view
from src.util.http_util import HttpUtil
from src.models.agency import Agency

@api_view(['POST'])
def add_agency(request):
    data = request.data
    
    try:   
        agency_id = data.get('agency_id', None)
        agency = Agency.objects.filter(agency_id=agency_id)
        if(agency_id!= None and (not agency.exists())):
            raise Exception('Invalid agency_id')
        
        name = data.get('name')
        if(name == '' or name == None):
            raise Exception('agency name cannot be empty')
        
        if(agency.exists()):
            obj = agency.first()
        else:
            obj = Agency()
            obj.agency_id = Agency.objects.get_next_agency_id()
        obj.name = name
        obj.website = data.get('website')
        obj.email = data.get('email')
        obj.save()

        dict = {
            'agency_id' : obj.agency_id,
            'name' : obj.name,
            'website' : obj.website,
            'email' : obj.email
        }
        return HttpUtil.respond(201, None, dict)
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))




