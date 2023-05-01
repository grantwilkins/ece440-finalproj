from concurrent import futures
import logging
import grpc
import lights_pb2
import lights_pb2_grpc
import mqtt_dispatch


class Lights(lights_pb2_grpc.LightsServicer):
    def ToggleLight(self, request, context):
        print("Received request: " + request.user_id + " " + str(request.light_id))
        mqtt_dispatch.toggle_lights(request.light_id)
        return lights_pb2.LightReply(user_id=request.user_id, light_id=request.light_id)

def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    lights_pb2_grpc.add_LightsServicer_to_server(Lights(), server)
    server.add_insecure_port('0.0.0.0:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()
    

if __name__ == '__main__':
    logging.basicConfig()
    mqtt_dispatch.setup_mqtt()
    serve()