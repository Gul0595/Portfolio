import streamlit as st
from streamlit_option_menu import option_menu

# Page Config
st.set_page_config(page_title="Gulshan's Portfolio", page_icon="🚀", layout="wide")

# Custom CSS for beautiful styling
st.markdown("""
<style>
    .main {
        background-color: #0e1117;
        color: #fafafa;
    }
    .block-container {
        max-width: 95% !important;
        padding-left: 10rem !important;
        padding-right: 10rem !important;
        padding-top: 6rem !important;
    }
    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }
    }
    .stApp {
        background: linear-gradient(135deg, #0f0f0f 0%, #1a1a2e 100%);
    }
    h1, h2, h3 {
        color: #00d4ff !important;
        font-family: 'Segoe UI', sans-serif;
    }
    .css-1d391kg {  /* Sidebar hide karne ke liye */
        display: none;
    }
    .highlight {
        background: linear-gradient(90deg, #00d4ff, #6e00ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: bold;
    }
    .skill-tag {
        background: #262730;
        padding: 8px 16px;
        border-radius: 50px;
        display: inline-block;
        margin: 5px;
        font-size: 14px;
        border: 1px solid #00d4ff;
    }
    .project-card {
        background: #161625;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #333;
        margin: 15px 0;
        transition: all 0.3s;
        box-shadow: 0 4px 15px rgba(0,212,255,0.1);
    }
    .project-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 10px 30px rgba(0,212,255,0.3);
        border-color: #00d4ff;
    }
    .contact-link {
        color: #00d4ff;
        text-decoration: none;
        font-weight: bold;
    }
    .contact-link:hover {
        text-decoration: underline;
    }
    .social-links a {
        transition: all 0.3s;
        padding: 8px;
        border-radius: 8px;
    }
    .social-links a:hover {
        transform: translateY(-3px);
        background: rgba(0,212,255,0.1);
    }
</style>
""", unsafe_allow_html=True)

# Horizontal Navigation Menu (Tabs)
selected = option_menu(
    menu_title=None,
    options=["Intro", "Skills", "Projects", "Experience", "Contact"],
    icons=["house", "code-slash", "folder", "briefcase", "envelope"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#0e1117"},
        "icon": {"color": "#00d4ff", "font-size": "20px"},
        "nav-link": {
            "font-size": "18px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#262730",
            "padding": "12px"
        },
        "nav-link-selected": {
            "background-color": "#00d4ff",
            "color": "black",
            "font-weight": "bold",
            "border-radius": "10px"
        },
    }
)

