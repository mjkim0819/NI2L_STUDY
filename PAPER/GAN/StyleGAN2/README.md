# StyleGAN2
## 순서
- PGGAN
  -  [Progressive Growing of GANs for Improved Quality, Stability, and Variation (2018)](https://arxiv.org/abs/1710.10196)
- StyleGAN
  - [A Style-Based Generator Architecture for Generative Adversarial Networks (2019)](https://arxiv.org/abs/1812.04948)
- StyleGAN2
  - [Analyzing and Improving the Image Quality of StyleGAN (2020)](https://arxiv.org/abs/1912.04958)
- StyleGAN3

## Introduction
- 이전 styleGAN에서 발견된 인위적인 결점 2가지를 해결한 버전
  - common blob-like artifact (water shape artifact)
    - ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3817e340-aba9-4282-a29a-8164780ecb25)
    - generator의 구조적 결함 문제
  - phase artifact
    - ![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/1793af3b-6e20-41ec-b3bd-206bb15684e9)
    - glowing training 방식의 문제
### Key Insights
- normalization의 변화
  - actual statistics(실제 통계, ex.AdaIN) 방식에서 estimated statistics (추정 통계)로 수정
- skip connection을 갖고 있는 계층 생성자 (hierarchical generator)를 사용
- 이미지 질 개선을 위해 perceptual path length 개념을 regularization에 도입

## Common blob-like artifacts
- 현상
  1. 생성된 이미지에는 artifacts가 두드러지지 않지만, feature map에서는 잘 확인됨
  2. 거의 모든 이미지가 64x64 feature map부터 생성됨
  3. 물방울 모양이 없는 경우는 대부분 최종 이미지가 제대로 생성되지 않는 경우임
  4. progressive growing 되면서 artifacts가 점점 더 커짐
- 결과
  - 데이터 상의 문제가 아닌 시스템의 구조적인 문제 (이미지가 잘못 생성되거나, 64x64 이전에는 찾아볼 수 없음)
  - normalization 단계를 제거하면, artifacts가 완전히 사라짐
  - discriminator가 artifact를 감지하지만 없애지 못하는 이유는 저자들도 찾지 못함
  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/7853ced5-4afd-4910-94b3-41084d101482)  
- 원인
  - **AdalN**의 구조적 문제 때문
    1) 각 channel 별로 feature map마다 평균과 분산으로 normalization
    2) statistics data를 input으로 normalization
    - channel 별로 다른 값으로 scaling 되어서 합쳐지면서 범주에 벗어난 값 등장
    - 값이 너무 작거나(검) 값이 너무 큰(흰) 부분 -> local한 부분으로 인한 spike 값
    - 평균과 분산을 사용하기 때문에 각 feature map 사이의 관계를 알지 못함 (범주에 벗어난 값인지 알지 못함)
    - 실제 통계를 기반으로 normalization하기 때문에 이상한 값도 그대로 반영
   
- 우연한 계기로 normalization을 제거하니 artifact가 사라짐 -> normalization과 artifact 사이의 관계 확인 
- 새로운 instance normalization 방법이 필요


![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/c8da9bb4-006b-4ccd-b03f-904909582331) 
 
### Generator architecture revisited

![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/14d05519-1b36-4f12-8fd9-7dde6c2361e1)  
- (b) : 기존 styleGAN
  - mean, variance로 normalization
  - AdaIN modulation으로 style을 입힘
  - style block 안에 noise와 bias 존재
- (c) : 초기의 새로운 styleGAN
  - variance
- (b) : 기존 styleGAN
  - mean, variance로 normalization
  - AdaIN modulation으로 style을 입힘
  - style block 안에 noise와 bias 존재
  - 이전 featuremap이 자신의 mean,variance로 normalization
  - A에서는 w에서 learnable affine transform으로 scaling factor와 bias를 뽑아 normalize된 featuremap에 각각 곱해지고 더해져 (AdaIN modulation) style을 입힙
  - Stochastic variation을 의한 Noise (B block)와 convolution의 bias는 style block안에서 더해지게 됨
- (c) : 초기의 새로운 styleGAN
  - eaturemap을 mean과 variance로 normalize하지 않고, variance로 나누기 (분산만 이용해도 충분)
  - bias와 Noise는 style magnitue와 반비례하게 영향을 주기 때문에, bias와 Noise를 style block밖으로 빼버림



