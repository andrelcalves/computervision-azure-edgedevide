from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os 
from PIL import Image
import sys 
import time
import cv2 

import dotenv

dotenv.load_dotenv()

'''Authenticate the client'''
subscription_key = os.getenv('COMPUTER_VISION_SUBSCRIPTION_KEY')
endpoint = os.getenv('COMPUTER_VISION_ENDPOINT')

computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))


'''streaming video from webcam'''
frame_counter = 0
video_capture = cv2.VideoCapture(0)
while True:
    frame_counter += 1

    '''read the video first frame '''
    ret, frame = video_capture.read()
    cv2.imshow('videos', frame)

    '''save every 5th frame to a file - for test porpuses'''
    if frame_counter % 5 == 0:
        cv2.imwrite('frames/frame%d.jpg' % frame_counter, frame)

        image_path = 'frames/frame%d.jpg' % frame_counter	

        '''Analyze the image , detect objects in the frame'''
        detect_objects_results = computervision_client.detect_objects_in_stream(open(image_path, "rb"))

        '''print the detected objects'''
        if detect_objects_results.objects:
            '''check if the object for suspicious behavior is detected'''
            for obj in detect_objects_results.objects:
                if obj.object_property == 'person' and obj.confidence > 0.5:
                    print("Analyzing the frame for suspicious behavior %d" % frame_counter)
                    print("**** ALERT!!!! Person detected , Suspicious behavior detected in my office ****")
                else:
                    print("No person detected")
       
    ret, frame = video_capture.read()

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   
