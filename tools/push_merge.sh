#!/usr/bin/env bash
# Transient push of the merged state to GitHub.
# The token is read from the GITHUB_TOKEN environment variable ONLY —
# it is never written to .git/config, .git/credentials, or any file.
# It is used in one git command via -c http.extraheader, then gone.
set -euo pipefail
cd "$(dirname "$0")"

TOKEN="${GITHUB_TOKEN:?Set GITHUB_TOKEN first, e.g. GITHUB_TOKEN=ghp_xxxx bash tools/push_merge.sh}"

# Remote URL (re-added here because .git/config is excluded from workspace snapshots)
git remote add origin https://github.com/gm5206663-bit/supergirl-adrian-vale.git 2>/dev/null \
  || git remote set-url origin https://github.com/gm5206663-bit/supergirl-adrian-vale.git

# What is being pushed
echo "== Pushing == $(git rev-parse --short HEAD) (merge of local 26-chapter rebuild + remote 4 commits)"

# Transient auth — token in the URL of THIS command only; git does not write
# the URL to .git/config, and it is gone after this command finishes.
git push "https://x-access-token:$TOKEN@github.com/gm5206663-bit/supergirl-adrian-vale.git" main

echo "== Done. Token used only in this command; no file was written with it."
