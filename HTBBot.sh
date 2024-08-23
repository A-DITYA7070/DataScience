#!/bin/bash
echo "Welcome to SIG HTB EP."
echo -e "\e[31m\nLegal Disclaimer for Bash Script Usage\n\
\n\
This Bash script and all associated files and documentation (collectively, the \"Script\") are proprietary to Synopsys (\"Company\"). The Script is made available strictly for use by employees of Synopsys and its authorized affiliates (\"SIG\"). Unauthorized use, duplication, distribution, or modification of this Script, in whole or in part, without express written permission from Synopsys is strictly prohibited.\n\\n\
Users of this Script must comply with all applicable policies, laws, and regulations, including but not limited to those pertaining to privacy, data protection, and intellectual property rights. The Script is provided \"as is\" without warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability or fitness for a particular purpose.\n\
\n\
The user agrees to use the Script responsibly and ethically. Any misuse, abuse, or unauthorized use of the Script will be subject to legal action, including but not limited to disciplinary action, termination of employment, and legal prosecution to the fullest extent of the law.\n\
\n\
By using the Script, the user acknowledges and agrees to these terms and conditions. If you do not agree to these terms, do not use the Script.\n\\e[0m"

echo -e "\e[38;5;214mIf you have issues running the script start here.\e[0m https://overthewire.org/wargames/bandit/"

ctrl_c_handler() {
    echo -e "\nCaught CTRL+C. Exiting gracefully."
    exit 1
}

# Trap CTRL+C (SIGINT) and call the handler function
trap ctrl_c_handler SIGINT

echo "Select an option:"
echo "1. Join HTB"
echo "2. Academy"
echo "3. Dedi and Pro"
echo "4. Revoke"
echo "5. Print Lab Info"
echo "6. Help"
read -p "Enter your choice: " choice

case $choice in
    1)  # Join HTB
        read -p "Enter your corporate email: " email
        curl -H "Content-Type: application/json" -d "{ \"email\": \"$email\" }" 'https://prod-156.westus.logic.azure.com:443/workflows/6be562b074324d31b8a508582d78815c/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=ZQk5Yy51ck2mr3q7cKMUC8IGF1AapxDSpkWLf50puuo'
        ;;
    2)  # Academy
        read -p "Enter your email: " email
        read -p "Enter time in days: " time
        read -p "Enter a valid reason (Reason can be VA, NSRT, Playground): " reason
        curl -H "Content-Type: application/json" -d "{ \"email\": \"$email\", \"lab\":\"2125\", \"time\":\"$time\", \"reason\":\"$reason\" }" 'https://prod-167.westus.logic.azure.com:443/workflows/e4477110f3de40dfbaf03338223bc101/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=IPI5CYjcE1wQGGE0FoIGIz5aTumbb7dKw0NW8F7KZdM'
        ;;
    3)  # Dedi and Pro
        read -p "Enter your email: " email
        read -p "Enter lab ID: " lab_id
        read -p "Enter time in days: " time
	read -p "Enter reason (Any reason): " reason
        curl -H "Content-Type: application/json" -d "{ \"email\": \"$email\", \"lab\":\"$lab_id\", \"time\":\"$time\", \"reason\":\"$reason\" }" 'https://prod-65.westus.logic.azure.com:443/workflows/c36656cd6646480e92db253c5185a468/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=JzaGQVKtx7AuPJJrMacoHbdE1ZdLOdFFl5WV7WaClqs'
	;;
    4) # Revoke
	read -p "Enter your email: " email
	read -p "Enter lab ID (e.g., 1300): " lab_id
	curl -H "Content-Type: application/json" -d "{ \"email\": \"$email\", \"lab\":\"$lab_id\" }" 'https://prod-113.westus.logic.azure.com:443/workflows/4bb044e9d7dd4f22b3a304f4653b504d/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=oHfyvnUgEmQM0V33i2_HFxHpMb-g3aEFvT5Yv3pEsuM'
	;;
    5) # Print Lab Info
	curl 'https://prod-177.westus.logic.azure.com:443/workflows/faf738349b684a02a8e5fa8d1f587d9d/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=X2mSCyNtwAR3Q-UMZq8Ln3u_jRdHSVV69KPKmKTxm9U'
	;;
    6) # Help
	echo "Help Menu: Each option in this script performs a specific operation related to HTB:"
	echo "1. Join HTB: Register with your email."
	echo "2. Academy: Request access to a Academy lab for a specified time and reason."
	echo "3. Dedi and Pro: Request access to dedicated and professional labs with predefined reason."
	echo "4. Revoke: Revoke access to a specific lab. (Use for every lab)"
	echo "5. Print Lab Info: Get information about the current status of the labs."
	;;
*)
echo "Invalid option."
;;
esac
echo -e "\e[32m\n[*]Script execution complete. Please check the Teams channel for updates.\e[0m"
