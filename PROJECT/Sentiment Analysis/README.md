#  Sentiment Analysis Project
___  



## 한국어 문장 감정 분류
  
> 데이터셋  

감정 분류를 위한 대화 음성 데이터셋  
![image](https://github.com/mjkim0819/NI2L_STUDY/assets/108729047/42f52d40-b967-4bc8-9260-bf4ef82bee12)  
한국어로 된 대화를 감정에 따라 분류해 둠.  
happiness, angry, disgust, fear, neutral, sadness, surprise 총 7개의 감정  
총 5명을 기준으로 라벨링이 되어있음.  
약 19,374개의 data   
https://aihub.or.kr/aihubdata/data/view.do?currMenu=&topMenu=&dataSetSn=263&aihubDataSe=extrldata  
  
  
> 사용 모델 

KoBERT  
구글에서 제안한 BERT 모델의 한국어판  
감정을 분석할 때, 긍정과 부정만으로 분류하는 것이 아닌 다중 분류가 가능한 것이 강점  

  
  
### Task
한국어로 주어진 문장에서 느껴지는 감정을 크게 7가지로 분류하기  
1. KoBert에 대해 공부하기
2. Colab에 기본적인 환경 세팅하기 (라이브러리, 데이터셋 불러오기)
3. 데이터 전처리 (한 문장에 담긴 감정이 여러개인데, 그 중 가장 많이 언급되는 감정을 따로 뽑기)
4. Tokenizer와 Padding을 통해 데이터 변환
5. 학습모델 생성 (KoBERT 사용)
6. 학습 진행 
  - 5명의 감정 중 대표되는 한가지의 감정만 출력하도록 학습 진행
  - 라벨링 5명을 각각 훈련해서 총 5개의 결과값을 보이고 그 중 가장 대표되는 감정을 뽑도록 학습 진행
  - 감정의 정도도 포함시키도록 학습 진행
7. 평가 및 수정
8. 결과 분석

### Problem
kobert api 제공이 변하면서 기존의 코드들을 사용하기 어려움

