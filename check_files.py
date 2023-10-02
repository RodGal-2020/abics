import os

file_path = "userinterface/ABICS.py"

if not os.path.exists(file_path):
    # Launch error and stop execution
    print("Error: %s does not exist" % file_path)
