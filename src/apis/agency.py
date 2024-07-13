from rest_framework.decorators import api_view
from src.util.http_util import HttpUtil
from src.models.agency import Agency

@api_view(['POST'])
def add_agency(request):
    data = request.data
    
    try:   
        name = data.get('name')
        if(name == '' or name == None):
            raise Exception('agency name cannot be empty')
            
        agency_id = Agency.objects.get_next_agency_id()
        obj = Agency()
        obj.name = name
        obj.website = data.get('website')
        obj.email = data.get('email')
        obj.agency_id = agency_id # 'M'+str(random.randint(100,999))
        obj.save()

        dict = {
            'agency_id' : obj.agency_id,
            'name' : obj.name
        }
        return HttpUtil.respond(201, None, dict)
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))




