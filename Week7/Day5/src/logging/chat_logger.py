import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Optional

LOG_FILE = Path("CHAT-LOGS.json")

def log_interaction(entry: Dict) -> None:
    logs = []

    if LOG_FILE.exists():
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except json.JSONDecodeError:
            logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=2)


def build_log_entry(
    *,
    session_id: str,
    mode: str,
    user_input: str,
    output: str,
    confidence: Optional[float] = None,
    faithfulness: Optional[float] = None,
    refined: Optional[bool] = None
) -> Dict:
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "session_id": session_id,
        "mode": mode,
        "input": user_input,
        "output": output,
        "confidence": confidence,
        "faithfulness": faithfulness,
        "refined": refined
    }