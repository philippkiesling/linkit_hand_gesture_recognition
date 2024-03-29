"""
Submission scripts.
Add your prediction Script here.

Note: Your final script should run with the following command:
`python submission.py`
"""
import torch # PyTorch
import cv2
from datetime import datetime
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def evaluate(model, n_runs = 100):
    # Load image

    print("Prediction script is running")
    img = cv2.imread('datasets/example/zidane.png')
    #results = inference(model, img)
    #print("mAP: {}".format(0.0000))
    start_time = datetime.now()

    # To benchmark inference speed (FPS), we loop over the inference function n_runs times
    for i in range(0,n_runs):
        results = inference(model, img)
    end_time = datetime.now()
    fps = n_runs / (end_time - start_time).total_seconds()
    print(f"FPS: {fps:.2f}")
    pass

def inference(model, img):
    # Load image
    results = model(img)
    return results

# Parse Argument evaluation url
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--evaluation_url", help="evaluation url")
args = parser.parse_args()
evaluation_url = args.evaluation_url

if __name__ == '__main__':
    # Read in your model here
    #print(f"evaluation_url: {evaluation_url}")

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

    # Add an inference method (returns results)

    # Add your prediction script here
    evaluate(model)