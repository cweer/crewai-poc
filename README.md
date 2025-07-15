# CrewAI POC - Question & Answer System

A simple proof-of-concept application demonstrating CrewAI's agent collaboration capabilities. This application features two agents working together: one to answer questions and another to evaluate the quality of those answers.

## Features

- **Answering Agent**: Provides comprehensive answers to user questions
- **Evaluation Agent**: Assesses answer quality, accuracy, and completeness
- **Interactive CLI**: Simple command-line interface for asking questions
- **YAML Configuration**: Maintainable agent and task definitions

## Setup

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure API key**:
   - Copy `.env` file and add your OpenAI API key:
   ```bash
   OPENAI_API_KEY=your_openai_api_key_here
   ```

3. **Run the application**:
   ```bash
   python src/main.py
   ```

## Usage

1. Start the application
2. Enter your question when prompted
3. Wait for the answering agent to process your question
4. Review the evaluation agent's assessment of the answer
5. Type 'quit' to exit

## Project Structure

```
crewai-poc/
├── src/
│   ├── crews/
│   │   └── qa_crew.py          # Main crew logic
│   └── main.py                 # CLI interface
├── config/
│   ├── agents.yaml             # Agent configurations
│   └── tasks.yaml              # Task definitions
├── requirements.txt            # Dependencies
├── .env                        # Environment variables
└── README.md                   # This file
```

## Example Interaction

```
💭 Enter your question: What is machine learning?

🤖 ANSWER:
   Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed...

📊 EVALUATION:
   Overall Quality Score: 8/10
   - Accuracy: Excellent - technically correct information
   - Completeness: Good - covers key concepts and examples
   - Clarity: Very good - well-structured and easy to follow
   - Usefulness: High - provides practical understanding
```

## Customization

- Modify agent roles and backstories in `config/agents.yaml`
- Adjust task descriptions and requirements in `config/tasks.yaml`
- Extend functionality in `src/crews/qa_crew.py`