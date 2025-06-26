class AccountManager:
    def __init__(self):
        self.accounts = []

    def add_account(self, email, password):
        self.accounts.append({'email': email, 'password': password})

    def remove_account(self, email):
        self.accounts = [account for account in self.accounts if account['email'] != email]

    def get_account(self, index):
        if 0 <= index < len(self.accounts):
            return self.accounts[index]
        return None

    def list_accounts(self):
        return [account['email'] for account in self.accounts]