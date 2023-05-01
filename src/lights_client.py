from __future__ import print_function

import logging
import time
from time import sleep
import grpc
import lights_pb2_grpc
import lights_pb2

IP_ADDR = '192.168.186.68'
PORT = '50051'

def toggle_lights(user_id, light_id):
    print("Will try to toggle lights ...")
    with grpc.insecure_channel(IP_ADDR + ':' + PORT) as channel:
        stub = lights_pb2_grpc.LightsStub(channel)
        response = stub.ToggleLight(lights_pb2.LightRequest(user_id=user_id, light_id=light_id))
    print("Received response: " + response.user_id + " " + str(response.light_id))


if __name__ == '__main__':
    times = []
    for i in range(0, 25):
        start = time.time()
        toggle_lights('test', 3)
        end = time.time()
        print("Time elapsed: " + str(end - start))
        times.append(end - start)
        sleep(0.2)
    print("Average time elapsed: " + str(sum(times) / len(times)))
    print("Max time elapsed: " + str(max(times)))
    print("Min time elapsed: " + str(min(times)))
    toggle_lights('test', 4)
    logging.basicConfig()