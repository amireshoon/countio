import json
import os.path
from pathlib import Path

class ioStorage:
    def __init__(self):
        if not Path(os.path.dirname(os.path.abspath(__file__)) + '/cloud/accounts.json').is_file():
            self.accounts = []
            self.counts = []
            self.__commit()
        
        self.accounts = self.__get_accounts()
        self.counts = self.__get_counts()

    def __get_accounts(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/cloud/accounts.json') as f:
            accounts = json.load(f)
            return accounts

    def __get_counts(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/cloud/counts.json') as f:
            counts = json.load(f)
            return counts
            
    def search_in_accounts(self, query):
        for account in self.accounts:
            if account['name'] == query or account['hid'] == query:
                return account
        return {}
        

    def get_account_counts(self, hid):
        if not self.search_in_accounts(hid):
            return "No account founded"
        
        for counts in self.counts:
            if counts['account'] == hid:
                return counts

    def store_account(self, name):
        if not self.search_in_accounts(name):
            import hashlib
            self.accounts.append({
            "hid" : hashlib.sha1(("auicio"+name+"#$").encode("UTF-8")).hexdigest()[:10],
            "name" : name
            })
            self.__commit()
            return "created"
        return "a user already exists with this name"

    def __commit(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/cloud/accounts.json', 'w+') as f:
            json.dump(self.accounts, f)
        with open(os.path.dirname(os.path.abspath(__file__)) + '/cloud/counts.json', 'w+') as f:
            json.dump(self.counts, f)

        self.__reload()

    def __reload(self):
        self.__init__()