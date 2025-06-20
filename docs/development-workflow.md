# Development Workflow Guide

## 🎯 Command Usage by Development Phase

### **Sprint 0: Project Setup**
```bash
# After initial project generation
poetry install
poetry run validate-infrastructure  # ✅ REQUIRED

# Expected: 🎉 Sprint 0 Infrastructure: COMPLETE
```
**Purpose**: Verify development environment is properly configured  
**Run**: Once at project start  
**Duration**: ~30 seconds

---

### **Development Phase: Sprint 1+**
```bash
# Quick checks during development (use frequently)
poetry run lint     # ⚡ Style checking (~10s)
poetry run test     # ⚡ Run tests (~45s) 
poetry run format   # ⚡ Auto-format (~5s)

# Before commits and sprint completion (comprehensive)
poetry run ci       # 🔬 Full validation (~3min)
```

---

## 📋 When to Use Each Command

| Command | Sprint 0 | During Dev | Sprint End | Pre-Commit |
|---------|----------|------------|------------|------------|
| `validate-infrastructure` | ✅ Required | ❌ No | ❌ No | ❌ No |
| `lint` | ❌ No | ✅ Frequent | ❌ No | ❌ No |
| `test` | ❌ No | ✅ Frequent | ❌ No | ❌ No |
| `format` | ❌ No | ✅ Frequent | ❌ No | ❌ No |
| `ci` | ❌ No | ⚠️ Optional | ✅ Required | ✅ Required |

---

## 🔄 Git Workflow Integration

### **Before Every Commit**
```bash
# Comprehensive validation before staging
poetry run ci

# If CI passes ✅
git add .
git commit -m "feat: implement feature"

# If CI fails ❌ 
# Fix issues, then retry ci before committing
```

### **Sprint Completion**
```bash
# End of each sprint (1, 2, 3, etc.)
poetry run ci

# Expected: 🎉 All CI checks passed!
# Status: Ready for next sprint
```

---

## ⚡ Command Performance Guide

**Use the right tool for the job:**

```bash
# ⚡ Quick (during development)
poetry run format   # ~5s  - Auto-fix formatting
poetry run lint     # ~10s - Check style only
poetry run test     # ~45s - Run tests

# 🔬 Comprehensive (before commits)  
poetry run ci       # ~3m  - Full quality gates
```

---

## 🚨 Important Guidelines

### **DO Use**
- ✅ `validate-infrastructure` at Sprint 0 completion
- ✅ `lint`, `test`, `format` during development
- ✅ `ci` before every commit
- ✅ `ci` at end of every sprint

### **DON'T Use**
- ❌ `validate-infrastructure` during development (unnecessary)
- ❌ `ci` for quick checks (too slow for frequent use)
- ❌ Committing without running `ci` first

---

## 🎮 IDE Integration

### **VS Code Tasks** (recommended)
Add to `.vscode/tasks.json`:
```json
{
    "tasks": [
        {
            "label": "Quick Test",
            "type": "shell", 
            "command": "poetry run test",
            "group": "test"
        },
        {
            "label": "Pre-Commit Check",
            "type": "shell",
            "command": "poetry run ci", 
            "group": "build"
        }
    ]
}
```

### **Pre-commit Hooks**
The project includes pre-commit hooks that automatically run `poetry run ci` before commits.

---

## 🏆 Benefits

### **Developer Experience**
- ✅ **Fast feedback** during development
- ✅ **Comprehensive validation** when needed
- ✅ **Clear expectations** for each phase

### **Code Quality**  
- ✅ **Consistent standards** across all commits
- ✅ **Early issue detection** before merge
- ✅ **Technical debt prevention**

### **Team Collaboration**
- ✅ **Standardized workflow** for all developers
- ✅ **Reliable builds** and predictable quality
- ✅ **Reduced merge conflicts** from quality issues

---

## 🔧 Troubleshooting

### **If `validate-infrastructure` Fails**
1. Run `poetry install` to ensure dependencies
2. Check you're in the project root directory
3. Verify Poetry is properly installed

### **If `ci` Fails**
1. Run individual commands to identify issue:
   - `poetry run lint` (style issues)
   - `poetry run test` (test failures)
   - Check coverage requirements
2. Fix issues then retry `poetry run ci`

### **If Tests Are Slow**
- Use `poetry run test` for development
- Use `poetry run ci` only when comprehensive validation needed
- Consider using test markers for faster subset testing

---

**Remember**: The goal is **fast feedback during development** and **comprehensive validation before commits**! 🚀
