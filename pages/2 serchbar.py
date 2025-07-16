import streamlit as st
import re

ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

# 텍스트를 입력받아서 해당 텍스트와 일치하는 이미지를 화면에 출력하는 검색창을 만들어 주세요.

image=st.text_input('text input')

print(re.search(image,'짱구는못말려'))

print(re.findall(image,'짱구는못말려'))
#if image:=st.text_input('text input') in ani_list:
#    st.image('https://i.imgur.com/t2ewhfH.png')