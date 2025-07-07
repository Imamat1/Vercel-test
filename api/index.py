# Vercel serverless function entry point
import sys
import os
from pathlib import Path

# Add current directory to path for local imports
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

# Add the backend directory to path
backend_path = current_dir.parent / "backend"
sys.path.insert(0, str(backend_path))

# Import the FastAPI app
from server import app

# Export the app for Vercel
handler = app