import sys
import re

filename = "penTest.html"

with open(filename, "r", encoding="utf-8") as f:
    content = f.read()

issues = []

# Example check 1: inline <script> tags
if re.search(r"<script.*?>", content, re.IGNORECASE):
    issues.append("Inline <script> tag found")

# Example check 2: inline event handlers like onclick=
if re.search(r'onclick\s*=', content, re.IGNORECASE):
    issues.append("Inline event handler (onclick) found")

if issues:
    print("Security issues found in penTest.html:")
    for issue in issues:
        print(f"- {issue}")
    sys.exit(1)  # Exit with error to fail the workflow
else:
    print("No issues found in penTest.html")