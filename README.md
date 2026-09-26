# Kenneth's Codex skills

A portable snapshot of 29 personal and installed skills from my laptops. Skill instructions, reference documents, scripts, metadata, and existing licenses are kept together under `skills/`.

## Set up another laptop

Install Git, Python 3, and Codex first. Sign in to GitHub with an account that can access this private repository, then run:

```sh
git clone https://github.com/perrykennethw/codex-skills.git
cd codex-skills
python3 install.py
```

The installer links each skill into `~/.agents/skills`, the user-level location documented in [OpenAI's Codex skills guide](https://learn.chatgpt.com/docs/build-skills). Keep the cloned repository in place: the links point to it. Codex supports symlinked skill folders and detects changes automatically; restart Codex if a skill does not appear.

On Windows, use `py -3 install.py --copy` if symlinks are unavailable. Copy installs must be refreshed by rerunning the installer after pulling updates.

### Existing skills

The installer stops before making changes if any destination already exists. Preview an installation or explicitly back up conflicts with:

```sh
python3 install.py --dry-run --backup
python3 install.py --backup
```

Backups are stored next to the destination, in a unique `skills-backup-<timestamp>-...` directory. Existing symlinks to this checkout are left alone. No skills are deleted. An alternate destination can be selected with `--dest PATH`.

Check for older copies in `~/.codex/skills` if a skill appears twice. This installer only manages its selected destination and does not change Codex settings or remove older copies.

## Keep laptops in sync

Edit files in this repository, then publish the changes:

```sh
git add skills
git commit -m "Update skills"
git push
```

On the other laptop:

```sh
git pull --ff-only
python3 install.py
```

Linked skills immediately use the pulled files; rerunning the installer adds newly introduced skills. For copy installations, run `python3 install.py --copy --backup` instead. If both laptops edited the same files, commit local changes and resolve the Git conflict before updating.

The original laptop's installed skills were copied to create this snapshot, not moved or replaced. Changes made to those original folders do not automatically reach the repository. Copy a changed skill back into `skills/` before committing, or switch that laptop to the repository links after backing up its existing installation. If a skill is later removed from the repository, remove its corresponding installed link manually.

## Contents and provenance

See [CATALOG.md](CATALOG.md) for the full skill list and [sources.json](sources.json) for original locations and recorded upstream sources. Source hashes are historical installation metadata; they do not assert that the current local copies are unchanged upstream versions.

- Personal Codex skills: UI design/refactoring, GitHub issue implementation, and pet creation.
- Installed skills from Matt Pocock's skills collection, Vercel's skill discovery tool, and Herdr, including local customizations.
- Herdr includes its standalone `SKILL.md` and license. Its application source and vendor tree are omitted; install the Herdr application separately to use that skill.

Codex's built-in `.system` skills, bundled plugin caches, credentials, conversation history, and machine settings are not included. Install any desired plugins separately on each laptop. Skills that use external tools still need those tools, app connections, and dependencies on the new laptop (for example GitHub CLI, Herdr, or image generation).

Existing per-skill licenses are preserved; see [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). This collection does not assign a new blanket license to third-party material.
