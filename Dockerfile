# Multi-stage Docker build for 4-in-a-row-game
# Development and production-ready containerization

# === Base Stage ===
FROM python:3.12-slim as base

# Install system dependencies for pygame
RUN apt-get update && apt-get install -y \
    # pygame dependencies
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libfreetype6-dev \
    libportmidi-dev \
    # Development tools
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create non-root user for security
RUN groupadd --gid 1000 gameuser && \
    useradd --uid 1000 --gid gameuser --shell /bin/bash --create-home gameuser

# Set working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Configure Poetry
ENV POETRY_NO_INTERACTION=1 \
    POETRY_VENV_IN_PROJECT=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

# === Development Stage ===  
FROM base as development

# Copy Poetry configuration
COPY pyproject.toml poetry.lock ./

# Install dependencies including dev dependencies
RUN poetry install --with dev && rm -rf $POETRY_CACHE_DIR

# Copy source code
COPY . .

# Change ownership to non-root user
RUN chown -R gameuser:gameuser /app
USER gameuser

# Expose port for any web interface (if added later)
EXPOSE 8000

# Development command
CMD ["poetry", "run", "python", "-m", "4_in_a_row_game.main"]

# === Production Stage ===
FROM base as production

# Copy Poetry configuration
COPY pyproject.toml poetry.lock ./

# Install only production dependencies
RUN poetry install --only=main && rm -rf $POETRY_CACHE_DIR

# Copy source code
COPY src/ ./src/
COPY assets/ ./assets/
COPY README.md ./

# Change ownership to non-root user  
RUN chown -R gameuser:gameuser /app
USER gameuser

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import 4_in_a_row_game; print('OK')" || exit 1

# Production command
CMD ["poetry", "run", "python", "-m", "4_in_a_row_game.main"]

# === Testing Stage ===
FROM development as testing

# Run tests and quality checks
RUN poetry run pytest --cov=src --cov-report=xml --cov-report=term
RUN poetry run ruff check .
RUN poetry run mypy src/

# === Release Stage ===
FROM production as release

# Add metadata labels
LABEL org.opencontainers.image.title="4-in-a-row-game" \
      org.opencontainers.image.description="Board game" \
      org.opencontainers.image.authors="Avidor <avidor@synaptixlabs.ai>" \
      org.opencontainers.image.source="https://github.com/https://github.com/SynaptixLabs/4-in-a-row-game" \
      org.opencontainers.image.version="0.1.0"

# Final configuration
VOLUME ["/app/data", "/app/saves"]
