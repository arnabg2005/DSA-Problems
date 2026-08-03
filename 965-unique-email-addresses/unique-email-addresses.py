class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        unique_emails = set()
        
        for email in emails:
            local, domain = email.split('@')
            
            if '+' in local:
                local = local.split('+')[0]
                
            local = local.replace('.', '')
            
            unique_emails.add((local, domain))
            
        return len(unique_emails)
