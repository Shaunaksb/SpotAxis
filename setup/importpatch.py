import os
from pathlib import Path

def patch_imports(base_dir):
    for pyfile in Path(base_dir).rglob("*.py"):
        try:
            with open(pyfile, encoding="utf-8") as f:
                code = f.read()
            replaced = code.replace(
                "from django.utils.encoding import smart_text",
                "from django.utils.encoding import smart_str as smart_text"
            )
            if replaced != code:
                with open(pyfile, "w", encoding="utf-8") as f:
                    f.write(replaced)
                print(f"Patched file: {pyfile}")
        except Exception as e:
            print(f"Error patching {pyfile}: {e}")

if __name__ == "__main__":
    import sys
    path = sys.argv[1] if len(sys.argv) > 1 else ".venv/lib"
    patch_imports(path)
