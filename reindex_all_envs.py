import subprocess

def run_drush_on_environments(site, command):
    # List of Pantheon environments
    environments = ['dev', 'test']  # Add more environments if needed
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

site = 'd10-lapides'  # Replace with your Pantheon site name
command = 'sapi-i'  # Replace with the Drush command you want to run
run_drush_on_environments(site, command)