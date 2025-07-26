#!/bin/bash
echo "Updating packages..."
sudo apt update && sudo apt upgrade -y
echo "Done!"
echo "Cleaning up..."
sudo apt autoremove -y
echo "Cleanup complete!"
echo "System packages have been updated successfully."
echo "You may need to restart your system for all changes to take effect."
echo "Exiting script."
exit 0
# End of script
# This script updates the system packages on a Debian-based Linux distribution.
# It uses apt to update the package list, upgrade installed packages, and clean up unnecessary files.
# Make sure to run this script with appropriate permissions (e.g., as a user with sudo privileges).
# Save this script as Update_System_Packages.sh and run it in your terminal.
# Usage: ./Update_System_Packages.sh
# Ensure you have the necessary permissions to execute this script.
# You can also schedule this script to run periodically using cron jobs for regular updates.        