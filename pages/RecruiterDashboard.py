import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Recruiter Dashboard",
    page_icon="💼",
    layout="wide"
)

# ---------------- LOGIN CHECK ----------------
if "loggedin_user" not in st.session_state:
    st.warning("⚠️ You must log in to access the Recruiter Dashboard.")
    st.switch_page("pages/login.py")
    st.stop()


# ---------------- ROLE CHECK ----------------
if st.session_state["loggedin_user"]["role"] != "Recruiter":
    st.error("🚫 Access Denied")
    st.warning("Only Recruiters are allowed to access this page.")
    st.stop()


# ---------------- USER DETAILS ----------------
user = st.session_state["loggedin_user"]

name = user.get("name", "Recruiter")
email = user.get("email", "")


# ---------------- HEADER ----------------
st.title("💼 Recruiter Dashboard")

st.markdown(
    f"""
    ### 👋 Welcome, {name}!

    **📧 Email:** {email}

    Manage your job postings and find the right candidates. 🚀
    """
)

st.divider()


# ---------------- DASHBOARD CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💼 Jobs Posted",
        "0"
    )

with col2:
    st.metric(
        "👥 Applications",
        "0"
    )

with col3:
    st.metric(
        "⭐ Shortlisted",
        "0"
    )


st.divider()


# ---------------- QUICK ACTIONS ----------------
st.subheader("⚡ Quick Actions")

col1, col2 = st.columns(2)

with col1:
    if st.button(
        "➕ Post a New Job",
        use_container_width=True
    ):
        st.info("🚧 Job posting feature coming soon!")

with col2:
    if st.button(
        "👥 View Applications",
        use_container_width=True
    ):
        st.info("🚧 Applications feature coming soon!")


st.divider()


# ---------------- INFORMATION ----------------
st.subheader("📊 Recruiter Overview")

st.info(
    "💡 Your recruiter dashboard will allow you to "
    "post jobs, manage applications, and shortlist candidates."
)


# ---------------- LOGOUT ----------------
st.divider()

if st.button("🚪 Logout", use_container_width=True):

    del st.session_state["loggedin_user"]

    st.success("✅ Logged out successfully!")

    st.switch_page("pages/login.py")