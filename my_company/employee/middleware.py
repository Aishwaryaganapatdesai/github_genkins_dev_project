# class FirstMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # One-time configuration and initialization.
#
#     def __call__(self, request):
#         # Code to be executed for each request before
#         print("Before view function")
#         # the view (and later middleware) are called.
#
#         response = self.get_response(request)
#
#         # Code to be executed for each request/response after
#         print("After view function")
#         # the view is called.
#
#         return response



from django.http import HttpResponse

class FirstMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("1"* 100)
        response = self.get_response(request)
        print("1"* 100)
        return response

        # return HttpResponse("<h1> Server is under maintainance please try after some time </h1>" )

    # def process_exception(self, request, exception):
    #     return HttpResponse("<h1> Something went wrong {}this is a mistake </h1>".format(exception))

class SecondMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("2"* 100)
        response = self.get_response(request)
        print("2"* 100)
        return response
