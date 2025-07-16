import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    [
       {"command": "st.selectbox", "rating": 4, "is_widget": True},
       {"command": "st.balloons", "rating": 5, "is_widget": False},
       {"command": "st.time_input", "rating": 3, "is_widget": True},
   ]
)


st.bar_chart(df.rating,x_label=df['command'])

st.bar_chart(df.rating, x_label='x축 제목') # streamlit의 default chart는 altair라는 다른 시각화 패키지

import plotly.express as px

# Plotly Bar Chart
fig = px.bar(
    df,
    x="command",     # x축에 command
    y="rating",      # y축에 rating
    color="command", # command별 색깔 구분
    labels={"command": "x축 제목", "rating": "Rating"},
    title="Command Rating Bar Chart"
)

# # Streamlit에 출력: use_container_width=True - 현재 창 사이즈 그대로 출력하겠다
st.plotly_chart(fig, use_container_width=True)


data = 'hello12'
# 1. 버튼을 누르면 화면에 True 라고 코드를 리턴하는 간단한 동작 작성

# 입력
trig=st.button('True')
if trig == True:
    st.write(trig)
# st.data_editor('Edit DF', df) <- 이걸로 하면 에러남
st.data_editor(df)
st.checkbox('Option 1')
st.radio('Pick Country:', ['France','Germany'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])

st.text_input('Enter Article')
st.number_input('Enter required number')
st.text_area('Entered article text')
st.date_input('Select date')
st.time_input('Select Time')
st.file_uploader('File CSV uploader')
st.download_button('Download Source data', data)

# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
save = st.camera_input('Click a Snap')

# 아래같이 써놓으면 처음 시작할 때 같이 실행되므로 save가 없는 상태여서 에러가 발생함
# st.download_button('다운로드하기',save, 'my.png') 

if save : 
  st.download_button('다운로드하기',save, 'my.png') 
  

st.color_picker('Pick a color')


ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 출력
st.text('Tushar-Aggarwal.com')
st.markdown('[Tushar-Aggarwal.com](https://tushar-aggarwal.com)')
st.caption('Success')
st.latex(r''' e^{i\pi} + 1 = 0 ''')
st.write('Supreme Applcations by Tushar Aggarwal')
st.write(['st', 'is <', 3]) # see *
st.title('Streamlit Magic Cheat Sheets')
st.header('Developed by Tushar Aggarwal')
st.subheader('visit tushar-aggarwal.com')
st.code('for i in range(8): print(i)')
st.image('https://i.imgur.com/t2ewhfH.png')
# * optional kwarg unsafe_allow_html = True


print(ani_list) # 콘솔에는 실행되지만 streamlit에는 반영이 안된다

st.code(ani_list) # st를 활용한 문법을 써야함
st.write(ani_list)


for ani in ani_list:
    st.write(ani)


# * optional kwarg unsafe_allow_html = True

# 입력을 변수로 받아서 출력에 넘겨주면 됩니다.

# 1. 버튼을 누르면 화면에 True 라고 코드를 리턴하는 간단한 동작 작성

# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성