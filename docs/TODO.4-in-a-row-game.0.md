# 4-in-a-row-game - Sprint 0: Infrastructure & Project Setup

## Sprint Overview
**Duration:** 2 weeks  
**Focus:** Complete project infrastructure, development environment, and foundational architecture  
**Goal:** Production-ready development environment with all quality gates operational

> **Windsurf Note**: This TODO contains step-by-step implementation guidance. Execute tasks sequentially and verify each section before proceeding.

## 🎯 Sprint Goals & Success Criteria
- [ ] Complete project environment setup with Poetry and Python 3.12
- [ ] Establish automated quality gates (Ruff, MyPy, pytest, coverage >85%)
- [ ] Create and configure GitHub repository with CI/CD pipeline
- [ ] Setup team collaboration tools and development workflow
- [ ] Validate all infrastructure components work correctly
- [ ] Tag Sprint 0 completion and prepare Sprint 1 branch

## 📋 Implementation Tasks

### Phase 1: Environment & Dependencies Setup

#### Task 1.1: Initialize Development Environment
```bash
# Verify Python version
python --version  # Should show Python 3.12

# Navigate to project directory (if not already there)
cd 4-in-a-row-game

# Create and activate virtual environment
python -m venv venv

# Windows activation:
venv\Scripts\activate

# Unix/macOS activation:
# source venv/bin/activate

# Install Poetry (if not already installed)
curl -sSL https://install.python-poetry.org | python3 -
```

**Validation**: Run `poetry --version` to confirm Poetry is installed

#### Task 1.2: Install Dependencies and Configure Tools
```bash
# Install all dependencies (including dev dependencies)
poetry install

# Verify Poetry task aliases work
poetry run --help

# Test key aliases
poetry run lint    # Should run successfully (may show style issues to fix)
poetry run test    # Should discover and run tests
poetry run ci      # Should run full CI pipeline locally
```

**Validation**: All Poetry commands should execute without errors

#### Task 1.3: Configure Pre-commit Hooks
```bash
# Install pre-commit hooks
poetry run pre-commit install

# Test pre-commit hooks on all files
poetry run pre-commit run --all-files

# If there are auto-fixable issues, commit them
git add .
git commit -m "style: auto-fix pre-commit issues"
```

**Validation**: Pre-commit should run clean or only show auto-fixed issues

### Phase 2: Quality Gates & Testing Infrastructure

#### Task 2.1: Configure and Test Code Quality Tools
```bash
# Run Ruff linting (should pass clean)
poetry run ruff check .

# Run Ruff formatting check
poetry run ruff format --check .

# Fix any formatting issues
poetry run ruff format .

# Run MyPy type checking
poetry run mypy src/

# Address any type checking issues in the generated code
```

**Validation**: All quality tools should pass with zero violations

#### Task 2.2: Validate Testing Infrastructure
```bash
# Run all tests with verbose output
poetry run pytest -v

# Run tests with coverage reporting
poetry run pytest --cov=src --cov-report=term-missing

# Check that coverage is >85%
poetry run pytest --cov=src --cov-fail-under=85

# Run performance tests (if any)
poetry run pytest tests/ -m performance -v
```

**Validation**: All tests pass, coverage >85%, no performance regressions

#### Task 2.3: Validate Infrastructure Components
```bash
# Test settings loading
poetry run python -c "
from src.4_in_a_row_game.config import settings
print(f'✅ Settings loaded: {settings.game_title}')
print(f'✅ Window size: {settings.window_size}')
print(f'✅ Board size: {settings.board_size}')
"

# Test constants
poetry run python -c "
from src.4_in_a_row_game.core.constants import Colors, GameState
print(f'✅ Colors loaded: {Colors.PLAYER_1}')
print(f'✅ Game states: {list(GameState)}')
"

# Test exceptions
poetry run python -c "
from src.4_in_a_row_game.core.exceptions import InvalidMoveError
try:
    raise InvalidMoveError('Test exception')
except InvalidMoveError as e:
    print(f'✅ Exceptions working: {e}')
"
```

**Validation**: All infrastructure components load and work correctly

### Phase 3: Repository & CI/CD Setup

#### Task 3.1: Initialize Git Repository
```bash
# Initialize Git repository (if not already done)
git init

# Configure Git (replace with your details)
git config user.name "Avidor"
git config user.email "avidor@synaptixlabs.ai"

# Add all files
git add .

# Create initial commit
git commit -m "feat: initial project infrastructure setup

- Complete Sprint 0 infrastructure implementation
- Python 3.12 + pygame + Poetry stack
- Comprehensive testing with pytest and coverage >85%
- Code quality tools: Ruff, MyPy, pre-commit hooks
- Game settings, constants, and exceptions infrastructure
- Sprint-based development with 4 TODO files

Generated from enhanced template"
```

