# Word2Vec
단어 벡터 간 유의미한 유사도를 반영할 수 있도록 단어의 의미를 수치화 할 수 있는 방법  

## Word Embedding
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/237035bf-6018-4bf5-8c83-b5d982ea1034)  
왼쪽은 희소 표현, 오른쪽은 밀집 표현  
  
### 희소 표현(Sparse Representation)
벡터 또는 행렬(matrix)의 대부분 값이 0으로 표현되는 방법  
Ex) 원 핫 벡터 [ 0, 0, 0, 0, 1, 0, 0 ]  
    
- 장점
  - 표현하고자 하는 단어를 간단하게 표현
- 단점
  - 데이터셋 내 단어가 많으면, 벡터가 기하급수적으로 커짐
  - 원 핫 벡터처럼 단위 벡터로 표현하면 단어간 유사 관계를 나타낼 수 없음 (word 자체가 갖는 정보를 담고 있지 않고 단순하게 index만을 담고 있음)  
  
  
  
### 밀집 표현(Dense Representation)
모든 단어의 벡터 표현 차원을 맞춰 각 벡터 값이 0과 1이 아닌 실수 값으로 표현되는 방법  
Ex) 워드 임베딩 (단어를 밀집 벡터 형태로 표현)  
    
- 장점
  - 저차원에서 단어의 의미를 여러 차원의 공간에 분산하여 표현하기 때문에 단어의 유사도 표현 가능 
  
### 희소 표현과 밀집 표현의 비교
데이터가 10000개 있을 때  
- 희소표현
  - 강아지 = [ 0 0 0 0 1 0 0 0 0 0 0 0 ... 중략 ... 0] # 이때 1 뒤의 0의 수는 9995개.  -> 차원은 10000
- 밀집표현
  - 강아지 = [0.2 1.8 1.1 -2.1 1.1 2.8 ... 중략 ...] # 이 벡터의 차원은 128  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/037005fb-aeae-4d4a-9146-e4123a2cfbb9)    
  
  
## Word2Vec
**분포 가설(distributional hypothesis)** 을 가정 하에 표현한 분산 표현을 따라 **벡터값을 통해 의미적으로 가까운 단어** 를 찾는 방법  
ex)  ‘강아지’라는 단어는 ‘귀엽다’, ‘예쁘다’, ‘애교’ 등의 단어와 자주 사용된다면, 단어들의 벡터화 값이 유사할 것이다.  
이미 분포 가설을 사용한 경우는 많지만 Word2Vec는 **효율성** 문제로 주목받게 됨.  
  
아래는 Word2Vec의 대표적인 학습 방법 2가지  
### CBoW(Continuous Bag of Words)
주변에 있는 단어들로 중간에 있는 단어들을 예측하는 방법  
주변 단어 크기에 따라 말뭉치(corpus)를 슬라이딩하면서 중심 단어의 주변 단어들을 보고 각 단어의 벡터 값을 업데이트 해나가는 방식  
  
#### 용어 설명
중심 단어(center word) : 예측하고자 하는 단어  
주변 단어(context word) : 예측에 사용하는 단어  
윈도우(window) : 중심 단어를 예측하기 위해 확인 할 앞 뒤 단어의 크기  
슬라이딩 윈도우(sliding window) : 윈도우를 옆으로 움직여서 주변 단어와 중심 단어의 선택을 변경해가며 학습을 위한 데이터 셋을 만드는 방법  
  
#### 학습 방법
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/8c6bf32d-fcaf-4291-878e-c256e90117a5)  
윈도우가 2개일 때 학습이 진행되는 방식을 표현하는 그림  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/775d83fe-a6de-48e6-be05-1960f72d3e10)   
- Input layer : 주변 단어들의 원 핫 인코딩  
- Ouput layer : 중심 단어의 원 핫 인코딩   
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/8f4aa242-8de1-4cbd-9cd5-3f8bd07792c5)  
- 은닉층이 하나인 얕은 신경망  
- 은닉층에 활성화 함수가 없으며, 연산을 담당하는 층 (투사층이라고도 불림)  
- 투사층의 크기 = 5 -> CBoW를 수행하고 얻는 단어의 임베팅 차원 = 5
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/cd10f627-272b-437a-bbf0-6134931005ba)   
- 가중치 W = V*M
- 입력 벡터와 가중치 W 행렬의 곱은 사실 W행렬의 i번째 행을 그대로 읽어오는 것
- lookup table이라고 불림
- W와 W'는 다름 (W = 5 * 7, W' = 7 * 5)
- CBOW의 목적은 W와 W'를 잘 훈련시키는 것  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/02bc9f8e-4ed8-435c-b6e0-e9a10d2a9dd7)  
- 주변 단어에 가중치 W가 곱해진 결과는 은닉층에서 평균으로 구해짐
- CBow와 Skip-Gram의 차이
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/9db69833-91bc-49c9-9ca9-fe803a06aaaf)  
- 구해진 평균은 은닉층을 거쳐 W'와 곱해짐  
- 다시 입력층과 같은 크기의 차원으로 변화  
- softmax를 통해 총합이 1이 나오도록 수정
- 손실함수로 cross-entropy 사용
- 원 핫 벡터로 다시 변
  
  
  
### Skip-Gram
중심 단어를 통해 주변의 단어들을 예측하는 방법  
입력층과 출력층만 CBoW와 반대이고 동일한 방식  
중심 단어에 대해서 주변 단어를 예측하므로 투사층에서 벡터들의 평균을 구하는 과정은 없음  
  
전반적으로 CBoW보다 성능이 좋다고 알려져 있음  
  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/30d6b4f9-5aa0-44e2-9e2f-bb46621a8fdb)  
  
  
## Word2Vec의 최적화
CBow와 Skip-Gram은 학습속도가 느림
- 입력으로 주어진 단어를 N차원의 벡터로 투영한 뒤, softmax함수를 이용하여 출력 단어를 맞추도록 학습  
- 정확한 계산을 위해 데이터 셋에 존재하는 모든 단어를 한꺼번에 고려하여 계산량이 매우 커졌기 때

### Hierarchical softmax
softmax함수를 빠르게 계산하기 위한 방식  
- 모든 단어 별 등장 빈도를 고려하여 이진트리 구성
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/1bea4972-c192-429c-ae53-99c0280bd638)   
1. 데이터 상 가장 높은 빈도의 단어를 트리의 루트로 지정
2. 자식 노드는 2,3번 높은 빈도의 단어로 지정
3. 반복  
  
  
### Negative sampling
softmax함수로 많은 단어를 계산하지 않고, 몇 개만 뽑아서 다른 방식으로 계산하는 방식  
긍정, 부정 예시 중 부정적인 예시의 일부만 뽑아서 사용하는 방식  
실제로 말뭉치(corpus)에는 부정적인 예시가 많이 존재  
- 긍정 부정 예시
  - 나는 임베딩 공부를 하고 있다 -> 중심단어가 임베딩 일때
  - 긍정 : 나는, 공부를
  - 부정 : 하고, 있다
  
## 한계점
1. 단어의 형태학적 특성을 반영하지 못함
  - ‘teach’, ‘teacher’, ‘teachers’
  - 의미적으로 유사하지만, 개별 단어(unique word)로 처리되어 벡터값이 다르게 구성됨
2. 희소한 단어(rare word)를 임베딩하지 못함
  - 분포 가설을 기반으로 학습하기 때문에 단어 빈도 수의 영향을 많이 받음
3. OOV의 처리가 어려움
  - 사전에 없는 단어
  - 새로운 단어가 등장하면 데이터 전체를 다시 학습시켜야 함   