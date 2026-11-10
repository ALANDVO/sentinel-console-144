
"""
Sentinel Console - Lint API endpoints.
"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from pathlib import Path

from rules.engine import get_engine, LintResult, Severity


router = APIRouter(prefix="/api/lint", tags=["lint"])


class LintRequest(BaseModel):
    content: str
    file_path: Optional[str] = None


class LintResponse(BaseModel):
    results: list[dict]
    summary: dict


class RulesSummaryResponse(BaseModel):
    version: str
    description: str
    ban_patterns: int
    require_patterns: int
    token_scales: dict


@router.get("/rules", response_model=RulesSummaryResponse)
async def get_rules_summary():
    """Get summary of loaded lint rules."""
    engine = get_engine()
    return engine.get_rules_summary()


@router.post("/css", response_model=LintResponse)
async def lint_css(request: LintRequest):
    """Lint CSS content against anti-slop rules."""
    engine = get_engine()
    results = engine.lint_css(request.content, request.file_path)

    # Count by severity
    error_count = sum(1 for r in results if r.severity == Severity.ERROR)
    warning_count = sum(1 for r in results if r.severity == Severity.WARNING)

    return LintResponse(
        results=[r.to_dict() for r in results],
        summary={
            "total": len(results),
            "errors": error_count,
            "warnings": warning_count,
            "passed": error_count == 0,
        },
    )


@router.post("/file")
async def lint_file(file_path: str):
    """Lint a CSS file by path."""
    engine = get_engine()
    path = Path(file_path)

    if not path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {file_path}")

    if not path.is_file():
        raise HTTPException(status_code=400, detail=f"Path is not a file: {file_path}")

    results = engine.lint_file(path)

    error_count = sum(1 for r in results if r.severity == Severity.ERROR)
    warning_count = sum(1 for r in results if r.severity == Severity.WARNING)

    return LintResponse(
        results=[r.to_dict() for r in results],
        summary={
            "total": len(results),
            "errors": error_count,
            "warnings": warning_count,
            "passed": error_count == 0,
            "file": str(path),
        },
    )
