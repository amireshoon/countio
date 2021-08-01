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
            return self.__throw("No app founded with this name or id", True)
        
        for counts in self.counts:
            if counts['hid'] == hid:
                return counts

    def store_account(self, name):
        if not self.search_in_accounts(name):
            import hashlib
            self.accounts.append({
                "hid" : hashlib.sha1(("auicio"+name+"#$").encode("UTF-8")).hexdigest()[:10],
                "name" : name
            })
            self.__commit()
            return self.search_in_accounts(name)
        return self.__throw("an app already founded with this name", True)

    def remove_account(self, query):
        account = self.search_in_accounts(query)
        if not account:
            return self.__throw("No app founded with this name or id", True)
        
        for i, account in enumerate(self.accounts):
            if account['name'] == query or account['hid'] == query:
                del self.accounts[i]
                break

        self.__commit()
        
        # TODO: Remove counts too
        return self.__throw("App removed successfully", False)

    def increase_count(self, account):
        return self.__do_the_math(account, 1)

    def decrease_count(self, account):
        return self.__do_the_math(account, -1)

    def __do_the_math(self, account, op):
        if not self.search_in_accounts(account):
            return self.__throw("No app founded with this name or id", True)
        
        for i, counts in enumerate(self.counts):
            if counts['hid'] == account:
                if op == 1:
                    self.counts[i]['count'] = self.counts[i]['count'] + 1
                else:
                    self.counts[i]['count'] = self.counts[i]['count'] - 1
                self.__commit()
                return self.get_account_counts(account)
        
        counts = {
            "hid" : account,
            "count" : int(op == 1 if 1 else -1)
        }
        
        self.counts.append(counts)
        self.__commit()
        return self.get_account_counts(account)

    def __commit(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + '/cloud/accounts.json', 'w+') as f:
            json.dump(self.accounts, f)
        with open(os.path.dirname(os.path.abspath(__file__)) + '/cloud/counts.json', 'w+') as f:
            json.dump(self.counts, f)

        self.__reload()

    def __reload(self):
        self.__init__()

    def __throw(self, message, error = True):
        return {
            "error" : error,
            "message" : message,
            "version" : 1.0
        }