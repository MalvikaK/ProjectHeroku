# IMPORT REQUIRED MODULES
import streamlit as st
import numpy as np
import pandas as pd
import sys
from PIL import Image
import time


# LHS METHOD SELECTION CODE
add_selectbox = st.sidebar.radio(
    "Welcome!! What do you want to do today",
    ("HOME", "Search Products")
)

st.markdown('<style>body{background-color: #b8c5f2;}</style>', unsafe_allow_html=True)

# IF COSINE SIMILARITY METHOD IS SELECTED, RETURNS COSINE SIMILARITY SEARCH OUTPUT FILE FOR RENDERING
if add_selectbox == 'HOME':
    def get_dataset(UserID):
        serverURL = "http://127.0.0.1:8000/docs#/default/read_item_search_recommendation_get" + userID
        req = requests.get(serverURL)
        return req.json()


    image = Image.open('Clothing-Fashion.jpg')
    st.image(image, use_column_width=True)
    st.markdown("<h1 style='text-align: left; color: black;'>Welcome to Senorita Store</h1>", unsafe_allow_html=True)
    title = st.number_input('Enter User ID to Login', min_value=0, max_value=10000000000, value=0)

    if st.checkbox('Login'):
        if (title in (
        245642504, 243480100, 278313783, 151065371, 251879409, 230970866, 287758725, 231166811, 237868680, 282432370)):

            data = pd.read_csv("version1.csv", sep=";")
            df1 = data['UserId']==title
            df2 = data[df1]
            if df2.empty:
                st.write("UserNotFound")
                image = Image.open('UserNotFound.jpg')
                st.image(image, use_column_width=True)
            else:
                st.write(data[df1])
                # st.image(data[df1['3'][2], use_column_width=None)

            data2 = pd.read_csv("PopularItems.csv")
            df3 = data2['UserID']==title
            df4 = data2[df3]
            st.markdown("<h2 style='text-align: left; color: black;'>Hot in your Area!!!</h2>", unsafe_allow_html=True)
            if df3.empty:
                st.image('No User Found')
                st.markdown("<h1 style='text-align: left; color: blue;'>empty</h1>", unsafe_allow_html=True)
            else:
                st.write(data2[df3])
                # st.image(data[df1['3'][2], use_column_width=None)


            ab = 0
            bc = 0
            action = st.selectbox("Action", ["","Add to Cart", "Buy"])
            if action == "Buy":
                ab = ab + 1
                st.success('Thank you for Shopping')
                st.balloons()
            elif action == "Add to Cart":
                bc = bc + 1
                with open('svdCart.txt', 'w') as g:
                    g.write('%d' % bc)
                    g.close()
            with open('svdBuy.txt', 'w') as f:
                f.write('%d' % ab)
                f.close()

        elif (title not in (
        300016375, 304434900, 308660401, 310843802, 312739061, 317117656, 317570835, 318517350, 319151414, 320997455245642504, 243480100, 278313783, 151065371, 251879409, 230970866, 287758725, 231166811, 237868680, 282432370)):
            st.write('No User Found')
            image = Image.open('UserNotFound.jpeg')
            st.image(image, use_column_width=True)

        elif (title in (
        300016375, 304434900, 308660401, 310843802, 312739061, 317117656, 317570835, 318517350, 319151414, 320997455)):
            # b=0
            data1 = pd.read_csv("version2proj.csv", sep=";")
            df1 = data1['UserID'] == title
            df2 = data1[df1]
            if df2.empty:
                st.write('No User Found')
            else:
                st.write(data1[df1])


            ab = 0
            bc = 0
            action = st.selectbox("Action for these Products", ["","Add to Cart", "Buy"])
            if action == "Buy":
                ab = ab + 1
                st.success('Thank you for Shopping')
                st.balloons()
            elif action == "Add to Cart":
                bc = bc + 1
                with open('ncfCart.txt', 'w') as g:
                    g.write('%d' % bc)
                    g.close()
            with open('ncfBuy.txt', 'w') as f:
                f.write('%d' % ab)
                f.close()


    #def get_data():
        #return pd.read_csv("svdimages.csv", sep=";", header=None)
    # IF FAISS METHOD IS SELECTED, RETURNS FAISS SIMILARITY SEARCH OUTPUT FILE FOR RENDERING
elif add_selectbox == 'Search Products':

    st.title("Search for Products :mag: ")
    st.write("-------------------------------------------------------------------------------------------------")


    def get_data():
        return pd.read_csv('df.csv')


    n = 1
    df = get_data()
    #images = df['0'].unique()
    st.subheader("Search Items :point_down:")
    pic = st.text_input("Search", value='6_0_031.png')
    st.write("**You selected:**")
    st.image(pic, width=None)

    # DISPLAYING OUTPUT
    z = 5
    #st.write("-------------------------------------------------------------------------------------------------")
    st.subheader("Products you my Like:")
    st.write('**Products similar to the items searched by you**')
    for index, row in df.iterrows():
        if row['0'] == pic:
            while n < z + 1:
                st.image(row[n], use_column_width=None, caption=row[n])
                n += 1