import os

import pandas as pd
import plotly.graph_objs as go

# 0. image 저장 폴더 생성
if not os.path.exists('images'):
    os.makedirs('images')

A = 'A377300'

# 1. OHLCV 데이터 불러오기
df = pd.read_csv(f'./OHLCV_data/{A}.csv', index_col=0, parse_dates=True, sep=',', names=['date', 'open', 'high', 'low', 'close', 'volume'])

# 2. 날짜 변경 line 저장
date_change_line_list = []
check_day = None
for i in range(len(df.index)) :
    # i 번째줄 date - 날짜[4:8] : mmdd
    cur_day = df.index[i][4:8]

    # 날짜가 바뀐지 확인 후 리스트 추가 및 기준점 변경
    if check_day != cur_day :
        date_change_line_list.append(i)
        check_day = cur_day
date_change_line_list = date_change_line_list[1:]

# # check
# print(len(date_change_line_list), date_change_line_list)
# for i in date_change_line_list :
#     print(df.index[i])
# exit()

# 3. 이미지 생성
for i in range(len(date_change_line_list) - 1) :
    start, end = date_change_line_list[i], date_change_line_list[i + 1] - 1
    print(start, end)

    fig = go.Figure(data=[go.Candlestick(x=df.index[start:end],
                                         open=df['open'][start:end],
                                         high=df['high'][start:end],
                                         low=df['low'][start:end],
                                         close=df['close'][start:end],
                                         decreasing=dict(fillcolor='blue', line=dict(color='blue')), # 음봉: 파란색 설정
                                         increasing=dict(fillcolor='red', line=dict(color='red')) # 양봉: 빨간색 설정
                                         )])

    fig.update_layout(xaxis_rangeslider_visible=False, xaxis={'visible': False}, yaxis={'visible': False}) # x축, y축 등 기타 요소 안보이게 설정

    # 4. 이미지 저장
    fig.write_image(f'images/{A}'+'_{0:05d}.png'.format(i)) # image 폴더에 저장