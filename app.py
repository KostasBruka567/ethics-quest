import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(page_title="Ethics Quest", layout="centered")

# --- ΓΛΩΣΣΕΣ ΚΑΙ ΚΕΙΜΕΝΑ ---
languages = {
    "Greek": {
        "title": "🎮 Ethics Quest",
        "author": "ΚΩΝΣΤΑΝΤΙΝΟΣ ΜΠΡΟΥΚΑ",
        "am": "ΑΜ: inf2023139",
        "question_header": "Ποια είναι η απόφασή σας;",
        "results_header": "📊 Το Ηθικό σου Προφίλ",
        "restart": "Επανεκκίνηση Παιχνιδιού",
        "idealist": ["Ο Ηθικός Ιδεαλιστής", "Βάζεις τις αξίες και τα ανθρώπινα δικαιώματα πάνω από το κέρδος και την τεχνολογία."],
        "technocrat": ["Ο Πραγματιστής Τεχνοκράτης", "Εστιάζεις στη λύση των προβλημάτων και στην αποτελεσματικότητα των συστημάτων."],
        "diplomat": ["Ο Συνετός Διπλωμάτης", "Προσπαθείς να βρεις τη 'χρυσή τομή' ανάμεσα στα δικαιώματα και τις ανάγκες της αγοράς."]
    },
    "English": {
        "title": "🎮 Ethics Quest",
        "author": "KONSTANTINOS BROUKA",
        "am": "ID: inf2023139",
        "question_header": "What is your decision?",
        "results_header": "📊 Your Ethical Profile",
        "restart": "Restart Game",
        "idealist": ["The Ethical Idealist", "You prioritize values and human rights over profit and technology."],
        "technocrat": ["The Pragmatic Technocrat", "You focus on problem-solving and system efficiency."],
        "diplomat": ["The Wise Diplomat", "You strive to find the 'golden mean' between rights and market needs."]
    }
}

# Επιλογή γλώσσας στο Sidebar
lang_choice = st.sidebar.selectbox("🌐 Language / Γλώσσα", ["Greek", "English"])
L = languages[lang_choice]

