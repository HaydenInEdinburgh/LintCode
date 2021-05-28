class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        # write your code here
        if not accounts:
            return []
        self.initialize(len(accounts))
        email_to_ppl = self.get_email_to_ids(accounts)
        #union
        for email, ids in email_to_ppl.items():
            root_id = ids[0]
            for id in ids[1:]:
                self.union(id, root_id)

        id_to_email_set = self.get_id_to_email_set(accounts)
        res = []
        for uid, email_set in id_to_email_set.items():
            name = accounts[uid][0]
            res.append([name, *sorted(email_set), ])
        return res

    def get_id_to_email_set(self, accounts):
        id_to_email = {}
        for user_id, account in enumerate(accounts):
            root_id = self.find(user_id)
            email_set = id_to_email.get(root_id, set())
            for email in account[1:]:
                email_set.add(email)

            id_to_email[root_id] = email_set
        return id_to_email

    def get_email_to_ids(self, accounts):
        email_to_ppl = {}
        for idx, record in enumerate(accounts):
            name = record[0]
            emails = record[1:]
            for email in emails:
                if email not in email_to_ppl:
                    email_to_ppl[email] = [idx]
                else:
                    email_to_ppl[email].append(idx)

        return email_to_ppl

    def union(self, a, b):
        self.father[self.find(a)] = self.find(b)

    def initialize(self, n):
        self.father = {}
        for i in range(n):
            self.father[i] = i

    def find(self, user_id):
        path = []
        while user_id != self.father[user_id]:
            path.append(user_id)
            user_id = self.father[user_id]

        for u in path:
            self.father[u] = user_id

        return user_id