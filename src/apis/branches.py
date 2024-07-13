from rest_framework.decorators import api_view
from src.util.http_util import HttpUtil
from src.models.branches import Branches
from src.models.agency import Agency 

@api_view(['POST'])
def add_branch(request):
    data = request.data

    try:  
        agency_id = data.get('agency_id')
        agency = Agency.objects.get(agency_id = agency_id) 
        
        branch_id = data.get('branch_id', None)
        if(branch_id != None and branch_id != ''):
            branch = Branches.objects.get(branch_id = branch_id)
        else:  
            branch = Branches()
            branch.branch_id = Branches.objects.get_next_branch_id(agency)
        
        address = data.get('address')
        if(address == '' or address == None):
            raise Exception('Address cannot be empty')
        
        city = data.get('city')
        if(city == '' or city == None):
            raise Exception('City cannot be empty')
        
        pincode = data.get('pincode')
        if(pincode == '' or pincode == None):
            raise Exception('Pincode cannot be empty')
        
        branch.agency = agency
        branch.address = address
        branch.city = city
        branch.pincode = pincode
        branch.maps_url = data.get('maps_url')     
        branch.save()

        dict = {
            'branch_id' : branch.branch_id
        }
        return HttpUtil.respond(201, None, dict)
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))




