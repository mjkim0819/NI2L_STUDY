### GAN 유형
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/2bf6dbaa-c0ee-4714-9e8b-c0718110b1fc)

#### Unconditional GAN (u-GAN)
- 조건 없이(Unconditional) 데이터를 생성하는 모델
- 생성자: 주어진 잠재 공간의 무작위한 포인트에서 데이터를 생성하려고 시도합니다.
- 판별자: 생성된 데이터와 실제 데이터 간의 차이를 구별하는 역할을 합니다.

#### Conditional GAN (c-GAN)
- 조건적(Conditional)인 정보를 이용하여 데이터를 생성하는 모델
- 생성자와 판별자에게 조건 정보(예: 클래스 레이블, 텍스트 설명)가 주어짐
- 특정 클래스에 해당하는 이미지를 생성하는 작업

#### Super-Resolution GAN (SRGAN)
- 이미지 해상도를 개선한 데이터를 생성하는 모델
- 저해상도 이미지를 고해상도 이미지로 변환하는 작업에 사용
- 생성자 : 저해상도 입력 이미지를 받아 고해상도 이미지를 생성
- 판별자 : 생성된 이미지의 질을 판단

# StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation [CVPR 2018]
**[논문](https://arxiv.org/pdf/1711.09020.pdf)**  
  
## Abstract
* 기존
  * cycleGAN과 같은 기존 모델은 2개 이상의 도메인을 다루기 어려움
  * 서로 다른 모델들이 각 이미지 도메인 쌍에 대해 독립적으로 생성됨
    
* StarGAN
  * 하나의 모델을 사용하여 여러가지 도메인에 대해 image-to-image translation하는 모델
  * 하나의 네트워크 안에서 다양한 도메인의 데이터셋을 동시 학습 가능

* 도메인?
- 주어진 이미지를 다른 특성으로 변환하는 것.
- attribute
  - 이미지에 있는 의미있는 특징들
  - 머리색, 성별 등
- attribute value
  - attribute의 값
  - 머리색의 경우에 흑발/금발/갈색머리, 성별에는 남자/여자 등
- domain
  - 같은 attribute value를 공유하는 이미지들의 집합
  - 흑발 머리 사람들의 이미지 집합, 금발 머리 사람들의 이미지 집합, 남성 이미지 집합 등

* 기존 모델과의 도메인 비교
  * cycleGAN
    * 도메인1 고양이, 도메인2 강아지
    * 도메인1 실사적 이미지, 도메인2 만화풍 이미지
    * 하나의 모델로 고양이 사진을 강아지 사진으로 바꿀 수 있음
    * 하나의 모델로 실사 이미지를 만화풍 이미지로 바꿀 수 있음
  * starGAN
    * 도메인1 고양이, 도메인2 강아지, 도메인3 실사적 이미지, 도메인4 만화풍 이미
    * 하나의 모델로 고양이 실사 사진을 강아지 만화풍 이미지로 바꿀 수 있음
      
---
    
## Introduction
* 기존 모델들은 k개의 domain을 학습하기 위해 k(k-1)개의 generator가 훈련되어야 함
* CycleGAN
  * 입력 요소
    * 두 도메인에 속하는 이미지 필요 ( 말 -> 얼룩말 변환 시, 말과 얼룩말 이미지 쌍이 필요 )
  * 도메인 정보
    * 도메인 정보 대신 이미지 간의 상호 관계를 통해 변환 수행
* StarGAN
  * 입력요소
    * 하나의 이미지 필요 ( 웃는 얼굴, 찡그린 얼굴, 중성적 얼굴로 변환하기 위해 하나의 얼굴 이미지 필요 )
  * 도메인 정보
    * 원 핫 벡터로 표현, 도메인 정보를 통해 입력 이미지를 원하는 출력 도메인으로 변환

![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/8cfa4668-e961-467d-b8f6-0a43b7d60185)  




## Result

#### NOT MIMICKING TRAIN DATA
**데이터를 기억하는지 학습하는지 확인**  
* ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3f6b8bac-eb42-4f88-abba-4c2ab531d74f)  
  1 epoch  
* ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/87888f00-26d5-4022-9e74-cfc4b459d2d5)  
  5 epoch  
* learning은 훈련 데이터들에 대한 파라미터 값이 최적이 되도록 일반화된 값을 찾는 것을 의미 (새로운 값에도 잘 작동)
* memory는 이전의 값들에만 최적이 되고 새로운 값에는 맞지 않은 것
* 사용한 SDG는 랜덤으로 초기화하기 때문에 첫 훈련부터 mapping을 할 수 없음
* 아직 1, 5epoch로 under-fitting인 상황임에도 불구하고 높은 품질의 이미지가 생성

#### WALKING IN THE LATENT SPACE
**특정 지점에서 다른 지접으로 움직이는 데이터를 만들 때 자연스럽게 만들어지는지 확인**
* ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/b5673b73-c210-43a8-a8af-5733f625e7ec)  
* latent vector의 값을 조금씩 바꿔가면서 시점을 변화시켰을 때 부드렵게 변경됨
* mapping이 아니라는 증거 (sample data와 mapping 되었다면 시점이 변했을 때 끊기고 부자연스러운 사진이 생성될 것)

#### FORGETTING TO DRAW CERTAIN OBJECTS
**filler를 이용하여 사진에서 원하는 부분 제거**
* ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/a3d18870-f0b1-4997-a779-d3c04118f002)  
* sample image에서 window를 찾아내 bounding box
* window bounding box 안에서는 positive한 결과, 다른 랜덤 이미지에는 negative한 반응을 보이는 필터 찾기
* 이미지에서 해당 filter을 dropout
* 창문이 제거된 이미지 생성

#### VECTOR ARITHMETIC ON FACE SAMPLES
**vector arithmetic이 사용되고 있음을 확인**
* ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/096e330e-7f04-4bce-84ad-039f3f53b64d)  
* 이미지에서도 벡터 연산이 가능하다는 것을 확인
* 이미지에서 인식된 특징을 카테고리화
