#!/usr/bin/env python3
"""
Update associative-network.md with sdlc-review and xlsx skills.
- Add sdlc-review to DEVOPS domain (increase count by 1).
- Add xlsx to PRODUCTIVITY domain (increase count by 1).
- Update total rows accordingly.
- Ensure both skill entries follow the table format.
"""
import re

ASSOCIATIVE_NETWORK_PATH = "C:\\Users\\syahd\\AppData\\Local\\hermes\\skills\\cognitive-architecture\\mind-map-cognition\\references\\associative-network.md"

def update_associative_network():
    with open(ASSOCIATIVE_NETWORK_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if sdlc-review is already present in DEVOPS section
    # If not, add it.
    # Find DEVOPS section header and its domain count.
    devops_pattern = r'(## Domain:\s*DEVOPS \((\d+) skills\)\n\|\|\| Skill \| Tags \| Edges \|\n\|\|-------\|------\|-------\|\n)(.*?)(?=\n##|\n---)'
    devops_match = re.search(devops_pattern, content, re.DOTALL)
    if devops_match:
        header = devops_match.group(1)
        body = devops_match.group(2)
        old_count = int(devops_match.group(2))
        # Ensure sdlc-review not already present
        if "sdlc-review" not in body:
            # Append new skill row at the end of body (before the section boundary)
            new_skill = "|| **sdlc-review** | kanban, review, quality, verification | kanban-orchestrator, kanban-worker ||\n"
            new_body = body.rstrip() + "\n" + new_skill
            new_header = f"## Domain: DEVOPS ({old_count + 1} skills)\n||| Skill | Tags | Edges |\n|||-------|------|-------|\n"
            new_section = new_header + new_body
            # Replace the old DEVOPS section
            content = re.sub(devops_pattern, new_section, content, flags=re.DOTALL)
            print("Added sdlc-review to DEVOPS domain")

    # Find PRODUCTIVITY section header and its domain count
    prod_pattern = r'(## Domain:\s*PRODUCTIVITY \((\d+) skills\)\n\|\|\| Skill \| Tags \| Edges \|\n\|\|-------\|------\|-------\|\n)(.*?)(?=\n##|\n---)'
    prod_match = re.search(prod_pattern, content, re.DOTALL)
    if prod_match:
        header = prod_match.group(1)
        body = prod_match.group(2)
        old_count = int(prod_match.group(2))
        if "xlsx" not in body:
            # Find a good insertion point (just before the closing of the section before next domain)
            new_skill = "|| **xlsx** | excel, spreadsheet, xlsx, csv, openpyxl, productivity | docx, pdf, powerpoint ||\n"
            new_body = body.rstrip() + "\n" + new_skill
            new_header = f"## Domain: PRODUCTIVITY ({old_count + 1} skills)\n||| Skill | Tags | Edges |\n|||-------|------|-------|\n"
            new_section = new_header + new_body
            content = re.sub(prod_pattern, new_section, content, flags=re.DOTALL)
            print("Added xlsx to PRODUCTIVITY domain")

    # Update the summary section
    # Find the "## Summary" section and the line with "|| **Total rows** | **170** ||"
    # We need to increase the total rows and unique skills count based on what we added.
    # The script counts unique skills + cross-domain duplicates.
    # For simplicity, just increase total rows by 2 and total unique skills by 2.
    # However, we need to be careful not to break the parsing of the script.
    # The verify_headers script expects the total rows and the note to match.
    # We'll modify the summary part manually using regex to update the totals.

    # Find the Summary block that contains the table and the note line.
    summary_pattern = r'(## Summary\n\|\|\|\| Domain \| Count \|\n\|\|--------\|-------\|\n.*?)(?=\n\n|\n---)'
    summary_match = re.search(summary_pattern, content, re.DOTALL)
    if summary_match:
        summary_block = summary_match.group(1)
        # Update the PRODUCTIVITY count
        summary_block = re.sub(r'\|\|\| PRODUCTIVITY \| (\d+) \|\|', lambda m: f"||| PRODUCTIVITY | {int(m.group(1)) + 1} ||", summary_block)
        # Update the DEVOPS count
        summary_block = re.sub(r'\|\|\| DEVOPS \| (\d+) \|\|', lambda m: f"||| DEVOPS | {int(m.group(1)) + 1} ||", summary_block)
        # Find total rows line and note line
        total_rows_match = re.search(r'(\|\|\| \*\*Total rows\*\* \| \*\*\d+\*\* ||)', summary_block)
        if total_rows_match:
            old_total = int(re.search(r'\*\*Total rows\*\* \| \*\*(\d+)\*\*', summary_block).group(1))
            new_total = old_total + 2
            summary_block = re.sub(r'\*\*Total rows\*\* \| \*\*\d+\*\*', f"**Total rows** | **{new_total}**", summary_block)
        # Update note line to reflect new unique count
        note_match = re.search(r'(\*\*Note\*\*.*)', summary_block)
        if note_match:
            note_line = note_match.group(1)
            # Update unique skills count by adding 2
            note_line = re.sub(r'(\d+) unique skills', lambda m: f"{int(m.group(1)) + 2} unique skills", note_line)
            summary_block = summary_block.replace(note_match.group(1), note_line)
        # Replace the original summary block in content
        content = content[:summary_match.start()] + summary_block + content[summary_match.end():]
        print("Updated summary section")

    # Write back
    with open(ASSOCIATIVE_NETWORK_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("Associative network updated successfully.")

if __name__ == "__main__":
    update_associative_network()