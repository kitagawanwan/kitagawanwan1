import streamlit as st
import random
st.title('人生がちゃ')
if st.button('おみくじを引く'):
   results = ['東大理三','ｓｆｃ','九大','分大医学部','ででーん。。。。活水女子大学。。。。','学習院大学''熊本大学']
   result = random.choice(results)
   st.write(f'結果:{result}')