echo "# COMP2152" >> README.md
```bash 
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:mateussfeir/COMP2152.git
git push -u origin main

(another way that worked in my mac:
git add .      or     git add "name of the file"
git commit -m "Write any comment"
git push origin main)