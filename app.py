import streamlit as st

# Neumorphism + Futuristic CSS
neumorphism_css = """
<style>
body {
    background: #e3edf7;
    font-family: 'Poppins', sans-serif;
    color: #333;
}

/* Neumorphic Containers */
.container {
    background: #e3edf7;
    border-radius: 15px;
    box-shadow: 8px 8px 16px #b8c6db, -8px -8px 16px #ffffff;
    padding: 20px;
    margin: 20px 0;
    text-align: left;
}

/* Futuristic Glowing Buttons */
.futuristic-button {
    background: linear-gradient(90deg, #00eaff, #ff00ff);
    border: none;
    padding: 12px 20px;
    font-size: 16px;
    font-weight: bold;
    text-transform: uppercase;
    border-radius: 10px;
    color: white;
    box-shadow: 0px 0px 15px rgba(0, 234, 255, 0.8);
    transition: all 0.3s ease-in-out;
    cursor: pointer;
    text-align: center;
    display: inline-block;
    text-decoration: none;
}

.futuristic-button:hover {
    transform: scale(1.1);
    box-shadow: 0px 0px 25px rgba(255, 0, 255, 1);
}

/* Neumorphic Cards */
.card {
    background: #e3edf7;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 6px 6px 12px #b8c6db, -6px -6px 12px #ffffff;
    transition: 0.3s;
    margin-bottom: 15px;
}

.card:hover {
    box-shadow: inset 4px 4px 8px #b8c6db, inset -4px -4px 8px #ffffff;
}

/* Copyright Footer */
.footer {
    text-align: center;
    padding: 20px;
    margin-top: 30px;
    font-size: 14px;
    color: #555;
}
</style>
"""
st.markdown(neumorphism_css, unsafe_allow_html=True)

# Home Section
st.markdown("<div class='container'><h1>Mohd Huzaif</h1>", unsafe_allow_html=True)
st.markdown("<h2>Data Scientist | Generative AI Enthusiast</h2></div>", unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 2])
with col1:
    st.markdown("""
    📍 **Location:** Sultanpur, Lucknow (UP)  
    ✉️ **Email:** [khanhuzaif348@gmail.com](mailto:khanhuzaif348@gmail.com)  
    📞 **Phone:** +91-9044039661  
    """)

    # ✅ FIXED Resume Download Button
    with open("Resume(Mohd Huzaif).pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    st.download_button(label="📜 Download Resume", data=pdf_data, file_name="Mohd_Huzaif_Resume.pdf", mime="application/pdf")

with col2:
    st.image("image.png", caption="", use_container_width=True)

# Top Skills Section
st.markdown("<div class='container'><h2>🚀 Top Skills</h2></div>", unsafe_allow_html=True)
st.markdown("""
- **HTML**  
- **Supervised Learning**  
- **Unsupervised Learning**  
""")

# Languages Section
st.markdown("<div class='container'><h2>🌍 Languages</h2></div>", unsafe_allow_html=True)
st.markdown("""
- **Hindi:** Native or Bilingual  
- **English:** Elementary  
""")

# Certifications Section
st.markdown("<div class='container'><h2>🏆 Certifications</h2></div>", unsafe_allow_html=True)
st.markdown("""
- **Windows Operating System Fundamentals**  
- **English Spoken Course**  
- **Microsoft PowerBI for Business Analytics and Intelligence**  
- **Generative AI**  
- **Streamlining Your Work with Microsoft Copilot**  
""")

# Projects Section
st.markdown("<div class='container'><h2>🚀 Projects</h2></div>", unsafe_allow_html=True)

projects = [
    {
        "name": "Customer Segmentation",
        "desc": "An AI-powered tool to segment customers based on their purchasing behavior.",
        "tech": "Machine Learning, K-Means, Python, Seaborn",
        "impact": "Enabled targeted marketing strategies, increasing engagement by 20%.",
        "github": "https://github.com/khanhuzaif348/customer-segmentation",
        "app_url": "https://customersegmentor.streamlit.app/"
    },
    {
        "name": "House Price Prediction",
        "desc": "Built a regression model to predict house prices based on multiple real estate parameters.",
        "tech": "Python, Machine Learning, Pandas, NumPy, Scikit-learn",
        "impact": "Achieved 90% accuracy in price prediction.",
        "github": "https://github.com/khanhuzaif348/house-price-prediction",
        "app_url": None
    },
    {
        "name": "Sales Dashboard",
        "desc": "Designed an interactive Power BI dashboard to analyze company sales trends and KPIs.",
        "tech": "Power BI, SQL, Data Visualization",
        "impact": "Helped business executives identify a 15% increase in profit trends.",
        "github": "https://github.com/khanhuzaif348/sales-dashboard",
        "app_url": None
    }
]

for project in projects:
    st.markdown(f"""
    <div class='card'>
        <h3>{project['name']}</h3>
        <p>{project['desc']}</p>
        <b>Tech Used:</b> {project['tech']}<br>
        <b>Impact:</b> {project['impact']}<br>
        <a href="{project['github']}" target="_blank" class="futuristic-button">🔗 View on GitHub</a>
    """, unsafe_allow_html=True)
    
    # ✅ Added "View App" Button for the First Project
    if project["app_url"]:
        st.markdown(f"""
        <br><a href="{project['app_url']}" target="_blank" class="futuristic-button">🚀 View App</a>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)

# Contact Section
st.markdown("<div class='container'><h2>📩 Contact Me</h2></div>", unsafe_allow_html=True)

contact_form = """
<form action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
    <input type="text" name="name" placeholder="Your Name" required><br>
    <input type="email" name="email" placeholder="Your Email" required><br>
    <textarea name="message" placeholder="Your Message" required></textarea><br>
    <button type="submit" class="futuristic-button">Send Message</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)

# Social Media Links
st.markdown("🔗 **Connect with me:**")
st.markdown("[LinkedIn](https://www.linkedin.com/in/mohd-huzaif-99a875264/) | [GitHub](https://github.com/khanhuzaif348) | [Email](mailto:khanhuzaif348@gmail.com)")

# Copyright Footer
st.markdown("<div class='footer'>Copyright © 2025 Mohd Huzaif | All rights reserved</div>", unsafe_allow_html=True)
