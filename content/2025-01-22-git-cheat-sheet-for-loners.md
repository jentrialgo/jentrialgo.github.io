Title: Essential git cheat sheet for loners
Date: 2025-01-22 12:00
Category: git
Tags: git

This are the basic commands to operate with git as a loner: no branches, no remotes, no
merges... Just the basic stuff.

The minimum concepts you need to know are:

- Git is a version control system. It allows you to store changes in your files. Don't
  mix it with GitHub, which is a platform to store your repositories.
- Working directory: the directory where you are working.
- Staging area: a place to store changes before committing them.
- Repository: the place where the changes are stored.
- Commit: a set of changes stored in the repository. They are identified by a hash. For
  example, `commit 1234567`.

The basic workflow is:

1. Make changes in the working directory.
2. Add changes to the staging area.
3. Commit changes to the repository.
4. Repeat.

Conceptually: working directory -> staging area -> repository.

# Configuration

```bash
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

# Create a new repository

In the directory of your project:

```bash
git init
```

# Add files to the repository

This adds all the changes in your current directory to the staging area.

```bash
git add .
```

If you only want to add a specific file:

```bash
git add file.txt
```

# Commit changes

This commits the changes in the staging area to the repository.

```bash
git commit -m "Your commit message"
```

# Check the status of the repository

```bash
git status
```

# Check the history of the repository

```bash
git log
```

# Compare changes

Working directory vs repository:

```bash
git diff
```

Staging area vs repository:

```bash
git diff --staged
```

# Discard changes in the working directory

```bash
git checkout -- .
```

Caution: This removes all uncommitted changes. For specific files, use `git checkout --
filename`.

# Discard changes in the staging area

```bash
git reset
```

Any other command you need, you can find it in the [official
documentation](https://git-scm.com/doc) or, better, ask to an LLM like ChatGPT.

Probably, the next step is to learn about remotes and, then, branches.