**Validation**: Git repository initialized with clean initial commit

#### Task 3.2: Create GitHub Repository
**Option A: Using GitHub CLI (recommended)**
```bash
# Create GitHub repository
gh repo create SynaptixLabs/4-in-a-row-game --public --description "Board game"

# Add remote and push
git remote add origin https://github.com/SynaptixLabs/4-in-a-row-game.git
git push -u origin main
```

**Option B: Manual GitHub Setup**
1. Go to https://github.com/SynaptixLabs/repositories/new
2. Repository name: `4-in-a-row-game`
3. Description: `Board game`
4. Make it public
5. Do NOT initialize with README (we already have one)
6. Create repository
7. Add remote and push:
```bash
git remote add origin https://github.com/SynaptixLabs/4-in-a-row-game.git
git push -u origin main
```

**Validation**: Repository created and initial code pushed to GitHub

#### Task 3.3: Validate CI/CD Pipeline
```bash
# Push code to trigger CI/CD pipeline
git push

# Check GitHub Actions tab to verify:
# 1. Pipeline runs automatically
# 2. All jobs pass (build-test, security-scan, quality-gates)
# 3. Coverage report is generated
# 4. No security vulnerabilities found
```

**Validation**: CI/CD pipeline runs successfully with all green checkmarks

### Phase 4: Environment Configuration

#### Task 4.1: Setup Environment Variables
```bash
# Copy environment template
cp .env.example .env

# Edit .env file for development
# Set DEBUG_MODE=true
# Customize game settings as desired:
# - WINDOW_WIDTH/HEIGHT for your development screen
# - FPS for your target performance
# - Colors for your preferred game theme
```

**Game-Specific Settings to Consider:**
- `BOARD_WIDTH=7` and `BOARD_HEIGHT=6` for classic Connect Four
- `CONNECT_LENGTH=4` for win condition
- `AI_DIFFICULTY=medium` for balanced gameplay
- `SHOW_FPS=true` for development performance monitoring

#### Task 4.2: Validate Game Settings
```bash
# Test settings with custom .env values
poetry run python -c "
from src.4_in_a_row_game.config import settings
print(f'Game: {settings.game_title}')
print(f'Board: {settings.board_width}x{settings.board_height}')
print(f'Window: {settings.window_width}x{settings.window_height}')
print(f'Debug mode: {settings.debug_mode}')
print('✅ All settings loaded correctly')
"
```

### Phase 5: Team Collaboration Setup

#### Task 5.1: Review Windsurf Configuration
- [ ] Review `.windsurfrules` for pygame development patterns
- [ ] Check `.windsurf_config.yaml` for team assistant roles:
  - Game_Architect (infrastructure, performance)
  - Game_Logic_Developer (core mechanics)
  - Rendering_Developer (pygame graphics)
  - Input_Audio_Developer (controls, sound)
  - AI_Player_Developer (AI opponents)
  - UI_Menu_Developer (interfaces, menus)
  - QA_Test_Engineer (testing, quality)
  - Game_Designer_Docs (documentation)

#### Task 5.2: Validate Development Workflow
```bash
# Run complete CI pipeline locally
poetry run ci

# Should execute:
# 1. Ruff linting and formatting checks
# 2. MyPy type checking
# 3. Pytest with coverage >85%
# 4. All infrastructure tests passing
```

**Validation**: Full CI pipeline passes locally matching GitHub Actions

### Phase 6: Documentation & Architecture

#### Task 6.1: Create Architecture Documentation
Create `docs/architecture.md`:
```markdown
# 4-in-a-row-game Architecture

## Overview
Connect Four game built with pygame following clean architecture principles.

## Layers
- **Presentation Layer**: pygame UI, rendering, animations
- **Game Logic Layer**: Board state, rules, win detection
- **Data Layer**: Settings, persistence, configuration
- **Infrastructure Layer**: Logging, errors, performance

## Key Components
- **Game Engine**: Main game loop, state management
- **Board**: 7x6 grid with piece placement logic
- **Players**: Human and AI player implementations
- **Renderer**: pygame graphics and animations
- **Input Handler**: Mouse/keyboard event processing

## Performance Targets
- 60fps sustained gameplay
- <200MB memory usage
- <3s startup time
```

#### Task 6.2: Document Technology Decisions
Create `docs/adr/0001-technology-stack.md`:
```markdown
# ADR-0001: Technology Stack Selection

## Status: Accepted

## Context
Building a Connect Four game requiring good performance and maintainability.

## Decision
- **Python 3.12**: Latest stable with performance improvements
- **pygame**: Mature game framework with strong community
- **Poetry**: Modern dependency management
- **Ruff + MyPy**: Fast, comprehensive code quality tools
- **Pytest**: Robust testing with coverage tracking

## Consequences
- Fast development with modern Python tooling
- Excellent debugging and profiling capabilities
- Strong type safety and code quality enforcement
- Easy deployment and distribution
```

