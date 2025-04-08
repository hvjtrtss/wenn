import streamlit as st
import time

# 设置页面样式：黑色背景，无标题栏
st.set_page_config(page_title="你看看你后面", layout="centered")

# 自定义CSS：黑色背景 + 抖动红字
custom_css = """
<style>
body {
    background-color: black;
    color: red;
}

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
    font-size: 30px;
    font-weight: bold;
    animation: shake 0.5s infinite;
    text-align: center;
    margin-top: 200px;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# 四句话循环
messages = [
    "你看看你后面呢",
    "你再看看你后面呢",
    "看看你后面",
    "好好的看看你后面吧！"
]

# 循环展示（你可以调整 range 的值，比如 100 表示重复很多次）
placeholder = st.empty()

for i in range(1000):
    msg = messages[i % len(messages)]
    placeholder.markdown(f"<div class='shaky-text'>{msg}</div>", unsafe_allow_html=True)
    time.sleep(0.5)
