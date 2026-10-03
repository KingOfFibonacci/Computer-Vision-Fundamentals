# Computer Vision Fundamentals

OpenCV examples for image and video input, grayscale, blur, crop, text, contours, and color detection, plus real-time webcam face, hand, pose, and YOLO object detection.

Run each script from its own folder. Several scripts load files with a relative path.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install opencv-python cvzone mediapipe numpy ultralytics
```

Webcam scripts quit when you press `q`.

## Intro to images

| Script | What it does |
| --- | --- |
| `read_images.py` | Opens `test.png` |
| `read_video.py` | Plays `test_video.mp4` |
| `read_webcam.py` | Shows the default webcam |

`test.png` and `test_video.mp4` are not in this repository. Put your own image and video in `Intro_to_images` using those filenames before running the first two scripts.

## Basic vision

These scripts are in `A_basic_vision`.

| Script | What it does |
| --- | --- |
| `gray_scale.py` | Converts `test.png` to grayscale |
| `blur.py` | Applies a Gaussian blur |
| `crop.py` | Crops a region of the image |
| `text.py` | Draws text on the image |
| `shapes.py` | Finds contours in `shapes1.png` |
| `Color_detect.py` | Isolates a color range from the webcam |
| `Color_contour.py` | Finds the contour and center of that color |

`gray_scale.py`, `blur.py`, `crop.py`, and `text.py` read `../Intro_to_images/test.png`. `shapes1.png` is included.

## Real-time vision

These scripts are in `B_Real_time_vision` and use the webcam.

| Script | What it does |
| --- | --- |
| `face_detect.py` | Detects faces |
| `hand_detect.py` | Tracks up to two hands |
| `body_detect.py` | Estimates body pose |
| `object_detect.py` | Draws YOLO detections |

`object_detect.py` loads `best.pt` from this folder. That weight file is not in the repository. Place your own YOLO `.pt` file there and name it `best.pt`. Ultralytics YOLO weights are licensed under AGPL-3.0, separate from the MIT license on this code.

The MediaPipe model files in this folder (`blaze_face_short_range.tflite`, `hand_landmarker.task`, and `pose_landmarker.task`) are Google models under the Apache License 2.0.

## License

The code in this repository is released under the MIT License. See [LICENSE](LICENSE).
