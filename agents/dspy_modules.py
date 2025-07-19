import dspy

AGENT_INSTRUCTIONS = {
    "handler": (
        "You are the Handler Agent. Your responsibilities are to:\n"
        "- Receive the user's input symptoms.\n"
        "- Summarize and contextualize them in clear medical language.\n"
        "- Retrieve similar historical cases (if any) and provide relevant insights.\n"
        "- Generate a structured initial output with potential personas for the specialized agents.\n"
        "- Do not speculate on diagnoses; your role is to prepare information for others.\n"
    ),

    "geneticist": (
        "You are a Geneticist specializing in rare hereditary and genetic disorders.\n"
        "- Analyze the provided symptoms from a genetic perspective.\n"
        "- Suggest possible rare genetic diseases (maximum 3), ranked by likelihood with confidence scores (0-1).\n"
        "- Briefly explain your reasoning for each suggestion.\n"
        "- If you are uncertain or require additional information, formulate clear and concise questions directed to other agents (e.g., Radiologist or Clinician).\n"
        "- Collaborate actively: use answers from others to refine your hypotheses in subsequent rounds.\n"
    ),

    "radiologist": (
        "You are a Radiologist specializing in interpreting imaging findings for rare diseases.\n"
        "- Analyze the symptoms from a radiological perspective and suggest up to 3 possible rare diseases associated with imaging findings.\n"
        "- Include a confidence score (0-1) and a short justification for each disease.\n"
        "- Ask targeted questions to other agents (e.g., Geneticist or Clinician) if imaging data is required or if more context is needed.\n"
        "- Your goal is to complement the team by identifying imaging patterns suggestive of rare conditions.\n"
    ),

    "clinician": (
        "You are a Clinician integrating information from all specialties to suggest a working diagnosis.\n"
        "- Analyze the symptoms holistically and propose up to 3 possible rare diseases, with confidence scores (0-1).\n"
        "- Clearly explain your reasoning based on clinical signs, symptoms, and the inputs from other agents.\n"
        "- If critical information is missing, ask clarifying questions to the Geneticist or Radiologist.\n"
        "- Act as the team lead for integrating insights into a coherent diagnostic picture.\n"
    )
}


def create_agent_response(agent_type, symptoms, context=""):
    instruction = AGENT_INSTRUCTIONS.get(agent_type, "")
    
    class AgentResponse(dspy.Signature):
        agent_type = dspy.InputField(desc="Type of agent")
        symptoms = dspy.InputField(desc="Patient symptoms")
        context = dspy.InputField(desc="Previous conversation")
        instruction = dspy.InputField(desc="Role-specific instruction for the agent")
        response = dspy.OutputField(desc="Agent's analysis and questions for other agents")
        confidence = dspy.OutputField(desc="Confidence score (0-1)")
        diseases = dspy.OutputField(desc="List of diseases")
        questions = dspy.OutputField(desc="Questions for other agents. In Key, Value format please specify to whom we are asking the question as the Key we can ask either (geneticist, radiologist or clinician)")

    predictor = dspy.Predict(AgentResponse)
    
    result = predictor(
        agent_type=agent_type, 
        symptoms=", ".join(symptoms),
        context=context if context else "No previous conversation",
        instruction=instruction
    )
    
    return {
        "agent_type": agent_type,
        "response": result.response,
        "confidence": result.confidence,
        "diseases": result.diseases,
        "questions": result.questions
    }

def agent_reply(agent_type, symptoms, question, context=""):
    instruction = AGENT_INSTRUCTIONS.get(agent_type, "")
    
    class AgentReply(dspy.Signature):
        agent_type = dspy.InputField(desc="Type of agent")
        symptoms = dspy.InputField(desc="Patient symptoms")
        question = dspy.InputField(desc="Question from another agent")
        context = dspy.InputField(desc="Previous conversation")
        instruction = dspy.InputField(desc="Role-specific instruction for the agent")
        reply = dspy.OutputField(desc="Agent's reply to the question")
        confidence = dspy.OutputField(desc="Confidence score (0-1)")
        diseases = dspy.OutputField(desc="Updated diseases list")
    
    predictor = dspy.Predict(AgentReply)
    
    result = predictor(
        agent_type=agent_type,
        symptoms=", ".join(symptoms),
        question=question,
        context=context if context else "No previous conversation",
        instruction=instruction
    )
    
    return {
        "agent_type": agent_type,
        "response": result.reply,
        "confidence": result.confidence,
        "diseases": result.diseases,
        "questions": []
    } 