# StyleGAN
## 순서
- PGGAN
  -  [Progressive Growing of GANs for Improved Quality, Stability, and Variation (2018)](https://arxiv.org/abs/1710.10196)
- StyleGAN
  - [A Style-Based Generator Architecture for Generative Adversarial Networks(2019)](https://arxiv.org/abs/1812.04948)
- StyleGAN2
- StyleGAN3

## Introduction
- 이미지 생성에서 스타일과 특징의 독립적인 조절을 가능하게 하는 GAN
- PGGAN 구조에서 Style transfer 개념을 적용하여 generator architetcture를 재구성 한 논문


## Entanglement, Disentanglement
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/a43a5978-d622-4310-bb76-38ccc29aea72)
- (a) : 이상적인 latent space
  - linear한 attrubute
- (b) : 기존의 generator ( PGGAN )
  - entangle 된 상태
  - style(특징)이 서로 상호작용 하여 영향을 미침
- (c) : disentangle한 latent space
  - W를 이용하여 각 특성의 변화를 linear하게 조절할 수 있게 됨
  - W(Linear Transformation)는 입력 벡터를 행렬과 벡터의 곱셈으로 변환하는 것을 의미
  - 표정, 머리 스타일, 머리카락 색상 등을 각각 다르게 제어
 
(b)는 PGGAN의 경우입니다. 데이터의 분포를 Gaussian으로 가정하기 때문에, Z space는 원래의 분포가 Gaussian에 맞춰 구부러져 모델링될 것입니다. 때문에 원래 분포보다 뒤틀림이 생기고, 보다 engtangle될 수 밖에 없습니다.

(c)의 경우는 이러한 entanglement를 방지하고자, mapping network를 통해 imediate latent space로 한번 보내서 less entangle하게 만듭니다. latent space Z보다 less entangle한 imediate latent space W에서 이미지를 생성하게되어 style을 interpolation하는 과정에서 더 linear하게 동작할 수 있습니다.

## Style-based Generator
- Generator에 latent vector z가 바로 입력되게 때문에 entangle하게 되어서 불가능 하다는 단점을 해
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/2f6e4b80-052b-441d-b011-fd70e109be6a) 
- Traditional Generator
  - latent vector(잠재 벡터)가 normalize(정규화) 되는 구조
  - training data가 latent space(잠재 공간)의 probability density(확률 밀도)를 따라야 하기 때문에 entanglement하게 됨
  - 즉 실제 데이터와 유사한 이미지만을 만들기 때문에 원하는 방향이 아닌 결과가 생성될 수 있음
- Style-based Generator
  1. Mapping Network
     - latent vector z를 중간 latent space W의 스타일 코드로 매핑(변환)하는 역할
     - 중간 latent space W를 사용함으로써, 이미지 스타일과 특징을 독립적으로 조절
  2. Synthesis Network
     - 중간 latent space W의 정보를 활용하여 이미지를 생성하는 역할
     - 중간 latent space의 스타일 코드와 이미지 특징을 조합하여 다양한 스타일의 이미지를 생성
     - 이미지 생성의 예측 가능성과 다양성을 높이는 데 도움을 줌
    
## Z-space entanglement
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/28ade84c-5bc8-4800-942a-d6987ac8ddd5)


  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/9718154e-4710-4a2e-96e0-d52108a30dd5)  


