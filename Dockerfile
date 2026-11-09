
FROM python:3.13-slim

# Python configuration
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /app

# Install uv
COPY --from=ghcr.io/astral-sh/uv:0.12.23 /uv /uvx /bin/

# Copy dependency files
COPY pyproject.toml uv.lock ./
COPY README.md ./

# Copy application source code
COPY src/ ./src/
COPY api/ ./api/

# Install project dependencies
RUN uv sync --frozen --no-dev

# Expose FastAPI port
EXPOSE 8000

# Start API
CMD ["uv", "run", "--no-sync", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
