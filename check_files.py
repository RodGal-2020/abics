import os

file_path = "support/server.py"

if not os.path.exists(file_path):
    # Launch error and stop execution
    print("Error: %s does not exist" % file_path)
