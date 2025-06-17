"""Comprehensive smart coverage management combining multiple strategies."""

from pathlib import Path
from typing import Dict, Any, Tuple

from .progressive_coverage import ProgressiveCoverage
from .differential_coverage import DifferentialCoverage
from .contextual_coverage import ContextualCoverage
from .coverage_ratchet import CoverageRatchet


class SmartCoverageManager:
    """Combines multiple coverage strategies for optimal results."""

    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.progressive = ProgressiveCoverage(project_root)
        self.differential = DifferentialCoverage(project_root)
        self.contextual = ContextualCoverage(project_root)
        self.ratchet = CoverageRatchet(project_root)

    def run_smart_coverage_check(self, strict: bool = False) -> bool:
        """
        Multi-strategy coverage validation.

        Args:
            strict: If True, all checks must pass. If False, allows some flexibility.
        """

        print("🎯 Running smart coverage analysis...")
        print("=" * 60)

        results = {
            "ratchet": False,
            "differential": False,
            "contextual": False,
            "progressive": False,
        }

        # 1. Coverage summary and trend analysis
        print("📊 Coverage Overview:")
        self.ratchet.print_coverage_summary()
        print()

        # 2. Check that we don't regress (ratcheting)
        print("🔒 Ratcheting Check (prevent regression):")
        results["ratchet"] = self.ratchet.check_coverage_ratchet(tolerance=2.0)
        if not results["ratchet"]:
            print("   ❌ Coverage regression detected")
        print()

        # 3. Ensure new code has high coverage (differential)
        print("🎯 Differential Coverage (new/changed code):")
        results["differential"] = self.differential.check_new_code_coverage(
            min_coverage=85
        )
        print()

        # 4. Apply context-aware rules to different file types
        print("📂 Contextual Coverage (by file type):")
        (
            contextual_passed,
            contextual_results,
        ) = self.contextual.check_contextual_coverage()
        results["contextual"] = contextual_passed

        if contextual_results:
            self._print_contextual_summary(contextual_results)
        print()

        # 5. Check overall progressive target
        print("📈 Progressive Coverage (sprint-based target):")
        sprint_target = self.progressive.get_required_coverage()
        current_metrics = self.ratchet.get_current_coverage()
        current_overall = current_metrics.get("total_coverage", 0.0)

        if current_overall >= sprint_target:
            print(f"✅ Overall target met: {current_overall:.1f}% ≥ {sprint_target}%")
            results["progressive"] = True
        else:
            print(
                f"⚠️  Overall target not met: {current_overall:.1f}% < {sprint_target}%"
            )
            results["progressive"] = False
        print()

        # 6. Final assessment
        return self._assess_final_result(results, strict)

    def _print_contextual_summary(self, contextual_results: Dict[str, Dict]):
        """Print a summary of contextual coverage results."""
        passed_categories = []
        failed_categories = []

        for category, result in contextual_results.items():
            if result["passed"]:
                passed_categories.append(f"{category} ({result['coverage']:.1f}%)")
            else:
                failed_categories.append(
                    f"{category} ({result['coverage']:.1f}% < {result['required']}%)"
                )

        if passed_categories:
            print(f"   ✅ Passed: {', '.join(passed_categories)}")
        if failed_categories:
            print(f"   ❌ Failed: {', '.join(failed_categories)}")

    def _assess_final_result(self, results: Dict[str, bool], strict: bool) -> bool:
        """Assess the final result based on all coverage checks."""

        print("🏁 Final Assessment:")
        print("-" * 40)

        # Print individual results
        status_emoji = {True: "✅", False: "❌"}
        print(f"   {status_emoji[results['ratchet']]} Ratcheting (no regression)")
        print(f"   {status_emoji[results['differential']]} Differential (new code)")
        print(f"   {status_emoji[results['contextual']]} Contextual (by file type)")
        print(f"   {status_emoji[results['progressive']]} Progressive (sprint target)")

        # Determine overall result
        critical_checks = ["ratchet", "differential"]
        important_checks = ["contextual"]

        # Critical checks must always pass
        critical_passed = all(results[check] for check in critical_checks)

        if strict:
            # In strict mode, everything must pass
            overall_passed = all(results.values())
            if overall_passed:
                print("\n🎉 All coverage checks passed! (Strict mode)")
            else:
                print(
                    "\n❌ Some coverage checks failed (Strict mode requires all to pass)"
                )
        else:
            # In flexible mode, prioritize critical checks
            if critical_passed:
                important_passed = all(results[check] for check in important_checks)

                if important_passed:
                    print("\n🎉 All critical and important coverage checks passed!")
                    if not results["progressive"]:
                        print(
                            "💡 Sprint target not met, but this is acceptable during development"
                        )
                else:
                    print(
                        "\n⚠️  Critical checks passed, but some important checks failed"
                    )
                    print("🔧 Consider improving test coverage for specific file types")

                overall_passed = True
            else:
                print("\n❌ Critical coverage checks failed")
                print("🚨 Must fix coverage regression or add tests for new code")
                overall_passed = False

        print("-" * 40)
        return overall_passed

    def generate_coverage_report(self) -> Dict[str, Any]:
        """Generate a comprehensive coverage report."""

        # Run all checks and collect results
        ratchet_passed = self.ratchet.check_coverage_ratchet(tolerance=2.0)
        differential_passed = self.differential.check_new_code_coverage(min_coverage=85)
        (
            contextual_passed,
            contextual_results,
        ) = self.contextual.check_contextual_coverage()

        current_metrics = self.ratchet.get_current_coverage()
        sprint_target = self.progressive.get_required_coverage()
        trend_info = self.ratchet.get_coverage_trend()

        report = {
            "timestamp": self.ratchet.get_current_coverage().get(
                "timestamp", "unknown"
            ),
            "overall_coverage": current_metrics.get("total_coverage", 0.0),
            "sprint_target": sprint_target,
            "checks": {
                "ratchet": ratchet_passed,
                "differential": differential_passed,
                "contextual": contextual_passed,
                "progressive": current_metrics.get("total_coverage", 0.0)
                >= sprint_target,
            },
            "contextual_details": contextual_results,
            "trend": trend_info,
            "metrics": current_metrics,
        }

        return report

    def run_coverage_with_report(
        self, strict: bool = False
    ) -> Tuple[bool, Dict[str, Any]]:
        """Run coverage checks and return both result and detailed report."""
        success = self.run_smart_coverage_check(strict=strict)
        report = self.generate_coverage_report()
        return success, report
