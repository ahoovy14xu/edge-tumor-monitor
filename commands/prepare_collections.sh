#!/usr/bin/env bash
set -euo pipefail
source_root="$1"
manifest_root="$2"
mkdir -p "$manifest_root"
find "$source_root" -type f \( -name '*.dcm' -o -name '*.nii.gz' \) -print0 | sort -z | xargs -0 -n1 basename > "$manifest_root/files.txt"
sha256sum "$manifest_root/files.txt" > "$manifest_root/files.sha256"
