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

*도메인?
- 주어진 이미지를 다른 특성으로 변환하는 것.
- attribute
  - 이미지에 있는 의미있는 특징들을 뜻하는데, 대표적으로는 머리색, 성별이나 나이등이 있다. 
- attribute value
  - attribute의 값을 의미하는데 예시로는 머리색의 경우에 흑발/금발/갈색머리, 성별에는 남자/여자가 있다. 
- domain
  - 같은 attribute value를 공유하는 이미지들의 집합을 칭한다. 예를 들면 여성의 이미지들은 하나의 domain을 구성하고 남성의 이미지들은 또 다른 domain을 구성한다.

* 도메인 예시
  * cycleGAN
    * 도메인1 고양이, 도메인2 강아지
    * 도메인1 실사적 이미지, 도메인2 만화풍 이미지
    * 하나의 모델로 고양이 사진을 강아지 사진으로 바꿀 수 있음
    * 하나의 모델로 실사 이미지를 만화풍 이미지로 바꿀 수 있음
  * starGAN
    * 도메인1 고양이, 도메인2 강아지, 도메인3 실사적 이미지, 도메인4 만화풍 이미
    * 하나의 모델로 고양이 실사 사진을 강아지 만화풍 이미지로 바꿀 수 있
 
---
    
## Introduction
* 대부분의 상황에서 안정적으로 학습 가능 -> Convolution 사용
* 자연어처리 word2vec과 같이 generator가 벡터 산술 연산 가능
* 특정 filter가 이미지의 특정 물체를 학습 (확인 조건)
  * generator가 이미지를 외워서 보여주는게(mapping) 아니라는 것을 확인
  * generator의 input 공간인 latent space (z space)에서 움직일 때 부드러운 변화를 확인

## Model Architecture
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/10bf0242-29d8-4284-9c89-038259e52543)  

### Max pooling to strided Convolution
* 공간적 해상도 감소 문제를 해결하기 위해 pooling이 아닌 transpose(합성곱 전치) 방식으로 진행
![.](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2Fcc9YHv%2FbtqEdydGzb1%2FPTOGzXMKTYZyxQB5SsKZa0%2Fimg.gif)  
![image](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbNEavB%2FbtqEcHPTz8d%2F0Vrz9E2V4jtk7YDO30Mxr0%2Fimg.gif)

https://eehoeskrap.tistory.com/431

* max pooling
  * 공간적 해상도를 줄이고 계산량을 감소시키는 convolution의 기본적인 계산
  * 입력 이미지의 중요한 특징을 추출하고 작은 변화에 강하게 반응 -> 이미지 분류에 유리
  * 작은 영역을 스캔하면서 각 영역에서 가장 큰 숫자 선택하는 방식으로 작동
  * 이미지를 줄이는 과정에서 중요하지 않은 정보는 제외하고 중요한 정보만 강조 (데이터 손실)
* convolutional transpose
  * convolution layer를 반대로 작동
  * 입력 데이터를 확대 또는 고해상도로 재구성 -> 이미지 생성에 유리
  * 출력 데이터와 필터 간의 내적을 계산하여 더 크기가 큰 입력 데이터를 재구성
* convolutional transpose를 사용하는 이유
  * 공간이 줄어들지 않아 해상도 유지에 효과적
  * 정보가 감소하지 않으므로 연속적인 특징을 학습할 수 있음
  * 공간적 차원을 확장하기 때문에 고해상도의 이미지 **생성**에 도움이 됨
    * Discriminator 네트워크가 저해상도 입력 이미지로부터 고해상도 이미지로 이동하는 정보를 학습하기 좋음
  
### Remove fully-Connected Layers
* 기존 GAN는 fully-connected layer 사용
* DCGAN은 합성곱 레이어를 사용
* fully connected layer
  * 데이터의 특징을 자세하게 추출하기 위해 모든 입력과 출력 간의 모든 뉴런이 서로 연결되어 있음
  * 입력데이터가 크거나 출력 뉴런 수가 많으면 파라미터 값이 많이 필요  
* 합성곱 레이어
  * 작은 윈도우를 슬라이딩하면서 지역적인 패턴을 감지
  * 공간적 특성을 보존 -> 공간의 구조나 패턴을 고려 가능 (얼굴에서 눈, 코, 입의 위치)
  * 물체의 경계에 대한 정보 보존 -> 객체 검출 성능 증가, 고해상도 이미지 생성 가능

### Use batch normalization
* 훈련의 안정성을 높이기 위해 입력 데이터를 정규화하는 과정
  * 훈련할 데이터를 미니 배치로 나눠 모든 입력 데이터에 대한 평균과 분산 계산
  * 각 미니 배치의 평균이 0, 분산이 1이 되도록 입력데이터를 수정하여 정규화
  * 데이터를 정규화 시키는 과정에서 추가된 파라미터를 역전파를 통해 학습
* 수동으로 데이터 분포를 조절해야하는 기존 방식과는 달리 데이터의 특성에 맞게 자동으로 데이터의 분포를 조절
* 더 높은 학습률을 설정할 수 있어, 학습을 빠르게 수렴시킬 수 있음
* 네트워크의 구조나 크기가 변경되더라도 적용이 가능
* **훈련 과정을 안정화하고 성능을 향상시키면서 동시에 단순화 및 자동화**

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
