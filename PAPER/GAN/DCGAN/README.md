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
CNN과 GAN의 조합이 DCGAN에서 처음 등장한 것은 아니지만, 처음으로 크게 성공한 모델이라 주목을 받음.  
### Max pooling to strided Convolution
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/bf3201a2-023c-4df7-af2b-e25bd3ddb113)  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/0e780187-2891-4086-af5d-b205ba0c296f)  
  
* 데이터의 세부정보를 유지하고, 더 간결하고 안정적으로 학습하기 위해 pooling이 아닌 strided 방식으로 진행
* max pooling
  * 작은 영역을 스캔하면서 각 영역에서 가장 큰 숫자 선택
  * 이미지를 줄이는 과정에서 중요하지 않은 정보는 제외하고 중요한 정보만 강조
* strided Convolution
  * convolution keneral을 이동시킬 때 한번에 여러 스텝을 건너뛰며 계산
  * 이미지를 줄이는 과정에서 중요하지 않은 정보는 간추리고 (제외는 아님) 중요한 정보를 추출

* strided convolution을 사용하는 이유
  * 정보를 잃지 않으면서 파라미터 수 줄이기
  * 이미지의 해상도 유지
  * 얼굴 생성 모델에서 미소의 주름 같이 미세한 세부사항도 학습 가능
  * 기울기 소실 문제를 줄이는데 효과적
  
### Remove fully-Connected Layers
* 기존 GAN는 fully-connected layer 사용
* DCGAN은 합성곱 레이어를 사용
* fully connected layer
  * 데이터의 특징을 자세하게 추출하기 위해 모든 입력과 출력 간의 모든 뉴런이 서로 연결되어 있음
  * 입력데이터가 크거나 출력 뉴런 수가 많으면 파라미터 값이 많이 필요
  * 
* 합성곱 레이어

### Use batch normalization

