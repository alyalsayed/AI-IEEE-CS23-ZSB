# https://leetcode.com/problems/unique-email-addresses/
# set is a data structure that only contains unique elements
# using spilt and replace we get the local name and domain name
# then we add the local name and domain name to the set
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0].replace('.', '')
            unique_emails.add(local_name + '@' + domain_name)
        return len(unique_emails)