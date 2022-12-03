from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, mixins, ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response
from pusher import pusher_client, Pusher

pusher = Pusher(app_id=u'1519175', key=u'8aff3c99d91668a780b1', secret=u'XXX_APP_SECRET', cluster=u'XXX_APP_CLUSTER')

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all().order_by('timestamp')
    serializer_class = MessageSerializer
    def post(self, request):
        pusher_client.trigger('chat', 'message', {
            'username': request.data['username'],
            'message': request.data['message']
        })
        return Response([])


    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        #  check if the method is post
        if request.method == 'POST':
            # try form validation
            # form = DocumentForm(request.POST, request.FILES)
            # if form.is_valid():
            #     f = form.save()
                # trigger a pusher request after saving the new feed element 
                pusher.trigger("channel-1", "test_event", { message: "hello world" })
                return HttpResponse('ok')
        # else:
                # return a form not valid error
            # return HttpResponse('form not valid')
        else:
            # return error, type isnt post
            return HttpResponse('error, please try again')

class ChatViewSet(ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

# def push_feed(request):
#     # check if the method is post
#     if request.method == 'POST':
#         # try form validation
#         form = DocumentForm(request.POST, request.FILES)
#         if form.is_valid():
#             f = form.save()
#             # trigger a pusher request after saving the new feed element 
#             pusher.trigger(u'a_channel', u'an_event', {u'description': f.description, u'document': f.document.url})
#             return HttpResponse('ok')
#         else:
#             # return a form not valid error
#             return HttpResponse('form not valid')
#     else:
#         # return error, type isnt post
#         return HttpResponse('error, please try again')