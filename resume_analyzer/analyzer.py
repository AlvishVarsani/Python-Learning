from llm_client import stream_llm_response
from config import DEFAULT_TEMPERATURE, DEFAULT_TOP_P, DEFAULT_MAX_TOKENS, GROQ_MODEL

def generate_resume_analysis_prompt(resume_text: str) -> str:
    """Constructs the prompt for resume analysis."""
    return """
SYSTEM ROLE:
You are a Senior Technical Recruiter, Talent Acquisition Partner, ATS Specialist, and Hiring Manager.

Your task is to analyze resumes exactly as a recruiter would during an initial screening process.

Focus on:

* ATS friendliness
* Candidate suitability
* Technical skills
* Experience relevance
* Achievement quality
* Resume formatting
* Hiring risks
* Interview recommendation

IMPORTANT RULES:

1. Return ONLY valid JSON.
2. Do not return markdown.
3. Do not return tables.
4. Do not include explanations outside JSON.
5. Be objective and recruiter-focused.
6. Use concise recruiter language.
7. Scores must be integers.

Analyze the resume and return the following JSON structure:

{
"candidate_summary": {
"name": "",
"current_role": "",
"experience_years": "",
"industry": "",
"seniority_level": "",
"summary": ""
},

"ats_assessment": {
"ats_score": 0,
"formatting_score": 0,
"keyword_match_score": 0,
"readability_score": 0,
"ats_issues": []
},

"skills": {
"technical_skills": [],
"frameworks": [],
"tools": [],
"cloud_platforms": [],
"databases": [],
"soft_skills": []
},

"strengths": [
"",
"",
""
],

"weaknesses": [
"",
"",
""
],

"missing_elements": [
"",
"",
""
],

"recruiter_assessment": {
"job_readiness": "",
"career_progression": "",
"leadership_evidence": "",
"achievement_quality": "",
"interview_recommendation": "Strong Yes | Yes | Maybe | No",
"hiring_risk_level": "Low | Medium | High"
},

"improvement_suggestions": [
"",
"",
"",
""
],

"red_flags": [
""
],

"overall_score": 0,

"final_verdict": ""
}

Resume:
""" + resume_text


def analyze_resume_stream(resume_text: str, temperature: float = DEFAULT_TEMPERATURE, top_p: float = DEFAULT_TOP_P, max_tokens: int = DEFAULT_MAX_TOKENS, model: str = GROQ_MODEL):
    """
    Analyzes a resume by streaming the results from the LLM.
    """
    prompt = generate_resume_analysis_prompt(resume_text)
    
    # Yield the chunks as they come from the llm_client
    for chunk in stream_llm_response(
        prompt=prompt, 
        model=model, 
        temperature=temperature, 
        top_p=top_p, 
        max_tokens=max_tokens
    ):
        yield chunk
