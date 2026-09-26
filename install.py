#!/usr/bin/env python3
"""Install this collection without silently replacing existing skills."""

import argparse
from datetime import datetime
from pathlib import Path
import shutil
import sys
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, default=Path.home() / ".agents" / "skills",
                        help="Skill directory (default: ~/.agents/skills)")
    parser.add_argument("--backup", action="store_true",
                        help="Move conflicting skills to a timestamped backup before installing")
    parser.add_argument("--copy", action="store_true",
                        help="Copy instead of linking (useful on Windows without symlink permission)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without changing any files")
    args = parser.parse_args()
    repository = Path(__file__).resolve().parent
    source = repository / "skills"
    destination = args.dest.expanduser().resolve()
    if destination == repository or repository in destination.parents:
        parser.error("The destination must be outside this repository.")
    skills = sorted(p.parent for p in source.glob("*/SKILL.md"))
    if not skills:
        parser.error("No skills found beside this installer.")
    if destination.exists() and not destination.is_dir():
        parser.error("The destination exists and is not a directory.")

    pending = []
    conflicts = []
    for skill in skills:
        target = destination / skill.name
        if target.is_symlink() and target.resolve() == skill.resolve() and not args.copy:
            print("Already linked:", skill.name)
            continue
        pending.append((skill, target))
        if target.exists() or target.is_symlink():
            conflicts.append(target)

    if conflicts and not args.backup:
        print("Existing skills would conflict; no files changed:", file=sys.stderr)
        for path in conflicts:
            print("  " + str(path), file=sys.stderr)
        print("Use --backup to preserve these skills and install the repo versions.", file=sys.stderr)
        return 1

    if args.dry_run:
        for skill, target in pending:
            action = "Copy" if args.copy else "Link"
            if target in conflicts:
                print("Back up:", target)
            print(f"{action}: {skill} -> {target}")
        print("Preview only; no files changed.")
        return 0

    if not pending:
        print("All skills are already linked.")
        return 0

    destination.mkdir(parents=True, exist_ok=True)
    backup = None
    if conflicts:
        prefix = "skills-backup-" + datetime.now().strftime("%Y%m%d-%H%M%S") + "-"
        backup = Path(tempfile.mkdtemp(prefix=prefix, dir=destination.parent))
        print("Backup directory:", backup)

    for skill, target in pending:
        # Prepare the replacement before moving any existing user files.
        with tempfile.TemporaryDirectory(prefix=".skill-install-", dir=destination.parent) as work:
            prepared = Path(work) / skill.name
            if args.copy:
                shutil.copytree(skill, prepared)
            else:
                prepared.symlink_to(skill, target_is_directory=True)
            saved = None
            if target.exists() or target.is_symlink():
                if backup is None:
                    raise RuntimeError(f"Destination appeared during installation: {target}")
                saved = backup / skill.name
                target.rename(saved)
            try:
                prepared.rename(target)
            except OSError:
                if saved is not None:
                    saved.rename(target)
                raise
        print("Installed:", skill.name)
    print(f"Installed {len(pending)} skills in {destination}.")
    print("Reload skills or restart your agent harness if the skills do not appear.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError) as error:
        print(f"Installation failed: {error}", file=sys.stderr)
        print("Earlier installed skills and any backups were preserved. "
              "For symlink permission errors, try --copy.", file=sys.stderr)
        sys.exit(1)