# Στοιχεία UI
st.markdown(f"<h1 style='text-align: center;'>{L['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 10px; border-radius: 10px; border: 1px solid #d1d5db; text-align: center;'>
        <p style='margin: 0; font-weight: bold; color: #1f2937;'>{L['author']}</p>
        <p style='margin: 0; color: #4b5563;'>{L['am']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

# Αρχικοποίηση scores
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.scores = {"Privacy": 50, "Security": 50, "Profit": 50, "Justice": 50}

# ΛΙΣΤΑ ΣΕΝΑΡΙΩΝ
scenarios = [
    {
        "title": {"Greek": "Σενάριο 1: Βιομετρική Επιτήρηση", "English": "Scenario 1: Biometric Surveillance"},
        "text": {
            "Greek": "Η δημοτική αρχή προτείνει κάμερες αναγνώρισης προσώπου για την πρόληψη του εγκλήματος.",
            "English": "The city council proposes facial recognition cameras for crime prevention."
        },
        "options": [
            {"text": {"Greek": "✅ Αποδοχή για ασφάλεια", "English": "✅ Accept for security"}, "impact": {"Security": 30, "Privacy": -40}},
            {"text": {"Greek": "❌ Απόρριψη για ιδιωτικότητα", "English": "❌ Reject for privacy"}, "impact": {"Security": -20, "Privacy": 40}}
        ]
    },
    {
        "title": {"Greek": "Σενάριο 2: Αλγοριθμική Προκατάληψη", "English": "Scenario 2: Algorithmic Bias"},
        "text": {
            "Greek": "Ο αλγόριθμος αστυνόμευσης στοχοποιεί συνεχώς υποβαθμισμένες περιοχές.",
            "English": "The policing algorithm constantly targets underprivileged areas."
        },
        "options": [
            {"text": {"Greek": "🛠️ Διόρθωση για δικαιοσύνη", "English": "🛠️ Fix for justice"}, "impact": {"Justice": 30, "Profit": -10}},
            {"text": {"Greek": "📈 Διατήρηση ακρίβειας", "English": "📈 Maintain accuracy"}, "impact": {"Justice": -40, "Profit": 30}}
        ]
    },
    {
        "title": {"Greek": "Σενάριο 3: Dark Patterns", "English": "Scenario 3: Dark Patterns"},
        "text": {
            "Greek": "Σχεδιασμός εφαρμογών που προκαλούν εθισμό για αύξηση κέρδους.",
            "English": "Designing addictive apps to increase profit."
        },
        "options": [
            {"text": {"Greek": "💰 Προτεραιότητα στο κέρδος", "English": "💰 Prioritize profit"}, "impact": {"Profit": 40, "Justice": -30}},
            {"text": {"Greek": "🌿 Ηθικός σχεδιασμός", "English": "🌿 Ethical design"}, "impact": {"Profit": -30, "Justice": 30}}
        ]
    },
    {
        "title": {"Greek": "Σενάριο 4: Ιατρικά Δεδομένα", "English": "Scenario 4: Medical Data"},
        "text": {
            "Greek": "Πώληση ανωνυμοποιημένων δεδομένων υγείας σε ασφαλιστικές εταιρείες.",
            "English": "Selling anonymized health data to insurance companies."
        },
        "options": [
            {"text": {"Greek": "🤝 Αποδοχή συμφωνίας", "English": "🤝 Accept deal"}, "impact": {"Profit": 40, "Privacy": -40}},
            {"text": {"Greek": "🚫 Απόρριψη συμφωνίας", "English": "🚫 Reject deal"}, "impact": {"Profit": -30, "Privacy": 40}}
        ]
    },
    {
        "title": {"Greek": "Σενάριο 5: Ransomware", "English": "Scenario 5: Ransomware"},
        "text": {
            "Greek": "Επίθεση σε δίκτυο ηλεκτροδότησης. Πληρωμή λύτρων ή όχι;",
            "English": "Attack on power grid. Pay the ransom or not?"
        },
        "options": [
            {"text": {"Greek": "🆘 Πληρωμή λύτρων", "English": "🆘 Pay ransom"}, "impact": {"Security": 30, "Justice": -20}},
            {"text": {"Greek": "🛡️ Άρνηση πληρωμής", "English": "🛡️ Refuse payment"}, "impact": {"Security": -20, "Justice": 20}}
        ]
    },
    {
        "title": {"Greek": "Σενάριο 6: AI Detectors", "English": "Scenario 6: AI Detectors"},
        "text": {
            "Greek": "Χρήση αμφιλεγόμενων εργαλείων ανίχνευσης AI στις εξετάσεις.",
            "English": "Using controversial AI detection tools in exams."
        },
        "options": [
            {"text": {"Greek": "🎓 Αυστηρή χρήση", "English": "🎓 Strict usage"}, "impact": {"Profit": 30, "Justice": -40}},
            {"text": {"Greek": "🔍 Συμβουλευτική χρήση", "English": "🔍 Advisory usage"}, "impact": {"Profit": -10, "Justice": 10}}
        ]
    }
]

# ΡΟΗ ΠΑΙΧΝΙΔΙΟΥ
if st.session_state.step < len(scenarios):
    s = scenarios[st.session_state.step]
    st.subheader(s["title"][lang_choice])
    st.info(s["text"][lang_choice])
    st.write(f"**{L['question_header']}**")
    
    for idx, opt in enumerate(s["options"]):
        if st.button(opt["text"][lang_choice], key=f"btn_{st.session_state.step}_{idx}"):
            for key, val in opt["impact"].items():
                st.session_state.scores[key] += val
            st.session_state.step += 1
            st.rerun()
else:
    st.balloons()
    st.header(L["results_header"])
    
    # Λογική Τίτλων
    final = st.session_state.scores
    if (final["Privacy"] + final["Justice"]) > (final["Security"] + final["Profit"] + 10):
        res = L["idealist"]
    elif (final["Security"] + final["Profit"]) > (final["Privacy"] + final["Justice"] + 10):
        res = L["technocrat"]
    else:
        res = L["diplomat"]

    st.subheader(res[0])
    st.write(f"*{res[1]}*")
    st.markdown("---")
    
    # Μπάρες Προόδου (Μετάφραση ονομάτων αξιών)
    labels = {"Privacy": "Ιδιωτικότητα / Privacy", "Security": "Ασφάλεια / Security", "Profit": "Κέρδος / Profit", "Justice": "Δικαιοσύνη / Justice"}
    for key, val in final.items():
        st.write(f"**{labels[key]}**")
        st.progress(max(0, min(100, val)) / 100)
        
    if st.button(L["restart"]):
        st.session_state.step = 0
        st.session_state.scores = {"Privacy": 50, "Security": 50, "Profit": 50, "Justice": 50}
        st.rerun()
