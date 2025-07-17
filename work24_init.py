
'''
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import warnings

warnings.filterwarnings('ignore')

# --- 1. 샘플 데이터 생성 (기존 코드를 바로 실행할 수 있도록) ---
# 실제 데이터프레임 'df1_unique'가 있다면 이 부분은 삭제하고 실제 데이터를 사용하세요.
# data = {
#     '3차분류': ['웹개발', '웹개발', '데이터분석', '데이터분석', 'UI/UX', 'UI/UX', '서버관리', '웹개발'],
#     '제목': ['과정A', '과정B', '과정C', '과정D', '과정E', '과정F', '과정G', '과정H'],
#     '만족도점수': [4.5, 4.7, 4.8, 4.6, 4.9, 4.7, 4.3, 4.5],
#     '정원_대비_신청률': [1.2, 1.5, 1.8, 1.3, 2.0, 1.6, 0.9, 1.4],
#     '실제훈련비': [3000000, 3200000, 4500000, 4200000, 3800000, 3500000, 2500000, 3100000],
#     '훈련기간_일': [90, 100, 120, 110, 95, 90, 80, 95]
# }
# df1_unique = pd.DataFrame(data)

df1_unique = pd.read_csv("훈련과정_전체데이터_ver4.csv")
mask = df1_unique['3차분류'].notna() # 예시를 위한 마스크

# --- 2. 데이터 집계 (사용자 코드) ---
agg_df = df1_unique[mask].groupby('3차분류').agg(
    훈련_개수=('제목', 'count'),
    만족도점수=('만족도점수', 'mean'),
    정원_대비_신청률=('정원_대비_신청률', 'mean'),
    실제훈련비=('실제훈련비', 'mean'),
    훈련기간_일=('훈련기간_일', 'mean')
)

# 실제훈련비/훈련기간_일 평균 컬럼 추가
agg_df['일_평균_훈련비'] = agg_df['실제훈련비'] / agg_df['훈련기간_일']


# --- 3. Streamlit 앱 구성 ---

st.set_page_config(layout="wide") # 넓은 레이아웃 사용

st.title('📚 3차 분류별 훈련 과정 분석')
st.info('이 앱은 3차 분류에 따른 훈련 과정의 개수와 주요 지표를 시각화합니다.')


# --- 4. 메인 막대그래프 시각화 ---
st.header('분류별 훈련 개수')

# Plotly 차트 생성 (hover_data는 그대로 유지하여 마우스오버 기능도 제공)
fig = px.bar(
    agg_df,
    x=agg_df.index,
    y='훈련_개수',
    hover_data=['만족도점수', '정원_대비_신청률', '일_평균_훈련비'],
    labels={'x': '3차 분류', '훈련_개수': '훈련 개수'},
    title='3차 분류별 훈련 과정 수'
)
fig.update_xaxes(tickangle=45)
fig.update_layout(title_x=0.5) # 제목 중앙 정렬

# Streamlit에 차트 표시
st.plotly_chart(fig, use_container_width=True)


st.divider() # 시각적 구분을 위한 라인


# --- 5. Hover 데이터를 별도 섹션으로 시각화 ---
st.header('분류별 상세 지표 비교')
st.markdown('아래 드롭다운에서 특정 `3차 분류`를 선택하여 상세 평균값을 확인하세요.')

# Selectbox로 사용자에게 3차 분류 선택 옵션 제공
selected_category = st.selectbox(
    '분석할 3차 분류를 선택하세요:',
    options=agg_df.index
)

# 선택된 분류의 데이터 추출
selected_data = agg_df.loc[selected_category]

# st.columns를 사용하여 깔끔하게 3개의 메트릭으로 표시
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label=f"⭐ 평균 만족도 점수",
        value=f"{selected_data['만족도점수']:.2f} 점"
    )

with col2:
    st.metric(
        label=f"📈 평균 신청률",
        value=f"{selected_data['정원_대비_신청률'] :.2f} %"
    )
print(selected_data['일_평균_훈련비'])

with col3:
    st.metric(
        label=f"💰 일 평균 훈련비",
        value=f"{selected_data['일_평균_훈련비']:,.0f} 원"
    )

# 선택된 데이터의 전체 정보도 테이블로 표시
st.subheader(f"'{selected_category}' 분류의 전체 데이터")
st.dataframe(selected_data.to_frame().T.style.format({
    '만족도점수': '{:.2f}',
    '정원_대비_신청률': '{:.2%}',
    '실제훈련비': '{:,.0f} 원',
    '훈련기간_일': '{:.0f} 일',
    '일_평균_훈련비': '{:,.0f} 원'
}))
'''
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import warnings

warnings.filterwarnings('ignore')

