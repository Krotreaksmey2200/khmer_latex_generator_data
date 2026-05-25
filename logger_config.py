import logging
import os
from pathlib import Path

# Ensure logs directory exists
Path("logs").mkdir(exist_ok=True)

logging.basicConfig(
    filename="logs/error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
