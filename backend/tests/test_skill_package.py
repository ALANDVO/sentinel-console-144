"""Tests for the skills/hallmark/ skill package (SKILL.md + references)."""
import json
import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
SKILL_DIR = REPO_ROOT / "skills" / "hallmark"
SKILL_MD = SKILL_DIR / "SKILL.md"
REFERENCES = SKILL_DIR / "references"


class SkillPackageTests(unittest.TestCase):
    def setUp(self):
        self.text = SKILL_MD.read_text(encoding="utf-8")

    def test_skill_md_exists(self):
        self.assertTrue(SKILL_MD.is_file())

    def test_no_relative_path_references(self):
        self.assertNotIn("../../", self.text)

    def test_reference_links_are_absolute_github_urls(self):
        for link in re.findall(r"\[[^\]]+\]\(([^)]+)\)", self.text):
            self.assertTrue(
                link.startswith("https://github.com/"),
                f"non-absolute reference link: {link}",
            )

    def test_references_directory_has_supporting_files(self):
        self.assertTrue(REFERENCES.is_dir())
        for name in ("design-tokens.md", "rules.json", "README.md"):
            self.assertTrue((REFERENCES / name).is_file(), f"missing {name}")

    def test_referenced_rules_json_is_valid(self):
        data = json.loads((REFERENCES / "rules.json").read_text(encoding="utf-8"))
        self.assertIn("colors", data)
        self.assertIn("radii", data)


if __name__ == "__main__":
    unittest.main()
