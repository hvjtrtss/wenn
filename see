import streamlit as st

st.set_page_config(page_title="看看你后面", layout="centered")

st.markdown("<h1 style='color:red; text-align:center;'>你看看你后面吧</h1>", unsafe_allow_html=True)
st.markdown("---")

# 注入 CSS 实现抖动效果
shake_css = """
<style>
@keyframes shake {
  0% { transform: translate(1px, 1px) rotate(0deg); }
  10% { transform: translate(-1px, -2px) rotate(-1deg); }
  20% { transform: translate(-3px, 0px) rotate(1deg); }
  30% { transform: translate(3px, 2px) rotate(0deg); }
  40% { transform: translate(1px, -1px) rotate(1deg); }
  50% { transform: translate(-1px, 2px) rotate(-1deg); }
  60% { transform: translate(-3px, 1px) rotate(0deg); }
  70% { transform: translate(3px, 1px) rotate(-1deg); }
  80% { transform: translate(-1px, -1px) rotate(1deg); }
  90% { transform: translate(1px, 2px) rotate(0deg); }
  100% { transform: translate(1px, -2px) rotate(-1deg); }
}

.shaky-text {
    color: red;
    font-size: 22px;
    font-weight: bold;
    animation: shake 0.5s infinite;
}
</style>
"""

st.markdown(shake_css, unsafe_allow_html=True)

# 输出震动的红色文字
for i in range(1, 1001):  # 1000 行，已经非常震撼
    st.markdown(f"<div class='shaky-text'>{i}. 你看看你后面吧</div>", unsafe_allow_html=True)
