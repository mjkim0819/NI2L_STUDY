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

## StarGAN Networks
![figure 3](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/177c47d8-d7de-4400-94da-63e808293b62)
- generator
  - 입력 이미지를 다른 도메인으로 변환하는 능력을 학습
    - 특정 도메인(label)으로 변환하는 확률분포를 모델링
    - 학습 과정에서 무작위로 선택한 도메인 라벨을 사용하여 입력 이미지를 유연하게 변환하도록 학습
    - 다양한 도메인 간의 이미지 변환 수행
- discriminator
  - 입력 이미지의 도메인을 예측
    - 입력 이미지가 원본 데이터일 확률 출력
    - 이미지의 도메인을 예측하는 확률분포 출력

### Multi-Domain Image to Image Translation
- multi-domain task를 수행할 수 있게 해주는 loss 함수에 대해 설명
- Adversarial Loss (적대적 손실)
  - 목표 : 가짜 이미지를 실제 이미지 처럼 만들기 위해 generator를 학습하는데 사용
  - 역할 : disciminator를 속이기 위해 생성된 이미지를 실제 이미지처럼 보이게 학습
  - 결과 : 생성 이미지의 품질 향상
- Domain Classification Loss (도메인 분류 손실)
  - 목표 : generator가 특정 도메인으로 이미지를 변환하도록 유도
  - 역할 : discriminator의 두번째 출력(domain 정보 출력)을 이용하여 generator의 출력 이미지가 원하는 도메인으로 분류되도록 학습하는데 사용
  - 결과 : 원하는 도메인으로 이미지를 변환 (다양한 도메인 간 변환)
- Reconstruction Loss (재구성 손실)
  - 목표 : generator가 변환한 이미지를 다시 기존 domain으로 복원
  - 역할 : 기존 이미지와 복원한 생성이미지의 차이 최소화
  - 결과 : 변환 과정에서의 이미지 품질 유지, 안전성 개선
--- 
#### Adversarial Loss (적대적 손실)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/8276091e-156e-475f-9103-32ebaee3c1d4)  
* 학습 방법
* 
#### Domain Classification Loss (도메인 분류 손실)
#### Reconstruction Loss (재구성 손실)




### Output
- 첫 번째 출력 (Adversarial Output, 적대적 출력)
- 두 번째 출력 (Domain Classification Output, 도메인 분류 출력)

