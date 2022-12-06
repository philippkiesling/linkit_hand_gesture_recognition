# linkit_hand_gesture_recognition
Linkit WS22-23- Intermediate Challenge 

## Setup
1. Install Dependencies
`pip install -r requirements.txt`

_Note:_ Requires Python 3.6 or higher
2. Open challenge.ipynb

## Repository Structure
```
.
├── README.md
├── challenge.ipynb
├── datasets
│   ├── yourdatasetname 
│   │   ├── images
│   │   │   ├── train
│   │   │   │   ├── 0.jpg
│   │   │   │   ├── 1.jpg
│   │   │   ├── val 
│   │   │   ├── test-dev
│   │   ├── labels
│   │   │   ├── train
│   │   │   │   ├── 0.txt
│   │   │   │   ├── 1.txt
│   │   │   ├── val 
│   │   │   ├── test-dev
│── .gitignore
├── requirements.txt
├── yolov5 [GIT SUBMODULE]
```

## Training 
### Monitoring
It is important to monitor the training process to ensure that the model is training properly. 
To do so, we recommend [Weights and Biases](https://wandb.ai/) (or [tensorboard](https://www.tensorflow.org/tensorboard)). 
Both tools keep track of the training process and automatically log the results. 
#### Weights and Biases
1. Create an account on [Weights and Biases](https://wandb.ai/)
2. Install the wandb package `pip install wandb`
3. Login to your account `wandb login`
4. Run the training script with the `--project` flag `python train.py --project <project_name>`
5. Go to your [Weights and Biases](https://wandb.ai/) dashboard to view the results

For more information on the YOLOV5 integration with Weights and Biases, refer to [here](https://docs.wandb.ai/guides/integrations/yolov5)

#### Tensorboard
If installed, training will automatically log to tensorboard.
### 

## Submission
1. Fill in the `predict` function in challenge.ipynb
2. We will run the code with github actions using the following command: 
`python submission.py`
*Note:* Feel free to borrow code from the yolov5 detect.py 

3. The Output of the code should be a csv file with the following format:
ADD_EXAMPLE CSV HERE
4. You can check your current model performance and fps via the actions tab on github
   1. Open the actions tab
   2. Click on your latest action
   3. Open the `Run Challenge` step and scroll down to the `Test Results` section

## Evaluation
We will evaluate your model on the following metrics:
1. Mean Average Precision (mAP)
2. FPS (Frames per second) must be greater than 5
3. Model Size

**BONUS:** Can convert and run your model in the [onnx format](https://onnx.ai/)?

## Contact
If you have any questions, please contact us on linkit-Teams (or email us) at
- Alex Rothmaier: alex.rothmaier@linkit.tech
- Philipp Kiesling: philipp.kiesling@linkit.tech