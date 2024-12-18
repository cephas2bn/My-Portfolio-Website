import os

# Define the project structure
project_structure = {
    "portfolio_website": [
        "app.py",  # Main Flask app file
        "requirements.txt",  # Dependencies
        {"templates": ["base.html", "home.html", "projects.html", "about.html", "contact.html"]},
        {"static": [
            {"css": ["styles.css"]},  # CSS folder
            {"images": ["profile.jpg"]}  # Images folder
        ]}
    ]
}

# Function to create folders and files
def create_structure(base_path, structure):
    for item in structure:
        if isinstance(item, dict):  # If it's a folder with children
            for folder, contents in item.items():
                folder_path = os.path.join(base_path, folder)
                os.makedirs(folder_path, exist_ok=True)
                print(f"Created folder: {folder_path}")
                create_structure(folder_path, contents)
        else:  # If it's a file
            file_path = os.path.join(base_path, item)
            with open(file_path, "w") as f:
                f.write("")  # Create an empty file
            print(f"Created file: {file_path}")

# Run the folder creation
if __name__ == "__main__":
    base_path = os.getcwd()  # Use the current working directory
    for project_name, structure in project_structure.items():
        project_path = os.path.join(base_path, project_name)
        os.makedirs(project_path, exist_ok=True)
        print(f"Created project folder: {project_path}")
        create_structure(project_path, structure)
