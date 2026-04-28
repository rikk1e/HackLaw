import re
from pathlib import Path
from collections import Counter

# a standard use of regex to count obligative and permissive phrases 
text = Path("assets/regex_text/output.md").read_text(encoding="utf-8")

pattern = r"\b(must|must not|may|should|required|requires|permitted|prohibited|liable|offence)\b"

matches = re.findall(pattern, text, flags=re.IGNORECASE)
counts = Counter(m.lower() for m in matches)

print(counts)
# because this is pretty easy to do with just ctrl-f, we can try finding all the references to subsections
section_pattern = r"\b(?:s|section|sections|subsection|subsections)\s+\d+[A-Z]?(?:\([^)]+\))*\b"

sections = re.findall(section_pattern, text, flags=re.IGNORECASE)

section_counts = Counter(s.lower() for s in sections)

for section, count in section_counts.most_common(10):
    print(section, count)
