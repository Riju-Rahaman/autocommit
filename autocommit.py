import os
import time
import random
import git

# Set the path to your local git repository
repo_dir = os.getcwd()  # Using current working directory
os.chdir(repo_dir)

# Initialize the Git repository
repo = git.Repo(repo_dir)

# Define a function for auto-commit
def auto_commit():
    try:
        # Create a random change in a file (you can customize this part)
        with open('file.txt', 'a') as f:
            f.write(f'Auto commit: {random.randint(1, 1000)}\n')

        # Stage the changes
        repo.git.add('file.txt')

        # Commit the changes
        repo.index.commit(f'Auto commit {random.randint(1, 1000)}')

        # Push the changes to the remote
        origin = repo.remote(name='origin')
        origin.push()

        print("Commit and push successful.")
    except Exception as e:
        print(f"Error: {e}")

# Run the commit function every 10 minutes
while True:
    auto_commit()
    time.sleep(0.001)  # Sleep for 600 seconds (10 minutes)
