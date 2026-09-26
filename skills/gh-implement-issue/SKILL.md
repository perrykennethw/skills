---
name: gh-implement-issue
description: Take a GitHub issue from investigation through implementation, validation, commit, push, and a draft pull request using local git and the GitHub CLI. Use when the user provides an issue URL or issue number and asks Codex to take it on, fix or implement it, ship it, make the changes, or open a PR. Do not use for issue summaries, PR reviews, or code changes that the user does not want published.
---

# Implement a GitHub Issue

Own the issue-to-PR workflow end to end. Use the GitHub CLI for GitHub reads and writes, including PR creation. Do not switch to a connector for PR creation unless the user explicitly requests it.

## 1. Resolve the context

- Extract the repository and issue number from the supplied URL or request.
- If the current directory is the matching repository, work there.
- If it is not a Git repository and the issue URL identifies the repository, clone into a new workspace subdirectory when the current directory is safe for that operation.
- If the current repository does not match, or local contents make the target ambiguous, stop and ask the user where to work.
- Read applicable `AGENTS.md` files before changing code.

## 2. Run preflight checks

- Check `gh --version`, `gh auth status`, `git status -sb`, and `git remote -v`.
- Request network permission when the environment requires it.
- If `gh` is missing, stop and ask the user to install it.
- If authentication is invalid, stop and give the exact repair command: `gh auth login -h github.com -p ssh -w`.
- Fetch the issue with `gh issue view`, including its title, body, labels, state, and URL.
- Confirm the issue is open and the local remote matches its repository.
- Inspect the working tree before creating a branch. Never discard, stash, or stage unrelated user changes. Ask for direction when existing changes overlap or make scope unclear.
- Derive the remote default branch with `gh repo view`, then fetch it from `origin` before implementation.
- Treat one issue as one task and one implementation branch or worktree. Never base a new issue branch on an unrelated feature branch.

## 3. Plan and implement

- Inspect the relevant code, tests, and repository conventions.
- Determine the root cause or required behavior from the issue and codebase evidence.
- Convert every issue acceptance criterion and other required behavior into a verification checklist before implementation.
- Unless already on the correctly scoped issue branch, create `issue-<number>-<short-description>` directly from the latest `origin/<default-branch>`. This applies in both local checkouts and detached Codex-managed worktrees.
- Never include Codex, agent, model, or other tool names in branch names.
- Make the smallest coherent change that fully addresses the issue.
- Add or update tests when they materially protect the requested behavior.
- Keep unrelated cleanup out of the patch.
- If the requested work expands into a different issue, feature, audit, revert, or unrelated refactor, stop that work and propose it as a follow-up task. Do not absorb it into the current branch.

## 4. Validate

- Run the most relevant focused tests first, then broader checks when proportionate to risk.
- Evaluate every acceptance criterion as passed, blocked, deferred, or unverified, with concrete evidence for passed items.
- Inspect `git diff`, `git diff --check`, and `git status -sb` after testing.
- Fix failures caused by the change. Clearly distinguish unrelated pre-existing failures.
- Do not publish when required validation fails unless the user explicitly directs otherwise.

## 5. Commit and push

- Stage only files belonging to the issue. Use explicit paths when the worktree contains anything unrelated.
- Use a terse commit message that describes the change, such as `Fix #<number>: <description>`.
- Push the branch to `origin` with upstream tracking.
- If push permission is missing, report the exact failure. Do not create a fork or change remotes without user authorization.

## 6. Open and verify the draft PR

- Derive the base branch from `gh repo view` unless the user specifies one.
- Create a draft PR with `gh pr create --draft`; do not use a GitHub connector for this step.
- Write the PR body as real Markdown using a temporary file. Include:
  - `Summary`: what changed.
  - `Root cause` or `Rationale`: why it changed.
  - `Validation`: exact checks run and their results.
  - `Acceptance criteria`: the status and evidence for every required criterion.
  - `Issue`: `Closes #<number>` only when every required criterion is satisfied. Otherwise use `Related to #<number>` and explain what remains.
- Use a concise title that summarizes the full diff.
- Verify the result with `gh pr view` and capture the URL, base branch, head branch, state, and draft status.
- Keep the pull request in draft whenever a required criterion is blocked, deferred, unverified, or failing. Do not merge unless the user explicitly requests it.

## Completion report

Report the issue, branch, commit, acceptance-criteria status, exact validation, and PR URL. Mention any skipped or failing checks. Do not claim the workflow is complete until the pushed commit and draft PR are verified.

Keep review feedback, CI fixes, and corrections required by this pull request in the same task. Start a new task and worktree for a different outcome. If the user later requests post-merge cleanup, first confirm the pull request is merged and the working tree is safe, then update the local default branch and remove only the merged issue branch or managed worktree.
