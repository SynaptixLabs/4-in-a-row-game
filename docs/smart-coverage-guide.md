# Smart Coverage System User Guide

## 🎯 Overview

The smart coverage system provides intelligent, context-aware test coverage management that adapts to your project's development phase and specific needs.

## 🚀 Quick Start

### Basic Usage
```bash
# Run CI with smart coverage (recommended)
poetry run ci

# Run detailed smart coverage analysis
poetry run smart-coverage

# Check coverage trend over time  
poetry run coverage-trend

# Check coverage for changed files only
poetry run diff-coverage
```

### Traditional Commands (still available)
```bash
# Basic coverage check
poetry run test

# Format and lint
poetry run format
poetry run lint
```

## 📊 Smart Coverage Features

### 1. Progressive Coverage (Sprint-Based)
Adjusts coverage requirements based on project maturity:

- **Sprint 0** (Infrastructure): 50% coverage required
- **Sprint 1** (Core Logic): 65% coverage required  
- **Sprint 2** (Feature Complete): 75% coverage required
- **Sprint 3** (Production Ready): 85% coverage required
- **Sprint 4+** (Optimization): 90% coverage required

### 2. Differential Coverage (New Code Focus)
- **New/Modified files**: 85-90% coverage required
- **Existing files**: Lower thresholds allowed during development
- **Git integration**: Automatically detects changed files

### 3. Context-Aware Coverage (File Type Rules)
Different coverage requirements based on code importance:

- **Core Logic** (`*/core/*`, `*/game/*`): 95% coverage
- **API Layer** (`*/api/*`): 85% coverage
- **Configuration** (`*/config/*`): 75% coverage
- **UI Layer** (`*/ui/*`): 70% coverage
- **Utilities** (`*/utils/*`): 60% coverage
- **Scripts** (`scripts/*`): 40% coverage
- **Experimental** (`*/experimental/*`): 20% coverage

### 4. Coverage Ratcheting (Prevent Regression)
- **Tracks coverage history** over time
- **Prevents significant decreases** (>2% tolerance)
- **Shows coverage trends** and improvements
- **Baseline protection** for established code

## 🛠 Command Details

### `poetry run ci`
**Full CI pipeline with smart coverage**
- Runs linting, formatting, type checking
- Executes smart coverage analysis
- **Non-strict mode**: Prioritizes critical checks
- **Fallback**: Uses basic coverage if smart system fails

### `poetry run smart-coverage`
**Detailed smart coverage analysis**
- Runs all coverage strategies
- Generates detailed JSON report (`coverage_report.json`)
- Shows file-by-file analysis
- Provides specific recommendations

### `poetry run coverage-trend`
**Coverage trend analysis**
- Shows current coverage metrics
- Displays trend over last 10 runs
- Indicates improving/declining/stable status
- Historical comparison data

### `poetry run diff-coverage`
**Differential coverage check**
- **High standard for new code** (90% coverage)
- Identifies files without tests
- Git-aware change detection
- Perfect for code reviews

## 📈 Understanding Output

### Coverage Check Results
```
🎯 Running smart coverage analysis...
============================================================

📊 Coverage Overview:
   Current: 67.3%
   Statements: 235
   Missing: 77
   Trend: 📈 Improving (+2.1%)

🔒 Ratcheting Check (prevent regression):
✅ Coverage maintained: 67.3% (+0.5%) - within tolerance

🎯 Differential Coverage (new/changed code):
📄 src/game/logic.py
✅ Differential coverage passed: 90%+ achieved for new code

📂 Contextual Coverage (by file type):
   ✅ Passed: config (100%), core_logic (85%)
   ❌ Failed: utilities (45% < 60%)

📈 Progressive Coverage (sprint-based target):
✅ Overall target met: 67.3% ≥ 65%

🏁 Final Assessment:
   ✅ Ratcheting (no regression)
   ✅ Differential (new code)
   ❌ Contextual (by file type)
   ✅ Progressive (sprint target)

🎉 All critical and important coverage checks passed!
```

### Status Indicators
- ✅ **Passed**: Check successful
- ❌ **Failed**: Check failed, action needed
- ⚠️ **Warning**: Issue noted but not blocking
- 💡 **Suggestion**: Improvement recommendation

## 🔧 Configuration

### Sprint Detection
The system automatically detects current sprint from `docs/state.md`:
```markdown
## ✅ Sprint 0: Environment Setup (COMPLETE)
## 🔄 Sprint 1: Core Logic (IN PROGRESS)
```

### Custom Coverage Rules
Edit coverage rules in `scripts/coverage/contextual_coverage.py`:
```python
COVERAGE_RULES = {
    "your_category": {
        "patterns": ["*/your_pattern/*"],
        "min_coverage": 80,
        "description": "Your code category"
    }
}
```

### Coverage History
- Stored in `.coverage_history.json` (local file)
- Tracks last 50 coverage runs
- Used for trend analysis and ratcheting
- Automatically managed by the system

## 🎯 Best Practices

### For Development
1. **Run `poetry run ci`** before committing
2. **Focus on new code quality** - differential coverage
3. **Check trends regularly** - `poetry run coverage-trend`
4. **Don't obsess over total percentage** during development

### For Code Reviews
1. **Use `poetry run diff-coverage`** to check PR changes
2. **Require 90%+ coverage** for new/modified files
3. **Allow existing code** to have lower coverage temporarily
4. **Focus on critical business logic** coverage

### For Production
1. **Enable strict mode** for production deployments
2. **Target 85%+ overall coverage** for mature projects
3. **Monitor coverage trends** over time
4. **Establish coverage baselines** for different modules

## 🔍 Troubleshooting

### "Smart coverage system not available"
```bash
# Check if coverage files exist
ls scripts/coverage/

# Try fallback
poetry run test
```

### Coverage seems incorrect
```bash
# Clear coverage cache
poetry run clean
rm -f .coverage* coverage.json

# Run fresh analysis
poetry run smart-coverage
```

### Git-related errors in differential coverage
```bash
# Ensure you're in a git repository
git status

# Check for remote branches
git remote -v
```

### Import errors
```bash
# Ensure proper Python path
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# Check virtual environment
poetry env info
```

## 📝 Integration with CI/CD

### GitHub Actions Example
```yaml
- name: Run Smart Coverage
  run: |
    poetry install
    poetry run ci
    
- name: Upload Coverage Report
  uses: actions/upload-artifact@v3
  with:
    name: coverage-report
    path: coverage_report.json
```

### Pre-commit Hook
```yaml
# .pre-commit-config.yaml
repos:
  - repo: local
    hooks:
      - id: smart-coverage
        name: Smart Coverage Check
        entry: poetry run diff-coverage
        language: system
        pass_filenames: false
```

This smart coverage system ensures your tests **help development** rather than **hinder progress** while maintaining high quality standards! 🚀
