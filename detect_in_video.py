from imageai.Detection import VideoObjectDetection
import os
# import cv2

execution_path = os.getcwd()

# camera = cv2.VideoCapture(0)

detector = VideoObjectDetection()

detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))

# detector.setModelTypeAsYOLOv3()
# detector.setModelPath( os.path.join(execution_path , "yolov3.h5"))

detector.loadModel()

# Detect with Video, more than 4 hours for a 10s video, took like forever on CPU, but still acceptable :)
video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join(execution_path, "finalmatch_10s.mp4"),
                            output_file_path=os.path.join(execution_path, "Resnet_detected_video_60fps")
                            , frames_per_second=60, log_progress=True)

# # Detect with Camera, you should buy GPU to run this
# video_path = detector.detectObjectsFromVideo(camera_input=camera,
#     output_file_path=os.path.join(execution_path, "camera_detected_video")
#     , frames_per_second=100, log_progress=True, minimum_percentage_probability=30)

print(video_path)