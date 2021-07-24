git add .
echo Commit Message: 
read MESSAGE
git commit -am "$MESSAGE"
git push origin master