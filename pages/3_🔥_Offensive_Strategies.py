import streamlit as st
import info

st.title("🔥 Offensive Strategies 🔥")


def OffensiveStrategies():
    st.write(info.p3Intro)
    st.write("---")

OffensiveStrategies()

def MachinesData(p3MachineData):
    st.header("Siege Machines")
    st.image(info.p3Img1)
    for bullet in p3MachineData:
        st.write(bullet)
    st.write("---")

MachinesData(info.p3MachineData)
    
def SiegeData(p3SiegeData):
    st.header("Sieging")
    st.image(info.p3Img2)
    for bullet in p3SiegeData:
        st.write(bullet)
    st.write("---")

SiegeData(info.p3SiegeData)

def SapperData(p3SapperData):
    st.header("Undermining")
    st.image(info.p3Img3)
    for bullet in p3SapperData:
        st.write(bullet)
    st.write("---")

SapperData(info.p3SapperData)
