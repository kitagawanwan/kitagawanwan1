import streamlit as st
import random
st.title('おみくじアプリ')
if st.button('おみくじを引く'):
   results = ['∫(5x^3+4x^2+8x)dx=','x^3-3x^2+5x+5=0を微分せよ','a1=2,a(n+1)=3an+4の一般功をを求めよ','x^2+y^2=7921の半径は?','2×7=','1+1=']
   result = random.choice(results)
   st.write(f'結果:{result}')