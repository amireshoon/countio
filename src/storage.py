import json
import os.path

class ioStorage:
    def __init__(self):
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
        pass

    def get_account_counts(self, auuid):
        pass

    def store_account(self, name):
        self.accounts.append({
            "uuid" : "test",
            "name" : name
        })

    def __commit(self):
        pass