# 텍스트를 입력받아서 해당 텍스트와 일치하는 이미지를 화면에 출력하는 검색창을 만들어 주세요.
import streamlit as st

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

ani_name = st.text_input('애니메이션 이름 입력')

if ani_name:
    for ani in ani_list:
        if ani_name in ani:
            st.image(img_list[ani_list.index(ani)])


if tmp_input := st.text_input('에니메이션을 입력해주세요.'):
     for i, el in enumerate(ani_list):
         if tmp_input in el:
             st.image(img_list[i])