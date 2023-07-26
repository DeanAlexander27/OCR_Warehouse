from pathlib import Path
import streamlit as st
from PIL import Image

#PATH SETTING
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Dean Alexander ATS.pdf"
profile_pic = current_dir / "assets" / "1672835590254.jpg"
EMAIL = "deanalexander1998@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/dean-alexander-paulus/",
    "GitHub": "https://github.com/DeanAlexander27",
    "R Studio": "https://rpubs.com/DeanAlexander27",
}

#GENERAL SET
PAGE_TITLE = "CV | Dean Alexander"
NAME = "Dean Alexander"
DESCRIPTION = """
Highly skilled supply chain professional with data science proficiency and optimization experience.
"""

st.set_page_config(page_title=PAGE_TITLE)
st.title("Hi There !")

# LOAD CSS
with open(css_file) as f :
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    # --- EDUCATION ---
    st.write('\n')
    st.subheader("Education")
    st.write("- Institut Teknologi Sepuluh Nopember (Surabaya) [August 2022 - January 2024]")
    st.write(
        """
*Master Management of Technology, Major in Supply Chain Management.*

**Cumulative GPA 3,75 / 4,00**
""")
    
    st.write("- Universitas Tarumanagara [August 2016 - January 2020]")
    st.write(
        """
*Bachelor of Engineering, Major in Industrial Engineering.*

**Cumulative GPA 3,47 / 4,00**
""")

    st.write("- Team Algoritma [January 2023 - May 2023]")
    st.write(
        """
*Class of Data Analyst, Data Visualization, Machine Learning, and Deep Learning.*

**Cumulative Score 134 / 140**
""")

with col2:
    # --- EXPERIENCE & QUALIFICATIONS ---
    st.write('\n')
    st.subheader("Experience & Qualifications")
    st.write(
        """
        - More or less 2 Years experience in supply chain and extracting actionable insights from data
        - Strong hands on experience and knowledge in Python and Excel
        - Good understanding of statistical principles and their respective applications
        - Excellent team-player and displaying strong sense of initiative on tasks
        """
        )


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python (Scikit-learn, Pandas), SQL, R
- 📊 Data Visulization: PowerBi, MS Excel, Plotly, Streamlit
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: MySQL
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Logistic Area SPV | PT. Astra Honda Motor**")
st.write("April 2022 - October 2022")
st.write(
    """
- Focused, ensured progress distribution and plan of demand accurate as the characterized area
(Semarang, Samarinda, North Sulawesi Maluku, and Central Sulawesi) per type and color, work close 
with sales area team and main dealer to support pareto saleable type and color of product to area and 
consider with “Fairness”. **Maintained market share Honda above 70% of those areas.**
- Managed and analyzed directly main dealer’s stock of unit and color with stock days as the 
measurement.
- Supervised on dealer virtual visit to know well progress of sales, info market’s commodity.
- Monthly report PICA about progress distribution, sales of area’s condition with planned corrective action 
for next step action.
"""
)
st.write("**Logistic Area Project**")
st.write("""

- Analyzed measurement distortion information from downstream to upstream to improve accuracy 
demand of color using time series predictive models. **The result of simulation improved accuracy
of availability color above 70% accurate.**

""")

# --- JOB 2
st.write('\n')
st.write("🚧", "**Procurement MRO | Asia Pulp and Paper Sinarmas**")
st.write("January 2021 - February 2022")
st.write(
    """
*MRO Contract* 
[January 2021 - October 2021]
- Supervised contract material group which is saved yearly spending and reduced the count of PR to PO 
with Spot buyer, got many choices brand and vendors with validity price minimum 1 year and negotiated
contract terms of agreement (term of payment, guarantee, commit of lead time and Incoterms)
- Recommended items by analyzing excel from each material group which potential items should be 
prioritized to increase the efficiency and effectiveness of the company's budget.
- Negotiated, Evaluated, Compared, and Requested vendor’s offer price including warranty, payment 
terms, delivery time
- **Within 10 months have approved 10 material groups contract should be presented in front of 
APP China and APP Indonesia.**
"""
)
st.write("""
*MRO Spot Mechanical Team*
         [July 2021 - February 2022]
- Received all daily PR requests from user mills with handled many materials of agroup, with **achieved 
average each PR to PO within 2 weeks, with all total PR around 550 PR in 6 months.**
- Recommended potential items with replacement/brand substitution by taking into account the 
specifications if there are supply constraints from suppliers or the level of urgency of field needs
""")

st.write("""
**MRO Hybrid Program**
         [July 2021 - October 2021]
- Coordinated all job role spot and contract in one time, with high flexibility and learnedhow they correlate 
with each other, and then consolidated end to end business of MRO to get effective and efficient way 
fulfill users needed.
""")

st.write("""
**MRO Projects assignment**
- July 2021, Contract e-Tender Result Program. All format tender in excel should be done in digital
program system, work close with vendor IT in 4 months, to decreased human error due to many items
should be handled
- December 2021, Technical Check List for Flexible Coupling due to many problems when do check 
specifications in mills to eliminated PR to PO within 2 weeks, when end user in mills opened PR, 
Technical Check List already attached to make easierfor negotiator to solved count of PR of flexible
coupling. **Result of project average end to end PR to PO under 2 weeks.**
""")