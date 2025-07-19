import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
PERPLEXITY_API_KEY = os.getenv("PERPLEXITY_API_KEY", "")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY", "")

# Agent Configuration
SPECIALIZED_AGENTS = ["geneticist", "radiologist", "clinician"]
MAX_ITERATIONS = 2
TOP_K_DISEASES = 3 