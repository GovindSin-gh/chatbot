import streamlit as st
from model import reply
from datetime import datetime

st.set_page_config(page_title="ChatBot 🤖", layout="centered")

# ---------- Session Init ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "clear_flag" not in st.session_state:
    st.session_state.clear_flag = False

# ---------- SAFE CLEAR (BEFORE widgets) ----------
if st.session_state.clear_flag:
    st.session_state.inst = ""
    st.session_state.inp = ""
    st.session_state.clear_flag = False

# ---------- CSS ----------
st.markdown("""
<style>
.main { background-color: #ECE5DD; }

.chat-container {
    max-width: 700px;
    margin: auto;
    padding-bottom: 80px;
}

.user-bubble {
    background-color: #DCF8C6;
    color: black;
    padding: 10px;
    border-radius: 12px;
    margin: 5px 0;
    margin-left: 20%;
}

.bot-bubble {
    background-color: #FFFFFF;
    color: black;
    padding: 10px;
    border-radius: 12px;
    margin: 5px 0;
    margin-right: 20%;
}

.timestamp {
    font-size: 10px;
    color: gray;
    text-align: right;
}

.input-container {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #F0F0F0;
    padding: 10px;
    border-top: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)

st.title("💬 ChatBot")

# ---------- Chat ----------
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
        <div class="user-bubble">
            {msg["content"]}
            <div class="timestamp">{msg["time"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="bot-bubble">
            {msg["content"]}
            <div class="timestamp">{msg["time"]}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Bottom Input ----------
st.markdown('<div class="input-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([3, 3, 1])

with col1:
    instruction = st.text_input("", key="inst", placeholder="Instruction...")

with col2:
    user_input = st.text_input("", key="inp", placeholder="Optional input...")

with col3:
    send = st.button("⬆️")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Send ----------
if send:
    if instruction.strip():

        now = datetime.now().strftime("%H:%M")

        data = {
            "instruction": instruction,
            "input": user_input if user_input else "",
            "output": ""
        }

        user_text = f"<b>{instruction}</b>"
        if user_input.strip():
            user_text += f"<br>{user_input}"

        st.session_state.messages.append({
            "role": "user",
            "content": user_text,
            "time": now
        })

        with st.spinner("Typing..."):
            response = reply(data)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response,
            "time": now
        })

        # ✅ trigger safe clear next run
        st.session_state.clear_flag = True

        st.rerun()

    else:
        st.warning("Instruction is required!")