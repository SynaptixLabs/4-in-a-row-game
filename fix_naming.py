#!/usr/bin/env python3
"""
Quick fix script for 4-in-a-row-game project naming issues
"""

import shutil
from pathlib import Path


def fix_project_naming():
    """Fix the naming issues in the current project"""

    print("🔧 Fixing project naming issues...")

    # 1. Rename source directory from 4_in_a_row_game to four_in_a_row_game
    old_src = Path("src/4_in_a_row_game")
    new_src = Path("src/four_in_a_row_game")

    if old_src.exists():
        print(f"📁 Renaming {old_src} → {new_src}")
        shutil.move(str(old_src), str(new_src))

    # 2. Remove duplicate template directory
    template_dir = Path("template")
    if template_dir.exists():
        print("🗑️ Removing duplicate template directory")
        shutil.rmtree(template_dir)

    # 3. Update all import statements in Python files
    python_files = []

    # Find all Python files
    for pattern in ["**/*.py"]:
        python_files.extend(Path().glob(pattern))

    # Update imports
    for py_file in python_files:
        if py_file.name == "fix_naming.py":  # Skip this script
            continue

        try:
            content = py_file.read_text(encoding="utf-8")

            # Replace module references
            old_imports = [
                "from src.4_in_a_row_game",
                "import src.4_in_a_row_game",
                "from 4_in_a_row_game",
                "import 4_in_a_row_game",
            ]

            new_imports = [
                "from src.four_in_a_row_game",
                "import src.four_in_a_row_game",
                "from four_in_a_row_game",
                "import four_in_a_row_game",
            ]

            updated = False
            for old, new in zip(old_imports, new_imports, strict=False):
                if old in content:
                    content = content.replace(old, new)
                    updated = True

            if updated:
                py_file.write_text(content, encoding="utf-8")
                print(f"📝 Updated imports in {py_file}")

        except Exception as e:
            print(f"⚠️ Could not update {py_file}: {e}")

    # 4. Update pyproject.toml
    pyproject = Path("pyproject.toml")
    if pyproject.exists():
        try:
            content = pyproject.read_text()
            content = content.replace("4_in_a_row_game", "four_in_a_row_game")
            content = content.replace("4-in-a-row-game", "four-in-a-row-game")
            pyproject.write_text(content)
            print("📝 Updated pyproject.toml")
        except Exception as e:
            print(f"⚠️ Could not update pyproject.toml: {e}")

    # 5. Auto-fix Ruff issues
    print("🧹 Auto-fixing code quality issues...")
    try:
        import subprocess

        result = subprocess.run(
            ["poetry", "run", "ruff", "format", "."], capture_output=True, text=True
        )
        if result.returncode == 0:
            print("✅ Ruff formatting applied")

        result = subprocess.run(
            ["poetry", "run", "ruff", "check", ".", "--fix"],
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ Ruff auto-fixes applied")

    except Exception as e:
        print(f"⚠️ Could not run auto-fixes: {e}")

    print("\n🎉 Project naming fixed!")
    print("\nNext steps:")
    print("1. Run: poetry run ci")
    print("2. If successful, update state.md")
    print("3. Begin Sprint 1 development")


if __name__ == "__main__":
    fix_project_naming()
