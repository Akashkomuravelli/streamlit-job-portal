import streamlit as st


st.set_page_config(
    page_title="Job Portal",
    page_icon="💼",
    layout="centered"
)


# ---------------- HOME PAGE ----------------

def home():

    st.title("💼 Job Portal")
    st.write("Welcome to Job Portal 🚀")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔐 Login")
        st.write("Already have an account?")

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):
            st.switch_page("pages/login.py")

    with col2:

        st.subheader("📝 Register")
        st.write("Create a new account")

        if st.button(
            "📝 Register",
            use_container_width=True
        ):
            st.switch_page("pages/Register.py")


# ---------------- PAGES ----------------

home_page = st.Page(
    home,
    title="Home",
    icon="🏠",
    default=True
)

login_page = st.Page(
    "pages/login.py",
    title="Login",
    icon="🔐"
)

register_page = st.Page(
    "pages/Register.py",
    title="Register",
    icon="📝"
)

recruiter_page = st.Page(
    "pages/RecruiterDashboard.py",
    title="Recruiter Dashboard",
    icon="💼"
)

jobseeker_page = st.Page(
    "pages/JobSeekerDashboard.py",
    title="JobSeeker Dashboard",
    icon="👨‍💻"
)


# ---------------- SIDEBAR NAVIGATION ----------------

pg = st.navigation(
    [
        home_page,
        login_page,
        register_page,
        recruiter_page,
        jobseeker_page
    ],
    position="sidebar"
)

pg.run()