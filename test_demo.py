#!/usr/bin/env python3
"""
Simple test script to demonstrate CrewAI POC functionality
"""

import sys
import os
from pathlib import Path

# Add the src directory to the path
sys.path.append(str(Path(__file__).parent / "src"))

from crews.qa_crew import QACrew

def demo_test():
    """Demo test with a simple question"""
    print("="*60)
    print("        CrewAI POC - Demo Test")
    print("="*60)
    
    # Check if API key is configured
    if not os.getenv('ANTHROPIC_API_KEY'):
        print("⚠️  Error: ANTHROPIC_API_KEY not found in environment variables.")
        return
    
    print("\n🚀 Initializing CrewAI agents...")
    
    try:
        qa_crew = QACrew()
        print("✅ Agents initialized successfully!")
        
        # Test question
        test_question = "What is artificial intelligence?"
        print(f"\n💭 Test Question: {test_question}")
        print("\n🔄 Processing question...")
        print("This may take a moment as agents work together...")
        
        # Process the question
        results = qa_crew.process_question(test_question)
        
        # Display results
        print("\n" + "="*60)
        print("RESULTS:")
        print("="*60)
        print(f"\n📝 QUESTION:\n{results['question']}")
        print(f"\n🤖 ANSWER:\n{results['answer']}")
        print(f"\n📊 EVALUATION:\n{results['evaluation']}")
        print("\n" + "="*60)
        print("✅ Demo completed successfully!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    demo_test()