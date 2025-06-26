from accounts import AccountManager
from epic_launcher import EpicLauncher

def main():
    account_manager = AccountManager()
    epic_launcher = EpicLauncher()

    # Load accounts (this could be from a file or hardcoded for simplicity)
    accounts = [
        {"email": "user1@example.com", "password": "password1"},
        {"email": "user2@example.com", "password": "password2"},
        {"email": "user3@example.com", "password": "password3"},
        {"email": "user4@example.com", "password": "password4"},
        {"email": "user5@example.com", "password": "password5"},
    ]

    for account in accounts:
        account_manager.add_account(account["email"], account["password"])

    while True:
        print("Select an account to log in:")
        for idx, account in enumerate(account_manager.get_accounts()):
            print(f"{idx + 1}: {account['email']}")
        print("0: Exit")

        choice = input("Enter your choice: ")
        if choice == '0':
            break

        try:
            account_index = int(choice) - 1
            selected_account = account_manager.get_accounts()[account_index]
            epic_launcher.logout()
            epic_launcher.login(selected_account["email"], selected_account["password"])
            print("Logged in successfully.")
        except (ValueError, IndexError):
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()