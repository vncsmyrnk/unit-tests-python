import sys
import os

# Get source files
calculator_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))

# Set files in path
sys.path.insert(0, calculator_dir)
