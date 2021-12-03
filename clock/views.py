from django.http import JsonResponse
from datetime import datetime, timedelta
from django.views.generic import View

class ClockAPI(View):

    def get(self, request):
        client_time = request.GET.get('client_time')
        server_request_time = datetime.now()


        server_response_time = datetime.now() + timedelta(seconds=2)


        return JsonResponse({'client_time': client_time, 'server_request_time': server_request_time, 'server_response_time': server_response_time})
