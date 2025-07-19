# Multi-Agent-LLMs

**main.ipynb** is the main file in this repository. It uses [LangGraph](https://github.com/langchain-ai/langgraph) and [dspy](https://github.com/stanfordnlp/dspy) to implement the multi-agent design described in [this document](https://docs.google.com/document/d/1wwL_FRew2MBR-DfGUJVBlPyg4wzm60Z6Cy2qcvWn__Q/edit?usp=sharing).

The system takes a list of symptoms as input and outputs the top K most likely rare diseases.

---

## Future Scope

1. **Support more input sources** (e.g., HPO, Genome Testing, etc.)
2. **Integrate Retrieval-Augmented Generation (RAG)** and utilize public databases to identify diseases more efficiently and reduce hallucinations.
3. **Enable multimodal input** (e.g., images, lab results) and process them effectively.
4. **Create a fresh dataset** to prevent data leakage and improve model robustness.
5. **Leverage a vector database** to provide more structured outputs, including references for each disease and detailed explanations.
