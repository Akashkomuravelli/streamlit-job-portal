import streamlit as st


st.set_page_config(
    page_title="Job Portal",
    page_icon="💼",
    layout="centered"
)


# ---------------- HOME ----------------

def home():

    st.markdown(
        """
        <div style="text-align:center; padding:60px 0 40px 0;">

            <div style="font-size:60px;">
                💼
            </div>

            <h1 style="font-size:42px;">
                Job Portal
            </h1>

            <p style="font-size:18px; color:gray;">
                Find Opportunities • Build Your Future
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ---------------- LOGIN & REGISTER ----------------

    col1, col2 = st.columns(2)


    with col1:

        st.markdown(
            """
            <div style="
                padding:30px;
                border:1px solid #ddd;
                border-radius:15px;
                text-align:center;
            ">

                <h2>🔐 Login</h2>

                <p>
                    Already have an account?
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🔐 Login",
            use_container_width=True
        ):
            st.switch_page("pages/login.py")


    with col2:

        st.markdown(
            """
            <div style="
                padding:30px;
                border:1px solid #ddd;
                border-radius:15px;
                text-align:center;
            ">

                <h2>📝 Register</h2>

                <p>
                    Create a new account
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "📝 Register",
            use_container_width=True
        ):
            st.switch_page("pages/register.py")


# ---------------- PAGES ----------------

home_page = st.Page(
    home,
    title="Home",
    icon="🏠"
)

login_page = st.Page(
    "pages/login.py",
    title="Login",
    icon="🔐"
)

register_page = st.Page(
    "pages/register.py",
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


# ---------------- NAVIGATION ----------------

pg = st.navigation(
    [
        home_page,
        login_page,
        register_page,
        recruiter_page,
        jobseeker_page
    ],
    position="hidden"
)

pg.run()