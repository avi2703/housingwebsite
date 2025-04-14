import streamlit as st

# Dummy credentials (you can replace with a database check)
USER_CREDENTIALS = {
    "admin": "DreamHome",
    "agent": "realestate",
    "buyer": "dreamhome"
}

def login():
    # If already logged in, don't show login page
    if st.session_state.get("logged_in"):
        st.success(f"Welcome back, {st.session_state['username']}! 👋")
        return True

    st.title("🔐 Login to DreamHomes")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")

        if submitted:
            if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password:
                st.session_state["logged_in"] = True
                st.session_state["username"] = username
                st.success(f"Welcome, {username}!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    return False

      # Footer
    st.caption("© 2025 DreamHomes. All rights reserved.")

