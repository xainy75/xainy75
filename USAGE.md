# 🎯 GitHub Contribution Graph Hack - Usage Guide

This repository includes two scripts to help you "hack" your GitHub contribution graph by creating backdated commits.

## 📋 Table of Contents
- [Overview](#overview)
- [Python Script (Recommended)](#python-script-recommended)
- [Bash Script (Quick)](#bash-script-quick)
- [Examples](#examples)
- [Important Warnings](#important-warnings)
- [FAQ](#faq)

## Overview

These scripts create backdated Git commits by manipulating the `GIT_AUTHOR_DATE` and `GIT_COMMITTER_DATE` environment variables. The commits are written to a `contributions.txt` file to keep your repository clean.

## Python Script (Recommended)

### Features
- ✅ Interactive configuration
- ✅ Custom date ranges
- ✅ Multiple frequency patterns
- ✅ Better randomization
- ✅ Cross-platform (Windows, Mac, Linux)

### Usage

```bash
python3 contribute.py
```

The script will prompt you for:
1. **Start Date**: Beginning of contribution period (default: 1 year ago)
2. **End Date**: End of contribution period (default: today)
3. **Frequency Pattern**:
   - Random: 70% daily chance, 1-5 commits
   - Daily: Every day, 1-3 commits
   - Weekdays: Monday-Friday only, 1-4 commits

### Example Session

```
====================================
   GitHub Contribution Graph Hack
====================================

📝 Configuration:
Start date (YYYY-MM-DD) [default: 2024-02-14]: 2024-01-01
End date (YYYY-MM-DD) [default: 2025-02-14]: 2024-12-31

Frequency options:
  1. Random (70% chance daily, 1-5 commits)
  2. Daily (1-3 commits every day)
  3. Weekdays only (1-4 commits)
Select frequency [1/2/3, default: 1]: 1

====================================
⚠️  WARNING: This will create backdated commits!
   Make sure you're on the correct branch.
Continue? (yes/no): yes

🚀 Starting contribution generation...
📅 Date range: 2024-01-01 to 2024-12-31
📊 Frequency: random

✓ Created commit for 2024-01-01 08:34:12
✓ Created commit for 2024-01-01 14:22:45
...

✨ Done! Created 487 commits.
📤 Push changes with: git push origin main --force
```

## Bash Script (Quick)

### Features
- ✅ Fast execution
- ✅ Simple command-line interface
- ✅ Cross-platform (Linux & macOS)
- ✅ Error checking and validation

### Usage

```bash
# Default: 2023-01-01 to 2024-12-31
./hack_contributions.sh

# Custom date range
./hack_contributions.sh "START_DATE" "END_DATE"
```

### Examples

```bash
# Fill entire year 2024
./hack_contributions.sh "2024-01-01" "2024-12-31"

# Last 6 months
./hack_contributions.sh "2024-08-01" "2025-02-14"

# Specific period
./hack_contributions.sh "2023-06-15" "2023-09-30"
```

## Examples

### Example 1: Fill Last Year

```bash
# Calculate dates
START_DATE=$(date -d "1 year ago" +%Y-%m-%d)
END_DATE=$(date +%Y-%m-%d)

# Run script
./hack_contributions.sh "$START_DATE" "$END_DATE"
```

### Example 2: Weekdays Only (Work Pattern)

```python
# Use Python script for more control
python3 contribute.py
# Select option 3 (Weekdays only)
```

### Example 3: Specific Date Range

```bash
# Fill summer 2024
./hack_contributions.sh "2024-06-01" "2024-08-31"
```

## Important Warnings

### ⚠️ Use Responsibly

1. **This is for educational/fun purposes**: Don't use this to misrepresent your actual work
2. **Separate repository recommended**: Consider creating a test repo instead of your profile repo
3. **Force push required**: This rewrites Git history - use `--force` carefully
4. **Cannot undo easily**: Once pushed, the fake commits are in your history

### 🔒 Best Practices

- Test in a separate repository first
- Make sure you're on the correct branch
- Backup your repository before running
- Consider the ethical implications
- Use for learning Git internals, not deception

### 📝 Ethical Considerations

While technically possible, consider:
- GitHub contribution graphs reflect actual work
- Employers/collaborators may check your commit history
- Artificially inflated graphs can damage credibility
- Better to build genuine contributions over time

## FAQ

### Q: Will this affect my other repositories?
**A:** No, commits are only created in the current repository where you run the script.

### Q: Can GitHub detect this?
**A:** The commits are real Git commits with backdated timestamps. They're technically valid, but obvious patterns might be noticeable.

### Q: How do I remove the fake commits?
**A:** You can use `git reset --hard <commit-hash>` to go back to before the fake commits, then force push.

### Q: Does this work on private repositories?
**A:** Commits in private repositories don't show on your public contribution graph unless you enable "Private contributions" in GitHub settings.

### Q: Can I customize the commit messages?
**A:** Yes! Edit the scripts to change the commit message format in the `git commit` commands.

### Q: What if I get merge conflicts?
**A:** Since this creates new commits on top of your current branch, conflicts are unlikely. If they occur, you may need to reset and try again.

### Q: Will this make me a better developer?
**A:** No! Real contributions, learning, and building projects are what make you better. Use this for fun or learning Git internals only.

## Pushing Your Changes

After running either script:

```bash
# Check what was created
git log --oneline -10

# Push to GitHub (use --force since we're rewriting history)
git push origin main --force

# Or for your profile repo specifically:
git push origin copilot/hack-github-contribution-graph --force
```

## Cleanup

To remove the contribution file:

```bash
git rm contributions.txt
git commit -m "Cleanup"
```

## Advanced Usage

### Custom Commit Patterns

Edit `contribute.py` to create custom patterns:

```python
# Create a heart shape, specific days only, etc.
# Modify the should_commit logic in generate_contributions()
```

### Different Branches

```bash
# Create a separate branch for experiments
git checkout -b contribution-experiment

# Run your scripts
python3 contribute.py

# Push to the experiment branch
git push origin contribution-experiment --force
```

---

## 🎓 Learning Outcomes

By using these scripts, you'll learn about:
- Git internals and commit timestamps
- Environment variables in Git
- Date manipulation in scripts
- The difference between author and committer dates
- Git history and how contributions are tracked

## 🤝 Contributing

Feel free to fork this repository and:
- Add new patterns (holidays off, work hours only, etc.)
- Improve the randomization algorithms
- Add more configuration options
- Create visualization tools

---

**Remember**: The best way to have a great contribution graph is to write code, contribute to open source, and build projects regularly! 🚀
