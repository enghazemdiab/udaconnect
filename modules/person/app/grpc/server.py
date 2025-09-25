import grpc
from concurrent import futures
import time

import person_pb2
import person_pb2_grpc

class PersonServiceServicer(person_pb2_grpc.PersonServiceServicer):
    def GetPersonById(self, request, context):
        # Dummy response for demonstration
        return person_pb2.PersonResponse(
            id=request.id,
            first_name="Hazem",
            last_name="Diab",
            company_name="ejada Systems"
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    person_pb2_grpc.add_PersonServiceServicer_to_server(PersonServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC server started: Port# 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
