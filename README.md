# 4-in-a-row-game

Board game

Built with **pygame** and modern Python tooling for production-ready game development.

## 🚀 Quick Start

### Generated Project Setup
This project was generated using the enhanced Python game development template. To begin development:

1. **Open in Windsurf IDE**
   ```bash
   cd 4-in-a-row-game
   windsurf .
   ```

2. **Execute Start-Coding Script**
   
   Use this simple prompt in Windsurf to begin:
   
   ```
   I just generated this 4-in-a-row-game project. Please run/execute the start-coding script in .commands/start-coding.md
   ```
   
   Windsurf will:
   - Execute comprehensive project initialization
   - Configure development environment and quality gates
   - Setup infrastructure with all dependencies
   - Prepare structured development workflow
   - Validate all components are working correctly

3. **Follow Structured Development**
   
   After initialization, continue with sprint-based development:
   ```
   I have completed initialization. Please help me begin Sprint 1 development from docs/TODO.4-in-a-row-game.1.md
   ```

## 📋 Command Scripts

The `.commands/` directory contains project initialization:

- `.commands/start-coding.md` - Complete project initialization and development continuation

The **`state.md`** file (root level) tracks project progress and enables session continuation:
- **Updated by Windsurf** after each sprint/milestone completion
- **Read by Windsurf** when returning to the project
- **Ensures continuity** across development sessions

This script provides Windsurf with specific, actionable instructions for setting up the development environment and maintaining project state.

## 🎮 4-In-A-Row-Game Game Project

### Technical Requirements
- **Framework**: pygame for graphics and input
- **Performance**: 60fps stable gameplay
- **Testing**: Comprehensive test suite with >85% coverage
- **Quality**: Modern Python tooling for production-ready development

## 📊 Sprint Development Plan

### Sprint 0: Infrastructure & Project Setup ✅
- Complete development environment with poetry and Python 3.12
- Quality gates (Ruff, MyPy, pytest >85% coverage)
- Game constants and settings configuration
- Git repository and CI/CD pipeline setup

### Sprint 1: Core Game Logic 🔄
- Game engine and core mechanics
- Player management and game state
- Rule implementation and validation
- Performance optimization

### Sprint 2: User Interface & Interaction 📋
- pygame rendering system
- Input handling (mouse/keyboard)
- Visual feedback and animations
- Game flow and user experience

### Sprint 3: Advanced Features & Polish 📋
- AI implementation (if applicable)
- Save/load functionality
- Sound effects and visual polish
- Settings and customization options
## 🛠 Technology Stack

- **Python 3.12** - Latest stable Python with performance improvements
- **pygame** - Mature game framework for graphics and input handling
- **Poetry** - Modern dependency management with task aliases
- **Pydantic** - Data validation and settings management
- **Ruff + MyPy** - Fast linting, formatting, and type checking
- **Pytest** - Comprehensive testing with coverage tracking
- **GitHub Actions** - CI/CD pipeline with quality gates

## 📊 Development Workflow

### Sprint 0: Project Setup
```bash
# After project generation
poetry install
poetry run validate-infrastructure  # ✅ Required for Sprint 0 completion

# Expected: 🎉 Sprint 0 Infrastructure: COMPLETE
```

### Development (Sprint 1+): Daily Workflow
```bash
# Quick checks during development
poetry run test             # ⚡ Quick testing (~45s)
poetry run lint             # ⚡ Quick linting (~10s)
poetry run format           # ⚡ Auto-format code (~5s)

# Start development session
poetry run dev              # Start game in development mode
```

### Sprint End + Pre-Commit: Comprehensive Validation
```bash
# Before every commit and sprint completion
poetry run ci               # 🔬 Full quality gates (~3min)

# Expected: 🎉 All CI checks passed!
```

### Command Usage Guide
| Command | When | Purpose | Duration |
|---------|------|---------|----------|
| `validate-infrastructure` | Sprint 0 only | Environment setup | ~30s |
| `lint`, `test`, `format` | During development | Quick feedback | ~10-45s |
| `ci` | Pre-commit + Sprint end | Comprehensive validation | ~3min |

📖 **Full workflow guide**: See `docs/development-workflow.md`

## 🧪 Testing & Quality

### Test Structure
```
tests/
├── unit/           # Unit tests for individual components
├── integration/    # Integration tests for system interactions
├── performance/    # Performance and benchmarking tests
└── conftest.py     # Shared fixtures and test configuration
```

### Quality Gates
- **Ruff**: Linting and formatting (150x faster than traditional tools)
- **MyPy**: Static type checking with strict mode
- **Pytest**: Unit and integration testing with coverage >85%
- **Pre-commit**: Automated quality checks on commit
- **GitHub Actions**: CI/CD pipeline with security scanning

## 🎮 Game Architecture

### Core Components
- **Game Engine**: Main game loop and state management
- **Game Logic**: Rules, validation, and mechanics
- **Rendering System**: pygame graphics and animations
- **Input Handler**: User input processing and feedback
- **Configuration**: Settings and customization management

### Performance Standards
```python
# Performance targets
TARGET_FPS = 60
MAX_MEMORY_MB = 200
MAX_INPUT_LATENCY_MS = 16
MAX_STARTUP_TIME_S = 3
```

## 🔧 Configuration

### Environment Setup
Copy `.env.example` to `.env` and customize:

```bash
# Display Configuration
WINDOW_WIDTH=800
WINDOW_HEIGHT=600
FPS=60

# Development
DEBUG_MODE=true
SHOW_FPS=true
```

## 👥 Team Collaboration

### Windsurf Assistant Roles
- **Game_Architect**: Infrastructure, performance, CI/CD optimization
- **Game_Logic_Developer**: Core mechanics and rules implementation
- **Rendering_Developer**: pygame graphics, animations, visual effects
- **Input_Audio_Developer**: Controls, sound effects, user feedback
- **QA_Test_Engineer**: Testing, edge cases, performance validation

### Development Standards
- **Performance First**: Maintain 60fps during gameplay
- **Test-Driven**: Write tests for core logic and critical paths
- **Type Safety**: Full MyPy compliance for robust code
- **Quality Focus**: All development meets production standards

## 🚀 Performance Targets

- **Frame Rate**: Sustained 60fps during gameplay
- **Memory Usage**: <200MB for complete game
- **Input Latency**: <16ms response time
- **Startup Time**: <3 seconds from launch to playable

## 📄 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

1. **Clone & install**
   ```bash
   git clone https://github.com/<ORG>/<REPO>.git
   cd 4-in-a-row-game
   poetry install
   ```
2. **Daily quality gate** – run `poetry run ci` before every commit and PR.
3. **Commit style** – Conventional Commits (`feat:`, `fix:`, `docs:` …).
4. **Branch & PR flow**
   1. Create a feature branch (`git checkout -b feat/<ticket>`)
   2. Push branch and open a PR to `main`.
   3. CI (GitHub Actions) must pass before review can be merged.
5. **Windsurf automation** – use `.commands/start-coding.md` for initialization; Windsurf updates `state.md` after each milestone.
6. **Performance & coverage targets** – sustain 60 fps and maintain ≥85 % unit-test coverage.
7. Keep documentation current when architecture or workflow changes.

---

**Generated with**: Enhanced Python Game Development Template  
**Framework**: pygame 3.12  
**Quality**: Production-ready infrastructure with comprehensive testing  
**Performance**: Optimized for 60fps gameplay