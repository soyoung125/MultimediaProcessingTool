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
