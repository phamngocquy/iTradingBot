#!/bin/bash

set -e
set -o pipefail

FORCE_RUN=${1:-no}
LATEST=${2:-no}

# shellcheck disable=SC2155
export VERSION=$(git describe --abbrev=4 --always --tags)

function distribute() {
  if [ "${LATEST}" = "yes" ]; then
    echo "Distribute as latest"

    docker build -f Dockerfile -t quypn/itradingbot:latest .

    docker push quypn/itradingbot:latest
  else
    echo "Distribute as ${VERSION}"
    docker build -f Dockerfile -t quypn/itradingbot:"${VERSION}" .

    docker tag quypn/itradingbot:"${VERSION}" quypn/itradingbot:latest
    docker push quypn/itradingbot:"${VERSION}"
    docker push quypn/itradingbot:latest
  fi
}

if [ "$FORCE_RUN" = "yes" ]; then
  distribute
else
  while true; do
    # shellcheck disable=SC2162
    read -p "Do you wish to distribute iTradingBot to Registry? " yn
    case $yn in
    [Yy]*)
      distribute
      exit 0
      ;;
    [Nn]*) exit 1 ;;
    *) echo "Please answer yes or no." ;;
    esac
  done
fi
