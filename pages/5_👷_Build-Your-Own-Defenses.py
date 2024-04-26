import streamlit as st
import info

st.title("👷 Build-Your-Own-Defenses 👷")

st.write(info.p5Intro1)
st.write(info.p5Intro2)
st.write(info.p5Intro3)

st.write("---")



def Location(LocData): 
    st.subheader("Starting with the Location")
    st.image(info.p5Img1)
    for bullet in LocData:
        st.write(bullet)
    st.write("---")

Location(info.p5LocData)

def Walls(WallData):
    st.subheader("Moving to the Fortifications")
    st.image(info.p5Img2)
    for bullet in WallData:
        st.write(bullet)
    st.write("---")

Walls(info.p5WallData)

def Keep(KeepData):
    st.subheader("Onto the Inner Citadel")
    st.image(info.p5Img3)
    for bullet in KeepData:
        st.write(bullet)
    st.write("---")

Keep(info.p5KeepData)

def Layout(LayData):
    st.subheader("Finally the Infrastructure")
    st.image(info.p5Img4)
    for bullet in LayData:
        st.write(bullet)
    st.write("---")

Layout(info.p5LayData)