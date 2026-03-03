# ROS development 
- OS: Ubuntu 20.04 LTS (Focal)
- ROS Version: Noetic Ninjemys
- Python: Python3
- Workspace: ~/catkin_ws

</br>


# ROS Install
1. source list
```bash
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
```
2. Set up your keys
```bash
sudo apt install curl
```
```bash
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
```
3. Installation
```bash
sudo apt update
```
4. ROS Desktop-Full 설치
```bash
sudo apt install ros-noetic-desktop-full
```
5. Environment setup
```bash
source /opt/ros/noetic/setup.bash
```
6. ROS 환경 설정
```bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
```
```bash
source ~/.bashrc
```
7. 설치 확인
```bash
rosversion -d
```
출력: noetic</br>

# Catkin Workspace 생성
1. Workspace 생성
```bash
$ mkdir -p ~/catkin_ws/src
$ cd ~/catkin_ws/
$ catkin_make
```
2. Workspace 환경 등록
```bash
$ echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
$ source ~/.bashrc
```
- source는 ROS를 사용할 수 있는 상태로 만들어주는 작업
</br>

# 필수 패키지 설치
```bash
$ sudo apt install ros-noetic-rospy
$ sudo apt install ros-noetic-rosbash
$ sudo apt install ros-noetic-turtlesim
```
설치 확인 :
```bash
rospack find rospy
```
</br>

# Test 실행
1. ROS Core 실행
```bash
roscore
```
2. Turtlesim 실행
```bash
rosrun turtlesim turtlesim_node
```
</br>

# 환경 변수 확인
- ROS가 패키지를 어디서 찾을지 알려주는 경로 목록을 알 수 있음
```bash
echo $ROS_PACKAGE_PATH
```
정상 예시 :
```bash
/home/user/catkin_ws/src:/opt/ros/noetic/share
```
</br>

# Turtlesim 실습
1. Turtlesim 방향키로 움직이기
```bash
rosrun turtlesim turtle_teleop_key
```
2. /turtle1/pose 관찰
```bash
ostopic echo /turtle1/pose
```
```
- x: 거북이의 X 좌표. 앞으로 이동하면 값이 증가한다

- y: 거북이의 Y 좌표. 위로 이동하면 값이 증가한다

- theta: 거북이의 방향 (라디안). 좌회전하면 값이 증가, 우회전하면 감소한다

- linear_velocity: 현재 직진 속도. 방향키 위를 누르면 2.0이 된다

- angular_velocity: 현재 회전 속도. 방향키 좌를 누르면 2.0이 된다
```
3. 토픽/메시지 구조 정리
- topic 목록 확인
```bash
/rosout
/rosout_agg
/turtle1/cmd_vel
/turtle1/color_sensor
/turtle1/pose
```
- 토픽의 메시지 타입 확인
```bash
$ rostopic type /turtle1/cmd_vel
- geometry_msgs/Twist
```
```
geometry_msgs/Twist 타입의 메시지만 받는다는 뜻

아무 데이터나 보내면 안 되고
Twist 형식으로 맞춰서 보내야 함.
```
- 메세지 구조 확인
```bash
$ rosmsg show geometry_msgs/Twist
```
```
geometry_msgs/Vector3 linear
  float64 x
  float64 y
  float64 z
geometry_msgs/Vector3 angular
  float64 x
  float64 y
  float64 z
```
## turtlesim 토픽 정리
### /turtle1/cmd_vel (geometry_msgs/Twist)

거북이에게 보내는 속도 명령
```bash
rostopic pub /turtle1/cmd_vel geometry_msgs/Twist \
"{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}"
```

- linear.x: 직진 속도 (앞/뒤) > 2.0

- linear.y: 좌/우 이동 (사용 안 함) > 0.0

- linear.z: 상/하 이동 (사용 안 함) > 0.0

- angular.x: Roll (사용 안 함) > 0.0

- angular.y: Pitch (사용 안 함) > 0.0

- angular.z: 회전 속도 (좌/우 회전) > 1.0

### /turtle1/pose (turtlesim/Pose)
```bash
rostopic pub /turtle1/pose turtlesim/Pose \
"{x: 1.0, y: 1.0, theta: 0.0, linear_velocity: 0.0, angular_velocity: 0.0}"
```

거북이의 현재 위치와 방향

- x: X 좌표 > 1.0

- y: Y 좌표 > 1.0

- theta: 방향 (라디안) > 0.0

- linear_velocity: 현재 직진 속도 > 0.0

- angular_velocity: 현재 회전 속도 > 0.0

### /turtle1/color_sensor (turtlesim/Color)
```bash
rostopic pub /turtle1/color_sensor turtlesim/Color \
"{r: 255, g: 225, b: 255}"
```

거북이 발 아래의 배경 색상

- r: 빨강 (0~255) > 255

- g: 초록 (0~255) > 255

- b: 파랑 (0~255) > 255
```
turtlesim은 이 토픽을 구독하지 않기 때문에 거북이 색이 바뀌지는 않음.
왜냐하면 이 토픽은 '상태 출력용(Publisher 전용)이기 때문.
```
