import streamlit as st
from openai import OpenAI

# OpenAI client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# Page title
st.title("AI Prototype: Identity Governance Operating Model Advisor")

st.write("""
This prototype explores how AI can help organizations design and improve
Identity Governance operating models across enterprise ecosystems.
""")

# Organization inputs
st.subheader("Organization Governance Inputs")

organization_size = st.selectbox(
    "Organization Size",
    ["Small", "Medium", "Large Enterprise", "Global Enterprise"]
)

iam_maturity = st.selectbox(
    "IAM Maturity",
    ["Low", "Medium", "High"]
)

operating_model = st.selectbox(
    "Current Governance Model",
    ["Centralized", "Federated", "Hybrid"]
)

industry = st.selectbox(
    "Industry",
    ["Banking", "Healthcare", "Pharmaceutical", "Retail", "Technology", "Manufacturing"]
)

key_challenges = st.multiselect(
    "Key Governance Challenges",
    [
        "Fragmented ownership",
        "Role explosion",
        "Slow approvals",
        "Excessive privilege",
        "Lifecycle gaps",
        "Audit findings",
        "Shadow identities",
        "Policy inconsistency"
    ]
)

if st.button("Generate Governance Recommendations"):

    prompt = f"""
    You are an enterprise IAM transformation advisor.

    Analyze the following organization profile and recommend:

    - ownership structures
    - approval models
    - federated governance approach
    - SoD accountability model
    - platform accountability structure
    - lifecycle governance ownership
    - role mining governance recommendations

    Organization Details:
    - Organization Size: {organization_size}
    - IAM Maturity: {iam_maturity}
    - Current Governance Model: {operating_model}
    - Industry: {industry}
    - Key Challenges: {key_challenges}

    Provide:
    1. Executive Summary
    2. Recommended Operating Model
    3. Governance Structure
    4. Ownership Recommendations
    5. Transformation Priorities
    6. Risks to Address
    """

    with st.spinner("Generating AI governance recommendations..."):

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a senior IAM governance and operating model transformation expert."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        output = response.choices[0].message.content

        st.subheader("AI Governance Operating Model Recommendations")

        st.write(output)
