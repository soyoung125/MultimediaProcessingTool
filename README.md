# MultimediaProcessingTool

2022 경기대학교 멀티미디어처리기술 Orange팀


## 설치 경로

프로젝트는 반드시 C드라이브에 clone합니다.

    C://MultimediaProcessingTool

## 필요한 라이브러리
실행에 위한 라이브러리는 다음과 같이 직접 설치해야 합니다. 

    pip install '라이브러리명'
사용한 라이브러리 리스트
- PyQt5
- scikit-image
- Pillow
- openCV-python
- numpy
- matplotlib


추가적으로 웹캠을 이용해 사람을 카운팅하기 위해

    git clone https://github.com/ultralytics/yolov5
    cd yolov5
    pip install -qr requirements.txt
을 터밀널에 입력합니다.

## 구현 기능
1. Showing the histogram of an image, convert to grayscale
2. Enhance image quality using
3. Saving an image to another formats
4. Rotate, scaling, flip, warp, crop an image
5. Convert video, webcam to grayscale, flip the video/webcam (90, 180, 270 degrees)
6. Counting person in a webcam using YOLO

## 팀원
- 경기대학교 컴퓨터공학부 [김가영](https://github.com/gykim0923) 
    - Showing the histogram of an image, convert to grayscale
    - Saving an image to another formats
    - Convert video, webcam to grayscale, flip the video/webcam (90, 180, 270 degrees)
        - Flip the webcam


- 경기대학교 컴퓨터공학부 [박소영](https://github.com/soyoung125)  
    - Enhance image quality using, Filter the image
        - Gamma Correction
    - Rotate, scaling, flip, warp, crop an image
    - Convert video, webcam to grayscale, flip the video/webcam (90, 180, 270 degrees)
        - Convert video, webcam to grayscale
    - Counting person in a webcam using YOLO


- 경기대학교 컴퓨터공학부 [최희정](https://github.com/choihj00)  
    - Enhance image quality, Filter the image
        - Histogram Equalization
        - Filter the image with blurring, smoothing, sharpening.
    - Convert video, webcam to grayscale, flip the video/webcam (90, 180, 270 degrees)
        - Flip the video

## 결과
<p align="center">
    <h3>Transformation</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077275-45fc40d4-bf84-4046-88e9-f12462afbce8.gif">
    <h3>Filter</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077172-6fc2f2fe-5c6c-4bab-83b3-79552311c33b.gif">
    <h3>Enhance</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077157-12025388-a8fa-4941-82f5-f3253110f9a4.gif">
    <h3>Save</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077303-29f28bf8-fbb7-4666-a999-1fa597bab490.gif">
    <h3>Implement</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077191-fefaafbc-9646-4981-915f-81a4b66037eb.gif">
    <h3>Video Transformation</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077265-e34fd790-a253-4345-b20b-febf7b996e3f.gif">
    <h3>Counting person</h3>
    <img src="https://user-images.githubusercontent.com/77377583/173077282-c454aba4-55a5-4a1b-9030-9cbeea12c2b1.gif">
</p>
