from rest_framework import generics

from polls.serializers import PollsSerializer
from polls.tasks import demo_task


class PollsView(generics.CreateAPIView):
    serializer_class = PollsSerializer

    def perform_create(self, serializer):
        demo_task.delay()
