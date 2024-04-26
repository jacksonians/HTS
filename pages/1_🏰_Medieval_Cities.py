import streamlit as st
import info

st.title("🏰 Medieval Cities 🏰")
st.write(info.p1Intro)
st.write("---")

st.header("Constantinople")
st.image(info.p1Img1)

def Constantinople(Const1, Const2, Const3):
    st.subheader("Notable Features:")
    Cexpander1 = st.expander("Political and Culutral Center: ")
    for bullet in Const1:
        Cexpander1.write(bullet)
    Cexpander2 = st.expander("Strategic Location: ")
    for bullet in Const2:
        Cexpander2.write(bullet)
    Cexpander3 = st.expander("Fortified Defenses: ")
    for bullet in Const3:
        Cexpander3.write(bullet)

Constantinople(info.p1Const1, info.p1Const2, info.p1Const3)

st.write("---")

st.header("Venice, Italy")
st.image(info.p1Img2)

def Venice(Ven1, Ven2, Ven3):
    st.subheader("Notable Features:")
    Vexpander1 = st.expander("Trading Empire: ")
    for bullet in Ven1:
        Vexpander1.write(bullet)
    Vexpander2 = st.expander("Maritime Power: ")
    for bullet in Ven2:
        Vexpander2.write(bullet)
    Vexpander3 = st.expander("Canal City: ")
    for bullet in Ven3:
        Vexpander3.write(bullet)

Venice(info.p1Ven1, info.p1Ven2, info.p1Ven3)

st.write("---")

st.header("Acre")
st.image(info.p1Img3)

def Acre(Acre1, Acre2, Acre3):
    st.subheader("Notable Features:")
    Aexpander1 = st.expander("Military Fortifications: ")
    for bullet in Acre1:
        Aexpander1.write(bullet)
    Aexpander2 = st.expander("Strategic Location: ")
    for bullet in Acre2:
        Aexpander2.write(bullet)
    Aexpander3 = st.expander("Crusader Stronghold: ")
    for bullet in Acre3:
        Aexpander3.write(bullet)

Acre(info.p1Acre1, info.p1Acre2, info.p1Acre3)

st.write("---")

st.header("Jerusalem")
st.image(info.p1Img4)

def Jeru(Jeru1, Jeru2, Jeru3):
    st.subheader("Notable Features:")
    Jexpander1 = st.expander("Religious Significance: ")
    for bullet in Jeru1:
        Jexpander1.write(bullet)
    Jexpander2 = st.expander("Strategic Importance: ")
    for bullet in Jeru2:
        Jexpander2.write(bullet)
    Jexpander3 = st.expander("Crusader Kingdom: ")
    for bullet in Jeru3:
        Jexpander3.write(bullet)

Jeru(info.p1Jeru1, info.p1Jeru2, info.p1Jeru3)

st.write("---")