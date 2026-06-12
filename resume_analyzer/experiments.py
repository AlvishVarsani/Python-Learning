import sys
from analyzer import analyze_resume_stream

def run_max_tokens_experiment(resume_text: str):
    """
    Tests the difference between max_tokens=500 and max_tokens=3000.
    """
    print("\n" + "="*50)
    print("EXPERIMENT: max_tokens = 500")
    print("Expectation: The output will be truncated midway.")
    print("="*50)
    
    try:
        for chunk in analyze_resume_stream(resume_text, max_tokens=500):
            print(chunk, end="", flush=True)
    except Exception as e:
        print(f"\nError: {e}")
        
    print("\n\n" + "="*50)
    print("EXPERIMENT: max_tokens = 3000")
    print("Expectation: The output should be complete.")
    print("="*50)
    
    try:
        for chunk in analyze_resume_stream(resume_text, max_tokens=3000):
            print(chunk, end="", flush=True)
    except Exception as e:
        print(f"\nError: {e}")
    
    print("\n")

def run_temperature_experiment(resume_text: str):
    """
    Tests the difference between temperature=0.1 and temperature=1.0.
    """
    print("\n" + "="*50)
    print("EXPERIMENT: temperature = 0.1")
    print("Expectation: The output will be highly deterministic, focused, and potentially repetitive or less creative.")
    print("="*50)
    
    try:
        for chunk in analyze_resume_stream(resume_text, temperature=0.1, max_tokens=3000):
            print(chunk, end="", flush=True)
    except Exception as e:
        print(f"\nError: {e}")
        
    print("\n\n" + "="*50)
    print("EXPERIMENT: temperature = 1.0")
    print("Expectation: The output will be more creative, varied, but potentially less coherent if too high.")
    print("="*50)
    
    try:
        for chunk in analyze_resume_stream(resume_text, temperature=1.0, max_tokens=3000):
            print(chunk, end="", flush=True)
    except Exception as e:
        print(f"\nError: {e}")
        
    print("\n")
