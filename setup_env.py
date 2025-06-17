#!/usr/bin/env python3
"""
Troubleshooting script for environment setup
"""

import subprocess
from pathlib import Path


def check_environment():
    """Check and fix environment setup"""

    print("🔍 Diagnosing environment setup...")
    print()

    # 1. Check if we're in project directory
    if not Path("pyproject.toml").exists():
        print("❌ Not in project directory (no pyproject.toml found)")
        return False

    print("✅ Found pyproject.toml")

    # 2. Check Poetry
    try:
        result = subprocess.run(["poetry", "--version"], capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ Poetry available: {result.stdout.strip()}")
        else:
            print("❌ Poetry not working")
            return False
    except FileNotFoundError:
        print("❌ Poetry not installed")
        return False

    # 3. Install dependencies
    print("\n📦 Installing dependencies...")
    try:
        result = subprocess.run(["poetry", "install"], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
        else:
            print("❌ Failed to install dependencies:")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Error during installation: {e}")
        return False

    # 4. Test Ruff
    print("\n🔧 Testing Ruff...")
    try:
        result = subprocess.run(
            ["poetry", "run", "ruff", "--version"], capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ Ruff working: {result.stdout.strip()}")
        else:
            print("❌ Ruff not working")
            return False
    except Exception as e:
        print(f"❌ Error testing Ruff: {e}")
        return False

    # 5. Test MyPy
    print("\n🔧 Testing MyPy...")
    try:
        result = subprocess.run(
            ["poetry", "run", "mypy", "--version"], capture_output=True, text=True
        )
        if result.returncode == 0:
            print(f"✅ MyPy working: {result.stdout.strip()}")
        else:
            print("❌ MyPy not working")
            return False
    except Exception as e:
        print(f"❌ Error testing MyPy: {e}")
        return False

    # 6. Quick Ruff format
    print("\n🧹 Auto-formatting code...")
    try:
        subprocess.run(
            ["poetry", "run", "ruff", "format", "."], capture_output=True, text=True
        )
        print("✅ Code formatted")
    except Exception as e:
        print(f"⚠️  Could not format: {e}")

    # 7. Quick Ruff fix
    print("\n🧹 Auto-fixing Ruff issues...")
    try:
        subprocess.run(
            ["poetry", "run", "ruff", "check", ".", "--fix"],
            capture_output=True,
            text=True,
        )
        print("✅ Auto-fixes applied")
    except Exception as e:
        print(f"⚠️  Could not auto-fix: {e}")

    print("\n🎉 Environment setup complete!")
    print("\n🚀 Now try: poetry run ci")

    return True


if __name__ == "__main__":
    if check_environment():
        print("\n✅ All checks passed!")
    else:
        print("\n❌ Some checks failed - fix issues above and try again")
