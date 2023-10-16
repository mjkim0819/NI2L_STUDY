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
- PGGAN, ProGAN, PGAN, Progressive GAN 등 다양한 이름으로 불리는 GAN
- StyleGAN의 시초
- 저해상도 사진에 layer를 추가하며 학습하여 고해상도의 사진을 생성하는 모델

### Progressive training
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/be25f5f6-4df9-4a41-b9d3-34854751c84d)
- 일반적으로 high-resolution(고해상도) 생성이 어려워 D가 가짜를 쉽게 구별함
- 만들기 쉬운 low-resolution(저해상도) 이미지를 생성하고 점진적으로 layer를 증가시키며 세부 사항을 추가하여 high-resolution 이미지를 생성함
- image distribution에서 큰 구조(coarse-grained)의 특징을 우선적으로 학습
- 점차 세말한 특징(fine-grained)들을 이어서 학습
- 장점
  - stable: 저해상도 사진은 class information도 적고 mode도 몇 없기 때문에 학습 초기에는 low-resolution 학습이 더 안정적
  - Reduced training time: 학습 시간 단축 (최대 6배 단축)
- 단점
  - latent vector인 z가 Normalize를 거친 후에 바로 생성자(Generator)에 입력으로 들어감
  - latent space의 entanglement(얽혀있음) 문제를 유발

### entangle, disentangle
- entangle
  - 특징이 서로 상호작용 하여 구분이 어려운 상태
- disentangle
  - 각 style들이 잘 구분 되어있는 상태
  - 선형적으로 변수를 변경했을 때 어떤 결과물의 feature인지 예측할 수 있는 상태.
 
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/2d4a9678-23f2-4d0b-bca5-f8c91b7ef72d)  
- (a)
  - 데이터셋
    - 안경 쓴 붉은 머리, 안경 쓴 붉은 머리, 안경 안쓴 검정 머리 (안경 안 쓴 검정 머리는 없음)
  - (a) 가로축 안경 유무 (왼쪽 안경 무, 오른쪽 안경 유), 세로축 머리 (위 검정 머리, 아래 붉은 머리)
  - 안경 안 쓴 검정 머리는 비어 있음
- (b)
  - 
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/958cbd01-c201-4340-9399-d68ebf09b26d)
 


