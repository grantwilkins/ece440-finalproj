from __future__ import print_function

import logging

import grpc
import lights_pb2_grpc
import lights_pb2

IP_ADDR = '192.168.187.68'
PORT = '50051'

def toggle_lights(user_id, light_id):
    print("Will try to toggle lights ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = lights_pb2_grpc.LightsStub(channel)
        response = stub.ToggleLight(lights_pb2.LightRequest(user_id=user_id, light_id=light_id))
    print("Received response: " + response.user_id + " " + response.light_id)


if __name__ == '__main__':
    logging.basicConfig()