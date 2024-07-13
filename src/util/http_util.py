from rest_framework.response import Response

class HttpUtil():

    @staticmethod
    def respond(response_code, messages, data = None):
        if(hasattr(messages, '__len__') and (not isinstance(messages, str))):
            pass
        else:
            messages = [messages]
        dict = {
            'status' : 'success' if response_code<300 else 'failed',
            'messages' : messages,
            'data' : data
        }


        return Response(dict, response_code)