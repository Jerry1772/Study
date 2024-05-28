from concurrent import futures
import time
import grpc

import calc_pb2
import calc_pb2_grpc

class Calculator(calc_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return calc_pb2.CalcResponse(n1=request.n1+request.n2)
    
    def Subtract(self, request, context):
        return calc_pb2.CalcResponse(n1=request.n1-request.n2)
    
    def Multiply(self, request, context):
        return calc_pb2.CalcResponse(n1=request.n1*request.n2)
    
    def Divide(self, request, context):
        ## div by 0 error를 일단 0 출력하게 고정 해 두었는데, 추후 에러 처리 방식을 확인해야함
        if request.n2 == 0:
            return calc_pb2.DivResponse(f1=0)
        return calc_pb2.DivResponse(f1=request.n1/request.n2)
    
def serve():
    print("Server Start ...")

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

    calc_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)

    server.add_insecure_port("[::]:50050")
    print("Port Opened")

    server.start()

    server.wait_for_termination()

if __name__ == "__main__":
    serve()