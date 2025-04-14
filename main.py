import streamlit as st
from streamlit_option_menu import option_menu
import price
import buy
import log
import home

# 1. as sidebar menu
# with st.sidebar:
#     selected = option_menu("Main Menu", ["Home", "House Price" , "Buy" ,'Account'], 
#         icons=['house','currency-rupee',"bag-fill" ,'person-circle'],
#           menu_icon="cast", default_index=1 )
#     selected

# 2. horizontal menu
selected2 = option_menu(None, ["Home", "House Price", "Buy", 'Account'], 
    icons=['house', 'currency-rupee', "bag-fill", 'person-circle'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

if selected2 == "Home":
    st.title(f"Your Dream House")
    home.acc()

if selected2 == "House Price":
    price.show()

if selected2 == "Account":
    log.login()

if selected2 == "Buy":
   buy.hi()

  # Footer
st.caption("© 2025 DreamHomes. All rights reserved.")
