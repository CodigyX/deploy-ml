from __future__ import print_function
import io
import json
import numpy as np
import requests

SERVER_URL = 'http://localhost:8000/predict'

def main():
    predict_request = '''
    {
        "Humidity": 50.0,
        "Temperature": 25.0,
        "Step_count": 1000.0
    }
    '''
    for _ in range(3):
        response = requests.post(SERVER_URL, data=predict_request)
    
    total_time = 0
    num_requests = 100000
    index = 0
    
    for _ in range(num_requests):
        response = requests.post(SERVER_URL, data=predict_request)
        response.raise_for_status()
        total_time += response.elapsed.total_seconds()
        prediction = response.json()
        print (prediction)

    print('Prediction class: {}, avg latency: {} ms'.format(
      prediction['Stress_Level'], (total_time * 1000) / num_requests))


if __name__ == '__main__':
  main()