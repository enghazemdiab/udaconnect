import grpc
import person_pb2
import person_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = person_pb2_grpc.PersonServiceStub(channel)
        response = stub.GetPersonById(person_pb2.PersonIdRequest(id=1))
        print("New Person received. Details:")
        print(f"ID: {response.id}")
        print(f"Name: {response.first_name} {response.last_name}")
        print(f"Company: {response.company_name}")

if __name__ == '__main__':
    run()
