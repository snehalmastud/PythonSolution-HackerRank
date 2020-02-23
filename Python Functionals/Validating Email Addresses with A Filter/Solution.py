def fun(s):
    if s.count('@')==1 and s.count('.')==1:
        username, websites = s.split('@')
        website, extension = websites.split('.')
        if  not (len(username)>0 and len(website)>0 and website.isalnum() and len(extension)<=3):
            return False        
        for i in username:
            if  not (i.isalpha() or i.isdigit() or i in ['-','_']):
                return False         
        return True
    return False
    
