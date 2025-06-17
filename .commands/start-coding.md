# 4-in-a-row-game - Start Coding Script

## 🚀 Project Initialization & Development Continuation

**Purpose**: This script initializes the 4-in-a-row-game project for development and handles session continuation based on current project state.

---

## 📋 Initialization Process

### Step 1: Project State Assessment
```bash
# Check if this is initial setup or continuation
if [ -f "state.md" ]; then
    echo "🔄 Existing project detected - resuming from current state"
    # Read current state from state.md
else
    echo "🆕 New project initialization starting"
    # Create initial state.md
fi
```

### Step 2: Documentation & Structure Review
**Windsurf Task**: Please perform comprehensive project review:

1. **📁 Review Project Structure**:
   - Examine `src/4_in_a_row_game/` source code organization
   - Check `tests/` structure and existing test files
   - Validate `docs/` documentation completeness
   - Review `pyproject.toml` dependencies and scripts

2. **📚 Analyze Documentation**:
   - Read `README.md` for project overview and specifications
   - Review `docs/projectRoadmap.md` for development plan
   - Check `docs/techStack.md` for technical decisions
   - Examine all `docs/TODO.4-in-a-row-game.*.md` files for sprint planning
   3. **🎯 Project Type Assessment**:
   - **Project Type**: game-development
   - **Game Framework**: pygame
   - **Target**: Board game

### Step 3: TODO Files & Sprint Planning Assessment

**Windsurf Decision Point**: Examine the TODO files in `docs/`:

#### Scenario A: TODO Files Are Placeholders
If TODO files contain generic placeholders or incomplete specifications:

1. **📝 Collaborate with User to Create Detailed TODOs**:
   - **For board_game games**: Work with user to define specific game rules, mechanics, win conditions
   - **Example**: "Let's define the specific rules for 4-in-a-row-game. Is this a classic Connect Four (7x6 board, 4-in-a-row) or a variation?"
   - **Sprint 1**: Core logic and game mechanics specific to this game type
   - **Sprint 2**: User interface and pygame implementation  
   - **Sprint 3**: Advanced features (AI, save/load, polish)

2. **📋 Create Detailed Sprint Plans**:
   - Update each `docs/TODO.4-in-a-row-game.N.md` with specific, actionable tasks
   - Ensure tasks are relevant to Board game
   - Include acceptance criteria and technical specifications

#### Scenario B: TODO Files Are Complete
If TODO files contain detailed, project-specific tasks:

1. **📊 Summarize Project Plan**:
   - Review and summarize all 4 sprints
   - Highlight key milestones and deliverables
   - Confirm technical approach and dependencies

2. **🎯 Begin Development**:
   - Proceed directly to Sprint 1 execution
   - Follow the detailed task list from `docs/TODO.4-in-a-row-game.1.md`
### Step 4: Environment & Infrastructure Validation
**Execute Environment Setup**:

```bash
# Validate development environment
poetry install
poetry run ci  # Must pass all quality gates

# Verify project-specific components
poetry run python -c "
from src.4_in_a_row_game import __version__
print(f'✅ 4-in-a-row-game v{__version__} ready')
"
```

**Quality Gates Verification**:
- ✅ All dependencies installed correctly
- ✅ Code quality tools (Ruff, MyPy) operational  
- ✅ Test suite passing (>85% coverage)
- ✅ Project structure validated

### Step 5: State Tracking Initialization
**⚠️ CRITICAL**: Initialize or update `state.md` file:

```markdown
# 4-in-a-row-game - Project State

**Last Updated**: [Current Date]
**Current Sprint**: Sprint 0 (Infrastructure Setup)
**Current Phase**: Project Initialization
**Progress**: Environment setup and planning complete

## Development Summary
Project generated from template. Environment validation completed. TODO planning finalized. Ready to begin Sprint 1 core development.

## Sprint Status
- **Sprint 0**: ✅ Complete - Infrastructure setup
- **Sprint 1**: 🔄 Starting - Core game logic
- **Sprint 2**: ⏳ Pending - User interface
- **Sprint 3**: ⏳ Pending - Advanced features
```

### Step 6: Begin Development
**Final Step**: After validation and state initialization:

```
✅ 4-in-a-row-game initialization complete!

📊 Project Summary:
- **Type**: game-development (pygame)
- **Sprint Plan**: 4 sprints planned
- **Current State**: Ready for Sprint 1
- **Next Tasks**: [Summarize top 3-5 tasks from TODO.4-in-a-row-game.1.md]

🚀 Beginning Sprint 1 development. Let's start with the first task from docs/TODO.4-in-a-row-game.1.md.
```
---

## 🔄 Session Continuation (Returning Users)

**When returning to this project**, Windsurf should:

1. **📖 Read Current State**: Check `state.md` for last known progress
2. **📊 Provide Summary**: Brief overview of completed work and current objectives  
3. **🎯 Resume Development**: Continue from the exact point where development left off
4. **⚠️ Update State**: Remember to update `state.md` after completing any sprint or major milestone

**Example Continuation**:
```
📊 4-in-a-row-game Status:
- **Last Session**: [Date from state.md]
- **Completed**: [List from state.md]
- **Current Sprint**: [Current sprint from state.md]
- **Next Task**: [Next task from state.md]

🚀 Continuing development from [specific point]...
```

---

## ⚠️ IMPORTANT: State Tracking Requirements

**Windsurf MUST update `state.md` after**:
- ✅ Completing any sprint (Sprint 0, 1, 2, 3)
- ✅ Finishing major development milestones
- ✅ Completing significant feature implementations
- ✅ Before ending any development session

**Keep the format simple**: Update metadata, summary, and sprint status only.

**This ensures seamless project continuation across sessions!**
