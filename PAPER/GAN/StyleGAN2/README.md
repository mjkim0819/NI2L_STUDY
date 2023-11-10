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
