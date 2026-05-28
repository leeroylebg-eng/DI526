# DISC Personality Assessment App 👤

A modern DISC personality assessment app built with **Streamlit** and **Python** for generating personalized DISC profiles.

## Features

- **Personalized DISC profiles** — Discover your unique personality style based on the DISC framework
- **Interactive UI** — Powered by Streamlit for easy navigation and a user-friendly experience
- **Radar & Bar charts** — Visual representation of your DISC profile
- **Style descriptions** — Detailed descriptions of single and combination styles
- **PDF and JSON Export** — Download your results as a PDF or JSON for future reference

## DISC Framework

| Style | Name | Description |
|-------|------|-------------|
| 🔴 **D** | Dominance | Direct, decisive, results-oriented |
| 🟡 **I** | Influence | Enthusiastic, optimistic, collaborative |
| 🟢 **S** | Steadiness | Patient, reliable, supportive |
| 🔵 **C** | Conscientiousness | Analytical, accurate, systematic |

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
git clone https://github.com/leeroylebg-eng/DI526.git
cd DI526/test/disc-personality-assessment
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run disc_style.py
```

The app opens automatically in your browser at `http://localhost:8501`.

## Usage

1. Enter your name (optional)
2. Answer 20 statements on a 1–5 scale
3. View your DISC profile with radar chart and bar chart
4. Read your primary and combination style descriptions
5. Download results as PDF or JSON

## Project Structure

```
disc-personality-assessment/
├── disc_style.py       # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## License

MIT License — see [LICENSE](LICENSE) for details.
