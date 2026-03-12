from collections import deque

# Step 1: Initialize
application_inbox = deque()
processed_history = []

# Step 2: Ingest data
startup_names = [" TechCorp ", "bio-gen", " AI Labs ", " FinTechX "]

for name in startup_names:
    clean_name = name.strip().lower()
    application_inbox.append(clean_name)

# Step 3: Process (FIFO)
while application_inbox:
    app = application_inbox.popleft()
    print("Approving:", app)
    processed_history.append(app)

# Step 4: Undo (LIFO)
mistake = processed_history.pop()
print("Reverting approval for:", mistake)