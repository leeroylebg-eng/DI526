import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import json
import io
from datetime import datetime

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DISC Personality Assessment",
    page_icon="👤",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Styles ────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    .main { background-color: #0e1117; }
    .disc-title { font-size: 2.4rem; font-weight: 800; text-align: center;
                  background: linear-gradient(90deg, #e94560, #0f3460, #16c79a, #f5a623);
                  -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .disc-subtitle { text-align: center; color: #888; font-size: 1rem; margin-bottom: 2rem; }
    .stProgress > div > div { background: linear-gradient(90deg, #e94560, #f5a623); }
    .result-card { border-radius: 16px; padding: 1.5rem; margin: 1rem 0;
                   border-left: 6px solid; }
    .section-header { font-size: 1.3rem; font-weight: 700; margin-top: 2rem; }
</style>
""", unsafe_allow_html=True)

# ── DISC Data ─────────────────────────────────────────────────────────────────
DISC_COLORS = {"D": "#e94560", "I": "#f5a623", "S": "#16c79a", "C": "#0f3460"}
DISC_NAMES  = {"D": "Dominance", "I": "Influence", "S": "Steadiness", "C": "Conscientiousness"}
DISC_EMOJIS = {"D": "🔴", "I": "🟡", "S": "🟢", "C": "🔵"}

DISC_DESCRIPTIONS = {
    "D": {
        "title": "Dominant — The Driver",
        "tagline": "Results-oriented, decisive, direct",
        "traits": ["Bold and assertive", "Goal-focused", "Competitive", "Direct communicator",
                   "Thrives under pressure", "Quick decision-maker"],
        "strengths": "Natural leader who drives results and tackles challenges head-on.",
        "growth": "May benefit from slowing down to consider others' perspectives and emotions.",
        "careers": "CEO, Entrepreneur, Sales Director, Military Officer, Lawyer",
        "famous": "Steve Jobs, Gordon Ramsay, Donald Trump",
    },
    "I": {
        "title": "Influential — The Inspirer",
        "tagline": "Enthusiastic, optimistic, collaborative",
        "traits": ["Outgoing and energetic", "Great communicator", "Optimistic", "Creative",
                   "Team motivator", "Loves social interaction"],
        "strengths": "Inspires and motivates others; brings energy and enthusiasm to every situation.",
        "growth": "May benefit from focusing on follow-through and attention to detail.",
        "careers": "Marketing, PR, Sales, Teacher, Performer, Coach",
        "famous": "Oprah Winfrey, Will Smith, Richard Branson",
    },
    "S": {
        "title": "Steady — The Supporter",
        "tagline": "Patient, reliable, supportive",
        "traits": ["Loyal and dependable", "Great listener", "Patient", "Team player",
                   "Consistent", "Calm under pressure"],
        "strengths": "The backbone of any team — reliable, empathetic and incredibly consistent.",
        "growth": "May benefit from asserting opinions more and embracing change.",
        "careers": "Nurse, Counselor, HR Manager, Social Worker, Teacher",
        "famous": "Mother Teresa, Jimmy Carter, Princess Diana",
    },
    "C": {
        "title": "Conscientious — The Analyst",
        "tagline": "Analytical, accurate, systematic",
        "traits": ["Detail-oriented", "Logical thinker", "High standards", "Data-driven",
                   "Organized", "Independent worker"],
        "strengths": "Produces high-quality, accurate work through careful analysis and planning.",
        "growth": "May benefit from making decisions faster and being more flexible.",
        "careers": "Engineer, Accountant, Data Scientist, Researcher, Programmer",
        "famous": "Bill Gates, Albert Einstein, Warren Buffett",
    },
}

COMBO_DESCRIPTIONS = {
    ("D", "I"): "A powerhouse communicator — drives results while inspiring others.",
    ("D", "C"): "Analytical leader — results-focused with high standards and precision.",
    ("D", "S"): "Determined yet empathetic — achieves goals while caring for the team.",
    ("I", "S"): "Warm influencer — people-oriented, enthusiastic, and supportive.",
    ("I", "C"): "Creative analyst — combines big ideas with attention to detail.",
    ("S", "C"): "Reliable specialist — consistent, thorough, and quality-driven.",
    ("I", "D"): "Charismatic driver — leads with energy and decisive action.",
    ("C", "D"): "Precise achiever — high standards meets relentless execution.",
    ("S", "D"): "Steady achiever — calm determination with strong follow-through.",
    ("S", "I"): "Supportive motivator — brings warmth and enthusiasm to teams.",
    ("C", "I"): "Thoughtful communicator — depth of thought with engaging delivery.",
    ("C", "S"): "Careful supporter — methodical, loyal, and consistently excellent.",
}

# ── Questions ─────────────────────────────────────────────────────────────────
QUESTIONS = [
    # D questions
    {"text": "I take charge in group situations and enjoy leading others.", "dim": "D"},
    {"text": "I prefer to make quick decisions rather than deliberate for long.", "dim": "D"},
    {"text": "I am comfortable with conflict and confrontation when necessary.", "dim": "D"},
    {"text": "I focus more on results than on the process of getting there.", "dim": "D"},
    {"text": "I enjoy competition and strive to win.", "dim": "D"},
    # I questions
    {"text": "I enjoy meeting new people and thrive in social settings.", "dim": "I"},
    {"text": "I am often the one who lifts the mood and motivates the group.", "dim": "I"},
    {"text": "I prefer to express ideas verbally rather than in writing.", "dim": "I"},
    {"text": "I am optimistic and see the positive side in most situations.", "dim": "I"},
    {"text": "I love brainstorming and generating creative ideas with others.", "dim": "I"},
    # S questions
    {"text": "I prefer a stable, predictable environment over constant change.", "dim": "S"},
    {"text": "I am a great listener and genuinely care about others' feelings.", "dim": "S"},
    {"text": "I stay calm and patient even in stressful situations.", "dim": "S"},
    {"text": "I am loyal and committed to my team and relationships.", "dim": "S"},
    {"text": "I prefer to finish one task completely before starting another.", "dim": "S"},
    # C questions
    {"text": "I pay close attention to details and strive for accuracy.", "dim": "C"},
    {"text": "I research thoroughly before making important decisions.", "dim": "C"},
    {"text": "I follow rules and procedures carefully.", "dim": "C"},
    {"text": "I prefer working independently on well-defined tasks.", "dim": "C"},
    {"text": "I hold myself to very high standards in everything I do.", "dim": "C"},
]

SCALE_LABELS = ["Strongly Disagree", "Disagree", "Neutral", "Agree", "Strongly Agree"]

# ── Helpers ───────────────────────────────────────────────────────────────────
def compute_scores(answers: dict) -> dict[str, float]:
    totals = {d: 0 for d in "DISC"}
    counts = {d: 0 for d in "DISC"}
    for i, q in enumerate(QUESTIONS):
        if i in answers:
            totals[q["dim"]] += answers[i]
            counts[q["dim"]] += 1
    return {d: (totals[d] / (counts[d] * 4) * 100) if counts[d] else 0 for d in "DISC"}


def primary_secondary(scores: dict) -> tuple[str, str]:
    ranked = sorted(scores, key=scores.get, reverse=True)
    return ranked[0], ranked[1]


def radar_chart(scores: dict) -> plt.Figure:
    dims   = list(scores.keys())
    values = [scores[d] for d in dims]
    values += values[:1]

    angles = np.linspace(0, 2 * np.pi, len(dims), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw={"polar": True})
    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#161b22")

    ax.plot(angles, values, "o-", lw=2, color="#e94560")
    ax.fill(angles, values, alpha=0.25, color="#e94560")

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(
        [f"{DISC_EMOJIS[d]} {d}" for d in dims],
        color="white", fontsize=13, fontweight="bold",
    )
    ax.set_ylim(0, 100)
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(["25", "50", "75", "100"], color="#555", fontsize=8)
    ax.tick_params(colors="white")
    ax.spines["polar"].set_color("#333")
    ax.grid(color="#333", linestyle="--", linewidth=0.7)

    return fig


def bar_chart(scores: dict) -> plt.Figure:
    dims   = list(scores.keys())
    values = [scores[d] for d in dims]
    colors = [DISC_COLORS[d] for d in dims]

    fig, ax = plt.subplots(figsize=(6, 3))
    fig.patch.set_facecolor("#0e1117")
    ax.set_facecolor("#161b22")

    bars = ax.barh(dims, values, color=colors, edgecolor="none", height=0.5)
    for bar, val in zip(bars, values):
        ax.text(val + 1, bar.get_y() + bar.get_height() / 2,
                f"{val:.0f}%", va="center", color="white", fontsize=11, fontweight="bold")

    ax.set_xlim(0, 110)
    ax.set_xlabel("Score (%)", color="white")
    ax.tick_params(colors="white", labelsize=13)
    ax.spines[:].set_color("#333")
    ax.set_facecolor("#161b22")
    for label, dim in zip(ax.get_yticklabels(), dims):
        label.set_color(DISC_COLORS[dim])
        label.set_fontweight("bold")

    return fig


def generate_pdf(name: str, scores: dict, primary: str, secondary: str) -> bytes:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.units import cm

    buf = io.BytesIO()
    doc = SimpleDocTemplate(buf, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm,
                            topMargin=2*cm, bottomMargin=2*cm)
    styles = getSampleStyleSheet()
    story  = []

    title_style = ParagraphStyle("title", parent=styles["Title"],
                                 fontSize=22, textColor=colors.HexColor("#e94560"),
                                 spaceAfter=6)
    h2_style = ParagraphStyle("h2", parent=styles["Heading2"],
                               fontSize=14, textColor=colors.HexColor("#0f3460"))
    body_style = ParagraphStyle("body", parent=styles["Normal"], fontSize=11, leading=16)

    story.append(Paragraph("DISC Personality Assessment", title_style))
    story.append(Paragraph(f"Results for: <b>{name}</b>", body_style))
    story.append(Paragraph(f"Date: {datetime.now().strftime('%B %d, %Y')}", body_style))
    story.append(Spacer(1, 0.5*cm))

    story.append(Paragraph("Your DISC Scores", h2_style))
    score_data = [["Dimension", "Name", "Score"]] + \
                 [[f"{DISC_EMOJIS[d]} {d}", DISC_NAMES[d], f"{scores[d]:.0f}%"] for d in "DISC"]
    t = Table(score_data, colWidths=[3*cm, 6*cm, 3*cm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#0f3460")),
        ("TEXTCOLOR",  (0, 0), (-1, 0), colors.white),
        ("FONTNAME",   (0, 0), (-1, 0), "Helvetica-Bold"),
        ("ALIGN",      (0, 0), (-1, -1), "CENTER"),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#f0f0f0"), colors.white]),
        ("GRID",       (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTSIZE",   (0, 0), (-1, -1), 11),
        ("PADDING",    (0, 0), (-1, -1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 0.5*cm))

    desc = DISC_DESCRIPTIONS[primary]
    story.append(Paragraph(f"Primary Style: {desc['title']}", h2_style))
    story.append(Paragraph(f"<i>{desc['tagline']}</i>", body_style))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(f"<b>Key Strengths:</b> {desc['strengths']}", body_style))
    story.append(Paragraph(f"<b>Growth Area:</b> {desc['growth']}", body_style))
    story.append(Paragraph(f"<b>Traits:</b> {', '.join(desc['traits'])}", body_style))
    story.append(Paragraph(f"<b>Ideal Careers:</b> {desc['careers']}", body_style))
    story.append(Paragraph(f"<b>Famous Examples:</b> {desc['famous']}", body_style))
    story.append(Spacer(1, 0.5*cm))

    combo_key = (primary, secondary)
    combo_desc = COMBO_DESCRIPTIONS.get(combo_key) or COMBO_DESCRIPTIONS.get((secondary, primary), "")
    if combo_desc:
        story.append(Paragraph(f"Combination Style: {primary}/{secondary}", h2_style))
        story.append(Paragraph(combo_desc, body_style))

    doc.build(story)
    return buf.getvalue()


def generate_json(name: str, scores: dict, primary: str, secondary: str) -> str:
    data = {
        "name": name,
        "date": datetime.now().isoformat(),
        "scores": {d: round(scores[d], 1) for d in "DISC"},
        "primary_style": primary,
        "secondary_style": secondary,
        "primary_description": DISC_DESCRIPTIONS[primary]["title"],
        "traits": DISC_DESCRIPTIONS[primary]["traits"],
        "careers": DISC_DESCRIPTIONS[primary]["careers"],
    }
    return json.dumps(data, indent=2)


# ── App ───────────────────────────────────────────────────────────────────────
def main():
    st.markdown('<p class="disc-title">👤 DISC Personality Assessment</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="disc-subtitle">Discover your personality style in under 5 minutes</p>',
        unsafe_allow_html=True,
    )

    if "page" not in st.session_state:
        st.session_state.page = "intro"
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    if "name" not in st.session_state:
        st.session_state.name = ""

    # ── INTRO ─────────────────────────────────────────────────────────────────
    if st.session_state.page == "intro":
        col1, col2, col3, col4 = st.columns(4)
        for col, d in zip([col1, col2, col3, col4], "DISC"):
            with col:
                st.markdown(
                    f"<div style='text-align:center; padding:1rem; border-radius:12px; "
                    f"background:{DISC_COLORS[d]}22; border:2px solid {DISC_COLORS[d]};'>"
                    f"<span style='font-size:2rem'>{DISC_EMOJIS[d]}</span><br>"
                    f"<b style='color:{DISC_COLORS[d]}'>{d}</b><br>"
                    f"<small style='color:#aaa'>{DISC_NAMES[d]}</small></div>",
                    unsafe_allow_html=True,
                )

        st.markdown("---")
        st.markdown("### Ready to discover your style?")
        name = st.text_input("Your name (optional)", placeholder="Enter your name...")
        st.markdown("You'll answer **20 quick statements** on a 1–5 scale.")

        if st.button("Start Assessment ▶", use_container_width=True, type="primary"):
            st.session_state.name = name or "Anonymous"
            st.session_state.page = "quiz"
            st.rerun()

    # ── QUIZ ──────────────────────────────────────────────────────────────────
    elif st.session_state.page == "quiz":
        answered = len(st.session_state.answers)
        progress = answered / len(QUESTIONS)
        st.progress(progress, text=f"Progress: {answered}/{len(QUESTIONS)} questions")

        for i, q in enumerate(QUESTIONS):
            with st.container():
                dim   = q["dim"]
                color = DISC_COLORS[dim]
                st.markdown(
                    f"<div style='border-left:4px solid {color}; padding-left:1rem; margin:0.8rem 0;'>"
                    f"<small style='color:{color}; font-weight:700'>{DISC_EMOJIS[dim]} {DISC_NAMES[dim]}</small><br>"
                    f"<b>Q{i+1}.</b> {q['text']}</div>",
                    unsafe_allow_html=True,
                )
                val = st.radio(
                    label=f"q{i}",
                    options=[1, 2, 3, 4, 5],
                    format_func=lambda x: SCALE_LABELS[x - 1],
                    key=f"radio_{i}",
                    horizontal=True,
                    label_visibility="collapsed",
                )
                st.session_state.answers[i] = val - 1  # 0–4

        st.markdown("---")
        col_back, col_submit = st.columns([1, 3])
        with col_back:
            if st.button("← Back", use_container_width=True):
                st.session_state.page = "intro"
                st.rerun()
        with col_submit:
            if st.button("See My Results 🎯", use_container_width=True, type="primary"):
                st.session_state.page = "results"
                st.rerun()

    # ── RESULTS ───────────────────────────────────────────────────────────────
    elif st.session_state.page == "results":
        scores    = compute_scores(st.session_state.answers)
        primary, secondary = primary_secondary(scores)
        desc      = DISC_DESCRIPTIONS[primary]
        name      = st.session_state.name

        st.markdown(f"## Hello, **{name}**! Here are your results 🎉")

        # Score cards
        cols = st.columns(4)
        for col, d in zip(cols, "DISC"):
            with col:
                is_primary = d == primary
                border = f"4px solid {DISC_COLORS[d]}" if is_primary else f"2px solid {DISC_COLORS[d]}44"
                st.markdown(
                    f"<div style='text-align:center; padding:1rem; border-radius:12px; "
                    f"background:{DISC_COLORS[d]}11; border:{border};'>"
                    f"<span style='font-size:1.8rem'>{DISC_EMOJIS[d]}</span><br>"
                    f"<b style='color:{DISC_COLORS[d]}; font-size:1.4rem'>{d}</b><br>"
                    f"<span style='font-size:1.6rem; font-weight:800'>{scores[d]:.0f}%</span><br>"
                    f"<small style='color:#aaa'>{DISC_NAMES[d]}</small>"
                    f"{'<br><small style=color:#ffe66d>★ Primary</small>' if is_primary else ''}"
                    f"</div>",
                    unsafe_allow_html=True,
                )

        st.markdown("---")

        # Charts
        col_radar, col_bar = st.columns(2)
        with col_radar:
            st.markdown("#### Radar Profile")
            st.pyplot(radar_chart(scores), use_container_width=True)
        with col_bar:
            st.markdown("#### Score Breakdown")
            st.pyplot(bar_chart(scores), use_container_width=True)

        st.markdown("---")

        # Primary style card
        st.markdown(
            f"<div style='border-radius:16px; padding:1.5rem; "
            f"background:{DISC_COLORS[primary]}15; border-left:6px solid {DISC_COLORS[primary]};'>"
            f"<h3 style='color:{DISC_COLORS[primary]}'>{DISC_EMOJIS[primary]} {desc['title']}</h3>"
            f"<i style='color:#aaa'>{desc['tagline']}</i><br><br>"
            f"<b>Strengths:</b> {desc['strengths']}<br><br>"
            f"<b>Growth Area:</b> {desc['growth']}</div>",
            unsafe_allow_html=True,
        )

        # Traits
        st.markdown("#### Key Traits")
        trait_cols = st.columns(3)
        for i, trait in enumerate(desc["traits"]):
            with trait_cols[i % 3]:
                st.markdown(
                    f"<div style='background:{DISC_COLORS[primary]}22; border-radius:8px; "
                    f"padding:0.5rem 1rem; margin:0.3rem 0; text-align:center; "
                    f"color:{DISC_COLORS[primary]}; font-weight:600'>{trait}</div>",
                    unsafe_allow_html=True,
                )

        # Combo style
        combo_key  = (primary, secondary)
        combo_desc = COMBO_DESCRIPTIONS.get(combo_key) or COMBO_DESCRIPTIONS.get((secondary, primary), "")
        if combo_desc:
            st.markdown(f"#### Combination Style: {DISC_EMOJIS[primary]}{DISC_EMOJIS[secondary]} {primary}/{secondary}")
            st.info(combo_desc)

        # Careers & famous
        col_c, col_f = st.columns(2)
        with col_c:
            st.markdown("#### Ideal Careers")
            for career in desc["careers"].split(", "):
                st.markdown(f"- {career}")
        with col_f:
            st.markdown("#### Famous Examples")
            for person in desc["famous"].split(", "):
                st.markdown(f"- {person}")

        st.markdown("---")

        # Secondary style
        st.markdown(f"#### Secondary Style: {DISC_EMOJIS[secondary]} {secondary} — {DISC_NAMES[secondary]}")
        st.markdown(
            f"<div style='border-radius:12px; padding:1rem; "
            f"background:{DISC_COLORS[secondary]}11; border:2px solid {DISC_COLORS[secondary]}44;'>"
            f"{DISC_DESCRIPTIONS[secondary]['strengths']}</div>",
            unsafe_allow_html=True,
        )

        st.markdown("---")

        # Exports
        st.markdown("### Download Your Results")
        col_pdf, col_json, col_retry = st.columns(3)

        with col_pdf:
            try:
                pdf_bytes = generate_pdf(name, scores, primary, secondary)
                st.download_button(
                    label="📄 Download PDF",
                    data=pdf_bytes,
                    file_name=f"DISC_{name.replace(' ', '_')}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )
            except Exception:
                st.warning("Install reportlab for PDF export.")

        with col_json:
            json_str = generate_json(name, scores, primary, secondary)
            st.download_button(
                label="📦 Download JSON",
                data=json_str,
                file_name=f"DISC_{name.replace(' ', '_')}.json",
                mime="application/json",
                use_container_width=True,
            )

        with col_retry:
            if st.button("🔄 Retake Assessment", use_container_width=True):
                st.session_state.page    = "intro"
                st.session_state.answers = {}
                st.session_state.name    = ""
                st.rerun()


if __name__ == "__main__":
    main()
