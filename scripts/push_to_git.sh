#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_data_files() {
  git checkout -b temp
  git add data/postni_nabiralniki.json
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
  git checkout master
  git merge temp
  git branch -d temp
}

upload_files() {
  git remote rm origin
  git remote add origin https://dpint:${GH_TOKEN}@github.com/dpint/PostniNabiralniki.git > /dev/null 2>&1
  git push --set-upstream origin master
}

setup_git
commit_data_files
upload_files