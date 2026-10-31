import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="CareerPsyche | Career Discovery",
    page_icon="🧠",
    layout="wide"
)

# ==================================================
# 1. DESIGN
# ==================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;600;700;800&display=swap');

.stApp {
    background:
        radial-gradient(circle at 8% 8%,rgba(166,226,202,.5),transparent 34%),
        radial-gradient(circle at 92% 12%,rgba(199,185,255,.45),transparent 35%),
        linear-gradient(135deg,#F4FAF6,#F8F6FF,#EDF8F4);
    font-family:'DM Sans',sans-serif;
    color:#24443A;
}
/* Make form labels dark green and readable */
.stTextInput label,
.stSelectbox label,
.stTextArea label,
.stNumberInput label,
.stSlider label,
.stRadio label,
.stCheckbox label,
[data-testid="stWidgetLabel"] {
    color: #174A40 !important;
    font-weight: 600 !important;
}

.block-container {
    max-width:1150px;
    padding-top:2rem;
    padding-bottom:3rem;
}

h1,h2,h3,h4 {
    color:#203D35!important;
    font-family:'Manrope',sans-serif!important;
}

.brand {
    font-size:1.2rem;
    font-weight:800;
    letter-spacing:3px;
    color:#176B59;
}

.brand-sub {
    font-size:.72rem;
    letter-spacing:2px;
    color:#7A8F84;
}

.hero,.panel {
    background:rgba(255,255,255,.82);
    border:1px solid white;
    border-radius:25px;
    padding:35px;
    box-shadow:0 15px 40px rgba(37,76,60,.08);
    margin:20px 0;
}

.hero-title {
    font-size:clamp(2.3rem,5vw,4rem);
    font-weight:800;
    line-height:1.15;
}

.hero-highlight {
    background:linear-gradient(90deg,#16866C,#7779DE);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.eyebrow {
    display:inline-block;
    background:#E1F3E9;
    color:#176B59;
    padding:9px 15px;
    border-radius:30px;
    font-weight:800;
    font-size:.76rem;
    letter-spacing:1px;
    margin-bottom:15px;
}

.feature-card {
    background:rgba(255,255,255,.85);
    border:1px solid white;
    border-radius:20px;
    padding:23px;
    min-height:160px;
    box-shadow:0 10px 25px rgba(39,76,61,.05);
}

.feature-icon {
    font-size:2rem;
    margin-bottom:10px;
}

.feature-title {
    font-weight:800;
    color:#29473C;
}

.metric-card {
    background:rgba(255,255,255,.85);
    border:1px solid white;
    border-radius:18px;
    padding:20px;
    text-align:center;
}

.metric-value {
    font-size:2rem;
    font-weight:800;
    color:#176B59;
}

.metric-label {
    font-size:.85rem;
    color:#718079;
}

/* BUTTONS */

.stButton>button,
.stDownloadButton>button,
.stFormSubmitButton>button {
    background:linear-gradient(110deg,#176B59,#279781)!important;
    color:white!important;
    border:none!important;
    border-radius:13px!important;
    min-height:48px;
    font-weight:700!important;
    font-size:15px!important;
}

.stButton>button p,
.stDownloadButton>button p,
.stFormSubmitButton>button p,
.stButton>button span,
.stDownloadButton>button span,
.stFormSubmitButton>button span {
    color:white!important;
    font-weight:700!important;
}

.stButton>button:hover,
.stDownloadButton>button:hover,
.stFormSubmitButton>button:hover {
    background:linear-gradient(110deg,#125747,#20836C)!important;
    color:white!important;
    transform:translateY(-2px);
}

.stRadio label,
.stRadio label p {
    color:#24443A!important;
}

.stRadio [role="radiogroup"] {
    gap:8px;
}

.stRadio [role="radiogroup"] label {
    background:rgba(255,255,255,.75);
    border:1px solid #D5E7DD;
    border-radius:12px;
    padding:8px 12px;
}

.stProgress [data-testid="stProgressBar"] {
    background:#DCEBE4!important;
}

.stProgress [data-testid="stProgressBar"]>div {
    background:linear-gradient(90deg,#176B59,#279781,#8BCFB6)!important;
}

.footer {
    text-align:center;
    color:#7A8F84;
    font-size:.82rem;
    padding:30px 0;
}
</style>
""", unsafe_allow_html=True)


# ==================================================
# 2. RIASEC DIMENSIONS
# ==================================================

dimensions = {
    "R": "Realistic",
    "I": "Investigative",
    "A": "Artistic",
    "S": "Social",
    "E": "Enterprising",
    "C": "Conventional"
}

dimension_info = {
    "Realistic": (
        "Practical, technical and hands-on activities.",
        "Engineering, mechanical work, healthcare technology, agriculture, aviation, skilled trades.",
        "Engineering, technical courses, healthcare technology, agriculture and vocational training.",
        "Technical knowledge, practical problem-solving, equipment handling and spatial skills."
    ),

    "Investigative": (
        "Research, scientific thinking, analysis and solving complex problems.",
        "Medicine, scientific research, data science, psychology research, biotechnology, laboratory science.",
        "Medicine, science, biotechnology, statistics, data science and research.",
        "Critical thinking, research methods, analytical reasoning and data interpretation."
    ),

    "Artistic": (
        "Creativity, imagination, originality and self-expression.",
        "Graphic design, architecture, fashion, animation, VFX, writing, media and creative direction.",
        "Design, fine arts, architecture, animation, communication and media studies.",
        "Creativity, visual communication, innovation, storytelling and design skills."
    ),

    "Social": (
        "Helping, teaching, supporting and working with people.",
        "Psychology, counselling pathways, teaching, nursing, social work, healthcare and community development.",
        "Psychology, education, nursing, social work, healthcare and human development.",
        "Communication, empathy, active listening, collaboration and teaching."
    ),

    "Enterprising": (
        "Leadership, business, persuasion, decision-making and entrepreneurship.",
        "Business management, marketing, entrepreneurship, law, sales, leadership and human resources.",
        "Business administration, management, marketing, law, finance and entrepreneurship.",
        "Leadership, negotiation, communication, decision-making and business planning."
    ),

    "Conventional": (
        "Organisation, accuracy, planning, structured tasks and working with information.",
        "Chartered accountancy, accounting, banking, auditing, finance, administration and data management.",
        "Accounting, finance, commerce, business administration, banking and information management.",
        "Organisation, numerical ability, attention to detail, planning and record management."
    )
}


# ==================================================
# 3. THIRTY ASSESSMENT QUESTIONS
# ==================================================

questions = [

    # REALISTIC

    ("I enjoy working with machines, equipment or technical tools.", "Realistic"),
    ("I like practical activities that involve building or creating something.", "Realistic"),
    ("I enjoy understanding how mechanical or technical systems work.", "Realistic"),
    ("I prefer hands-on activities over purely theoretical tasks.", "Realistic"),
    ("I enjoy solving practical problems using physical or technical methods.", "Realistic"),

    # INVESTIGATIVE

    ("I enjoy analysing information to understand complex problems.", "Investigative"),
    ("I like conducting research and discovering new information.", "Investigative"),
    ("I enjoy studying scientific concepts and theories.", "Investigative"),
    ("I like interpreting data, statistics and numerical information.", "Investigative"),
    ("I enjoy understanding why things happen and finding evidence-based explanations.", "Investigative"),

    # ARTISTIC

    ("I enjoy expressing my ideas through creative activities.", "Artistic"),
    ("I like designing, drawing or creating visual content.", "Artistic"),
    ("I enjoy writing, storytelling or developing original ideas.", "Artistic"),
    ("I prefer opportunities that allow freedom and creativity.", "Artistic"),
    ("I enjoy exploring new approaches to make something unique.", "Artistic"),

    # SOCIAL

    ("I enjoy helping people understand and overcome difficulties.", "Social"),
    ("I feel comfortable communicating with different kinds of people.", "Social"),
    ("I enjoy teaching or explaining concepts to others.", "Social"),
    ("I like participating in activities that benefit communities.", "Social"),
    ("I enjoy listening to people and understanding their perspectives.", "Social"),

    # ENTERPRISING

    ("I enjoy taking leadership roles in group activities.", "Enterprising"),
    ("I like persuading others and presenting my ideas confidently.", "Enterprising"),
    ("I enjoy planning business activities or entrepreneurial projects.", "Enterprising"),
    ("I feel comfortable making decisions and taking responsibility.", "Enterprising"),
    ("I enjoy organising people to achieve a common goal.", "Enterprising"),

    # CONVENTIONAL

    ("I enjoy organising information, documents and records.", "Conventional"),
    ("I like working with numbers, calculations and financial information.", "Conventional"),
    ("I prefer tasks that require accuracy and attention to detail.", "Conventional"),
    ("I enjoy planning schedules and managing structured activities.", "Conventional"),
    ("I feel comfortable following organised procedures and systems.", "Conventional")
]


# ==================================================
# 4. RESPONSE SCALE
# ==================================================

LIKERT = [
    "1 — Strongly disagree",
    "2 — Disagree",
    "3 — Neither agree nor disagree",
    "4 — Agree",
    "5 — Strongly agree"
]


# ==================================================
# 5. EDUCATIONAL FIELDS
# ==================================================

education_fields = {

    "Commerce & Finance": [
        "B.Com",
        "M.Com",
        "Chartered Accountancy (CA)",
        "Cost and Management Accountancy (CMA)",
        "Company Secretary (CS)",
        "ACCA",
        "CFA",
        "Banking",
        "Finance",
        "Economics"
    ],

    "Management & Business": [
        "BBA",
        "MBA",
        "Business Administration",
        "Marketing",
        "Entrepreneurship",
        "International Business",
        "Operations Management"
    ],

    "Science": [
        "Physics",
        "Chemistry",
        "Mathematics",
        "Biology",
        "Biotechnology",
        "Microbiology",
        "Biochemistry",
        "Zoology",
        "Botany"
    ],

    "Medical & Healthcare": [
        "MBBS",
        "BDS",
        "Nursing",
        "Pharmacy",
        "Physiotherapy",
        "Allied Health Sciences",
        "Occupational Therapy",
        "Radiology",
        "Nutrition and Dietetics",
        "Veterinary Science"
    ],

    "Engineering": [
        "Computer Science Engineering",
        "Mechanical Engineering",
        "Civil Engineering",
        "Electrical Engineering",
        "Electronics Engineering",
        "Chemical Engineering",
        "Biomedical Engineering",
        "Aerospace Engineering"
    ],

    "IT & Technology": [
        "BCA",
        "MCA",
        "Computer Science",
        "Information Technology",
        "Artificial Intelligence",
        "Data Science",
        "Cybersecurity",
        "Software Development"
    ],

    "Arts & Humanities": [
        "English",
        "History",
        "Sociology",
        "Political Science",
        "Economics",
        "Languages",
        "Philosophy",
        "Journalism"
    ],

    "Psychology": [
        "B.Sc Psychology",
        "BA Psychology",
        "Applied Psychology",
        "Clinical Psychology",
        "Counselling Psychology",
        "Neuropsychology",
        "Organisational Psychology"
    ],

    "Law": [
        "LLB",
        "LLM",
        "BA LLB",
        "Corporate Law",
        "Criminal Law",
        "Constitutional Law"
    ],

    "Design & Creative Arts": [
        "Fashion Design",
        "Graphic Design",
        "Animation",
        "VFX",
        "Fine Arts",
        "Interior Design",
        "Product Design",
        "Architecture"
    ],

    "Education": [
        "B.Ed",
        "M.Ed",
        "Early Childhood Education",
        "Special Education",
        "Educational Leadership"
    ],

    "Hospitality & Tourism": [
        "Hotel Management",
        "Tourism Management",
        "Event Management",
        "Travel and Hospitality"
    ],

    "Agriculture & Environment": [
        "Agriculture",
        "Environmental Science",
        "Forestry",
        "Food Technology",
        "Environmental Engineering"
    ],

    "Government & Public Services": [
        "Civil Services",
        "Public Administration",
        "Defence Services",
        "Government Administration"
    ],

    "Other": [
        "Diploma",
        "Vocational Training",
        "Professional Certification",
        "Other Qualification"
    ]
}


# ==================================================
# 6. SESSION STATE
# ==================================================

defaults = {
    "page": "home",
    "current": 0,
    "answers": {},
    "student_name": "",
    "education": "Undergraduate",
    "field": "",
    "interest": ""
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


# ==================================================
# 7. HEADER
# ==================================================

st.markdown(
    '<div class="brand">🧠 CAREERPSYCHE</div>'
    '<div class="brand-sub">CAREER EXPLORATION · SELF-DISCOVERY · GROWTH</div>',
    unsafe_allow_html=True
)


# ==================================================
# 8. HOME PAGE
# ==================================================

def home():

    st.markdown("""
    <div class="hero">
        <div class="eyebrow">YOUR JOURNEY · YOUR POTENTIAL</div>
        <div class="hero-title">
            Discover where<br>
            your <span class="hero-highlight">potential leads.</span>
        </div>
        <p style="font-size:1.05rem;line-height:1.8;color:#718079">
        Explore your interests, understand your work preferences
        and discover career possibilities through a psychology-informed
        career exploration experience.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Discover six dimensions of your interests")

    cols = st.columns(3)

    cards = [
        ("🛠️", "Realistic", "Practical and technical interests."),
        ("🔬", "Investigative", "Research, science and analytical thinking."),
        ("🎨", "Artistic", "Creativity and self-expression."),
        ("🤝", "Social", "Helping, teaching and supporting people."),
        ("🚀", "Enterprising", "Leadership and business interests."),
        ("📊", "Conventional", "Organisation, finance and structured work.")
    ]

    for col, (icon, title, description) in zip(
        [cols[0], cols[1], cols[2], cols[0], cols[1], cols[2]],
        cards
    ):
        with col:
            st.markdown(
                f'<div class="feature-card">'
                f'<div class="feature-icon">{icon}</div>'
                f'<div class="feature-title">{title}</div>'
                f'<p>{description}</p></div>',
                unsafe_allow_html=True
            )

    st.markdown('<div class="panel">', unsafe_allow_html=True)

    st.markdown("### Before you begin")

    st.write(
        "The assessment contains 30 statements and takes approximately "
        "5–8 minutes. Choose the response that honestly reflects your interests."
    )

    st.info(
        "CareerPsyche is a preliminary, researcher-created educational "
        "exploration tool. It is not a validated psychological assessment, "
        "diagnostic instrument or definitive career-selection test."
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Begin Your Career Exploration →", use_container_width=True):
        st.session_state.page = "student"
        st.rerun()


# ==================================================
# 9. STUDENT DETAILS
# ==================================================

def student_form():

    st.markdown('<div class="eyebrow">STEP 1 · YOUR DETAILS</div>',
                unsafe_allow_html=True)

    st.title("Let's get to know you")

    st.write("Your educational background helps us understand your context.")

    with st.form("student_form"):

        st.markdown("### 👤 Personal Information")

        name = st.text_input(
            "Full name *",
            value=st.session_state.student_name,
            placeholder="Enter your name"
        )

        st.markdown("### 🎓 Educational Background")

        education = st.selectbox(
            "Current educational level",
            [
                "School Student",
                "Higher Secondary",
                "Undergraduate",
                "Postgraduate",
                "Diploma",
                "Professional Course",
                "Doctoral / PhD",
                "Other"
            ]
        )

        category = st.selectbox(
            "Select your field",
            list(education_fields.keys())
        )

        field_options = education_fields[category] + ["Other / Not listed"]

        selected_field = st.selectbox(
            "Select your qualification or subject",
            field_options
        )

        custom_field = ""

        if selected_field == "Other / Not listed":
            custom_field = st.text_input(
                "Enter your qualification or subject"
            )

        st.markdown("### 💡 Career Interests")

        interest = st.text_input(
            "Do you already have a career in mind?",
            placeholder="e.g. CA, Doctor, Entrepreneur, Lawyer, Designer"
        )

        submitted = st.form_submit_button(
            "Continue to Assessment →",
            use_container_width=True
        )

    if submitted:

        if not name.strip():
            st.error("Please enter your name.")

        elif selected_field == "Other / Not listed" and not custom_field.strip():
            st.error("Please enter your qualification or subject.")

        else:

            st.session_state.student_name = name.strip()
            st.session_state.education = education

            if selected_field == "Other / Not listed":
                st.session_state.field = custom_field.strip()
            else:
                st.session_state.field = selected_field

            st.session_state.interest = interest.strip() or "Not sure yet"

            st.session_state.page = "assessment"
            st.session_state.current = 0
            st.session_state.answers = {}

            st.rerun()

    if st.button("← Back to home"):
        st.session_state.page = "home"
        st.rerun()


# ==================================================
# 10. ASSESSMENT
# ==================================================

def assessment():

    current = st.session_state.current

    question_text, dimension = questions[current]

    total = len(questions)

    st.markdown(
        '<div class="eyebrow">STEP 2 · CAREER INTEREST ASSESSMENT</div>',
        unsafe_allow_html=True
    )

    st.progress((current + 1) / total)

    st.caption(
        f"Question {current + 1} of {total}"
    )

    st.markdown(
        f'<div class="question-tag">{dimension.upper()}</div>',
        unsafe_allow_html=True
    )

    st.markdown(f"## {question_text}")

    st.write("How much do you agree with this statement?")

    previous = st.session_state.answers.get(current, 3)

    chosen = st.radio(
        "Your response",
        [1, 2, 3, 4, 5],
        index=previous - 1,
        format_func=lambda x: LIKERT[x - 1],
        key=f"response_{current}",
        label_visibility="collapsed"
    )

    st.write("")

    left, middle, right = st.columns([1, 1, 1.4])

    with left:

        if current > 0:

            if st.button("← Previous", use_container_width=True):

                st.session_state.answers[current] = chosen
                st.session_state.current -= 1
                st.rerun()

    with right:

        if current < total - 1:

            if st.button("Next Question →", use_container_width=True):

                st.session_state.answers[current] = chosen
                st.session_state.current += 1
                st.rerun()

        else:

            if st.button("Complete Assessment ✨", use_container_width=True):

                st.session_state.answers[current] = chosen

                if len(st.session_state.answers) == total:
                    st.session_state.page = "results"
                    st.rerun()

                else:
                    st.warning("Please answer all questions.")

    st.caption(
        "There are no right or wrong answers. Respond based on your genuine interests."
    )

    if st.button("Exit assessment"):
        st.session_state.page = "student"
        st.rerun()


# ==================================================
# 11. RESULTS AND CAREER RECOMMENDATIONS
# ==================================================

def results():

    answers = st.session_state.answers

    scores = {}

    for dimension in dimensions.values():

        relevant = [
            answers[i]
            for i, question in enumerate(questions)
            if question[1] == dimension
        ]

        scores[dimension] = sum(relevant)

    ranked = sorted(
        scores,
        key=scores.get,
        reverse=True
    )

    st.markdown(
        '<div class="eyebrow">STEP 3 · YOUR CAREER PROFILE</div>',
        unsafe_allow_html=True
    )

    st.title(
        f"Your Career Discovery Report, {st.session_state.student_name} ✨"
    )

    st.write(
        f"Educational background: **{st.session_state.field}**"
    )

    st.write(
        f"Career interest: **{st.session_state.interest}**"
    )

    st.info(
        "Your scores represent your responses to this exploratory questionnaire. "
        "They are not validated aptitude scores or predictions of career success."
    )

    # SCORE CARDS

    st.markdown("### Your six interest dimensions")

    cols = st.columns(3)

    for col, dimension in zip(cols * 2, dimensions.values()):

        with col:

            st.markdown(
                f'<div class="metric-card">'
                f'<div class="metric-value">{scores[dimension]}/25</div>'
                f'<div class="metric-label">{dimension}</div>'
                f'</div>',
                unsafe_allow_html=True
            )

    # CHART

    st.markdown("### 📊 Your Career Interest Dashboard")

    st.bar_chart(
        {
            "Interest Area": list(scores.keys()),
            "Score": list(scores.values())
        },
        x="Interest Area",
        y="Score",
        y_label="Interest Score (out of 25)"
    )

    # TOP THREE PROFILE

    st.markdown("### 🌟 Your strongest interest areas")

    for number, dimension in enumerate(ranked[:3], 1):

        description, careers, courses, skills = dimension_info[dimension]

        with st.container(border=True):

            st.markdown(f"### {number}. {dimension}")

            st.write(description)

            st.markdown("**Career possibilities:**")
            st.write(careers)

    # TOP FIVE CAREER AREAS

    st.markdown("### 🎯 Suggested career exploration pathways")

    st.write(
        "These are possible directions based on your interest profile. "
        "They are not guarantees of suitability or professional eligibility."
    )

    for number, dimension in enumerate(ranked[:5], 1):

        description, careers, courses, skills = dimension_info[dimension]

        with st.container(border=True):

            st.markdown(f"**{number}. {dimension}-oriented careers**")

            st.write(description)

            st.markdown("**Example professions:**")
            st.write(careers)

            st.markdown("**Relevant courses or qualifications:**")
            st.write(courses)

            st.markdown("**Useful skills to develop:**")
            st.write(skills)

    # REFLECTION

    st.markdown("### 🌱 Personal reflection")

    st.write("• Which interest dimension describes you best?")
    st.write("• Which career possibility would you like to explore further?")
    st.write("• What skills would you like to develop?")
    st.write("• Does your current educational background connect with your interests?")

    # REPORT

    lines = [
        "CAREERPSYCHE - CAREER DISCOVERY REPORT",
        "=" * 45,
        f"Name: {st.session_state.student_name}",
        f"Education: {st.session_state.education}",
        f"Field: {st.session_state.field}",
        f"Existing career interest: {st.session_state.interest}",
        f"Date: {datetime.now().strftime('%d %B %Y')}",
        "",
        "RIASEC INTEREST SCORES"
    ]

    for dimension, score in sorted(
        scores.items(),
        key=lambda x: x[1],
        reverse=True
    ):

        lines.append(f"{dimension}: {score}/25")

    lines += [
        "",
        "SUGGESTED CAREER EXPLORATION PATHWAYS"
    ]

    for dimension in ranked:

        description, careers, courses, skills = dimension_info[dimension]

        lines += [
            "",
            dimension,
            description,
            f"Example professions: {careers}",
            f"Relevant courses: {courses}",
            f"Skills: {skills}"
        ]

    lines += [
        "",
        "IMPORTANT DISCLAIMER",
        "CareerPsyche is a preliminary, researcher-created educational "
        "career exploration tool. It is not a validated psychological "
        "assessment, aptitude test or definitive career recommendation. "
        "The RIASEC-inspired questions are original exploratory statements. "
        "Scores should be interpreted as self-reported interest patterns only."
    ]

    report = "\n".join(lines)

    st.download_button(
        "📄 Download Your Career Report",
        report.encode("utf-8"),
        file_name="CareerPsyche_Report.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button("↻ Retake Assessment", use_container_width=True):

        st.session_state.answers = {}
        st.session_state.current = 0
        st.session_state.page = "assessment"
        st.rerun()

    if st.button("Return to Home", use_container_width=True):

        st.session_state.answers = {}
        st.session_state.current = 0
        st.session_state.page = "home"
        st.rerun()


# ==================================================
# 12. PAGE NAVIGATION
# ==================================================

if st.session_state.page == "home":

    home()

elif st.session_state.page == "student":

    student_form()

elif st.session_state.page == "assessment":

    assessment()

elif st.session_state.page == "results":

    results()


# ==================================================
# 13. FOOTER
# ==================================================

st.markdown(
    '<div class="footer">'
    'CAREERPSYCHE · Explore thoughtfully. Grow intentionally.<br>'
    'Educational career exploration tool · Not a validated assessment'
    '</div>',
    unsafe_allow_html=True
)