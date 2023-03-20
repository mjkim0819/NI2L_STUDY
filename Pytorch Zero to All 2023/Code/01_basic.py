w_list = []
# weight(가중치)들을 모아 놓은 리스트
mse_list = []
# 오차값들을 모아 놓은 리스트

# 가중치 값 기계산하기
for w in np.arange(0.0, 4.1, 0.1):
# 0.0에서 4.1전까지 w값을 0.1씩 증가시키면서 반복
# 0.0  0.1  0.2  0.3  ...  3.8  3.9  4.0
    print("w=", w)
    # w=@ 형태로 w 값 출력
    l_sum = 0
    # l_sum : loss((예측값-정답)^2)들의 합
    
    for x_val, y_val in zip(x_data, y_data):
    # x_val에 x_data들을(1.0 2.0 3.0), y_val에 y_data들(2.0 4.0 6.0)을 묶어서 대입
        y_pred_val = forward(x_val)
        # x_val 데이터를 forword 함수에 넣은 값 : 예측값
        # y_pred_val = x_val * w
        l = loss(x_val, y_val)
        # x_val과 y_val를 이용하여 loss 계산 : 오차값 계산
        # l = (y_pred_val - y) * (y_pred_val - y)
        l_sum += l
        # l_sum에 구한 l을 계속 더하기
        
        print("\t", x_val, y_val, y_pred_val, l)
        # x_val, y_val, y_pred_val, l 프린트하기
        # \t은 들여쓰기해서 출력
        # 보기 쉽게 정리하기 위해 \t 사용
    # Now compute the Mean squared error (mse) of each
    # Aggregate the weight/mse from this run
    # MSE는 Mean squared error(평균제곱오차) 오차의 제곱 최솟값을 구하면서 weight를 찾아가는 방식
    print("MSE=", l_sum / len(x_data))
    # l_sum / len(x_data) : x_data의 크기로 l_sum을 나누기 => 평균 구하기
    
    # 출력 예시
    # w= 0.0
	#    1.0 2.0 0.0 4.0
	#    2.0 4.0 0.0 16.0
	#    3.0 6.0 0.0 36.0
    # MSE= 18.666666666666668
    # w= 0.1
	#    1.0 2.0 0.1 3.61
	#    2.0 4.0 0.2 14.44
	#    3.0 6.0 0.30000000000000004 32.49
    # MSE= 16.846666666666668
    # w= 0.2
	#    1.0 2.0 0.2 3.24
	#    2.0 4.0 0.4 12.96
	#    3.0 6.0 0.6000000000000001 29.160000000000004
    # MSE= 15.120000000000003
    
    
    w_list.append(w)
    # w_list에 w 추가
    mse_list.append(l_sum / len(x_data))
    # mse_list에 평균 추가
