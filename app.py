import streamlit as st
from PIL import Image

st.title("テストです")
st.caption("これはテストアプリです。")
st.subheader("自己紹介")
st.text("Puthonのテストしてます〜")

code = '''
import streamlit as st

st.title("テストです")
'''

st.code(code, language='Python')

image = Image.open('IMG_9940.PNG')
st.image(image, width=200)

with st.form(key = 'profile_form'):
    name = st.text_input("名前")
    address = st.text_input("住所")   
    
    age_category = st.selectbox(
        '年齢層',
        ['子供', '大人']
        )

    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
    if submit_btn:
        st.text(f'ようこそ{name}さん{address}に書類を送付')
        st.text(f'年齢層{age_category}')