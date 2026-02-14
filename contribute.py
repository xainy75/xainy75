#!/usr/bin/env python3
"""
GitHub Contribution Graph Hack
This script creates backdated commits to populate your GitHub contribution graph.
"""

import os
import sys
import subprocess
from datetime import datetime, timedelta
import random

def create_commit(date, commit_count=1):
    """
    Create commits on a specific date.
    
    Args:
        date: The date for the commit (datetime object)
        commit_count: Number of commits to create on this date
    """
    for i in range(commit_count):
        # Create a unique timestamp for each commit
        commit_time = date + timedelta(hours=random.randint(0, 23), 
                                       minutes=random.randint(0, 59))
        
        # Format date for git
        date_str = commit_time.strftime('%Y-%m-%d %H:%M:%S')
        
        # Append to contribution data file
        with open('contributions.txt', 'a') as f:
            f.write(f'Contribution on {date_str}\n')
        
        # Set environment variables for git commit date
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_str
        env['GIT_COMMITTER_DATE'] = date_str
        
        # Create git commit (use -f to force add ignored file)
        try:
            subprocess.run(['git', 'add', '-f', 'contributions.txt'], 
                         check=True, capture_output=True, text=True)
            subprocess.run(['git', 'commit', '-m', f'Contribution: {date_str}', '--quiet'],
                         env=env, check=True, capture_output=True, text=True)
            print(f'✓ Created commit for {date_str}')
        except subprocess.CalledProcessError as e:
            print(f'❌ Error creating commit for {date_str}: {e.stderr}')
            sys.exit(1)

def generate_contributions(start_date, end_date, frequency='random'):
    """
    Generate contributions between start_date and end_date.
    
    Args:
        start_date: Start date (datetime object)
        end_date: End date (datetime object)
        frequency: 'daily', 'random', or 'weekdays'
    """
    current_date = start_date
    total_commits = 0
    
    print(f"\n🚀 Starting contribution generation...")
    print(f"📅 Date range: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    print(f"📊 Frequency: {frequency}\n")
    
    while current_date <= end_date:
        should_commit = False
        commit_count = 1
        
        if frequency == 'daily':
            should_commit = True
            commit_count = random.randint(1, 3)
        elif frequency == 'random':
            # 70% chance of committing on any given day
            should_commit = random.random() < 0.7
            if should_commit:
                commit_count = random.randint(1, 5)
        elif frequency == 'weekdays':
            # Only commit on weekdays (Monday=0, Sunday=6)
            if current_date.weekday() < 5:
                should_commit = True
                commit_count = random.randint(1, 4)
        
        if should_commit:
            create_commit(current_date, commit_count)
            total_commits += commit_count
        
        current_date += timedelta(days=1)
    
    print(f"\n✨ Done! Created {total_commits} commits.")
    
    # Get current branch name
    try:
        result = subprocess.run(['git', 'branch', '--show-current'], 
                              check=True, capture_output=True, text=True)
        branch = result.stdout.strip()
        print(f"📤 Push changes with: git push origin {branch} --force")
    except subprocess.CalledProcessError:
        print(f"📤 Push changes with: git push origin <branch> --force")

def main():
    """Main function to run the contribution hack."""
    print("=" * 60)
    print("   GitHub Contribution Graph Hack")
    print("=" * 60)
    
    # Get user input for date range
    print("\n📝 Configuration:")
    
    # Default: Last year
    default_start = datetime.now() - timedelta(days=365)
    default_end = datetime.now()
    
    start_input = input(f"Start date (YYYY-MM-DD) [default: {default_start.strftime('%Y-%m-%d')}]: ").strip()
    if start_input:
        try:
            start_date = datetime.strptime(start_input, '%Y-%m-%d')
        except ValueError:
            print("❌ Invalid date format. Using default.")
            start_date = default_start
    else:
        start_date = default_start
    
    end_input = input(f"End date (YYYY-MM-DD) [default: {default_end.strftime('%Y-%m-%d')}]: ").strip()
    if end_input:
        try:
            end_date = datetime.strptime(end_input, '%Y-%m-%d')
        except ValueError:
            print("❌ Invalid date format. Using default.")
            end_date = default_end
    else:
        end_date = default_end
    
    # Frequency selection
    print("\nFrequency options:")
    print("  1. Random (70% chance daily, 1-5 commits)")
    print("  2. Daily (1-3 commits every day)")
    print("  3. Weekdays only (1-4 commits)")
    
    freq_choice = input("Select frequency [1/2/3, default: 1]: ").strip()
    frequency_map = {
        '1': 'random',
        '2': 'daily',
        '3': 'weekdays',
        '': 'random'
    }
    frequency = frequency_map.get(freq_choice, 'random')
    
    # Confirmation
    print("\n" + "=" * 60)
    print("⚠️  WARNING: This will create backdated commits!")
    print("   Make sure you're on the correct branch.")
    confirm = input("Continue? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("❌ Aborted.")
        sys.exit(0)
    
    # Initialize contributions file if it doesn't exist
    if not os.path.exists('contributions.txt'):
        with open('contributions.txt', 'w') as f:
            f.write('# GitHub Contribution History\n')
            f.write('# This file tracks backdated contributions\n\n')
    
    # Generate contributions
    generate_contributions(start_date, end_date, frequency)

if __name__ == '__main__':
    main()
