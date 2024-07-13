from rest_framework.decorators import api_view
from src.util.http_util import HttpUtil
from src.models.branches import Branches
from src.models.agency import Agency 
from src.models.screens import Screens

@api_view(['POST'])
def add_screens(request):
    data = request.data

    try:   
        branch_id = data.get('branch_id')
        branch = Branches.objects.filter(branch_id = branch_id)
        if(not branch.exists()):
            raise Exception('Invalid branch_id')
        branch = branch.first()

        number = data.get('number')
        if(number == '' or number == None):
            raise Exception('Number cannot be empty')

        screen = Screens()
        screen.branch = branch
        screen.number =number
        screen.save()

        return HttpUtil.respond(201, None, None)
    except Exception as e0: 
        return HttpUtil.respond(400, str(e0))
