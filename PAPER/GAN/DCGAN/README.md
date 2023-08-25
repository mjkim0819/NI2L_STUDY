# Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks [ICLR 2016]
**[논문](https://arxiv.org/pdf/1511.06434.pdf)**  
  
## Abstract
* 기존 GAN에 Convolutional Neural Network를 적용
* 이전의 CNN은 Supervised learning에 중점에 두어 unsupervised learning에서는 큰 성능을 내지 못함
* CNN을 사용하고도 좋은 unsupervised learning 성능을 보여주는 모델
* 고화질 이미지를 생성하는데 중점을 둔 생성 모델

## Introduction
* 

## Related Work

### Representation Learning From Unlabeld Data


### Generating Natural Images


### Visualizing the internals of CNNs
* 



## Approach and Model Architecture
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


