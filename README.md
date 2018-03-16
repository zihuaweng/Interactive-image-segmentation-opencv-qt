# image-matting-opencv-qt
## 使用opencv进行交互式抠图
This is a simple interactive image matting app written by python opencv and pyqt

This app apply Grabcut algorithm in opencv for matting images. Grabcut is an improved version of Graph cut algorithm. Check these papers([paper1](http://www.cs.cornell.edu/~rdz/Papers/BVZ-pami01-final.pdf), [paper2](http://www.csd.uwo.ca/~yuri/Papers/iccv01.pdf)) for detail information~~

The gui part is mostly from this great work [labelImg](https://github.com/tzutalin/labelImg). It is quite a good example for pygt beginner!


## Requirement:
- Ubuntu 16.04
- python3
- pyqt5
- cv2

## Usage:
python app.py

## Result:
I will update this screen record once I find another better recorder ：（
![Performence of app](https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/results.gif)

## Result images:
![result_1](https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images_out/testing_1.png)
![result_2](https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images_out/testing_2.png)
![result_3](https://github.com/zihuaweng/image-matting-opencv-qt/blob/master/testing_images_out/testing_3.png)


## TODO:
- Auto resize images in mainwindow according to mouse movement
- Image item switch
- Rec edit and auto matting
- Show only one Rec every selection



