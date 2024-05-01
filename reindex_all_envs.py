import subprocess
import json
# Function to get all environments for a Pantheon site
def get_all_environments(site):
    # Run Terminus command to get environments JSON
    terminus_command = f'terminus site:environments {site} --format=json'
    process = subprocess.Popen(terminus_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    # Parse JSON output to extract environment names
    if output:
        environments = json.loads(output)
        return [env['id'] for env in environments]
    else:
        print(f"Error: {error.decode()}")
        return []
# Function to run Terminus Drush command on each environment
def run_drush_on_environments(site, command):
    # Get all environments for the site
    environments = get_all_environments(site)
    for env in environments:
        # Construct the Terminus Drush command
        terminus_command = f'terminus drush {site}.{env} -- {command}'
        # Run the Terminus Drush command using subprocess
        process = subprocess.Popen(terminus_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        # Print output and error messages
        print(f"Output for {site}.{env}:")
        print(output.decode())
        if error:
            print(f"Error for {site}.{env}:")
            print(error.decode())
        print()
# Example usage
site = 'd10-lapides'  # Replace with your Pantheon site name
command = 'sqpi-i'  # Replace with the Drush command you want to run
run_drush_on_environments(site, command)