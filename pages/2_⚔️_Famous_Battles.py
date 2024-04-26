import streamlit as st
import info

st.title("⚔️ Famous Battles ⚔️")
st.write(info.p2Intro)
st.write("---")

st.header("Siege of Antioch (1098)")
st.image(info.p2Img2)

def SiegeAnt(SAnt1, SAnt2, SAnt3, SAnt4):
    st.subheader("Crucial Information: ")
    SAntExp1 = st.expander("Context and Objectives: ")
    for bullet in SAnt1:
        SAntExp1.write(bullet)
    SAntExp2 = st.expander("Journey to Antioch: ")
    for bullet in SAnt2:
        SAntExp2.write(bullet)
    SAntExp3 = st.expander("Assault on the City: ")
    for bullet in SAnt3:
        SAntExp3.write(bullet)
    SAntExp4 = st.expander("Legacy and Impact: ")
    for bullet in SAnt4:
        SAntExp4.write(bullet)

SiegeAnt(info.p2SAnt1, info.p2SAnt2, info.p2SAnt3, info.p2SAnt4)
st.write("---")

st.header("Siege of Jerusalem (1099)")
st.image(info.p2Img1)

def SiegeJeru(SJeru1, SJeru2, SJeru3, SJeru4): 
    st.subheader("Crucial Information: ")
    SJeruExp1 = st.expander("Context and Motivation: ")
    for bullet in SJeru1:
        SJeruExp1.write(bullet)
    SJeruExp2 = st.expander("Journey to Jerusalem: ")
    for bullet in SJeru2:
        SJeruExp2.write(bullet)
    SJeruExp3 = st.expander("Assault on the City: ")
    for bullet in SJeru3:
        SJeruExp3.write(bullet) 
    SJeruExp4 = st.expander("Legacy and Impact: ")
    for bullet in SJeru4:
        SJeruExp4.write(bullet)

SiegeJeru(info.p2SJeru1, info.p2SJeru2, info.p2SJeru3, info.p2SJeru4)

st.write("---")

st.header("Siege of Lisbon (1147)")
st.image(info.p2Img3)

def SiegeLis(SLis1, SLis2, SLis3, SLis4): 
    st.subheader("Crucial Information: ")
    SLisExp1 = st.expander("Context and Motivation: ")
    for bullet in SLis1:
        SLisExp1.write(bullet)
    SLisExp2 = st.expander("Journey to Lisbon: ")
    for bullet in SLis2:
        SLisExp2.write(bullet)
    SLisExp3 = st.expander("Assault on the City: ")
    for bullet in SLis3:
        SLisExp3.write(bullet)
    SLisExp4 = st.expander("Legacy and Impact: ")
    for bullet in SLis4:
        SLisExp4.write(bullet)

SiegeLis(info.p2SLis1, info.p2SLis2, info.p2SLis3, info.p2SLis4)

st.write("---")

st.header("Siege of Acre (1189-1191)")
st.image(info.p2Img4)

def SiegeAcr(SAcr1, SAcr2, SAcr3, SAcr4):
    st.subheader("Crucial Information: ")
    SAcrExp1 = st.expander("Context and Motivation: ")
    for bullet in SAcr1:
        SAcrExp1.write(bullet)
    SAcrExp2 = st.expander("Arriving at Acre: ")
    for bullet in SAcr2:
        SAcrExp2.write(bullet)
    SAcrExp3 = st.expander("Assault and Fall of Acre: ")
    for bullet in SAcr3:
        SAcrExp3.write(bullet)
    SAcrExp4 = st.expander("Legacy and Impact: ")
    for bullet in SAcr4:
        SAcrExp4.write(bullet)

SiegeAcr(info.p2SAcr1, info.p2SAcr2, info.p2SAcr3, info.p2SAcr4)

st.write("---")

st.header("Siege of  Damietta (1218-1219)")
st.image(info.p2Img5)

def SiegeDam(SDam1, SDam2, SDam3, SDam4):
    st.subheader("Crucial Information: ")
    SDamExp1 = st.expander("Context and Objectives: ")
    for bullet in SDam1:
        SDamExp1.write(bullet)
    SDamExp2 = st.expander("Arrival and Encirclement of Damietta: ")
    for bullet in SDam2:
        SDamExp2.write(bullet)
    SDamExp3 = st.expander("Assault on Damietta: ")
    for bullet in SDam3:
        SDamExp3.write(bullet)
    SDamExp4 = st.expander("Aftermath and Legacy: ")
    for bullet in SDam4:
        SDamExp4.write(bullet)

SiegeDam(info.p2SDam1, info.p2SDam2, info.p2SDam3, info.p2SDam4)

st.write("---")

