title: Problems with the GitHub Default Remote Using SSH
date: 2025-05-28 12:00
category: git, GitHub
tags: git, GitHub

Second time that I have this problem, so I thought I would write it down.

When I create a new repository on GitHub, the default instructions to add the remote repository to my local git repository are:

```bash
git remote add origin git@github.com:my_username/new_repo_name.git
git branch -M main
git push -u origin main
```

The problem is that this assumes that I'm using the SSH protocol to connect to GitHub. However, I prefer using HTTPS for my connections. Therefore, I need to change the remote URL to use HTTPS instead of SSH. To do this, I can use the following command:

```bash
git remote set-url origin https://github.com/my_username/new_repo_name.git
```

To avoid this, the instructions to add the HTTPS connection directly should be:

```bash
git remote add origin https://github.com/my_username/new_repo_name.git
git branch -M main
git push -u origin main
```
