#!/bin/sh
git config diff.orderFile .gitorder
git config diff.c++draft.xfuncname '\\rSec[0-9]+(\[.*\])\{'

precommit="$(git rev-parse --git-dir)/hooks/pre-commit"

test -f "${precommit}" && exit
read -p "Install 'make check' pre-commit hook? [Y/n] " hook
if [ -z "${hook}" -o "${hook}" = "y" -o "${hook}" = "Y" ]; then
  cat <<EOF > "${precommit}"
#!/bin/sh
cd \$(git rev-parse --show-toplevel)/source
make check
EOF
  chmod +x "${precommit}"
fi