# ===================== INTRO =====================
if selected == "Intro":
    col1, col2 = st.columns([3, 5])
    with col1:
        st.image("image.jpg", width=300, caption="Gulshanpreet Kaur")

         # email code
        st.markdown(
        """
        <head>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
        </head>
        """,
        unsafe_allow_html=True)

        st.markdown(
        """
        <p style="font-size: 15px; margin-bottom: -10px; margin-left: 25px;">
        <a href="mailto:preetgulshan3@gmail.com">
            <i class="fa fa-envelope" style="font-size: 15px; color: #464443;"></i>
        </a>&nbsp;
            <a href="mailto:preetgulshan3@gmail.com" style="text-decoration: none; color: #FFF0F5;">preetgulshan3@gmail.com</a>
        </p>
        """,
        unsafe_allow_html=True)

        # github code
        st.markdown(
            """
            <p style="font-size: 15px; line-height: 1.5; margin-left: 25px; margin-bottom: -10px;">
                <a href="https://github.com/Gul0595" target="_blank">
                    <i class="fab fa-github" style="font-size: 15px; color: #464443;"></i>
                </a>&nbsp;
                <a href="https://github.com/Gul0595" target="_blank" style="text-decoration: none; color: #FFF0F5;">@Gul0595</a>
            </p>
            """,
            unsafe_allow_html=True)

        # linkedin code
        st.markdown(
        """
        <p style="font-size: 15px; line-height: 1.6; margin-left: 25px; margin-bottom: -10px;">
            <a href="https://www.linkedin.com/in/gulshanpreet-kaur/" target="_blank">
                <i class="fab fa-linkedin" style="font-size: 15px; color: #0e76a8;"></i>
            </a>&nbsp;
            <a href="https://www.linkedin.com/in/gulshanpreet-kaur/" target="_blank" style="text-decoration: none; color: #FFF0F5;">@LinkedIn</a>
        </p>
        """,
        unsafe_allow_html=True)

        # 3. Resume button ALAG se render karo (yeh trick hai!)
        st.markdown("""
        <div style="text-align: left; margin: 20px 0;">
            <a href="https://drive.google.com/uc?export=download&id=1TdsJUYt3upWLEs_n6SwP_N3sKbbCdPd5" 
            style="background: linear-gradient(45deg, #00d4ff, #1C1C1C); 
                    color: white; 
                    padding: 14px 32px; 
                    border-radius: 50px; 
                    text-decoration: none; 
                    font-weight: bold; 
                    font-size: 18px;
                    box-shadow: 0 8px 25px rgba(0,212,255,0.1);
                    display: inline-block;">
                <i class="fas fa-download"></i> Download Resume
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<h1>Hi, I'm <span class='highlight'>Gulshanpreet Kaur</span> 👋</h1>", unsafe_allow_html=True)
        st.markdown("""
        <p style='font-size:18px;'>
        Data Science & Machine Learning enthusiast with hands-on experience in EDA, feature engineering, predictive modeling, and model evaluation.<br>
        I’m currently learning and building ML projects that involve real-world datasets, visualization dashboards, and practical problem-solving.<br>
        My goal is to master end-to-end ML workflows—from data cleaning to deployment—and grow into a full-stack Data Scientist.<br>
        </p>
        """, unsafe_allow_html=True)
        
        st.markdown("### 🚀 Currently working on AI-powered projects")
        st.markdown("### 🎯 Learning Generative AI & Cloud Architecture")

        
        col_a, col_b, col_c = st.columns([2,4,3])
        with col_a:
            st.info("📍 Mohali, India")
        with col_b:
            # st.markdown("""
            # <div style="
            #     background: linear-gradient(90deg, #00d4ff, #6e00ff);
            #     color: white;
            #     padding: 10px 20px;
            #     border-radius: 50px;
            #     font-weight: bold;
            #     text-align: center;
            #     font-size: 15px;
            #     box-shadow: 0 4px 15px rgba(0,212,255,0.4);
            # ">
            # ✅ Looking for Internship
            # </div>
            # """, unsafe_allow_html=True)
            st.success("✅  Looking for Internship")
        with col_c:
            st.warning("💼 Open to Work")

# ===================== SKILLS =====================
elif selected == "Skills":
    st.markdown("<h1>My <span class='highlight'>Skills</span></h1>", unsafe_allow_html=True)
    
    st.markdown("### Programming Languages")
    st.markdown("""
    <div>
        <span class='skill-tag'>Python</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Web Technologies")
    st.markdown("""
    <div>
        <span class='skill-tag'>FastAPI</span>
        <span class='skill-tag'>Streamlit</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Databases & Cloud")
    st.markdown("""
    <div>
        <span class='skill-tag'>MongoDB</span>
        <span class='skill-tag'>MySQL</span>
        <span class='skill-tag'>Firebase</span>
        <span class='skill-tag'>AWS</span>
        <span class='skill-tag'>Docker</span>
        <span class='skill-tag'>Git/GitHub</span>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### Tools & Others")
    st.markdown("""
    <div>
        <span class='skill-tag'>VS Code</span>
        <span class='skill-tag'>Jupyter Notebook</span>
        <span class='skill-tag'>Linux</span>
        <span class='skill-tag'>Machine Learning</span>
    </div>
    """, unsafe_allow_html=True)

# ===================== PROJECTS =====================
elif selected == "Projects":
    st.markdown("<h1>My <span class='highlight'>Projects</span></h1>", unsafe_allow_html=True)
    
    # Project 1
    with st.container():
        st.markdown("""
        <div class='project-card'>
            <h3>🔥 AI Chatbot with Memory</h3>
            <p>Built a smart chatbot using LangChain, Streamlit, and OpenAI that remembers conversation history.</p>
            <p><strong>Tech:</strong> Python, Streamlit, LangChain, OpenAI, Pinecone</p>
            <a href="https://github.com" class='contact-link'>GitHub</a> • <a href="#" class='contact-link'>Live Demo</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Project 2
    with st.container():
        st.markdown("""
        <div class='project-card'>
            <h3>📊 Sales Dashboard</h3>
            <p>Interactive dashboard with filters, charts, and real-time analytics using Streamlit & Plotly.</p>
            <p><strong>Tech:</strong> Streamlit, Pandas, Plotly, Python</p>
            <a href="https://github.com" class='contact-link'>GitHub</a> • <a href="#" class='contact-link'>Live Demo</a>
        </div>
        """, unsafe_allow_html=True)
    
    # Project 3
    with st.container():
        st.markdown("""
        <div class='project-card'>
            <h3>🛒 E-Commerce Website</h3>
            <p>Full-stack MERN e-commerce site with payment integration and admin panel.</p>
            <p><strong>Tech:</strong> React, Node.js, MongoDB, Stripe</p>
            <a href="https://github.com" class='contact-link'>GitHub</a> • <a href="#" class='contact-link'>Live Demo</a>
        </div>
        """, unsafe_allow_html=True)

# ===================== EXPERIENCE =====================
elif selected == "Experience":
    st.markdown("<h1>Work <span class='highlight'>Experience</span></h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background:#161625; padding:20px; border-radius:15px; border-left:5px solid #00d4ff; margin:20px 0;'>
        <h3>Professional Certificate Program in AI and Data Science</h3>
        <p><strong>June 2025 - Present</strong></p>
        <p>Currently enrolled in a Professional Certificate Program in AI & Data Science, 
                gaining hands-on experience in Machine Learning, data analysis, and end-to-end model development.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background:#161625; padding:20px; border-radius:15px; border-left:5px solid #00d4ff; margin:20px 0;'>
        <h3>Python Developer Intern</h3>
        <p><strong>ABC Company • 2025 - 2026</strong></p>
        <p>Developed automation tools and data pipelines using Python, FastAPI, and PostgreSQL.</p>
    </div>
    """, unsafe_allow_html=True)

# ===================== CONTACT =====================
elif selected == "Contact":
    st.markdown("<h1>Get In <span class='highlight'>Touch</span></h1>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2,3])
    with col2:
        st.markdown("""
        <h3>Let's Connect!</h3>
        <p>📧 <a href="mailto:preetgulshan3@gmail.com" class='contact-link'>preetgulshan3@gmail.com</a></p>
        <p>💼 <a href="https://www.linkedin.com/in/gulshanpreet-kaur/" class='contact-link'>LinkedIn</a></p>
        <p>🐙 <a href="https://github.com/Gul0595" class='contact-link'>GitHub</a></p>
        <p>🌍 Mohali, India</p>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <h3>Send a Message</h3>
        """, unsafe_allow_html=True)
        with st.form("contact_form"):
            name = st.text_input("Your Name")
            email = st.text_input("Your Email")
            message = st.text_area("Message")
            submit = st.form_submit_button("Send Message")
            if submit:
                st.success("Thanks! I'll get back to you soon 😊")

# Footer
st.markdown("---")
st.markdown("<p style='text-align:center; color:#666;'>© 2025 Gulshanpreet Kaur. All rights reserved.</p>", unsafe_allow_html=True)