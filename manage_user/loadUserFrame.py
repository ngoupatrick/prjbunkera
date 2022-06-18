
from cProfile import label
from api_client.users import Users
from api_client import baseLocalURL, baseREMOTEURL

import pandas as pd  # type:ignore
def loadWindowUser(st):
    oneUser = st.empty()
    listUser = st.empty()
    users = Users(baseREMOTEURL)

    with oneUser.expander("Manage user"):
        # Prepare user interface
        # Fields
        col_data_1, col_data_2, _ = st.columns([2, 2, 1])
        key = col_data_1.text_input(
            label="Key", placeholder="Set key for update", key="key")
        name = col_data_1.text_input(
            label="Name", placeholder="Set the user name", key="name")
        age = col_data_2.number_input(
            label="Age", min_value=0, max_value=150)  # CHECK FORMAT OPTIONS
        hometown = col_data_2.text_input(
            label="Hometown", placeholder="Set the user living town", key="hometown")
        # Buttons
        col_btn_save, col_btn_load, col_btn_delete, col_btn_clean = st.columns(
            4)
        btn_save = col_btn_save.button(label="Save")
        btn_load = col_btn_load.button(label="Load")
        btn_delete = col_btn_delete.button(label="Delete")
        btn_clean = col_btn_clean.button(label="Clean fields")
        # Result messages
        msg = st.empty()
        #Processing and Actions
        # Saving and Updating Data
        if btn_save:
            name = name.strip()
            hometown = hometown.strip()
            key=key.strip()
            if not name:
                msg.error("Please fill name field!")
            else:   
                func=users.saveUser             
                data = {"name": name, "age": age, "hometown": hometown}
                if key:
                    data["key"]=key
                    func=users.updateUser
                result = func(data=data)
                # TODO: add message if all is Ok or NOT
                st.write(result)
        #Load Data from KEY
        if btn_load:
            key=key.strip()
            if not key:
                msg.error("Please fill key field!")
            else:
                data = users.getUser(key=key)
                st.table(data=pd.json_normalize(data[0]))
        #Delete data From KEY
        if btn_delete:
            key = key.strip()
            if not key:
                msg.error("Please fill key field!")
            else:
                result = users.deleteUser(key=key)
                # TODO: add message if all is Ok or NOT
                st.write(result)

    with listUser.expander("List of users", expanded=True):
        # TODO: check "clear memo" and "clear singleton" of STREAMLIT
        data = users.getAllUsers()
        df = pd.json_normalize(data[0])
        st.table(data=df)
        