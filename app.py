import streamlit as st
import pandas as pd
import random
import datetime

st.set_page_config(
    page_title = 'デジタルおみくじ',
    page_icon="🎋",
    layout="centered"
    )

# 今日の日付を取得
today = datetime.date.today()
# 曜日の日本語表記
weekday_jp = ["月", "火", "水", "木", "金", "土", "日"]
weekday = weekday_jp[today.weekday()]
# 日付を表示
st.markdown(f"### {today.year}年{today.month}月{today.day}日({weekday})")
st.write(' ')

omikuji_df = pd.read_csv('omikuji.csv', encoding='utf-8') 

st.markdown('<div class="footer">毎日一回、心を清めておみくじを引きましょう</div>', unsafe_allow_html=True)
st.write(' ')

if st.button('🎋 おみくじを引く 🎋'):
    i = random.randint(0,99)
    result = omikuji_df.iloc[i, :]

    st.markdown(f'## {result["運勢"]}！')
    st.write(' ')
    st.markdown(f"> {result['和歌／漢詩']}")
    st.markdown(f"*現代語訳: {result['現代語訳']}*")
    st.write(' ')
    st.expander('詳細', expanded=False).markdown(
        f"""
        🙏願望: {result['願望']}  
        🧑‍🤝‍🧑待人: {result['待人']}  
        🔍失物: {result['失物']}  
        🧳旅行: {result['旅行']}  
        💰商売: {result['商売']}  
        🎓学問: {result['学問']}  
        🤼争事: {result['争事']}  
        💘恋愛: {result['恋愛']}  
        🏠転居: {result['転居']}  
        🩺病気: {result['病気']}  
        """
    )

# サイドバー
with st.sidebar:
    st.write("おみくじの背景について")
    st.markdown("""
    おみくじは古来より神社仏閣で行われてきた日本の伝統的な占いです。  
    このアプリでは、古典的な和歌や漢詩と共に運勢を占います。
    
    一日一回、清らかな気持ちで引くことをお勧めします。
    """)
    
    st.markdown("---")
    st.markdown("##### バージョン情報")
    st.markdown("デジタルおみくじ v1.0.0")
    st.markdown("©2025 ojizou003")
