
from api_client.users import Users
from api_client import baseLocalURL,baseREMOTEURL

import pandas as pd #type:ignore


def loadWindow(st):
    oneUser = st.empty()
    listUser = st.empty()
    users = Users(baseREMOTEURL)
    
    with oneUser.expander("Manage user"):
        #TODO: user interface for adding new user
        st.write("test expand")
        
    with listUser.expander("List of users"):
        data=users.getAllUsers()
        df = pd.json_normalize(data[0])
        st.write(df)
        