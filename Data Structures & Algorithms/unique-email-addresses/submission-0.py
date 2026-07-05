class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        mySet = set()

        for email in emails:
            #first break email into local + domain
            i = 0
            local = ''
            domain = ''
            for c in email:
                if c == '@':
                    break
                i += 1

            print("i = ", i)
            local = email[:i]
            print("local = ", local)
            domain = email[i+1:]
            print("domain = ", domain)

            #simplify local
            temp = ''
            for i in range(len(local)):
                if local[i] == '+':
                    break
                elif local[i] == '.':
                    continue
                
                temp += local[i]

            print("temp = ", temp)

            newEmail = temp + "@" + domain
            print("newEmail = ", newEmail)
            mySet.add(newEmail)

        return len(mySet)

