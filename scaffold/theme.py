import os
class theme: 
    id=''
    theme_full_path=''
    cache_full_path=''
    body=''

    def theme_path(self,path):
        self.theme_full_path=path
        
    def theme_cache(self,folder,prefix=''):
        self.cache_full_path=path

    def body(self,text):
        self.body=text

    def render(self):
        fp = open(self.theme_full_path+'header.html')
        output=fp.read()
        fp.close()
        output+=self.body
        fp = open(self.theme_full_path+'footer.html')
        output+=fp.read()
        fp.close()  
        return output

