import streamlit as st
import pickle
import pandas as pd
from PIL import Image

def recommend(product):

    # Get the index of the input title in the programme_list
    programme_list = products['TITLE'].to_list()
    index = programme_list.index(product)

    # Create a list of tuples containing the similarity score and index
    # between the input title and all other programmes in the dataset
    sim_scores = list(enumerate(cosine_sim[index]))

    # Sort the list of tuples by similarity score in descending order
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:11]

    # Get the recommended products titles and their similarity scores
    recommend_index = [i[0] for i in sim_scores]
    rec_products = products['TITLE'].iloc[recommend_index].tolist()
    # rec_SKU = products.loc[products['TITLE'].isin(rec_products), 'SKU'].tolist()
    # rec_score = [round(i[1], 4) for i in sim_scores]

    # Create a pandas DataFrame to display the recommendations
    rec_table = pd.DataFrame((list(rec_products)), columns=['Recommendation'])
    # st.write(rec_table)
    # # image =
    # # image = products[products['TITLE'] == recommendations.iloc[i]]['IMAGE1']
    # st.image(
    #     products.loc[products['TITLE'].isin(rec_table.iloc[0]), 'IMAGE1'].tolist(),
    #     width=400, # Manually Adjust the width of the image as per requirement
    # )

    return rec_table


product_dict = pickle.load(open('product_dict.pkl','rb'))
products = pd.DataFrame(product_dict)

cosine_sim = pickle.load(open('cosine_similarity.pkl', 'rb'))

st.title('Etsy Recommender System')

selected_product_name = st.selectbox(
    'Please choose any product',
    products['TITLE'].values)


if st.button('Recommend'):
    recommendations = recommend(selected_product_name)
    for i in range(len(recommendations)):
        st.write(recommendations.iloc[i])
        # image =
        # image = products[products['TITLE'] == recommendations.iloc[i]]['IMAGE1']
        st.image(
            products.loc[products['TITLE'].isin(recommendations.iloc[i]), 'IMAGE1'].tolist(),
            width=400, # Manually Adjust the width of the image as per requirement
        )
# col1, col2, col3 = st.columns(3)
#     with col1:
#         st.write(recommendations.iloc[1])
#         st.image(products.loc[products['TITLE'].isin(recommendations.iloc[1]), 'IMAGE1'].tolist(),
#             width=300,)
#
#         st.write(recommendations.iloc[4])
#         st.image(products.loc[products['TITLE'].isin(recommendations.iloc[3]), 'IMAGE1'].tolist(),
#             width=300,)
#
#     with col2:
#         st.write(recommendations.iloc[2])
#         st.image(products.loc[products['TITLE'].isin(recommendations.iloc[2]), 'IMAGE1'].tolist(),
#             width=300,)
#
#     with col3:
#         st.write(recommendations.iloc[3])
#         st.image(products.loc[products['TITLE'].isin(recommendations.iloc[3]), 'IMAGE1'].tolist(),
#             width=300,)


