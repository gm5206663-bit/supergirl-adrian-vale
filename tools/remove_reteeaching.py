import os
import re

chapters_dir = "/home/user/supergirl-adrian-vale/chapters"

def get_chapter_num(filename):
    m = re.search(r'Chapter_(\d+)_', filename)
    return int(m.group(1)) if m else 0

def remove_canon_re_teaching(text, ch_num):
    """Remove all 'since the roof in November' and 'since the sun' except establishment chapters."""
    
    # Rules:
    # - "since the roof in November" appears ONCE in Ch2 (establishment), ZERO elsewhere
    # - "since the sun" appears ONCE in Ch11 (establishment), ZERO elsewhere
    # - Also remove the extended re-teaching blocks that follow these phrases
    
    changes = []
    lines = text.split('\n')
    new_lines = []
    
    for line_idx, line in enumerate(lines):
        orig_line = line
        
        # Remove "since the roof in November" 
        if 'since the roof in November' in line:
            if ch_num == 2:
                # Keep the first instance in Ch2 (establishment)
                # Only keep it, don't remove
                pass
            else:
                # Remove all instances
                line = line.replace('since the roof in November', '')
                line = re.sub(r'\s{2,}', ' ', line)
                line = re.sub(r'\s+,', ',', line)
                line = re.sub(r',\s*,', ',', line)
                line = line.strip()
                changes.append(f"  Removed 'since the roof in November' (line {line_idx})")
        
        # Remove "since the sun"
        if 'since the sun' in orig_line and 'since the roof' not in orig_line:
            if ch_num == 11:
                # Keep the first instance in Ch11 (establishment)
                pass
            else:
                line = line.replace('since the sun', '')
                line = re.sub(r'\s{2,}', ' ', line)
                line = re.sub(r'\s+,', ',', line)
                line = re.sub(r',\s*,', ',', line)
                line = line.strip()
                changes.append(f"  Removed 'since the sun' (line {line_idx})")
        
        # Remove the extended re-teaching block that follows
        # Pattern: "since the roof in November. Adrian had learned under red sun that red sun can harm..."
        if ch_num != 2 and 'Kara and Adrian had learned' in orig_line:
            # This is the re-teaching block - remove the whole sentence
            # Find the period and remove everything from "Kara and Adrian had learned" to the next sentence
            idx = line.find('Kara and Adrian had learned')
            if idx != -1:
                # Find the next period after this phrase
                period_idx = line.find('.', idx)
                if period_idx != -1:
                    # Check if this is the full sentence or part of a larger block
                    # Remove from "Kara and Adrian had learned" to the period + 1
                    before = line[:idx].strip()
                    after = line[period_idx+1:].strip()
                    if before and after:
                        line = before + '. ' + after
                    elif before:
                        line = before + '.'
                    elif after:
                        line = after
                    else:
                        line = ''
                    changes.append(f"  Removed re-teach block (line {line_idx})")
        
        # Remove "Kara and Adrian had learned since the roof in November, since the sun that ordinary is choice."
        if ch_num != 2 and 'Kara and Adrian had learned since' in orig_line:
            idx = line.find('Kara and Adrian had learned since')
            if idx != -1:
                period_idx = line.find('.', idx)
                if period_idx != -1:
                    before = line[:idx].strip()
                    after = line[period_idx+1:].strip()
                    if before and after:
                        line = before + '. ' + after
                    elif before:
                        line = before + '.'
                    elif after:
                        line = after
                    else:
                        line = ''
                    changes.append(f"  Removed combined re-teach block (line {line_idx})")
        
        # Clean up any leftover artifacts
        line = re.sub(r'\s{2,}', ' ', line)
        line = re.sub(r' ,', ',', line)
        line = re.sub(r'\s+,', ',', line)
        line = line.strip()
        
        if line or orig_line.strip():
            new_lines.append(line)
    
    new_text = '\n'.join(new_lines)
    return new_text, changes

total_changes = 0
for i in range(1, 27):
    fname = f"Chapter_{i:02d}_"
    for fn in os.listdir(chapters_dir):
        if fn.startswith(fname) and fn.endswith('.md'):
            filepath = os.path.join(chapters_dir, fn)
            with open(filepath, 'r') as f:
                text = f.read()
            
            orig_words = len(text.split())
            text, changes = remove_canon_re_teaching(text, i)
            new_words = len(text.split())
            
            if changes:
                with open(filepath, 'w') as f:
                    f.write(text)
                print(f"Chapter {i:02d}: {orig_words} -> {new_words} ({new_words - orig_words:+d})")
                for c in changes:
                    print(c)
                print()
                total_changes += len(changes)
            else:
                print(f"Chapter {i:02d}: no changes")
            break

print(f"\n=== TOTAL CHANGES: {total_changes} ===")
print("=== CANON RE-TEACHING REMOVAL COMPLETE ===")
