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
    
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/9a33f489-fd94-4c70-82e3-2f7d177321f1)  
## mapping network
- mapping network는 8-layer MLP로 구성
- 512차원 z를 512차원 w로 mapping해주는 역할  

**Z (잠재 공간 Z)**  
- 정규분포(Gaussian)를 따르는 잠재 벡터(벡터 형태의 숫자) 공간
- Z 내의 값은 무작위로 샘플링되며 이미지 생성에 무작위성을 주입하기 위해 사용
- 주로 이미지 생성의 난수 초기값으로 활용되며, 초기에는 무작위한 이미지를 생성합니다.  

**W (중간 잠재 공간 W)**
- 매핑 네트워크(Mapping Network)를 통해 변환된 스타일 코드(Style Code)를 담는 공간
- 이미지 스타일 및 특징을 표현하고 제어
- 각 차원은 이미지의 특정 특징 또는 스타일을 나타냄
### 정리  
- Z는 초기 무작위 벡터로부터 시작하여 이미지 생성을 위한 무작위성과 다양성을 제공하는 공간
- W는 이미지의 스타일과 특징을 조절하고 제어하는 중간 공간
- W는 Z를 더 구조적이고 예측 가능한 방식으로 변환하여 이미지 생성의 예측 가능성과 다양성을 향상시키는 역할

## synthesis network
- 4x4부터 1024x1024 resolution feature map을 만드는 총 9개의 style block으로 구성
- 마지막에는 RGB로 바꿔주는 layer
- style block의 input은 이전 style block의 output인 featuremap
- style block당 두번의 convolution을 진행

### Style Modules (AdaIN-Adaptive Instance Normalization)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/fdf0472d-ee2b-4f55-a313-d4518f3b7042)
- content 이미지 x에 style 이미지 y의 스타일을 입힐 때 사용하는 normalization
- style transfer를 하는 경우 꼭 필요한 단계
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/974b9239-0697-47ca-b1ac-41ee2bf303fe)

### Constant Input
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/e30b4e76-400f-4abd-97c5-1b3c49ab2a50)
- synthesis network는 4x4x512 contant tensor에서 부터 시작
- w를 입력으로 받기 때문에, PGGAN과 같이 z에서 convolution연산을 하지 않아도 됨
- random한 noise에서 시작하는 것보다 contant에서 시작하는 것이 더욱 성능이 좋음
- disenstangle한 w를 사용하기 때문에 entangle된 z를 사용하는 것을 피하는 효과 때문이라고 예상 (특징과 스타일이 서로 분리)

### Stochastic Variation (확률적 변화)
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/3f99b407-85d3-4de0-8dd4-fe942469d4df)
- 머리카락의 배치이나 모공, 주근깨 같이 아주 세밀하고 때에 따라 달라지는 특징 (Stochastic Variation)
- 세부적인 attribute를 추가하기 위해 Noise를 추가하여 이미지의 다양성을 증가시키는 부분
- Gaussian에서 sampling한 nosie를 Convolution의 output인 featuremap에 더해줌
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/008087d7-6afa-4e5f-99fc-7890b76fd34d)

## Properties of the style-based generator
### Style Mixing
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/b83ba643-6605-49ce-90a1-b0daacd777f7)
- correlation되지 않게 style을 섞어주는 방법 (상호작용 없이 style 섞기)
- latent code 2개를 sampling (z1, z2)한 후, mapping network를 거쳐 2개의 style code(w1, w2)를 만드는 것
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/1e9e96bd-a523-4145-8454-22261177cb38)
- w_A로만 만든 source A와 w_b로만 만든 source B
- 어느 resolution에서 cross over하여 style을 합성하는지에 따른 결과
  - Coarse style : coarse resolution (4^2 -> 8^2)
    - high level aspects (ex. pose, general hair style, face shape, eyeglasses) 전반적인, 큰 정보
  - Middle style : middle resolution(16^2 -> 32^2)
    - smaller scale facial features, hair style,eyes open/closed from B
  - Fine style : fine resolution(64^2 -> 1024^2)
    - hair color, 피부톤 같은 세밀한 정보 
- fine resolution에서 cross over한다면, 전반적인 style은 source A를 따르고 머리색이나 세밀한 부분들같은 fine style는 source B를 담아 생성된 결과
### Stochastic variation
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/d0a373b9-d745-4ff4-bc11-6f486f69db39)


- content 이미지 정규화
- style 이미지에 affine transform
- style scaling factor σ(y)와 style bias factor μ(y)를 얻음
- 정규화된 content이미지는 이에 맞춰 scaling되고 bias가 더해짐
Adaptive Instance Normalization인만큼 Instance Normalization에서 style factor들이 적용된 것입니다. AdaIN역시 IN과 동일하게 instance(각 이미지), channel별로 normalize


  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/9718154e-4710-4a2e-96e0-d52108a30dd5)  


