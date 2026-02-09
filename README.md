# 🧠 **Multi-Agent RAG Intelligence Platform**  
*A collaborative AI engine for research intelligence, trend forecasting, narrative generation,  
and technical insight discovery.*

This project is a modular, end-to-end intelligence system powered by a network of specialized agents.  
Together, they ingest research papers, extract insights, analyze signals, build narratives, generate forecasts,  
and present everything through a clean and intuitive Streamlit interface.

A playground for experimentation.  
A foundation for real-world analytical tools.  
A step toward autonomous reasoning engines.

---

## ✨ **Key Features**

### 🔹 Multi-Agent Cognitive Architecture  
A coordinated ensemble of autonomous agents, each performing a distinct thinking role:

- **Retrieval Agent** – extracts relevant information from the vector store  
- **Trend Agent** – uncovers emerging signals & important shifts  
- **Velocity Agent** – measures acceleration & rate-of-change of trends  
- **Forecast Agent** – predicts future directions  
- **Narrative Agent** – converts analysis into human-like summaries  
- **Timeline Agent** – generates chronological intelligence flows  
- **Evaluator Agent** – scores quality, consistency & coherence  

Each agent works independently yet communicates through an orchestrated LangGraph-style pipeline.

---

## 📥 **Data Pipeline**

### **1. Ingestion**  
Fetches research papers, PDFs, and structured documents.

### **2. Preprocessing**  
Cleans, chunks, embeds metadata, normalizes content.

### **3. Vectorization**  
Documents are embedded and stored in **ChromaDB** (`chroma_db/`).

### **4. Multi-Agent Processing**  
Agents collaborate to generate:

- insights  
- narratives  
- trend convergence signals  
- velocity indicators  
- forecasts  
- timeline flows  
- complete research intelligence reports  

### **5. Interactive Streamlit Interface**  
Query the system, explore trends, or export full reports with a click.

---

## 🗂 **Project Structure**

```
multi-agent-rag-platform/
│
├── agents/               # Individual agent logic
├── app/                  # Streamlit UI
├── chroma_db/            # Local vector store
├── data_ingestion/       # Fetching & preprocessing scripts
├── graph/                # Multi-agent orchestration pipeline
├── prompts/              # Engineered prompts for each agent
├── utils/                # PDF export, citations, helpers
├── visuals/              # Trend and timeline visualizations
└── requirements.txt      # Dependencies
```

---

## 🚀 **Run Locally**

### **1. Create a virtual environment**
```bash
python -m venv venv
venv/Scripts/activate   # Windows
```

### **2. Install dependencies**
```bash
pip install -r requirements.txt
```

### **3. Start the Streamlit App**
```bash
streamlit run app/streamlit_app.py
```

Visit the app at:  
**http://localhost:8501**

---

## 📊 **Visual Intelligence**

The platform dynamically generates:

- trend charts  
- TRL (Technology Readiness Level) indicators  
- convergence graphs  
- velocity badges  
- timeline visualizations  

All are accessible directly in the Streamlit UI  
and can be exported as PDF reports.

---

## 🧰 **Technologies Used**

- Python  
- Streamlit  
- ChromaDB  
- LangChain / LangGraph  
- Matplotlib  
- PDF generation utilities  
- Custom multi-agent orchestration

---

## 🎯 **Purpose of This Project**

Built as a foundation for:

- research intelligence  
- technology monitoring  
- trend forecasting  
- narrative generation  
- automated analysis pipelines  
- multi-agent LLM experimentation  

A system that thinks, reasons, and tells the evolving story of technology.

---

## 📜 **License**

This project is open-source under the **MIT License**.  
See the `LICENSE` file for details.
