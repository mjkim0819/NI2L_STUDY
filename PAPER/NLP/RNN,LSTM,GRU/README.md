# RNN,LSTM,GRU
결과값이 출력층으로만 향하지 않고, 출력층과 동시에 다시 은닉층의 다음 계산 입력으로 들어감
### Sequence?
연속적인 입력(Sequential Input)으로부터 연속적인 출력(Sequential Output)을 생성하는 모델

![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/ef478ec7-8ef7-4909-bd2b-9b6a43a47653)  
- Xt : 입력 벡터  
- Yt : 출력 벡터  
- cell : 은닉층에서 결과를 내보내는 역할을 하는 노드  

RNN에서는 cell이 이전의 값을 기억하는 메모리의 역할 수행. (메모리 셀, RNN 셀)  
  




## 순환 신경망(Recurrent Neural Network, RNN)
- 내부에 순환 구조가 포함되어 있는 가장 기본적인 sequence 모델

![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/1c921eca-02c1-4a99-aebd-94965b5820c7)  
> t를 순서대로 펼친 그림  

### RNN 구조
![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/2c67b3f1-6509-4b66-8c61-264b9a77dcca) ![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/566e5e7e-373f-4c1c-99b7-d0da90eb5f84)
  
- h는 메모리 셀에서의 출력 값  
- y는 해당 시점에서의 출력  
- u(입력층을 위한 은닉층 가중치), v(출력층 가중치), w(이전 시점에서의 메모리 셀을 위한 은닉층 가중치)는 각각 가중치  

  - 은닉층 : 가중치 2개 사용  
  ![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/844aa8c3-8a19-48c0-aae2-9072e45bfd47)  
  - 출력층 : 한개의 가중치 사용  
  ![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/b03f1058-405a-4235-955c-3b7df91e6d7a)  

  
### RNN의 Short-term dependencies  
t는 t-1에서 전달된 정보에 의존  
=> 비교적 짧은 시퀀스에 대해서만 높은 효과를 보임.

![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/2ca10204-6d7e-466f-b974-7eed83562b9c)  
역방향으로 미분을 곱해 나가면서 계산을 진행하기 때문에, 시간의 크기가 커지면 기울기가 불안해지는 문제 발생.  


## 장단기 메모리(Long Short-Term Memory, LSTM)
- 덧셈과 곱셈 연산을 통해 불필요한 기억은 지우고, 필요한 부분을 기억.  
- cell state를 추가하여 멀리 떨어진 과거의 정보도 현재에 영향을 주도록 고안.  

![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/dd20f7c7-288c-47ed-b0c8-9865951ac3fe)  

### LSTM 구조
1. Gate
- **forget gate**  
![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/3468175b-9262-4804-9fd5-1de05ec2edaa)  
장기 상태의 어느 부분이 **삭제** 되어야 하는지 제어하는 역할  
  - f(t) : 현재 시점의 x와 이전 시점의 은닉 상태가 시그모이드 함수(삭제된 정보) 통과
  - c(t)와 곱연산
    - 0 => 정보가 많이 삭제된 상태
    - 1 => 정보가 온전한 상태
- **input gate**  
![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/8a2c031e-3cab-44d8-b8b4-c3648b4ec5e0)  
장기 상태의 어느 부분이 **기억** 되어야 하는지 제어하는 역할  
  - i(t) : 현재 시점의 x와 이전 시점의 은닉 상태가 시그모이드 함수 통과 (0~1)  
  - g(t) : 현재 시점의 x와 이전시점의 은닉 상태가 하이퍼볼릭탄젠트 함수 통과 (-1~1)  
  
2. Cell state
- Cell state  
![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/dedcd7fa-8f6f-424f-9cf6-4e99d23729e9)  
삭제 게이트와 입력 게이트를 거쳐 장기 기억을 하는 역할  
  - i(t)와 g(t) 곱연산 후 c(t)와 합연산  
    - 삭제 게이트의 출력값인 f(t)가 0 => 이전 시점의 셀 상태값의 영향력 0, 현재 시점의 셀 상태값만 의존  
    - 입력 게이트의 출력값인 i(t)가 0 => 현재 시점의 셀 상태값의 영향력 0, 이전 시점의 셀 상태값만 의존  
3. Hidden state  
- Hidden state  
![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/5eca7179-357e-45ad-be86-25fb74201a2f)  
장기 상태의 어느 부분을 읽어서 **현재 시점의 은닉상태**를 결정는 역할  
  - o(t) : 셀 상태값이 하이퍼볼릭탄젠트 함수 통과 (-1~1)  
    - 출력값과 연산되어 값이 걸러지는 효과  


## 게이트 순환 유닛(Gated Recurrent Unit, GRU)
- 더 단순한 구조(장기 의존성 문제 해결 유지, 은닉 상태 업데이트 계산 감소)  
- LSTM : 입력,삭제,출력 gate (3개)  
- GRU : 업데이트, 리셋 gate (2개)  

![image](https://github.com/mjkim0819/DP_Paper/assets/108729047/03385ddc-f12d-47f6-bd91-fb682a76133e)  

### GLU 구조
1. Gate
- **update gate**   
LSTM의 삭제 게이트와 입력 게이트 역할  
  - z(t) : 현재 시점의 x와 이전 시점의 은닉 상태가 시그모이드 함수(삭제된 정보) 통과  
    - 1 => 삭제 게이트가 열려 현재 시점의 셀 상태값에 이전 상태값이 반영 안됨  
- **reset gate**  
이전 상태의 어느 부분이 g(t)에 노출될지 제어하는 역  
  - r(t) : 현재 시점의 x와 이전 시점의 은닉 상태가 시그모이드 함수 통과 (0~1)  

parameter의 수가 작을수록 일반화 성능 증가 => 학습속도 
