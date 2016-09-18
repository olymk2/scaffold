#ln -s .git_precommit.sh .git/hooks/pre-commit

# save state should only run against staged files
git stash -q --keep-index

drone exec 
RESULT=$?
[ $RESULT -ne 0 ] && exit 1
exit 0

# restore state
git stash pop -q
