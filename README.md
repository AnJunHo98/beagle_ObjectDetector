# beagle_ObjectDetector

roboidai 카메라 객체 인식 결과를 ROS 2 토픽으로 publish하는 Beagle 로봇용 ROS 2 패키지 (2023)

## 개요

ROS 2 `ament_python` 패키지 `beagle_ex`입니다. USB 카메라(`roboidai.Camera('usb0')`) 영상에서 roboidai `ObjectDetector`로 객체를 인식하고,
인식된 라벨 목록을 `my_robot_interfaces/msg/Objectlist` 메시지로 `object_topic`에 0.5초 주기로 publish합니다.
인식 결과는 카메라 창에 표시됩니다.

## 저장소 구조

```
beagle_ex/
├── package.xml, setup.py, setup.cfg, resource/   # ROS 2 ament_python 패키지 설정
├── beagle_ex/beagle.py                           # object_node: 객체 인식 + Objectlist publish
├── beagle_ex/submodules/
│   ├── ObjectDetector.py   # ROS 없이 객체 인식만 확인하는 단독 실행 스크립트
│   ├── linetrice.py        # IP 카메라로 파란 트랙을 따라가는 Beagle 주행 예제
│   ├── objectback.py       # 전방 lidar 거리가 가까우면 비프 후 후진하는 예제
│   └── imported.py         # import 테스트용 함수
└── test/                   # ament 기본 테스트 (copyright, flake8, pep257)
```

## 요구사항

`package.xml` 기준 의존성:

- `rclpy`, `example_interfaces`
- `roboid`, `roboidai` (Beagle 로봇 / AI 카메라 Python 라이브러리)
- `my_robot_interfaces` — `Objectlist` 메시지를 정의하는 별도 인터페이스 패키지로, 이 저장소에는 포함되어 있지 않습니다.

## 사용법

`setup.py`에 `object_node` 실행 파일(`beagle_ex.beagle:main`)이 등록되어 있습니다.

```bash
# ROS 2 workspace의 src/ 아래에 beagle_ex/를 두고 빌드
colcon build --packages-select beagle_ex
source install/setup.bash

ros2 run beagle_ex object_node
```

- 노드 이름: `object_node`, 토픽: `object_topic` (`my_robot_interfaces/msg/Objectlist`, 필드 `object_list`)
- 실행 시 roboidai 객체 인식 모델을 다운로드한 뒤 로드합니다.

## 상태

2023년 프로젝트이며 더 이상 유지보수되지 않습니다.

## 라이선스

비공개 저장소이며 별도 라이선스 파일은 없습니다.
