#!/bin/bash

# GitHub Contribution Graph Hack Script
# Creates backdated commits to populate your contribution graph

echo "======================================"
echo "  GitHub Contribution Graph Hack"
echo "======================================"
echo ""

# Configuration
START_DATE=${1:-"2023-01-01"}  # Default: 1 year ago
END_DATE=${2:-"2024-12-31"}    # Default: today
REPO_PATH=$(pwd)

echo "📅 Start Date: $START_DATE"
echo "📅 End Date: $END_DATE"
echo "📂 Repository: $REPO_PATH"
echo ""

# Create contributions file if it doesn't exist
if [ ! -f "contributions.txt" ]; then
    echo "# GitHub Contribution History" > contributions.txt
    echo "# This file tracks backdated contributions" >> contributions.txt
    echo "" >> contributions.txt
fi

# Convert dates to seconds since epoch
start_ts=$(date -d "$START_DATE" +%s)
end_ts=$(date -d "$END_DATE" +%s)

# Calculate number of days
days=$(( (end_ts - start_ts) / 86400 ))

echo "🚀 Generating $days days of contributions..."
echo ""

commit_count=0

# Loop through each day
for ((i=0; i<=days; i++)); do
    # Calculate current date
    current_ts=$((start_ts + i * 86400))
    current_date=$(date -d "@$current_ts" +"%Y-%m-%d")
    
    # Random decision: 70% chance of committing
    if [ $((RANDOM % 10)) -lt 7 ]; then
        # Random number of commits (1-5)
        num_commits=$((RANDOM % 5 + 1))
        
        for ((j=0; j<num_commits; j++)); do
            # Random time during the day
            hour=$((RANDOM % 24))
            minute=$((RANDOM % 60))
            commit_datetime="$current_date $hour:$minute:00"
            
            # Append to contributions file
            echo "Contribution on $commit_datetime" >> contributions.txt
            
            # Set git dates
            export GIT_AUTHOR_DATE="$commit_datetime"
            export GIT_COMMITTER_DATE="$commit_datetime"
            
            # Create commit
            git add contributions.txt
            git commit -m "Contribution: $commit_datetime" --quiet
            
            commit_count=$((commit_count + 1))
        done
        
        echo "✓ Created $num_commits commit(s) for $current_date"
    fi
done

echo ""
echo "✨ Done! Created $commit_count commits."
echo "📤 Push changes with: git push origin main --force"
echo ""
echo "⚠️  Note: Use --force carefully! This rewrites history."
