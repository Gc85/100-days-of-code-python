import os

base_dir = "100-days-of-code-python"

# Ensure base directory exists
if not os.path.exists(base_dir):
    os.makedirs(base_dir)

for day in range(1, 101):
    folder_name = f"Day{day:03d}"
    folder_path = os.path.join(base_dir, folder_name)
    os.makedirs(folder_path, exist_ok=True)

    # notes.md content
    notes_content = f"""# Day {day:03d} – Notes

## 🔑 Key Concepts Learned

_TODO: Fill in what you learned today._

## 💡 Reflection

_TODO: Add personal thoughts or summaries._
"""

    # project.py placeholder
    project_content = f"""# Day {day:03d} - Project Placeholder

# TODO: Implement today's project here.
"""

    # Write files
    with open(os.path.join(folder_path, "notes.md"), "w", encoding="utf-8") as notes_file:
        notes_file.write(notes_content)

    with open(os.path.join(folder_path, "project.py"), "w", encoding="utf-8") as project_file:
        project_file.write(project_content)

print("✅ 100 folders generated with notes.md and project.py placeholders.")
