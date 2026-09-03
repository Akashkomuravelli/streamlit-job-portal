import streamlit as st
import json

st.set_page_config(
    page_title="Login | Job Portal",
    page_icon="🔐",
    layout="centered"
)

# ---------------- HEADER ----------------

st.markdown(
    """
    <div style="text-align:center; padding:20px 0 10px 0;">
        <div style="font-size:55px;">🔐</div>

        <h1 style="
            margin-bottom:5px;
            color:#1f2937;
        ">
            Welcome Back!
        </h1>

        <p style="
            color:#6b7280;
            font-size:17px;
        ">
            Login to continue your journey with Job Portal 🚀
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- LOGIN FORM ----------------

with st.form("LoginForm"):

    st.markdown(
        """
        <h3 style="margin-bottom:15px;">
            🔑 Account Login
        </h3>
        """,
        unsafe_allow_html=True
    )

    e = st.text_input(
        "📧 Email",
        placeholder="Enter your email"
    )

    p = st.text_input(
        "🔒 Password",
        placeholder="Enter your password",
        type="password"
    )

    r = st.selectbox(
        "👤 Login As",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button(
        "🔐 Login",
        use_container_width=True
    )


# ---------------- LOGIN LOGIC ----------------

if btn:

    if not e or not p:
        st.warning("⚠️ Please enter your email and password.")

    else:

        with open("users.json", "r") as r_file:
            all_users = json.load(r_file)

        user_found = False

        for user in all_users:

            if (
                user.get("email") == e
                and user.get("password") == p
                and user.get("role") == r
            ):

                user_found = True

                st.session_state["loggedin_user"] = {
                    "name": user.get("name"),
                    "email": user.get("email"),
                    "role": user.get("role")
                }

                if r == "Recruiter":

                    st.success(
                        "✅ Logged in as Recruiter successfully!"
                    )

                    st.switch_page(
                        "pages/RecruiterDashboard.py"
                    )

                elif r == "JobSeeker":

                    st.success(
                        "✅ Logged in as JobSeeker successfully!"
                    )

                    st.switch_page(
                        "pages/JobSeekerDashboard.py"
                    )

                break

        if not user_found:
            st.error(
                "❌ Invalid email, password, or selected role."
            )


# ---------------- REGISTER LINK ----------------

st.write("")
st.divider()

st.markdown(
    """
    <div style="text-align:center;">
        <p style="color:#6b7280;">
            Don't have an account?
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

if st.button(
    "📝 Create New Account",
    use_container_width=True
):
    st.switch_page("pages/register.py")