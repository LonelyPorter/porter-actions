#!/usr/bin/env bash

echo "This current path is $(pwd)"
echo "Files under the current directory are:"
ls

if [ -f project.toml ]; then
  cat project.toml
else
  echo "project.toml file not exists! Check your project setup!"
  exit 1
fi

echo "Current branch is: "
git branch -vv
echo "Git log hisotry are: "
git log

echo "Check if version is being updated..."
if git log -p HEAD^..HEAD -- project.toml | grep version; then
  echo "Version has been updated, can merge safely"
  exit 0
else
  echo "No version being updated! Check before merge!"
  exit 1
fi
