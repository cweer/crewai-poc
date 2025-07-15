#!/usr/bin/env python3
"""
Simple demo using CrewAI's built-in models
"""

from crewai import Agent, Task, Crew

def simple_demo():
    """Simple demo without custom LLM configuration"""
    print("="*60)
    print("        CrewAI POC - Simple Demo")
    print("="*60)
    
    # Create agents with default LLM
    answering_agent = Agent(
        role="Expert Knowledge Assistant",
        goal="Provide comprehensive, accurate, and well-structured answers to user questions",
        backstory="You are a highly knowledgeable assistant with expertise across multiple domains.",
        verbose=True,
        allow_delegation=False
    )
    
    evaluation_agent = Agent(
        role="Quality Assessment Specialist", 
        goal="Evaluate the quality, accuracy, and completeness of answers",
        backstory="You are a meticulous quality assessor responsible for evaluating answers.",
        verbose=True,
        allow_delegation=False
    )
    
    # Test question
    test_question = "What is artificial intelligence?"
    print(f"\n💭 Test Question: {test_question}")
    
    # Create answer task
    answer_task = Task(
        description=f"Answer the following question comprehensively: {test_question}",
        expected_output="A comprehensive, well-structured answer",
        agent=answering_agent
    )
    
    # Create crew for answering
    answer_crew = Crew(
        agents=[answering_agent],
        tasks=[answer_task],
        verbose=True
    )
    
    print("\n🔄 Getting answer...")
    try:
        answer_result = answer_crew.kickoff()
        answer = str(answer_result)
        
        print(f"\n🤖 ANSWER:\n{answer}")
        
        # Create evaluation task
        eval_task = Task(
            description=f"Evaluate this answer to '{test_question}': {answer}. Provide a score 1-10 and detailed feedback.",
            expected_output="A detailed evaluation with score and feedback",
            agent=evaluation_agent
        )
        
        # Create crew for evaluation
        eval_crew = Crew(
            agents=[evaluation_agent],
            tasks=[eval_task],
            verbose=True
        )
        
        print("\n🔄 Getting evaluation...")
        evaluation_result = eval_crew.kickoff()
        evaluation = str(evaluation_result)
        
        print(f"\n📊 EVALUATION:\n{evaluation}")
        
        print("\n" + "="*60)
        print("✅ Demo completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Note: This demo requires an OpenAI API key or other LLM configuration")

if __name__ == "__main__":
    simple_demo()