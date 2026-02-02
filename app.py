import streamlit as st

# Ρύθμιση σελίδας
st.set_page_config(page_title="Ethics Quest", layout="centered")

# --- ΓΛΩΣΣΕΣ ΚΑΙ ΚΕΙΜΕΝΑ UI ---
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
        "diplomat": ["Ο Συνετός Διπλωμάτης", "Προσπαθείς να βρεις τη 'χρυσή τομή' ανάμεσα στα δικαιώματα και τις ανάγκες της αγοράς."],
        "metrics": ["Ιδιωτικότητα", "Ασφάλεια", "Κέρδος/Αποδοτικότητα", "Κοινωνική Δικαιοσύνη"]
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
        "diplomat": ["The Wise Diplomat", "You strive to find the 'golden mean' between rights and market needs."],
        "metrics": ["Privacy", "Security", "Profit/Efficiency", "Social Justice"]
    }
}

lang_choice = st.sidebar.selectbox("🌐 Language / Γλώσσα", ["Greek", "English"])
L = languages[lang_choice]

# UI Header
st.markdown(f"<h1 style='text-align: center;'>{L['title']}</h1>", unsafe_allow_html=True)
st.markdown(f"""
    <div style='background-color: #f0f2f6; padding: 10px; border-radius: 10px; border: 1px solid #d1d5db; text-align: center;'>
        <p style='margin: 0; font-weight: bold; color: #1f2937;'>{L['author']}</p>
        <p style='margin: 0; color: #4b5563;'>{L['am']}</p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("---")

if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.scores = {"Ιδιωτικότητα": 50, "Ασφάλεια": 50, "Κέρδος/Αποδοτικότητα": 50, "Κοινωνική Δικαιοσύνη": 50}

# --- ΠΛΗΡΗ ΣΕΝΑΡΙΑ ΜΕ ΜΕΤΑΦΡΑΣΗ ---
scenarios = [
    {
        "title": {
            "Greek": "Σενάριο 1: Έξυπνες Πόλεις & Βιομετρική Επιτήρηση",
            "English": "Scenario 1: Smart Cities & Biometric Surveillance"
        },
        "text": {
            "Greek": """**Πλαίσιο:** Η δημοτική αρχή προτείνει την εγκατάσταση καμερών με αναγνώριση προσώπου για την πρόληψη του εγκλήματος σε πραγματικό χρόνο.
        
**Το Ηθικό Δίλημμα:** Η τεχνολογία αυτή μπορεί να εντοπίσει καταζητούμενους, αλλά ταυτόχρονα καταργεί την ανωνυμία των πολιτών στον δημόσιο χώρο, δημιουργώντας μια κοινωνία διαρκούς παρακολούθησης.""",
            "English": """**Context:** The local government proposes the installation of facial recognition cameras for real-time crime prevention.
        
**Ethical Dilemma:** This technology can identify fugitives, but it simultaneously eliminates citizen anonymity in public spaces, creating a society of constant surveillance."""
        },
        "options": [
            {
                "text": {
                    "Greek": "✅ Πλήρης Εφαρμογή: Η δημόσια ασφάλεια προέχει. Αν κάποιος δεν παρανομεί, η καταγραφή δεν αποτελεί απειλή γι' αυτόν.",
                    "English": "✅ Full Implementation: Public safety comes first. If one is law-abiding, surveillance is not a threat."
                },
                "impact": {"Ασφάλεια": 30, "Ιδιωτικότητα": -40, "Κέρδος/Αποδοτικότητα": 20}
            },
            {
                "text": {
                    "Greek": "⚠️ Περιορισμένη Χρήση: Εγκατάσταση μόνο σε σημεία υψηλού κινδύνου, προσπαθώντας να εξισορροπηθεί η προστασία με τα ατομικά δικαιώματα.",
                    "English": "⚠️ Limited Use: Installation only in high-risk areas, attempting to balance protection with individual rights."
                },
                "impact": {"Ασφάλεια": 10, "Ιδιωτικότητα": -10, "Κοινωνική Δικαιοσύνη": -10}
            },
            {
                "text": {
                    "Greek": "❌ Απόρριψη Έργου: Η μαζική επιτήρηση υπονομεύει τις δημοκρατικές ελευθερίες και το δικαίωμα στην ιδιωτική ζωή.",
                    "English": "❌ Project Rejection: Mass surveillance undermines democratic freedoms and the right to privacy."
                },
                "impact": {"Ασφάλεια": -20, "Ιδιωτικότητα": 40, "Κοινωνική Δικαιοσύνη": 20}
            }
        ]
    },
    {
        "title": {
            "Greek": "Σενάριο 2: Αλγοριθμική Προκατάληψη στην Αστυνόμευση",
            "English": "Scenario 2: Algorithmic Bias in Policing"
        },
        "text": {
            "Greek": """**Πλαίσιο:** Χρησιμοποιείς έναν αλγόριθμο που προβλέπει περιοχές υψηλής εγκληματικότητας. Το σύστημα όμως στοχοποιεί συνεχώς υποβαθμισμένες γειτονιές, ανακυκλώνοντας παλιές κοινωνικές προκαταλήψεις.
        
**Το Ηθικό Δίλημμα:** Η διατήρηση του αλγορίθμου ενισχύει τις διακρίσεις, ενώ η χειροκίνητη παρέμβαση στον κώδικα για λόγους δικαιοσύνης ενδέχεται να μειώσει τη στατιστική ακρίβεια των προβλέψεων.""",
            "English": """**Context:** You use an algorithm to predict high-crime areas. However, the system consistently targets disadvantaged neighborhoods, recycling old social prejudices.
        
**Ethical Dilemma:** Maintaining the algorithm reinforces discrimination, while manual intervention for fairness may reduce the statistical accuracy of the predictions."""
        },
        "options": [
            {
                "text": {
                    "Greek": "✅ Διατήρηση Ακρίβειας: Ο αλγόριθμος πρέπει να παραμείνει αντικειμενικός βάσει των δεδομένων, χωρίς ανθρώπινη παρέμβαση στα αποτελέσματα.",
                    "English": "✅ Maintain Accuracy: The algorithm must remain objective based on data, without human intervention in results."
                },
                "impact": {"Κέρδος/Αποδοτικότητα": 30, "Κοινωνική Δικαιοσύνη": -40}
            },
            {
                "text": {
                    "Greek": "🛠️ Ηθική Διόρθωση: Τροποποίηση του συστήματος ώστε να κατανέμει δίκαια τις περιπολίες, δίνοντας προτεραιότητα στην κοινωνική ισότητα.",
                    "English": "🛠️ Ethical Correction: Modify the system to distribute patrols fairly, prioritizing social equality."
                },
                "impact": {"Κοινωνική Δικαιοσύνη": 30, "Κέρδος/Αποδοτικότητα": -10}
            },
            {
                "text": {
                    "Greek": "📢 Διαφάνεια & Έλεγχος: Δημοσιοποίηση της λειτουργίας του αλγορίθμου, ώστε η κοινωνία να αποφασίσει για τα όρια της χρήσης του.",
                    "English": "📢 Transparency & Oversight: Publicly disclose how the algorithm works so society can decide on its limits."
                },
                "impact": {"Κοινωνική Δικαιοσύνη": 40, "Κέρδος/Αποδοτικότητα": -30, "Ασφάλεια": -10}
            }
        ]
    },
    {
        "title": {
            "Greek": "Σενάριο 3: Σχεδιασμός για Εθισμό (Dark Patterns)",
            "English": "Scenario 3: Designing for Addiction (Dark Patterns)"
        },
        "text": {
            "Greek": """**Πλαίσιο:** Σου ζητείται να ενσωματώσεις στα Social Media λειτουργίες που εκμεταλλεύονται την ψυχολογία του χρήστη (π.χ. άπειρο σκρολάρισμα) για να αυξηθεί ο χρόνος παραμονής στην εφαρμογή.
        
**Το Ηθικό Δίλημμα:** Αυτές οι πρακτικές αυξάνουν τα έσοδα της εταιρείας, αλλά συνδέονται με προβλήματα ψυχικής υγείας και εθισμό, ειδικά στους νεότερους χρήστες.""",
            "English": """**Context:** You are asked to integrate Social Media features that exploit user psychology (e.g., infinite scrolling) to increase time spent on the app.
        
**Ethical Dilemma:** These practices increase company revenue but are linked to mental health issues and addiction, especially among younger users."""
        },
        "options": [
            {
                "text": {
                    "Greek": "💰 Προτεραιότητα στο Κέρδος: Η ευθύνη χρήσης ανήκει στον χρήστη. Στόχος της εφαρμογής είναι η μέγιστη αποδοτικότητα και η βιωσιμότητα.",
                    "English": "💰 Profit First: The responsibility of use lies with the user. The app's goal is maximum efficiency and viability."
                },
                "impact": {"Κέρδος/Αποδοτικότητα": 40, "Κοινωνική Δικαιοσύνη": -30}
            },
            {
                "text": {
                    "Greek": "🛡️ Μέτρα Προστασίας: Εφαρμογή των λειτουργιών, αλλά με ταυτόχρονη εισαγωγή ειδοποιήσεων για τον χρόνο χρήσης (digital wellbeing).",
                    "English": "🛡️ Safeguards: Implement features but simultaneously introduce usage time alerts (digital wellbeing)."
                },
                "impact": {"Κοινωνική Δικαιοσύνη": 10, "Κέρδος/Αποδοτικότητα": 10}
            },
            {
                "text": {
                    "Greek": "🌿 Ηθικός Σχεδιασμός: Άρνηση χρήσης χειραγωγικών μοτίβων. Σχεδιασμός που σέβεται την αυτονομία και την ψυχική ηρεμία του ατόμου.",
                    "English": "🌿 Ethical Design: Refuse to use manipulative patterns. Design that respects individual autonomy and peace of mind."
                },
                "impact": {"Ιδιωτικότητα": 30, "Κέρδος/Αποδοτικότητα": -30}
            }
        ]
    },
    {
        "title": {
            "Greek": "Σενάριο 4: Διαχείριση και Πώληση Ιατρικών Δεδομένων",
            "English": "Scenario 4: Medical Data Management & Sale"
        },
        "text": {
            "Greek": """**Πλαίσιο:** Μια ασφαλιστική εταιρεία ζητά πρόσβαση σε 'ανωνυμοποιημένα' δεδομένα ασθενών για ερευνητικούς σκοπούς, προσφέροντας μεγάλη χρηματοδότηση στο νοσοκομείο.
        
**Το Ηθικό Δίλημμα:** Υπάρχει ο τεχνικός κίνδυνος ταυτοποίησης των ασθενών (de-anonymization). Η διαρροή τέτοιων πληροφοριών μπορεί να οδηγήσει σε διακρίσεις κατά των ασθενών από ασφαλιστικούς φορείς.""",
            "English": """**Context:** An insurance company requests access to 'anonymized' patient data for research purposes, offering significant funding to the hospital.
        
**Ethical Dilemma:** There is a technical risk of patient re-identification (de-anonymization). Leaking such info can lead to discrimination against patients by insurance providers."""
        },
        "options": [
            {
                "text": {
                    "Greek": "🤝 Αποδοχή Συμφωνίας: Η χρηματοδότηση είναι απαραίτητη για τη βελτίωση των υποδομών υγείας. Το νομικό πλαίσιο ανωνυμοποίησης μας καλύπτει.",
                    "English": "🤝 Accept Deal: Funding is essential for improving health infrastructure. The legal anonymization framework covers us."
                },
                "impact": {"Κέρδος/Αποδοτικότητα": 40, "Ιδιωτικότητα": -40}
            },
            {
                "text": {
                    "Greek": "🔐 Τεχνική Διασφάλιση: Χρήση προηγμένων μεθόδων κρυπτογράφησης (Differential Privacy) που προστατεύουν τους ασθενείς, έστω και με κόστος στην ακρίβεια και μείωση της χρηματοδότησης.",
                    "English": "🔐 Technical Assurance: Use advanced encryption (Differential Privacy) to protect patients, even at a cost to accuracy and funds decrease."
                },
                "impact": {"Ιδιωτικότητα": 20, "Κέρδος/Αποδοτικότητα": 10}
            },
            {
                "text": {
                    "Greek": "🚫 Απόρριψη Συναλλαγής: Τα προσωπικά δεδομένα υγείας δεν πρέπει να γίνονται αντικείμενο εμπορικής εκμετάλλευσης χωρίς ρητή συγκατάθεση.",
                    "English": "🚫 Reject Transaction: Personal health data should not be subject to commercial exploitation without explicit consent."
                },
                "impact": {"Ιδιωτικότητα": 40, "Κέρδος/Αποδοτικότητα": -30}
            }
        ]
    },
    {
        "title": {
            "Greek": "Σενάριο 5: Κυβερνοασφάλεια και Κρίσιμες Υποδομές",
            "English": "Scenario 5: Cybersecurity & Critical Infrastructure"
        },
        "text": {
            "Greek": """**Πλαίσιο:** Μια επίθεση Ransomware έχει κλειδώσει το σύστημα ηλεκτροδότησης της πόλης. Οι επιτιθέμενοι απαιτούν λύτρα για να ξεκλειδώσουν το δίκτυο.
        
**Το Ηθικό Δίλημμα:** Η πληρωμή λύτρων χρηματοδοτεί το έγκλημα, ενώ η άρνηση θέτει σε άμεσο κίνδυνο τη λειτουργία νοσοκομείων και την ασφάλεια των πολιτών για ημέρες.""",
            "English": """**Context:** A Ransomware attack has locked the city's power grid. The attackers demand ransom to unlock the network.
        
**Ethical Dilemma:** Paying the ransom funds crime, while refusing puts hospital operations and citizen safety at immediate risk for days."""
        },
        "options": [
            {
                "text": {
                    "Greek": "🆘 Καταβολή Λύτρων: Η προστασία της ανθρώπινης ζωής είναι υπεράνω κάθε ηθικής αρχής. Απαιτείται η άμεση αποκατάσταση του ρεύματος.",
                    "English": "🆘 Pay Ransom: Protecting human life is above any ethical principle. Immediate power restoration is required."
                },
                "impact": {"Ασφάλεια": 30, "Κοινωνική Δικαιοσύνη": -20, "Κέρδος/Αποδοτικότητα": -10}
            },
            {
                "text": {
                    "Greek": "🛡️ Άρνηση Συμβιβασμού: Καμία διαπραγμάτευση με εγκληματίες. Επιλογή της δύσκολης οδού της ανάκτησης συστημάτων, παρά το κοινωνικό κόστος(2 μέρες).",
                    "English": "🛡️ Refuse Compromise: No negotiations with criminals. Choosing the hard path of system recovery, despite the social cost(2 days)."
                },
                "impact": {"Ασφάλεια": -20, "Κοινωνική Δικαιοσύνη": 20}
            },
            {
                "text": {
                    "Greek": "⚔️ Επιθετική Αντεπίθεση: Προσπάθεια 'αντι-χακαρίσματος' για ανάκτηση του ελέγχου, Είναι παράνομο και τεχνικά ριψοκίνδυνο. Αν οι χάκερ καταλάβουν ότι τους επιτίθεσαι μπορεί να διαγράψουν τα πάντα οριστικά 'από εκδίκηση' (kill switch), οπότε το ρεύμα δεν θα επανέλθει ποτέ.",
                    "English": "⚔️ Aggressive Counter-attack: Attempt to 'hack back' to regain control. It is illegal and technically risky. If the hackers realize you are attacking them, they might delete everything permanently as an act of 'revenge' (kill switch), meaning the power grid would never be restored."
                },
                "impact": {"Ασφάλεια": 10, "Κέρδος/Αποδοτικότητα": -20}
            }
        ]
    },
    {
        "title": {
            "Greek": "Σενάριο 6: AI Detectors στην Ακαδημαϊκή Εκπαίδευση",
            "English": "Scenario 6: AI Detectors in Academic Education"
        },
        "text": {
            "Greek": """**Πλαίσιο:** Το Πανεπιστήμιο χρησιμοποιεί αλγόριθμο για την ανίχνευση εργασιών που γράφτηκαν από AI. Το σύστημα όμως εμφανίζει συχνά 'ψευδώς θετικά' αποτελέσματα για φοιτητές που γράφουν σε μη μητρική γλώσσα.
        
**Το Ηθικό Δίλημμα:** Η χρήση του εργαλείου προστατεύει το κύρος του πτυχίου από την αντιγραφή, αλλά κινδυνεύει να στοχοποιήσει άδικα φοιτητές χωρίς αδιαμφισβήτητες αποδείξεις.""",
            "English": """**Context:** The University uses an algorithm to detect AI-written papers. The system often shows 'false positives' for students writing in a non-native language.
        
**Ethical Dilemma:** Using the tool protects degree integrity from copying but risks unfairly targeting students without undeniable evidence."""
        },
        "options": [
            {
                "text": {
                    "Greek": "🎓 Αυστηρή Επιβολή: Η καταπολέμηση της λογοκλοπής είναι απαραίτητη για την ακαδημαϊκή ακεραιότητα, παρά τις ατέλειες του συστήματος.",
                    "English": "🎓 Strict Enforcement: Fighting plagiarism is essential for academic integrity, despite system imperfections."
                },
                "impact": {"Κοινωνική Δικαιοσύνη": -40, "Κέρδος/Αποδοτικότητα": 30}
            },
            {
                "text": {
                    "Greek": "🔍 Συμβουλευτικός Ρόλος: Το εργαλείο παρέχει μόνο ενδείξεις. Η τελική κρίση απαιτεί προσωπική εξέταση του φοιτητή από τον καθηγητή.",
                    "English": "🔍 Advisory Role: The tool only provides indications. Final judgment requires personal examination of the student by the professor."
                },
                "impact": {"Κοινωνική Δικαιοσύνη": 10, "Κέρδος/Αποδοτικότητα": -10}
            },
            {
                "text": {
                    "Greek": "🛑 Απόρριψη Εργαλείου: Ένα ανακριβές σύστημα που εισάγει διακρίσεις δεν μπορεί να αποτελεί κριτήριο αξιολόγησης στην εκπαίδευση.",
                    "English": "🛑 Reject Tool: An inaccurate system that introduces discrimination cannot be an evaluation criterion in education."
                },
                "impact": {"Κοινωνική Δικαιοσύνη": 40, "Κέρδος/Αποδοτικότητα": -20}
            }
        ]
    }
]

# --- GAME LOGIC ---
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
    
    final = st.session_state.scores
    # Profile Logic
    # Calculate balance between "Human/Social" and "Security/Efficiency"
    social_score = final["Ιδιωτικότητα"] + final["Κοινωνική Δικαιοσύνη"]
    util_score = final["Ασφάλεια"] + final["Κέρδος/Αποδοτικότητα"]
    
    if social_score > util_score + 15:
        res = L["idealist"]
    elif util_score > social_score + 15:
        res = L["technocrat"]
    else:
        res = L["diplomat"]

    st.subheader(res[0])
    st.write(f"*{res[1]}*")
    st.markdown("---")
    
    # Progress Bars
    metrics_map = {
        "Ιδιωτικότητα": L["metrics"][0],
        "Ασφάλεια": L["metrics"][1],
        "Κέρδος/Αποδοτικότητα": L["metrics"][2],
        "Κοινωνική Δικαιοσύνη": L["metrics"][3]
    }
    
    for key_gr, label_display in metrics_map.items():
        val = final[key_gr]
        st.write(f"**{label_display}**")
        st.progress(max(0, min(100, val)) / 100)
        
    if st.button(L["restart"]):
        st.session_state.step = 0
        st.session_state.scores = {"Ιδιωτικότητα": 50, "Ασφάλεια": 50, "Κέρδος/Αποδοτικότητα": 50, "Κοινωνική Δικαιοσύνη": 50}
        st.rerun()
