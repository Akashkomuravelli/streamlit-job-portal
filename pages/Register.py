import streamlit as st
import json

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Register | Job Portal",
    page_icon="📝",
    layout="centered"
)

# ---------------- HEADER ----------------
st.markdown(
    """
    <div style="text-align:center;">
        <h1>📝 Create Your Account</h1>
        <p style="font-size:18px; color:gray;">
            Join our Job Portal and get started today 🚀
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- REGISTER FORM ----------------
with st.form("RegisterForm"):

    st.subheader("👤 Personal Information")

    n = st.text_input(
        "👤 Name",
        placeholder="Enter your name"
    )

    e = st.text_input(
        "📧 Email",
        placeholder="Enter your email address"
    )

    st.subheader("🔐 Account Security")

    p = st.text_input(
        "🔑 Password",
        placeholder="Enter your password",
        type="password"
    )

    c_p = st.text_input(
        "🔑 Confirm Password",
        placeholder="Re-enter your password",
        type="password"
    )

    st.subheader("💼 Account Type")

    r = st.selectbox(
        "Choose Role",
        ["Recruiter", "JobSeeker"]
    )

    btn = st.form_submit_button(
        "🚀 Create Account",
        use_container_width=True
    )


# ---------------- REGISTER LOGIC ----------------
if btn:

    # Check empty fields
    if not n or not e or not p or not c_p:
        st.error("⚠️ Please fill in all required fields.")

    # Check password
    elif p != c_p:
        st.error("❌ Passwords do not match.")

    else:

        # Read existing users
        with open("users.json", "r") as r_file:
            all_users = json.load(r_file)

        # Check whether email already exists
        email_exists = False

        for user in all_users:
            if user.get("email") == e:
                email_exists = True
                break

        if email_exists:

            st.error("❌ This email is already registered.")

        else:

            # Create new user
            new_user = {
                "name": n,
                "email": e,
                "password": p,
                "role": r
            }

            # Add user
            all_users.append(new_user)

            # Save users
            with open("users.json", "w") as w_file:
                json.dump(
                    all_users,
                    w_file,
                    indent=4
                )

            st.success(
                "✅ Registration successful! Redirecting to Login..."
            )

            st.switch_page("pages/login.py")