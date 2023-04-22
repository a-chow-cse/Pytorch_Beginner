### **Delete connection to remote git**
Go to the folder and run `rm -rf .git/`
### **Upload a newly cloned repo inside your already owned repo**
`git clone git::repo_link `\
`git add <newly cloned repo folder>/`
### **Uncommit "committed but not pushed" while keeping local changes**
`git reset HEAD~1 --soft `

### **Unstage staged changed folder**
`git reset -- <folder_path>/* `

### **Unstage staged changed file**
`git reset -- <file_path>/file_name `

### Git Single Large File Upload (larger than 100MB)

