#!/usr/bin/env bash
set -euo pipefail
tool_dir="$RUNNER_TEMP/freshness-tools"
mkdir -p "$tool_dir"
cd "$tool_dir"
curl -fsSL https://github.com/lycheeverse/lychee/releases/download/lychee-v0.24.2/lychee-x86_64-unknown-linux-gnu.tar.gz -o lychee.tar.gz
printf '%s\n' '1f4e0ef7f6554a6ed33dd7ac144fb2e1bbed98598e7af973042fc5cd43951c9a  lychee.tar.gz' | sha256sum -c -
tar -xzf lychee.tar.gz
install -m 755 lychee-x86_64-unknown-linux-gnu/lychee "$tool_dir/lychee"
"$tool_dir/lychee" --version
printf '%s\n' "$tool_dir" >> "$GITHUB_PATH"
