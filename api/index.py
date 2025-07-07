# Vercel serverless function entry point
import sys
import os
from pathlib import Path

# Add the backend directory to path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

# Import the FastAPI app
from server import app

# Export the app for Vercel
handler = app