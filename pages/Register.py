import streamlit as st
import json

st.title("Register Form")

with st.form("RegisterForm"):

    n = st.text_input(
        "Name",
        placeholder="Enter Name here"
    )

    e = st.text_input(
        "Email",
        placeholder="Enter Email here"
    )

    p = st.text_input(
        "Password",
        placeholder="Enter Password here",
        type="password"
    )

    c_p = st.text_input(
        "Confirm Password",
        placeholder="Re-Enter Password here",
        type="password"
    )

    r = st.selectbox(
        "Choose Role",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button("Register")


if btn:

    if p != c_p:
        st.error("Passwords do not match.")

    elif not n or not e or not p:
        st.error("Please fill all required fields.")

    else:

        with open("users.json", "r") as r_file:
            all_users = json.load(r_file)

        # Check whether email already exists
        email_exists = False

        for user in all_users:
            if user["email"] == e:
                email_exists = True
                break

        if email_exists:
            st.error("Email already registered.")

        else:
            new_user = {
                "name": n,
                "email": e,
                "password": p,
                "role": r
            }

            all_users.append(new_user)

            with open("users.json", "w") as w_file:
                json.dump(all_users, w_file, indent=4)

            st.success("Successfully registered!")

            st.switch_page("pages/login.py")