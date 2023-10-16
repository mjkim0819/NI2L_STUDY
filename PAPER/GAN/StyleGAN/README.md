# StyleGAN
## 순서
- PGGAN
  -  [Progressive Growing of GANs for Improved Quality, Stability, and Variation (2018)](https://arxiv.org/abs/1710.10196)
- StyleGAN
  - [A Style-Based Generator Architecture for Generative Adversarial Networks(2019)](https://arxiv.org/abs/1812.04948)
- StyleGAN2
- StyleGAN3

## PGGAN
![image](https://raw.githubusercontent.com/happy-jihye/happy-jihye.github.io/master/_posts/images/gan/pggan1.gif)
- PGGAN, ProGAN, PGAN 등 다양한 이름으로 불리는 GAN
- StyleGAN의 시초
- 저해상도 사진에 layer를 추가하며 학습하여 고해상도의 사진을 생성하는 모델
### Progressive Growing of GANs

- high-resolution(고해상도) 이미지를 생성할 때 G는 정교하게 생성하는데 어려움이 있어 D가 쉽게 가짜이미지를 구별해낸다.
- 따라서 만들기 쉬운 low-resolution(저해상도) 이미지를 생성하고 점진적으로 layer를 증가시키며 세부 사항을 추가하여 high-resolution 이미지 생성한다.

### Progressive training
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/0c58c1d7-0cc6-4356-bdcb-e3d7fe8eb008)
- 일반적으로 high-resolution(고해상도) 생성이 어려워 D가 가짜를 쉽게 구별함
- 만들기 쉬운 low-resolution(저해상도) 이미지를 생성하고 점진적으로 layer를 증가시키며 세부 사항을 추가하여 high-resolution 이미지를 생성함
- image distribution에서 큰 구조(coarse-grained)의 특징을 우선적으로 학습
- 점차 세말한 특징(fine-grained)들을 이어서 학습
- 장점
  - stable: 저해상도 사진은 class information도 적고 mode도 몇 없기 때문에 학습 초기에는 low-resolution 학습이 더 안정적
  - Reduced training time: 학습 시간 단축 (최대 6배 단축)

### Fading in higher resolution layers
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/0ad2b656-5f62-4fa6-b6db-596ce65cb8f7)

