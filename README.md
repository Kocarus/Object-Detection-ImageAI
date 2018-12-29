## Real-time object detection in World Cup 2018 final match with ImageAI
# Steps
1. Clone the repo
2. Open the command line and navigate to the repo
3. Type **pip install -r requirements.txt** and enter
4. Download supported pre-trained models **RetinaNet / YOLOv3 / TinyYOLOv3** at [Models for Image Recognition and Object Detection](https://github.com/OlafenwaMoses/ImageAI/releases/tag/1.0/) and put them to the repo. Now you can detect and recognize 80 different kind of common everyday objects in any video
5. To train you own model to recognize everything you want, please refer to [Custom Training with ImageAI](https://imageai.readthedocs.io/en/latest/custom/index.html)
6. Author of ImageAI: https://github.com/OlafenwaMoses/ImageAI

# More info
- If you run this on CPU, you can only test with a very short video. Trust me, it took me 4 hrs to proceed a 10s video on my potato one. Otherwise, just buy GPU :grin:
- Video source: [France vs Croatia WC 2018 Final](https://www.youtube.com/watch?v=GrsEAvRerTg)

# Result
![Resnet50](https://thumbs.gfycat.com/TastyMiserlyCod-size_restricted.gif)
**Using Resnet50 model, small ball can't be recognized**

![Yolov3](https://thumbs.gfycat.com/PoliticalTinyAchillestang-size_restricted.gif)
**Using Yolov3 model, more accuracy!**