# --- 1. 샘플 데이터 생성 ---
# 실제 데이터프레임 'df1_unique'가 있다면 이 부분은 삭제하고 실제 데이터를 사용하세요.
data = {
    '3차분류': ['웹개발', '웹개발', '데이터분석', '데이터분석', 'UI/UX', 'UI/UX', '서버관리', '웹개발'],
    '제목': ['과정A', '과정B', '과정C', '과정D', '과정E', '과정F', '과정G', '과정H'],
    '만족도점수': [4.5, 4.7, 4.8, 4.6, 4.9, 4.7, 4.3, 4.5],
    '정원_대비_신청률': [1.2, 1.5, 1.8, 1.3, 2.0, 1.6, 0.9, 1.4],
    '실제훈련비': [3000000, 3200000, 4500000, 4200000, 3800000, 3500000, 2500000, 3100000],
    '훈련기간_일': [90, 100, 120, 110, 95, 90, 80, 95]
}
df1_unique = pd.DataFrame(data)
mask = df1_unique['3차분류'].notna()

# --- 2. 데이터 집계 ---
agg_df = df1_unique[mask].groupby('3차분류').agg(
    훈련_개수=('제목', 'count'),
    만족도점수=('만족도점수', 'mean'),
    정원_대비_신청률=('정원_대비_신청률', 'mean'),
    실제훈련비=('실제훈련비', 'mean'),
    훈련기간_일=('훈련기간_일', 'mean')
).sort_values(by='훈련_개수', ascending=False) # 훈련 개수 순으로 정렬

agg_df['일_평균_훈련비'] = agg_df['실제훈련비'] / agg_df['훈련기간_일']


# --- 3. Streamlit 앱 구성 ---
st.set_page_config(layout="wide")
st.title('📚 3차 분류별 훈련 과정 분석')

# --- 4. 메인 막대그래프 (훈련 개수 기준) ---
st.header('분류별 훈련 개수')
fig_main = px.bar(
    agg_df,
    x=agg_df.index,
    y='훈련_개수',
    title='3차 분류별 훈련 과정 수'
)
st.plotly_chart(fig_main, use_container_width=True)

st.divider()

# --- 5. 모든 Hover 데이터를 그래프로 한 번에 시각화 ---
st.header('주요 지표 전체 비교')
st.markdown('각 주요 지표를 기준으로 모든 분류를 한눈에 비교합니다.')

# 3개의 컬럼을 만들어 각 그래프를 나란히 배치
g_col1, g_col2, g_col3 = st.columns(3)

with g_col1:
    # 만족도 점수 그래프 (높은 순)
    fig1 = px.bar(agg_df.sort_values('만족도점수', ascending=False),
                  x='만족도점수', y=agg_df.index, orientation='h',
                  title='⭐ 평균 만족도 점수', labels={'y': '3차 분류'})
    st.plotly_chart(fig1, use_container_width=True)

with g_col2:
    # 평균 신청률 그래프 (높은 순)
    fig2 = px.bar(agg_df.sort_values('정원_대비_신청률', ascending=False),
                  x='정원_대비_신청률', y=agg_df.index, orientation='h',
                  title='📈 평균 신청률', labels={'y': '3차 분류'})
    fig2.update_xaxes(tickformat=".0%") # x축 서식을 %로 변경
    st.plotly_chart(fig2, use_container_width=True)

with g_col3:
    # 일 평균 훈련비 그래프 (높은 순)
    fig3 = px.bar(agg_df.sort_values('일_평균_훈련비', ascending=False),
                  x='일_평균_훈련비', y=agg_df.index, orientation='h',
                  title='💰 일 평균 훈련비', labels={'y': '3차 분류'})
    st.plotly_chart(fig3, use_container_width=True)

st.divider()

# --- 6. 분류별 상세 지표 확인 (훈련 개수 포함) ---
st.header('분류별 상세 지표 확인')

selected_category = st.selectbox(
    '분석할 3차 분류를 선택하세요:',
    options=agg_df.index
)

selected_data = agg_df.loc[selected_category]

# 4개의 컬럼을 만들어 메트릭 표시 (훈련 개수 추가)
m_col1, m_col2, m_col3, m_col4 = st.columns(4)

with m_col1:
    st.metric(
        label=f"🔢 훈련 개수",
        value=f"{selected_data['훈련_개수']} 개"
    )

with m_col2:
    st.metric(
        label=f"⭐ 평균 만족도 점수",
        value=f"{selected_data['만족도점수']:.2f} 점"
    )

with m_col3:
    st.metric(
        label=f"📈 평균 신청률",
        value=f"{selected_data['정원_대비_신청률'] * 100:.1f} %"
    )

with m_col4:
    st.metric(
        label=f"💰 일 평균 훈련비",
        value=f"{selected_data['일_평균_훈련비']:,.0f} 원"
    )

# 전체 데이터 테이블 표시 (포맷팅에 '훈련_개수' 추가)
st.subheader(f"'{selected_category}' 분류의 전체 데이터")
st.dataframe(selected_data.to_frame().T.style.format({
    '훈련_개수': '{:d} 개',
    '만족도점수': '{:.2f}',
    '정원_대비_신청률': '{:.2%}',
    '실제훈련비': '{:,.0f} 원',
    '훈련기간_일': '{:.0f} 일',
    '일_평균_훈련비': '{:,.0f} 원'
}), use_container_width=True)