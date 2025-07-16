import yaml
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv
import os

load_dotenv()

class QACrew:
    """Question-Answer Crew for processing questions and evaluating answers"""
    
    def __init__(self):
        self.agents_config = self._load_config('config/agents.yaml')
        self.tasks_config = self._load_config('config/tasks.yaml')
        # Configure LLM with Anthropic using the current model
        self.llm = "claude-3-5-sonnet-20241022"
        
    def _load_config(self, config_path):
        """Load configuration from YAML file"""
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    
    def answering_agent(self):
        """Create the answering agent"""
        config = self.agents_config['answering_agent']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
        )
    
    def evaluation_agent(self):
        """Create the evaluation agent"""
        config = self.agents_config['evaluation_agent']
        return Agent(
            role=config['role'],
            goal=config['goal'],
            backstory=config['backstory'],
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
        )
    
    def answer_question_task(self, question):
        """Create task for answering a question"""
        config = self.tasks_config['answer_question_task']
        return Task(
            description=config['description'].format(question=question),
            expected_output=config['expected_output'],
            agent=self.answering_agent(),
        )
    
    def evaluate_answer_task(self, question, answer):
        """Create task for evaluating an answer"""
        config = self.tasks_config['evaluate_answer_task']
        return Task(
            description=config['description'].format(question=question, answer=answer),
            expected_output=config['expected_output'],
            agent=self.evaluation_agent(),
        )
    
    def process_question(self, question):
        """Process a question through the Q&A workflow"""
        # Create agents
        answering_agent = self.answering_agent()
        evaluation_agent = self.evaluation_agent()
        
        # Create initial task for answering
        answer_task = self.answer_question_task(question)
        
        # Create crew for answering
        answer_crew = Crew(
            agents=[answering_agent],
            tasks=[answer_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Get the answer
        answer_result = answer_crew.kickoff()
        answer = str(answer_result)
        
        # Create evaluation task
        eval_task = self.evaluate_answer_task(question, answer)
        
        # Create crew for evaluation
        eval_crew = Crew(
            agents=[evaluation_agent],
            tasks=[eval_task],
            process=Process.sequential,
            verbose=True
        )
        
        # Get the evaluation
        evaluation_result = eval_crew.kickoff()
        evaluation = str(evaluation_result)
        
        return {
            'question': question,
            'answer': answer,
            'evaluation': evaluation
        }