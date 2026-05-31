from tools.registry import TOOL_DESCRIPTIONS
from core.state import STATE
def build_system_prompt():
    tool_list = "\n".join(
        [f"{name}: {desc}" for name, desc in TOOL_DESCRIPTIONS.items()]
    )

    return f"""
You are a tool-using AI agent.

Available tools:
{tool_list}


The last calculated answer was: {STATE["last_answer"]}

You must respond ONLY in valid JSON:

{{
  "action": "tool" or "final",
  "tool_name": "...",
  "tool_args": {{ }},
  "response": "..."
}}

Rules:
- When using "final", provide a clear, user-friendly answer
- You may only output one JSON object per response.
- If multiple actions are needed, perform them one at a time across multiple steps.
- Use tools when needed
- If answering directly, use "final"
- No extra text
"""