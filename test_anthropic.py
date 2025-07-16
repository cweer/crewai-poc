#!/usr/bin/env python3
"""
Test Anthropic API directly to diagnose the issue
"""

import os
from dotenv import load_dotenv
import anthropic

load_dotenv()

def test_anthropic_direct():
    """Test Anthropic API directly"""
    api_key = os.getenv('ANTHROPIC_API_KEY')
    
    if not api_key:
        print("❌ No ANTHROPIC_API_KEY found")
        return
    
    print(f"🔑 API Key loaded: {api_key[:20]}...")
    
    try:
        client = anthropic.Anthropic(api_key=api_key)
        
        print("🔄 Testing API call...")
        message = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=100,
            messages=[
                {"role": "user", "content": "What is artificial intelligence? Answer briefly."}
            ]
        )
        
        print("✅ API call successful!")
        print(f"Response: {message.content[0].text}")
        
    except Exception as e:
        print(f"❌ Direct API test failed: {e}")
        print(f"Error type: {type(e).__name__}")

if __name__ == "__main__":
    test_anthropic_direct()