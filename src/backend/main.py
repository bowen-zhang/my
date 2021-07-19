import datetime
import grpc
import time
from absl import app as absl_app
from concurrent import futures
from proto import service_pb2, service_pb2_grpc

import settings
from backend import service as service_lib
from third_party.common import app


class ServiceApp(app.App):
  def __init__(self):
    super().__init__(name='Service')
    self.init_logging('../../log')
    self._service = service_lib.MyService()

  def run(self):
    self.logger.info('Starting GRPC service.')
    grpc_server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_MyServiceServicer_to_server(
        self._service, grpc_server)
    port = settings.current['services']['my_service']['port']
    grpc_server.add_insecure_port('[::]:{0}'.format(port))
    grpc_server.start()
    self.logger.info('Started GRPC service on port {0}.'.format(port))

    while True:
      time.sleep(1)


if __name__ == '__main__':
  app.start(ServiceApp)
