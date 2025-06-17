# scripts/cli.py
"""CLI commands for 4-in-a-row-game."""

import shutil
import subprocess
import sys
from pathlib import Path


def run():
    """Run the game."""
    subprocess.run([sys.executable, "-m", "four_in_a_row_game.main"], check=True)  # noqa: S603


def dev():
    """Start development mode with debug features."""
    print("Starting game in development mode...")
    subprocess.run(  # noqa: S603
        [sys.executable, "-m", "four_in_a_row_game.main", "--debug"], check=True
    )


def lint():
    """Run linting checks."""
    subprocess.run(["poetry", "run", "ruff", "check", "."], check=True)  # noqa: S603


def test():
    """Run tests with coverage."""
    subprocess.run(  # noqa: S603
        [
            "poetry",
            "run",
            "pytest",
            "--cov=src/four_in_a_row_game",
            "--cov-report=term-missing",
            "--cov-report=html",
        ],
        check=True,
    )


def ci():
    """Run full CI pipeline with smart coverage."""
    print("Running CI pipeline with smart coverage...")
    print("=" * 60)

    # Standard checks
    try:
        # Linting
        print("🔍 Running linting...")
        subprocess.run(["poetry", "run", "ruff", "check", "."], check=True)  # noqa: S603
        print("✅ Linting passed")
        print()

        # Formatting check
        print("📐 Checking formatting...")
        subprocess.run(["poetry", "run", "ruff", "format", "--check", "."], check=True)  # noqa: S603
        print("✅ Formatting check passed")
        print()

        # Type checking
        print("🔧 Running type checks...")
        subprocess.run(["poetry", "run", "mypy", "src/"], check=True)  # noqa: S603
        print("✅ Type checking passed")
        print()

    except subprocess.CalledProcessError as e:
        print("❌ CI pipeline failed at static analysis stage")
        print("   Command failed: {}".format(" ".join(e.cmd)))
        sys.exit(1)

    # Smart coverage analysis
    try:
        from scripts.coverage import SmartCoverageManager

        coverage_mgr = SmartCoverageManager(Path("."))

        # Run smart coverage (non-strict mode for development)
        success = coverage_mgr.run_smart_coverage_check(strict=False)

        if success:
            print("🎉 All CI checks passed with smart coverage!")
        else:
            print("❌ Smart coverage checks failed")
            print("💡 See output above for specific recommendations")
            sys.exit(1)

    except ImportError as e:
        print(f"⚠️  Warning: Could not import smart coverage system: {e}")
        print("🔄 Falling back to basic coverage check...")

        # Fallback to basic coverage
        try:
            subprocess.run(
                ["poetry", "run", "pytest", "--cov=src", "--cov-fail-under=60"],
                check=True,
            )  # noqa: S603
            print("✅ Basic coverage check passed")
        except subprocess.CalledProcessError:
            print("❌ Coverage check failed")
            sys.exit(1)

    except Exception as e:
        print(f"❌ Unexpected error in smart coverage system: {e}")
        print("🔄 Falling back to basic coverage check...")

        # Fallback to basic coverage
        try:
            subprocess.run(
                ["poetry", "run", "pytest", "--cov=src", "--cov-fail-under=60"],
                check=True,
            )  # noqa: S603
            print("✅ Basic coverage check passed")
        except subprocess.CalledProcessError:
            print("❌ Coverage check failed")
            sys.exit(1)


def format_code():
    """Format code using ruff."""
    subprocess.run(["poetry", "run", "ruff", "format", "."], check=True)  # noqa: S603
    subprocess.run(["poetry", "run", "ruff", "check", "--fix", "."], check=True)  # noqa: S603


def profile():
    """Run game with performance profiling."""
    print("Running game with performance profiling...")
    py_spy_available = shutil.which("py-spy")
    if py_spy_available:
        subprocess.run(  # noqa: S603
            [
                "py-spy",
                "record",
                "-o",
                "profile.svg",
                "--",
                sys.executable,
                "-m",
                "four_in_a_row_game.main",
            ],
            check=True,
        )
        print("Profile saved to profile.svg")
    else:
        print("py-spy not available. Install with: poetry add --group dev py-spy")


def memory_profile():
    """Run game with memory profiling."""
    print("Running game with memory profiling...")
    subprocess.run(  # noqa: S603
        [
            "poetry",
            "run",
            "python",
            "-m",
            "memory_profiler",
            "four_in_a_row_game/main.py",
        ],
        check=True,
    )


def smart_coverage():
    """Run smart coverage analysis with detailed report."""
    try:
        from scripts.coverage import SmartCoverageManager

        coverage_mgr = SmartCoverageManager(Path("."))
        success, report = coverage_mgr.run_coverage_with_report(strict=False)

        # Save report to file
        report_file = Path("coverage_report.json")
        import json

        with open(report_file, "w") as f:
            json.dump(report, f, indent=2)

        print("\n📊 Detailed report saved to: {}".format(report_file))

        if not success:
            sys.exit(1)

    except ImportError:
        print("❌ Smart coverage system not available")
        sys.exit(1)


def coverage_trend():
    """Show coverage trend analysis."""
    try:
        from scripts.coverage import CoverageRatchet

        ratchet = CoverageRatchet(Path("."))
        ratchet.print_coverage_summary()

        trend_info = ratchet.get_coverage_trend(days=10)
        print("\n📈 Coverage Trend (last 10 runs):")
        print(f"   Status: {trend_info['trend'].title()}")
        if trend_info["trend"] != "insufficient_data":
            print(f"   Change: {trend_info['change']:+.1f}%")
            print(
                f"   Range: {trend_info['first_coverage']:.1f}% → {trend_info['last_coverage']:.1f}%"
            )

    except ImportError:
        print("❌ Smart coverage system not available")
        sys.exit(1)


def diff_coverage():
    """Check coverage for changed files only."""
    try:
        from scripts.coverage import DifferentialCoverage

        diff_cov = DifferentialCoverage(Path("."))
        success = diff_cov.check_new_code_coverage(min_coverage=90)

        if not success:
            sys.exit(1)

    except ImportError:
        print("❌ Smart coverage system not available")
        sys.exit(1)


def clean():
    """Clean build artifacts and cache files."""
    patterns = [
        "**/__pycache__",
        "**/*.pyc",
        "**/*.pyo",
        ".pytest_cache",
        ".mypy_cache",
        ".ruff_cache",
        "htmlcov",
        "dist",
        "build",
        "*.egg-info",
        # Game-specific cleanup
        "*.log",
        "save_*.json",  # Game save files
        "profile.svg",  # Performance profiles
    ]

    root = Path()
    for pattern in patterns:
        for path in root.glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"Removed directory: {path}")
            else:
                path.unlink()
                print(f"Removed file: {path}")

    print("🧹 Cleanup completed!")


# For Poetry script compatibility
def main():
    """Default main function."""
    run()
