# 이건 중간에 하위폴더 생성이어서 새로고침으로 갱신안되고 app.py를 다시 새로 시작해야한다

import streamlit as st
# 입력을 변수로 받아서 출력에 넘겨주면 됩니다.

# 1. 버튼을 누르면 화면에 True 라고 코드를 리턴하는 간단한 동작 작성
a = st.button('클릭') # False가 기본값으로 매겨진
st.write(a)

if st.button('클릭2'):
    st.write(True)

# 2. 사진을 찍으면 다운로드 버튼으로 사진을 다운로드 받을 수 있게 작성
if image := st.camera_input('Click a Snap2'): # 사진을 찍기 전에는 들여쓰기 안의 코드를 실행하지 않습니다.
    st.download_button('다운로드', image, 'my.png')