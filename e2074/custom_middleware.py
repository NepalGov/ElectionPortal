from django.shortcuts import redirect


class CheckUser(object):

    def __init__(self, get_response):
        print ("init working")
        self.get_response = get_response

    def __call__(self, request):


        response = self.get_response(request)

        if not request.user.is_authenticated() and \
                        request.path.startswith('/wp-admin/'):
            return redirect("/accounts/login/?next=/wp-admin/")

        return response


