
"""
Sentinel Console - Anti-slop rule engine.
Loads rules from config and lints CSS/design tokens.
"""
import json
import re
from pathlib import Path
from typing import Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class LintResult:
    rule_id: str
    severity: Severity
    message: str
    line: Optional[int] = None
    column: Optional[int] = None
    match: Optional[str] = None
    file: Optional[str] = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "rule_id": self.rule_id,
            "severity": self.severity.value,
            "message": self.message,
            "line": self.line,
            "column": self.column,
            "match": self.match,
            "file": self.file,
        }


@dataclass
class RuleConfig:
    version: str
    description: str
    token_scales: dict[str, Any]
    ban_patterns: list[dict[str, Any]]
    require_patterns: list[dict[str, Any]]


class RuleEngine:
    """Loads and applies anti-slop design rules."""

    def __init__(self, config_path: Optional[Path] = None):
        self.config_path = config_path or Path(__file__).parent.parent / "config" / "rules.json"
        self.config: Optional[RuleConfig] = None
        self._compiled_ban_patterns: list[tuple[re.Pattern, dict]] = []
        self._load_config()

    def _load_config(self) -> None:
        with open(self.config_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.config = RuleConfig(
            version=data["version"],
            description=data["description"],
            token_scales=data["token_scales"],
            ban_patterns=data["ban_patterns"],
            require_patterns=data["require_patterns"],
        )

        # Compile ban patterns
        self._compiled_ban_patterns = []
        for rule in self.config.ban_patterns:
            pattern = re.compile(rule["pattern"], re.MULTILINE | re.IGNORECASE)
            self._compiled_ban_patterns.append((pattern, rule))

    def reload(self) -> None:
        """Reload configuration from disk."""
        self._load_config()

    def get_token_scales(self) -> dict[str, Any]:
        """Return the configured token scales."""
        if not self.config:
            return {}
        return self.config.token_scales

    def lint_css(self, css_content: str, file_path: Optional[str] = None) -> list[LintResult]:
        """Lint CSS content against ban patterns."""
        results: list[LintResult] = []

        if not self.config:
            return results

        lines = css_content.splitlines()

        for pattern, rule in self._compiled_ban_patterns:
            for match in pattern.finditer(css_content):
                # Find line number
                line_no = css_content[: match.start()].count("\n") + 1
                column = match.start() - css_content.rfind("\n", 0, match.start())

                # Format message with token scales if placeholders exist
                message = rule["message"]
                if "{spacing_scale}" in message:
                    message = message.format(
                        spacing_scale=", ".join(f"{v}px" for v in self.config.token_scales.get("spacing", []))
                    )
                if "{radius_scale}" in message:
                    message = message.format(
                        radius_scale=", ".join(self.config.token_scales.get("border_radius", []))
                    )
                if "{font_size_scale}" in message:
                    message = message.format(
                        font_size_scale=", ".join(self.config.token_scales.get("font_size", []))
                    )
                if "{shadow_scale}" in message:
                    message = message.format(
                        shadow_scale=", ".join(self.config.token_scales.get("shadow", []))
                    )
                if "{match}" in message:
                    message = message.format(match=match.group(0))

                results.append(
                    LintResult(
                        rule_id=rule["id"],
                        severity=Severity(rule["severity"]),
                        message=message,
                        line=line_no,
                        column=column,
                        match=match.group(0),
                        file=file_path,
                    )
                )

        return results

    def lint_file(self, file_path: Path) -> list[LintResult]:
        """Lint a CSS file."""
        content = file_path.read_text(encoding="utf-8")
        return self.lint_css(content, str(file_path))

    def get_rules_summary(self) -> dict[str, Any]:
        """Return a summary of loaded rules."""
        if not self.config:
            return {"ban_patterns": 0, "require_patterns": 0, "token_scales": {}}

        return {
            "version": self.config.version,
            "description": self.config.description,
            "ban_patterns": len(self.config.ban_patterns),
            "require_patterns": len(self.config.require_patterns),
            "token_scales": {k: (len(v) if isinstance(v, list) else len(v)) for k, v in self.config.token_scales.items()},
        }


# Global engine instance
_engine: Optional[RuleEngine] = None


def get_engine(config_path: Optional[Path] = None) -> RuleEngine:
    """Get or create the global rule engine instance."""
    global _engine
    if _engine is None or config_path is not None:
        _engine = RuleEngine(config_path)
    return _engine
