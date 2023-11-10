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
- 추가적으로 이미지 질 개선을 위해 perceptual path length 개념을 regularization에 도입

## Common blob-like artifacts
- 생성된 이미지에는 물방울 모양이 두드러지지 않지만, featuremap에서는 잘 확인됨
- 거의 모든 이미지가 64x64 feature map부터 생성됨
  - 데이터의 문제가 아닌 시스템 구조적 문제 ( 64x64 이전에는 찾아볼 수 없음 )
- progressive growing 되면서 artifact가 점점 더 커짐
- discriminator가 artifact를 감지하지만 없애지 않는 이유는 저자들도 찾지 못함
- 원인은 **AdalN**의 구조적 문제 때문

### AdalN
- GAN에서 스타일 전이 및 이미지 특징 정규화를 위한 기법
- 평균(mean), 분산(variance)를 사용하여 
