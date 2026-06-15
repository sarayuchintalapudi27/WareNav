import streamlit as st

st.title("🤖 WareNav Assistant")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt=st.chat_input("Ask me anything about WareNav")

if prompt:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    text=prompt.lower()

    if "inventory" in text:
        answer="Inventory can be viewed in the Inventory page."

    elif "route" in text:
        answer="Route Optimizer calculates shortest picking routes."

    elif "locator" in text:
        answer="Use Product Locator to find product bins."

    elif "qr" in text:
        answer="QR verification confirms correct bin selection."

    else:
        answer="I can help with inventory, routes, products and warehouse operations."

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)