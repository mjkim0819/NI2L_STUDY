# GloVe
## 등장배경
- LSA (카운트 기반)
  - 전체적인 통계 정보(문서 전체의 각 단어의 빈도수를 담은 행렬)를 입력으로 받아 차원을 축소(Truncated SVD)하여 잠재된 의미를 끌어내는 방법론
  - 말뭉치 (corpus)의 전체적인 통계정보를 반영할 때 유
- Word Embedding (예측 기반)
  - window를 사용해 문서 전체가 아니라 중심단어를 둘러싼 주변단어의 실제값과 예측값에 대한 오차를 손실 함수를 통해 줄여나가며 학습하는 방법론
  - 단어 간 유추에 뛰어난 성능  
두 방식을 부분적으로 차용하여 GloVe 등장
- GloVe
  - 임베딩된 두 단어벡터의 내적이 말뭉치 전체에서의 동시 등장확률 로그값이 되도록 목적함수를 정의
  - 단어 임베딩의 선형성(내적)을 내포한 채로 문서 전체의 통계치를 반영
  
## 목적

## 윈도우 기반 동시 발 행렬 (Window based Co-occurrence Matrix)

## 동시 등장 확 (Co-occurrence Probability)
### 1) k = soild 일 때
### 2) k = gas 일 때
### 3) k = water 일 때
### 4) k = fasion 일 때

## 손실 함수(Loss function)
