from apps.customers.models.customer_token import CustomerToken
from apps.employees.models.employee_token import EmployeeToken
from movies.settings import TOKEN_EXPIRY_TIME_IN_MINUTES
from rest_framework.renderers import JSONRenderer
from datetime import datetime, timedelta
from util.http import build_response
from util.logger import logger
import traceback

'''
    Authentication Middleware
'''
class Authenticate():
    excluded_urls = [
      "employees/apis/generate/otp",
    ]

    def __init__(self, get_response):
        self.get_response = get_response

    def __unauthorized_api_response(self):
        response = build_response(401, "Authentication Failed")
        response.content_type = "application/json"
        response.accepted_renderer = JSONRenderer()
        response.accepted_media_type = "application/json"
        response.renderer_context = {}
        response.render()
        return response

    def __call__(self, request):
        full_path = request.get_full_path()
        for excluded_url in self.excluded_urls:
            if(excluded_url in full_path):
                return self.get_response(request)
        
        url_segments = full_path.replace("https://", "").replace("http://", "").split('/')
        usertype = url_segments[1].lower()
        headers = request.headers
        token = headers.get('Token', None)
        identifier = headers.get('Identifier', None)
        
        authenticated = self.__authorize(usertype, token, identifier)
        if(authenticated):
            return self.get_response(request)
        else:
            return self.__unauthorized_api_response()
 
    
    def __authorize(self, type, token, identifier):
        logger.debug("{} authorization info : {} | Identifier : {} ".format(type, token, identifier))
        try:
            return True
        except Exception as e:        
            logger.error('Failed to authenticate [in middleware] : {}\n{}'.format(e, traceback.format_exc()))
            return False