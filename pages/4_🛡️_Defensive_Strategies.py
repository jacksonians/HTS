import streamlit as st
import info

st.title("🛡️ Defensive Strategies 🛡️")

def DefensiveStrategy():
    st.write(info.p4Intro)
    st.write("---")

DefensiveStrategy()

def PositionData(p4PositionData):
    st.header("Strategic Positioning")
    st.image(info.p4Img1)
    for bullet in p4PositionData:
        st.write(bullet)
    st.write("---")

PositionData(info.p4PositionData)

def WallsData(p4WallsData):
    st.header("Fortifications")
    st.image(info.p4Img2)
    for bullet in p4WallsData:
        st.write(bullet)
    st.write("---")

WallsData(info.p4WallsData)

def DefendData(p4DefendData):
    st.header("Ample Supplies and Logistics")
    st.image(info.p4Img3)
    for bullet in p4DefendData:
        st.write(bullet)
    st.write("---")

DefendData(info.p4DefendData)
