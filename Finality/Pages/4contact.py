import streamlit as st

# Set up the page layout
page_layout = """
<style>
body {
    background-color: #F2F2F2;
}
</style>
"""
st.markdown(page_layout, unsafe_allow_html=True)

st.title("Contact Us")

st.subheader("Email Support")
contact_email = "<benmwangi968@gmail.com>"
st.write(f"[Click here to send an email](mailto:{contact_email})")

st.subheader("Follow Us On Social Media")
st.markdown("[![Instagram Follow](https://img.shields.io/badge/Instagram-%23E4405F.svg?logo=Instagram&logoColor=white)](https://www.instagram.com/s.gerrera/)", unsafe_allow_html=True)
st.markdown("[![Twitter Follow](https://img.shields.io/twitter/follow/ShadowSageCode?style=social)](https://twitter.com/ShadowSageCode)", unsafe_allow_html=True)
st.markdown("[![GitHub followers](https://img.shields.io/github/followers/Kabuddy768?label=follow&style=social)](https://github.com/Kabuddy768)", unsafe_allow_html=True)
st.markdown("[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ben-mwangi-a3b75b278/)", unsafe_allow_html=True)

st.subheader("Find More Information")
st.markdown("[Visit our Website](https://streamlit.io/)")