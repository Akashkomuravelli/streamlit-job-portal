import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="JobSeeker Dashboard",
    page_icon="👨‍💻",
    layout="wide"
)

# ---------------- LOGIN CHECK ----------------
if "loggedin_user" not in st.session_state:
    st.warning("⚠️ You must log in to access the JobSeeker Dashboard.")
    st.switch_page("pages/login.py")
    st.stop()


# ---------------- ROLE CHECK ----------------
if st.session_state["loggedin_user"]["role"] != "JobSeeker":
    st.error("🚫 Access Denied")
    st.warning("Only JobSeekers are allowed to access this page.")
    st.stop()


# ---------------- USER DETAILS ----------------
user = st.session_state["loggedin_user"]

name = user.get("name", "JobSeeker")
email = user.get("email", "")


# ---------------- HEADER ----------------
st.title("👨‍💻 JobSeeker Dashboard")

st.markdown(
    f"""
    ### 👋 Welcome, {name}!

    **📧 Email:** {email}

    Find your dream job and manage your applications. 🚀
    """
)

st.divider()


# ---------------- DASHBOARD CARDS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "🔎 Jobs Available",
        "0"
    )

with col2:
    st.metric(
        "📄 Applications",
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
        "🔎 Browse Jobs",
        use_container_width=True
    ):
        st.info("🚧 Job browsing feature coming soon!")

with col2:
    if st.button(
        "📄 My Applications",
        use_container_width=True
    ):
        st.info("🚧 Applications feature coming soon!")


st.divider()


# ---------------- INFORMATION ----------------
st.subheader("📊 JobSeeker Overview")

st.info(
    "💡 Your JobSeeker dashboard will allow you to "
    "browse jobs, apply for positions, and track your applications."
)


# ---------------- LOGOUT ----------------
st.divider()

if st.button("🚪 Logout", use_container_width=True):

    del st.session_state["loggedin_user"]

    st.success("✅ Logged out successfully!")

    st.switch_page("pages/login.py")