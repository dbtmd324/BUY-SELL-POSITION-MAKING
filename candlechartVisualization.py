import os

import pandas as pd
import plotly.graph_objs as go

# 0. image 저장 폴더 생성
if not os.path.exists('images'):
    os.makedirs('images')

# 1. OHLCV 데이터 불러오기
df = pd.read_csv('A035420.csv', index_col=0, parse_dates=True, sep=',', names=['date', 'open', 'high', 'low', 'close', 'volume'])

# 2. 이미지 생성
fig = go.Figure(data=[go.Candlestick(x=df.index[:79], # x축 범위 설정(79인 이유): 하루 장시간 범위가 79임
                                     open=df['open'],
                                     high=df['high'],
                                     low=df['low'],
                                     close=df['close'],
                                     decreasing=dict(fillcolor='blue', line=dict(color='blue')), # 음봉: 파란색 설정
                                     increasing=dict(fillcolor='red', line=dict(color='red')) # 양봉: 빨간색 설정
                                     )])

fig.update_layout(xaxis_rangeslider_visible=False, xaxis={'visible': False}, yaxis={'visible': False}) # x축, y축 등 기타 요소 안보이게 설정

# 3. 이미지 저장
fig.write_image('images/naver_test.png') # image 폴더에 저장