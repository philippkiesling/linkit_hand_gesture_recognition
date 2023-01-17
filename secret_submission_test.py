
# Parse Argument evaluation url
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--evaluation_url", help="evaluation url")
args = parser.parse_args()
evaluation_url = args.evaluation_url
# request evaluation url
import requests
import json
import os

if __name__ == '__main__':
    # Read in your model here

    print(f"evaluation_url: {evaluation_url}")
    response = requests.get(evaluation_url)
    print(response)
    print(response.text)
    print("run rest of script")
    #model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Add an inference method (returns results)

    # Add your prediction script here
    #evaluate(model)