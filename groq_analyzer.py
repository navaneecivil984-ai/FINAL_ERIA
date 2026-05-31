from groq import Groq

client = Groq(
    api_key="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"
)

def get_summary(text):

    prompt = f"""
    Analyze this education regulation and provide:

    1. Easy Summary
    2. Purpose
    3. Stakeholders Affected
    4. Student Impact
    5. Faculty Impact
    6. Institution Impact
    7. Short-Term Impact
    8. Medium-Term Impact
    9. Long-Term Impact
    10. Risks
    11. Opportunities

    Regulation:

    {text[:12000]}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content