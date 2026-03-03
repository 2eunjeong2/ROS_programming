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

