# PM-AI: Agentic AI Workflow for Product Managers

## 🤖 Problem Statement
Automate core responsibilities of a Product Manager (PM) using a multi-agent system, covering:
- Talent acquisition  
- Roadmap planning  
- Progress tracking  
- Go-to-market (GTM) strategy  
- Sales & feedback loop  

## 🛠️ Tech Stack
- **LangGraph** for agentic orchestration  
- **LangChain** for LLM tools and chains  
- **OpenAI / Hugging Face LLMs** for intelligence  
- **Streamlit** frontend for interaction  
- **APIs**: Google Calendar, FAISS, Jira/Trello (mocked), Mailchimp, etc.  

## 🧭 Agent Flow
[Talent Acquisition] → [Roadmap Planning] ←⟲ Feedback Loop ⟲← [Sales & Feedback]
↓
[Progress Monitoring]
↓
[GTM Strategy]
↓
[Sales & Feedback]


## 🧠 Agents Description

### 1. Talent Acquisition Agent
- **Input**: Job description, resume PDFs  
- **Output**: Ranked candidates + Interview schedule  
- **Tools**: Affinda parser, FAISS, Google Calendar API  

### 2. Roadmap Planning Agent
- **Input**: Feedback, competitor features, team capacity  
- **Output**: 3-month Kanban roadmap  

### 3. Progress Monitoring Agent
- **Input**: Jira/Trello task updates  
- **Output**: Status report, stakeholder email  

### 4. GTM Strategy Agent
- **Input**: Features + Personas  
- **Output**: Launch content + timing + campaign plan  

### 5. Sales & Feedback Agent
- **Input**: CRM data, reviews  
- **Output**: Sales trends + product improvement loop  

## 🧬 LLMs Used
- GPT-4 (OpenAI)  
- Mistral 7B (Hugging Face fallback)  

## 👤 Participant
- **Name**: Kidhir Hussain  
- **Track**: Hackathon – Real-time Agentic AI Application  

## ⚙️ How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
📁 Repository Structure

├── agents/
├── state.py
├── graph.py
├── app.py
├── README.md
├── requirements.txt
├── .env
├── diagram.png
📝 Notes

.env required with OPENAI_API_KEY or Hugging Face token
No commits after 5:30 PM (as per hackathon rules)
Public repository required
🎥 Demo

Link to Loom/YT video or attach demo.mp4 here