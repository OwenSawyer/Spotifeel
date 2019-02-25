import base64
import urllib

import requests
from django.views.generic import RedirectView, TemplateView

#https://stackoverflow.com/questions/51919651/spotify-authorization-code-flow-returns-incomplete-response

with open('/home/osawyer/website/spotify.txt', 'r') as fp:
    env = [i.strip() for i in fp.readlines()]
    CLIENT_ID = env[2]
    CLIENT_SECRET = env[3]
    SCOPE = env[0]

AUTH_HEADER = {
    "Authorization": "Basic "
    + base64.b64encode(
        f"{CLIENT_ID}:{CLIENT_SECRET}".encode()
    ).decode()
}

class SpotifyLoginView(RedirectView):
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        params = {
            "client_id": CLIENT_ID,
            "response_type": "code",
            "redirect_uri": self.request.build_absolute_uri("callback"),
            "scope": SCOPE,
        }

        url = "https://accounts.spotify.com/authorize?" + urllib.parse.urlencode(params)
        print(url)
        return url


class SpotifyCallbackView(TemplateView):
    template_name = "callback.html"

    def handle_callback(self, request):
        code = request.GET["code"]

        response = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "grant_type": "authorization_code",
                "code": code,
                "redirect_uri": request.build_absolute_uri("callback"),
            },
            headers=AUTH_HEADER,
        )

        return response.json()

    def get(self, request, *args, **kwargs):
        print("callback: " + str(self.handle_callback(request)))

        return super().get(request, *args, **kwargs)


# # ModelViewSet provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
# class TimelineViewSet(viewsets.ModelViewSet):
#
#     serializer_class = TimelineSerializer
#     permission_classes = ()
#
#     @action(methods=['post'], detail=True)
#     def aggregate_user_timeline(self, request):
#         queryset = Record.objects.filter(user_id = request['user_id']) #all,filter,get,order_by
#
#         return Response(self.get_serializer(queryset))
