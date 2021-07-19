import random

from proto import service_pb2, service_pb2_grpc
from third_party.common import pattern


class MyService(service_pb2_grpc.MyServiceServicer, pattern.Logger):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  def Test(self, request, context):
    self.log(f'MyService.Test({request.count})')
    reply = service_pb2.TestReply()
    for i in range(0, request.count):
      reply.data.add(x=i, y=random.randint(0, 100))
    return reply
