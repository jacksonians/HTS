import streamlit as st
import info

st.set_page_config(
    page_title = "Multipage App",
    page_icon = "👑",
    #layout = "wide"
)
st.sidebar.success("Select a page above.")

def HomePage():
    st.title("Conquest and War Throughout: Medieval Europe")
    st.image(info.homepageImg)
    name = st.text_input("May I have your name?")
    st.subheader(f'Greetings {name}')
    st.write(info.homepageTxt1)
    st.write(info.homepageTxt2)
    st.write(info.introQuestion)
    st.subheader(info.researchQuestion)
    st.write(info.homepageTxt3)
    st.write("---")

HomePage()


