import streamlit as st
import json


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Login | Job Portal",
    page_icon="🔐",
    layout="centered"
)


# ---------------- LOGIN FORM ----------------

st.title("🔐 Login")

with st.form("LoginForm"):

    e = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    p = st.text_input(
        "🔑 Password",
        placeholder="Enter your password",
        type="password"
    )

    r = st.selectbox(
        "💼 Choose Role",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button(
        "🔐 Login",
        use_container_width=True
    )


# ---------------- LOGIN LOGIC ----------------

if btn:

    # Check empty fields
    if not e or not p:
        st.error("⚠️ Please enter your email and password.")

    else:

        # Read users.json
        with open("users.json", "r") as r_file:
            all_users = json.load(r_file)

        user_found = False

        # Check credentials
        for user in all_users:

            if (
                user.get("email") == e
                and user.get("password") == p
                and user.get("role") == r
            ):

                user_found = True

                # Store logged-in user
                st.session_state["loggedin_user"] = {
                    "name": user.get("name"),
                    "email": user.get("email"),
                    "role": user.get("role")
                }

                # Recruiter
                if r == "Recruiter":

                    st.success(
                        "✅ Logged in as Recruiter successfully!"
                    )

                    st.switch_page(
                        "pages/RecruiterDashboard.py"
                    )

                # JobSeeker
                elif r == "JobSeeker":

                    st.success(
                        "✅ Logged in as JobSeeker successfully!"
                    )

                    st.switch_page(
                        "pages/JobSeekerDashboard.py"
                    )

                break


        # Invalid credentials
        if not user_found:

            st.error(
                "❌ Invalid email, password, or role."
            )


# ---------------- REGISTER ----------------

st.write("")

st.write("Don't have an account?")

if st.button(
    "📝 Create an Account",
    use_container_width=True
):
    st.switch_page("pages/register.py")