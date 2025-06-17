#!/usr/bin/env python3
"""Test script to verify smart coverage system functionality."""

import sys
from pathlib import Path


def test_smart_coverage_import():
    """Test that smart coverage modules can be imported."""
    try:
        # Import all modules to test availability
        import scripts.coverage  # noqa: F401

        print("✅ All smart coverage modules imported successfully")
        return True

    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False


def test_smart_coverage_basic_functionality():
    """Test basic functionality of smart coverage system."""
    try:
        from scripts.coverage import SmartCoverageManager

        # Initialize the manager
        project_root = Path(".")
        manager = SmartCoverageManager(project_root)

        print("✅ SmartCoverageManager initialized successfully")

        # Test individual components
        progressive = manager.progressive
        sprint = progressive.get_current_sprint()
        threshold = progressive.get_required_coverage()

        print(f"✅ Progressive coverage: Sprint {sprint}, Threshold {threshold}%")

        # Test differential coverage
        differential = manager.differential
        changed_files = differential.get_changed_files()

        print(f"✅ Differential coverage: {len(changed_files)} changed files detected")

        # Test contextual coverage
        contextual = manager.contextual
        python_files = contextual.get_python_files()

        print(f"✅ Contextual coverage: {len(python_files)} Python files found")

        # Test ratchet
        ratchet = manager.ratchet
        trend_info = ratchet.get_coverage_trend()

        print(f"✅ Coverage ratchet: Trend status - {trend_info['trend']}")

        return True

    except Exception as e:
        print(f"❌ Functionality test error: {e}")
        return False


def test_cli_commands():
    """Test that CLI commands are properly configured."""
    import subprocess

    commands_to_test = [
        [
            "poetry",
            "run",
            "python",
            "-c",
            "from scripts.cli import smart_coverage; print('smart_coverage imported')",
        ],
        [
            "poetry",
            "run",
            "python",
            "-c",
            "from scripts.cli import coverage_trend; print('coverage_trend imported')",
        ],
        [
            "poetry",
            "run",
            "python",
            "-c",
            "from scripts.cli import diff_coverage; print('diff_coverage imported')",
        ],
    ]

    for cmd in commands_to_test:
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                print(f"✅ CLI command test passed: {cmd[-1]}")
            else:
                print(f"❌ CLI command test failed: {cmd[-1]}")
                print(f"   Error: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ CLI command test error: {e}")
            return False

    return True


def main():
    """Run all smart coverage tests."""
    print("🧪 Testing Smart Coverage System")
    print("=" * 50)

    tests = [
        ("Import Tests", test_smart_coverage_import),
        ("Functionality Tests", test_smart_coverage_basic_functionality),
        ("CLI Command Tests", test_cli_commands),
    ]

    all_passed = True

    for test_name, test_func in tests:
        print(f"\n📋 Running {test_name}...")
        if test_func():
            print(f"✅ {test_name} passed")
        else:
            print(f"❌ {test_name} failed")
            all_passed = False

    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 All smart coverage tests passed!")
        print("\n💡 Try running:")
        print("   poetry run smart-coverage")
        print("   poetry run coverage-trend")
        print("   poetry run ci")
    else:
        print("❌ Some smart coverage tests failed")
        print("💡 Check the error messages above for details")
        sys.exit(1)


if __name__ == "__main__":
    main()
