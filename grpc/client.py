import grpc

import calc_pb2
import calc_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50050")

    stub = calc_pb2_grpc.CalculatorStub(channel)

    response = stub.Add(calc_pb2.CalcRequest(n1=20, n2=10))
    print("add result ===")
    print(response.n1)

    response = stub.Subtract(calc_pb2.CalcRequest(n1=20, n2=10))
    print("sub result ===")
    print(response.n1)

    response = stub.Multiply(calc_pb2.CalcRequest(n1=20, n2=10))
    print("mul result ===")
    print(response.n1)

    response = stub.Divide(calc_pb2.CalcRequest(n1=20, n2=10))
    print("div result ===")
    print(response.f1)

if __name__ == "__main__":
    run()