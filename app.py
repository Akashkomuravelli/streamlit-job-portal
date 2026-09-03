import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Job Portal",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding: 10px 0 25px 0;">
            <div style="font-size: 45px;">💼</div>
            <h2 style="margin: 0;">Job Portal</h2>
            <p style="color: #6b7280; font-size: 14px;">
                Find Opportunities • Build Your Future
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown(
        """
        <div style="padding: 5px 10px;">
            <p style="font-size: 13px; color: #6b7280; margin-bottom: 5px;">
                NAVIGATION
            </p>
            <p style="font-size: 14px;">
                🏠 <b>Home</b>
            </p>
            <p style="font-size: 14px;">
                🔐 Login
            </p>
            <p style="font-size: 14px;">
                📝 Register
            </p>
            <p style="font-size: 14px;">
                💼 Recruiter Dashboard
            </p>
            <p style="font-size: 14px;">
                👨‍💻 JobSeeker Dashboard
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    st.info(
        "🚀 Start your career journey today!"
    )


# ---------------- HOME PAGE ----------------

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 45px 20px 20px 20px;
    ">
        <div style="font-size: 55px;">👋</div>

        <h1 style="
            font-size: 48px;
            margin-bottom: 10px;
            color: #1f2937;
        ">
            Welcome to <span style="color:#2563eb;">Job Portal</span>
        </h1>

        <p style="
            font-size: 20px;
            color: #6b7280;
            max-width: 700px;
            margin: auto;
        ">
            Your one-stop platform to discover exciting job opportunities,
            connect with recruiters, and build a successful career.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- ACTION CARDS ----------------

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            padding: 28px;
            border-radius: 18px;
            border: 1px solid #dbeafe;
            background: #f8fbff;
            min-height: 190px;
        ">
            <div style="font-size: 40px;">🔐</div>
            <h2 style="margin: 5px 0;">Login</h2>
            <p style="color:#6b7280;">
                Already have an account?
                Login and continue your career journey.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("🔐 Login Now", use_container_width=True):
        st.switch_page("pages/login.py")


with col2:
    st.markdown(
        """
        <div style="
            padding: 28px;
            border-radius: 18px;
            border: 1px solid #d1fae5;
            background: #f7fffb;
            min-height: 190px;
        ">
            <div style="font-size: 40px;">📝</div>
            <h2 style="margin: 5px 0;">Register</h2>
            <p style="color:#6b7280;">
                New to Job Portal?
                Create an account and get started today.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("📝 Register Now", use_container_width=True):
        st.switch_page("pages/RSegister.py")


# ---------------- FEATURES ----------------

st.write("")
st.write("")
st.markdown(
    """
    <h2 style="text-align:center;">
        ✨ Everything You Need
    </h2>
    """,
    unsafe_allow_html=True
)

st.write("")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        """
        <div style="text-align:center; padding:15px;">
            <div style="font-size:35px;">💼</div>
            <h4>Find Jobs</h4>
            <p style="color:#6b7280;">
                Discover opportunities that match your skills.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        """
        <div style="text-align:center; padding:15px;">
            <div style="font-size:35px;">🏢</div>
            <h4>For Recruiters</h4>
            <p style="color:#6b7280;">
                Find talented candidates for your company.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        """
        <div style="text-align:center; padding:15px;">
            <div style="font-size:35px;">📈</div>
            <h4>Grow Your Career</h4>
            <p style="color:#6b7280;">
                Take the next step toward your career goals.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        """
        <div style="text-align:center; padding:15px;">
            <div style="font-size:35px;">🤝</div>
            <h4>Connect</h4>
            <p style="color:#6b7280;">
                Connect job seekers with the right recruiters.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- FOOTER ----------------

st.divider()

st.markdown(
    """
    <div style="
        text-align:center;
        color:#6b7280;
        padding:15px;
    ">
        <p>🚀 Build your future with Job Portal</p>
        <p style="font-size:13px;">
            © 2026 Job Portal • Made with ❤️ using Streamlit
        </p>
    </div>
    """,
    unsafe_allow_html=True
)