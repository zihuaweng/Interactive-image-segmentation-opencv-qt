# Interactive-image-segmentation-opencv-qt V-1.0
## 使用opencv进行交互式抠图
This is a simple interactive image segmentation app written by python opencv and pyqt.

This app applys Grabcut algorithm in opencv for matting images. Grabcut is an improved version of Graphcut algorithm. Check these papers([paper1](http://www.cs.cornell.edu/~rdz/Papers/BVZ-pami01-final.pdf), [paper2](http://www.csd.uwo.ca/~yuri/Papers/iccv01.pdf)) for detail information~~

The gui part is mostly from this great work [labelImg](https://github.com/tzutalin/labelImg). It is a very good example for pygt beginner!


## Requirement:
- Ubuntu 16.04
- python3
- pyqt5
- cv2

## Usage:
python app.py

## Result:

![Performence of app](https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/results.gif)

### input:
<img src="https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images/testing.jpeg" width="300">

### output:
<img src="https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images_out/testing_1.png" width="60"> <img src="https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images_out/testing_2.png" width="80"> <img src="https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images_out/testing_3.png" width="80">


## TODO:
- Auto resize images in mainwindow according to mouse movement
- Image item switch
- Rect edit and auto matting
- Show only one Rect every selection



