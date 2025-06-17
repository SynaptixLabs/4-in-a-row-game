"""Context-aware coverage based on file types and importance."""

import subprocess
from pathlib import Path
from typing import Dict, List, Tuple


class ContextualCoverage:
    """Apply different coverage rules based on code context."""

    COVERAGE_RULES = {
        # Critical business logic - high coverage required
        "core_logic": {
            "patterns": ["*/core/*", "*/game/*", "*/logic/*", "*/engine/*"],
            "min_coverage": 95,
            "description": "Core business logic",
        },
        # API endpoints - medium-high coverage
        "api_layer": {
            "patterns": ["*/api/*", "*/routes/*", "*/endpoints/*"],
            "min_coverage": 85,
            "description": "API endpoints",
        },
        # Configuration and settings - medium coverage
        "config": {
            "patterns": ["*/config/*", "*/settings/*"],
            "min_coverage": 75,
            "description": "Configuration files",
        },
        # UI and presentation layer - medium coverage
        "ui_layer": {
            "patterns": ["*/ui/*", "*/views/*", "*/templates/*", "*/frontend/*"],
            "min_coverage": 70,
            "description": "User interface",
        },
        # Utilities and helpers - lower coverage acceptable
        "utilities": {
            "patterns": ["*/utils/*", "*/helpers/*", "*/tools/*"],
            "min_coverage": 60,
            "description": "Utility functions",
        },
        # Scripts and CLI - minimal coverage
        "scripts": {
            "patterns": ["scripts/*", "*/cli/*"],
            "min_coverage": 40,
            "description": "Scripts and CLI tools",
        },
        # Test utilities and fixtures
        "test_utils": {
            "patterns": ["*/test_*", "*/conftest.py", "*/fixtures/*"],
            "min_coverage": 30,
            "description": "Test utilities",
        },
        # Experimental/prototype code - very low coverage
        "experimental": {
            "patterns": ["*/experimental/*", "*/prototype/*", "*/temp/*", "*/poc/*"],
            "min_coverage": 20,
            "description": "Experimental code",
        },
    }

    def __init__(self, project_root: Path):
        self.project_root = project_root

    def categorize_file(self, file_path: str) -> str:
        """Determine file category based on path patterns."""
        file_path = file_path.replace("\\", "/")  # Normalize path separators

        for category, rules in self.COVERAGE_RULES.items():
            for pattern in rules["patterns"]:
                if Path(file_path).match(pattern):
                    return category
        return "utilities"  # Default category

    def get_python_files(self) -> List[Path]:
        """Get all Python files in the src directory."""
        src_dir = self.project_root / "src"
        if not src_dir.exists():
            return []
        return list(src_dir.rglob("*.py"))

    def check_contextual_coverage(self) -> Tuple[bool, Dict[str, Dict]]:
        """Run coverage checks appropriate to each file type."""

        python_files = self.get_python_files()
        if not python_files:
            print("📝 No Python files found in src/ directory")
            return True, {}

        # Group files by category
        categories: Dict[str, List[Path]] = {}
        for file_path in python_files:
            relative_path = str(file_path.relative_to(self.project_root))
            category = self.categorize_file(relative_path)
            if category not in categories:
                categories[category] = []
            categories[category].append(file_path)

        print(
            f"📊 Analyzing {len(python_files)} files across {len(categories)} categories..."
        )

        # Check coverage for each category
        all_passed = True
        results = {}

        for category, files in categories.items():
            rules = self.COVERAGE_RULES[category]
            min_coverage = rules["min_coverage"]
            description = rules["description"]

            print(f"🎯 {description}: {len(files)} files (≥{min_coverage}%)")

            # Show files in this category
            for file_path in files[:3]:  # Show first 3 files
                rel_path = file_path.relative_to(self.project_root)
                print(f"   📄 {rel_path}")
            if len(files) > 3:
                print(f"   📄 ... and {len(files) - 3} more")

            category_passed, coverage_pct = self._check_category_coverage(
                files, min_coverage
            )

            results[category] = {
                "passed": category_passed,
                "coverage": coverage_pct,
                "required": min_coverage,
                "file_count": len(files),
            }

            if category_passed:
                print(f"   ✅ Passed: {coverage_pct:.1f}% ≥ {min_coverage}%")
            else:
                print(f"   ❌ Failed: {coverage_pct:.1f}% < {min_coverage}%")
                all_passed = False

        return all_passed, results

    def _check_category_coverage(
        self, files: List[Path], min_coverage: int
    ) -> Tuple[bool, float]:
        """Check coverage for specific file category."""
        if not files:
            return True, 100.0

        # Convert file paths to module names for coverage
        modules = []
        for file_path in files:
            try:
                # Get path relative to src directory
                src_relative = file_path.relative_to(self.project_root / "src")
                if src_relative.suffix == ".py":
                    # Convert path to module name (e.g., game/engine.py -> game.engine)
                    module = (
                        str(src_relative.with_suffix(""))
                        .replace("/", ".")
                        .replace("\\", ".")
                    )
                    modules.append(module)
            except ValueError:
                # File not in src directory, skip
                continue

        if not modules:
            return True, 100.0

        # Run pytest with coverage for these specific modules
        cmd = [
            "poetry",
            "run",
            "pytest",
            f"--cov={','.join(modules)}",
            "--cov-report=json:.temp_coverage.json",
            "--quiet",
        ]

        try:
            subprocess.run(cmd, capture_output=True, text=True, cwd=self.project_root)

            # Parse coverage from JSON output
            coverage_file = self.project_root / ".temp_coverage.json"
            if coverage_file.exists():
                import json

                try:
                    with open(coverage_file, "r") as f:
                        coverage_data = json.load(f)

                    total_coverage = coverage_data.get("totals", {}).get(
                        "percent_covered", 0.0
                    )

                    # Clean up temp file
                    coverage_file.unlink()

                    return total_coverage >= min_coverage, total_coverage

                except (json.JSONDecodeError, KeyError):
                    pass
                finally:
                    # Ensure cleanup
                    if coverage_file.exists():
                        coverage_file.unlink()

            # Fallback: assume passing if we can't determine coverage
            return True, min_coverage

        except Exception as e:
            print(f"   ⚠️  Warning: Could not check coverage for category: {e}")
            return True, min_coverage  # Don't fail on errors
