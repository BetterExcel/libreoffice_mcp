
PYTHONPATH=. python - <<'PY'
import src.main as m
for name, tool in sorted(m.mcp.tools.items()):
    print(f"- {name}: {(tool.__doc__ or '').strip()}")
PY