### Phase 7: Performance & Monitoring

#### Task 7.1: Create Performance Baseline
```bash
# Create and run performance tests
mkdir -p tests/performance

# Run any existing performance tests
poetry run pytest tests/ -m performance -v

# Establish baseline metrics for:
# - Settings loading time (<100ms)
# - Constants access time (<1ms)
# - Module import time (<500ms)
```

#### Task 7.2: Setup Performance Monitoring
- [ ] Review game settings for performance impact
- [ ] Configure FPS monitoring (show_fps=true in development)
- [ ] Setup memory usage tracking for development
- [ ] Document performance targets in architecture docs

### Phase 8: Final Validation & Sprint Completion

#### Task 8.1: Complete System Validation
```bash
# Run full validation suite
echo "🧪 Running complete system validation..."

# 1. Code quality (must pass)
poetry run ruff check . && echo "✅ Ruff linting passed"
poetry run ruff format --check . && echo "✅ Ruff formatting passed"
poetry run mypy src/ && echo "✅ MyPy type checking passed"

# 2. Testing (must pass with >85% coverage)
poetry run pytest --cov=src --cov-fail-under=85 && echo "✅ Tests passed with adequate coverage"

# 3. Infrastructure components (must work)
poetry run python -c "
from src.4_in_a_row_game import settings, GameState, InvalidMoveError
print('✅ All infrastructure components imported successfully')
"

# 4. Pre-commit hooks (must pass)
poetry run pre-commit run --all-files && echo "✅ Pre-commit hooks passed"

echo "🎉 All validation checks passed!"
```

#### Task 8.2: Tag Sprint 0 Completion
```bash
# Tag Sprint 0 completion
git add .
git commit -m "feat: complete Sprint 0 infrastructure setup

✅ Development environment fully configured
✅ Quality gates enforced (>85% test coverage)  
✅ CI/CD pipeline operational
✅ All infrastructure tests passing
✅ Performance baseline established
✅ Team collaboration tools configured

Sprint 0 complete - ready for Sprint 1 development"

# Create Sprint 0 tag
git tag -a sprint-0 -m "Sprint 0: Infrastructure setup complete

Infrastructure achievements:
- Python 3.12 + pygame + Poetry environment
- Comprehensive testing with >85% coverage
- CI/CD pipeline with quality gates
- Game settings, constants, exceptions working
- Performance monitoring baseline
- Team collaboration configured

Ready for Sprint 1: Core Game Logic & Engine"

# Create Sprint 1 branch for next development phase
git checkout -b sprint-1

# Push everything to remote
git push origin main
git push origin --tags
git push -u origin sprint-1

echo "🚀 Sprint 0 complete! Ready to begin Sprint 1."
```

## ✅ Sprint 0 Definition of Done

### Infrastructure Requirements
- [ ] Python 3.12 environment with Poetry working
- [ ] All quality gates passing (Ruff, MyPy, pytest, coverage >85%)
- [ ] CI/CD pipeline operational with all checks green
- [ ] Git repository with proper branching strategy
- [ ] Pre-commit hooks configured and passing

### Code Quality Requirements  
- [ ] Zero linting violations (Ruff)
- [ ] Zero type checking errors (MyPy strict mode)
- [ ] All tests passing with >85% coverage
- [ ] Performance baseline established
- [ ] No security vulnerabilities detected

### Infrastructure Components Working
- [ ] Game settings loading from environment
- [ ] Constants and enums accessible
- [ ] Exception hierarchy functional
- [ ] Test fixtures and utilities operational
- [ ] Logging infrastructure configured

### Team Collaboration Ready
- [ ] Windsurf rules configured for pygame development
- [ ] Assistant roles defined and boundaries clear
- [ ] Development workflow documented
- [ ] Architecture decisions recorded (ADRs)

### Ready for Sprint 1
- [ ] Sprint 0 tagged and Sprint 1 branch created
- [ ] All infrastructure validated and working
- [ ] Development environment optimized for pygame
- [ ] Team ready to begin core game logic development

## 🚀 Next Steps After Sprint 0

1. **Begin Sprint 1**: Switch to `sprint-1` branch and review `docs/TODO.4-in-a-row-game.1.md`
2. **Start Core Development**: Implement game board, player management, and basic rules
3. **Maintain Quality**: Use `poetry run ci` before each commit
4. **Monitor Performance**: Track frame rate and memory usage during development

---

**Sprint 0 Success**: When all checkboxes are complete, you have a production-ready development environment optimized for pygame game development with comprehensive quality gates and team collaboration tools operational.