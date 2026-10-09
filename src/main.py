import logging
import os
from src.core.adapter import ResilienceAdapter
from src.ui.console import ResilienceConsole

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resilience.log"))
    ]
)
logger = logging.getLogger(__name__)

import customtkinter as ctk

def main():
    root = ctk.CTk()

    
    # Initialize Core Logic
    # We initialize it here, but connection happens on demand or via Health Check
    adapter = ResilienceAdapter()
    
    # Initialize UI
    app = ResilienceConsole(root, adapter)
    
    logger.info("Resilience Adapter Started")
    
    root.mainloop()

if __name__ == "__main__":
    main()
