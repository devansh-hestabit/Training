import json
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime

MEMORY_FILE = Path("src/memory/memory.json")
MEMORY_FILE.parent.mkdir(parents=True, exist_ok=True)

def load_memory() -> Dict[str, List[dict]]:
    if not MEMORY_FILE.exists():
        return {}
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_memory(memory: Dict[str, List[dict]]) -> None:
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f, indent=2)


def _session_key(session_id: str, mode: Optional[str]) -> str:
    return f"{session_id}::{mode}" if mode else session_id

def get_conversation(
    session_id: str,
    mode: Optional[str] = None,
    max_turns: int = 5
) -> List[dict]:
    memory = load_memory()
    key = _session_key(session_id, mode)
    convo = memory.get(key, [])
    return convo[-(max_turns * 2):]

def add_message(
    session_id: str,
    role: str,
    content: str,
    mode: Optional[str] = None
) -> None:
    memory = load_memory()
    key = _session_key(session_id, mode)

    memory.setdefault(key, []).append({
        "role": role,
        "content": content,
        "timestamp": datetime.now().strftime("%H:%M:%S")
    })

    save_memory(memory)

def clear_conversation(session_id: str, mode: Optional[str] = None) -> None:
    memory = load_memory()
    key = _session_key(session_id, mode)

    if key in memory:
        del memory[key]
        save_memory(memory)