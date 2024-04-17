# Use case : Suspcious Behavior

The solution will connect to a security video stream using a service such as ring.com, which monitors security footage outside of the home. The use case involves the following steps:

Connect to the video stream.
Analyze the stream for suspicious activity.
Generate an alert.

This approach outlines a clear process for monitoring and responding to security concerns effectively.

!["Simple Architecture"](/img/simple_cv_architecture%20.png)


## Frame Parsing
The Azure video API doesn't support video stream so as raw input we have to pass the frames in a cert way and there are certain specs to how the frame should be.

## Steps

1. Create a azure resource group, for this use case I created one with the name "cv-resouce-susp-behavior".

2. Create a auzre AI Service, computer vision resouce named "cv-ai-service-susp-behavior".

3. Now, if you go to your resource, you have access to the Keys and endpoint for our Azure AI Service. There are two key but you only need one key.

4. Now, go to [Azure Cognite Portal](portal.vision.cognitive.azure.com)

5. Let's code
    1. If you don't have Azure Cognitive Services installed, you need to install it using:
 ``` pip install azure-cognitiveservices-vision-computervision ```
    2. If you don't have OpenCV installed, you need to install it using:  
```  pip install opencv-python opencv-python-headless ```
    3.If you don't have dotEnv installed, you need to install it using: 
```  pip install python-dotenv --user ```
    4. The next step is to setup the Azure API and KEY in the env file
    5. We need to break the video into a bunch of frames.




