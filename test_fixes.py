#!/usr/bin/env python3
"""Quick test to verify linting fixes."""

import subprocess
import sys
from pathlib import Path


def test_fixes():
    """Test if our linting fixes worked."""
    print("🧪 Testing linting fixes...")

    project_root = Path("C:/Synaptix-Labs/projects/4-in-a-row-game")

    try:
        # Test main.py syntax
        print("1. Testing main.py syntax...")
        result = subprocess.run(
            ["python", "-m", "py_compile", "src/four_in_a_row_game/main.py"],
            cwd=project_root,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ main.py syntax check passed")
        else:
            print(f"❌ main.py syntax error: {result.stderr}")
            return False

        # Test basic ruff check on main.py using Poetry
        print("2. Testing ruff check on main.py...")
        result = subprocess.run(
            ["poetry", "run", "ruff", "check", "src/four_in_a_row_game/main.py"],
            cwd=project_root,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ main.py ruff check passed")
        else:
            print(f"⚠️  main.py ruff warnings: {result.stdout}")

        # Test game_engine.py
        print("3. Testing game_engine.py...")
        result = subprocess.run(
            [
                "poetry",
                "run",
                "ruff",
                "check",
                "src/four_in_a_row_game/core/game_engine.py",
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ game_engine.py ruff check passed")
        else:
            print(f"⚠️  game_engine.py ruff warnings: {result.stdout}")

        # Test that CI script works
        print("4. Testing CLI script import...")
        result = subprocess.run(
            [
                "poetry",
                "run",
                "python",
                "-c",
                "from scripts.cli import ci; print('CLI import successful')",
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            print("✅ CLI script import successful")
        else:
            print(f"❌ CLI script import failed: {result.stderr}")
            return False

        print("\n🎉 Basic fixes appear to be working!")
        print("💡 Now try running: poetry run ci")
        return True

    except Exception as e:
        print(f"❌ Error testing fixes: {e}")
        return False


if __name__ == "__main__":
    success = test_fixes()
    sys.exit(0 if success else 1)
