# Sentinel Console - Anti-AI-slop Design Skill

## Overview

Anti-AI-slop design skill for Claude Code, Cursor, and Codex.

This skill helps developers avoid generic AI output by enforcing design taste as explicit, enforceable rules. It validates design tokens against curated allowlists and bans sloppy patterns.

## Usage

Install with:
```bash
npx skills add ALANDVO/sentinel-console-144
```

The skill runs in your editor context without requiring separate tooling or context switching.

## Capabilities

- **Token Linting**: Validates design tokens against curated allowlists
- **Ban List Enforcement**: Hard bans on sloppy patterns (untyped colors, inconsistent radii, manual px values)
- **Claude Code Integration**: Works in your editor context
- **Cursor & Codex Ready**: Same rule engine across all AI assistants
- **Extensible Rules**: Add project-specific rules via config
- **CI Integration**: Fail builds on slop with `sentinel lint`

## Links

Installation: https://github.com/ALANDVO/sentinel-console-144

## References

- [Design Tokens Documentation](https://github.com/ALANDVO/sentinel-console-144/blob/main/docs/design-tokens.md)
- [Rule Configuration](https://github.com/ALANDVO/sentinel-console-144/blob/main/backend/config/rules.json)
- [API Documentation](https://github.com/ALANDVO/sentinel-console-144/blob/main/README.md)

## Contact

Alan Vo <alanvo@gmail.com>
https://alanvo.net
https://x.com/alanvoasi
