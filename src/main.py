#!/usr/bin/env python3
"""
CrewAI POC - Question & Answer with Evaluation
A simple demonstration of CrewAI agents working together
"""

import sys
import os
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent))

from crews.qa_crew import QACrew


def print_header():
    """Print application header"""
    print("="*60)
    print("        CrewAI POC - Question & Answer System")
    print("="*60)
    print()


def print_separator():
    """Print a separator line"""
    print("\n" + "-"*60 + "\n")


def display_results(results):
    """Display the results in a formatted way"""
    print("📝 QUESTION:")
    print(f"   {results['question']}")
    print_separator()
    
    print("🤖 ANSWER:")
    print(f"   {results['answer']}")
    print_separator()
    
    print("📊 EVALUATION:")
    print(f"   {results['evaluation']}")
    print_separator()


def main():
    """Main application entry point"""
    print_header()
    
    # Check if API key is configured
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("⚠️  Warning: ANTHROPIC_API_KEY not found in environment variables.")
        print("Please set your API key in the .env file or environment.")
        print("Example: ANTHROPIC_API_KEY=your_api_key_here")
        return
    
    # Initialize the QA crew
    print("🚀 Initializing CrewAI agents...")
    try:
        qa_crew = QACrew()
        print("✅ Agents initialized successfully!")
        print_separator()
    except Exception as e:
        print(f"❌ Error initializing agents: {e}")
        return
    
    # Interactive loop
    while True:
        try:
            # Get user input
            question = input("💭 Enter your question (or 'quit' to exit): ").strip()
            
            if question.lower() in ['quit', 'exit', 'q']:
                print("\n👋 Thanks for using CrewAI POC!")
                break
                
            if not question:
                print("Please enter a valid question.")
                continue
            
            print(f"\n🔄 Processing your question...")
            print("This may take a moment as agents work together...")
            
            # Process the question
            results = qa_crew.process_question(question)
            
            # Display results
            print_separator()
            display_results(results)
            
        except KeyboardInterrupt:
            print("\n\n👋 Thanks for using CrewAI POC!")
            break
        except Exception as e:
            print(f"\n❌ Error processing question: {e}")
            print("Please try again with a different question.")


if __name__ == "__main__":
    main()