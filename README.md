# LangChainPractice

Implementing LangChain agents

## Overview

This repo is a hands-on exploration of [LangChain](https://www.langchain.com/), demonstrating how to:

- Configure and call OpenAI LLMs
- Build prompt templates and chains
- Wire up a simple Streamlit front-end
- Create agents that can use external tools (Wikipedia, calculator, search)

Everything is illustrated step-by-step in `main.ipynb`, with reusable helper code in `langchain_helper.py` and a little Streamlit app in `app.py`.

## Prerequisites

- Python 3.8+
- An OpenAI API key (set in a `.env` file as `OPENAI_API_KEY`)
- `pip install -r requirements.txt`

## Installation

```bash
git clone https://github.com/maghaeef/LangChainPractice.git
cd LangChainPractice
pip install -r requirements.txt
```

## Usage

1. **Notebook demo**  
   Launch and run the walkthrough in `main.ipynb` (Jupyter or VSCode).

2. **Streamlit app**  
   ```bash
   streamlit run app.py
   ```
   Pick a cuisine in the sidebar and watch LangChain generate a restaurant name + menu.

## Lessons Learned

1. **Environment setup & key management**  
   - Use `python-dotenv` to load your OpenAI key securely.

2. **Direct LLM calls**  
   - Call `llm = OpenAI(temperature=0.6)` and then `llm(prompt)` for quick testing.

3. **Prompt templating**  
   - Define reusable prompts via `PromptTemplate`, e.g.  
     ```python
     tmpl = PromptTemplate(
       input_variables=["cuisine"],
       template="Suggest a fancy name for a {cuisine} restaurant."
     )
     ```

4. **LLMChain**  
   - Wrap an LLM + prompt into a chain (`LLMChain`) for clear separation of concerns.

5. **Sequential chains**  
   - **SimpleSequentialChain** for chaining outputs into inputs.  
   - **SequentialChain** when you need to manage multiple inputs/outputs explicitly.

6. **Building a Streamlit front-end**  
   - Expose your chain via a minimal `app.py`—allowing users to pick options in a sidebar.

7. **Agents & tools**  
   - Initialize agents with `initialize_agent` and `load_tools` to give your LLM:
     - **Wikipedia** lookup
     - **Calculator** (`llm-math`)
     - (Optionally) **Google search** via `google-search-results`
   - Use `AgentType.ZERO_SHOT_REACT_DESCRIPTION` for zero-shot reasoning and tool use.

8. **Verbose reasoning & observability**  
   - Run agents in verbose mode to see “thought → action → observation” traces for debugging.

## File Structure

```
.
├── .gitignore
├── main.ipynb          ← step-by-step exploration
├── langchain_helper.py ← helper functions & chains
├── app.py              ← Streamlit demo
└── requirements.txt    ← dependencies
```

---

Happy chaining! 🚀  