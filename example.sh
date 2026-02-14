#!/bin/bash

# Quick Example: Generate contributions for the last 3 months
# This demonstrates how to use the contribution hack scripts

echo "🎯 GitHub Contribution Graph Hack - Quick Example"
echo "=================================================="
echo ""
echo "This example will create backdated commits for the last 3 months."
echo ""

# Calculate dates (last 3 months)
END_DATE=$(date +%Y-%m-%d)
START_DATE=$(date -d "3 months ago" +%Y-%m-%d)

echo "📅 Date Range: $START_DATE to $END_DATE"
echo ""
echo "Choose your method:"
echo "  1. Python (Interactive & Recommended)"
echo "  2. Bash (Quick)"
echo ""
read -p "Select [1/2]: " choice

case $choice in
    1)
        echo ""
        echo "Running Python script with automated input..."
        echo "Using random frequency pattern..."
        cat << EOF | python3 contribute.py
$START_DATE
$END_DATE
1
yes
EOF
        ;;
    2)
        echo ""
        echo "Running Bash script..."
        ./hack_contributions.sh "$START_DATE" "$END_DATE"
        ;;
    *)
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "✅ Example complete!"
echo ""
echo "📊 Check your commits:"
echo "   git log --oneline | head -20"
echo ""
echo "⚠️  To push (this rewrites history!):"
echo "   git push origin $(git branch --show-current) --force"
echo ""
