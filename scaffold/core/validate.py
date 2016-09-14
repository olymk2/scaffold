#!/usr/bin/python -O 
#Copyright (C) 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015 scaffold team
#
#This file is part of Scaffold web framework
#
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.
#
#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#In addition, as a special exception, Oliver Marks gives permission to link
#the code of its release of usm with the OpenSSL project's "OpenSSL" library
#(or modified versions of the "OpenSSL" library that use the same license
#as the original version), and distribute the linked executables.

class validate():
    #do not use 0 this can be used as a default to indicate the value has not run through the validator
    MATCH_EXACT = 1       #1 = exact match 
    MATCH_INSERTED = 2    #2 = inserted match, character was inserted like a space
    MATCH_REMOVAL = 3     #3 = invalid characters removed
    MATCH_STOPPED = 4     #4 = stoped at invlaid match
    MATCH_NULL = 5        #5 = no Value when one required
    MATCH_FAILURE = 6     #6 = fatal error no result returned or no result passed
    seperators=('.', ',', ':')
    numeric=('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    
    alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    alphabet+=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
    multi_line=(chr(10),chr(13))
    decimal_number=('.',)+numeric
    currency=(',',)+decimal_number
    hexadecimal_number=numeric+('a','b','c','d','e','f')
    date=("-",":","/")+numeric
    alpha_numeric=alphabet+numeric
    alpha_simple=alpha_numeric+('_','-','.',' ')
    alpha_default=alpha_numeric+multi_line+('.','_','-',' ',':',",","=","\\","%",";","/","+","*","[","]","(",")","!","?")
    
    filepath=alpha_default+('/','@')
    filepathlist=filepath+('\\','n')
    email=alpha_default+('@',)
    url=alpha_default+('@','&','?',':','/',)
    
    format_list={}
    format_list["multiline"]=(chr(10),chr(13))
    format_list["z"]=()
    
    format_list["n"] = ('0','1','2','3','4','5','6','7','8','9') #numeric
    format_list["c"] = (',',) + format_list["n"] #decimal_number
    format_list["l"] = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',)
    format_list["l"] += ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',)
    format_list["t"] = format_list["n"] + format_list["l"] #alpha numeric
    format_list["a"] = format_list["t"] + ('_','-','.',' ')
    format_list["T"] = format_list["t"] + format_list["multiline"] + ('.','_','-',' ',':',",","=","\\","%",";","/","+","*","[","]","(",")","!","?")
    
    format_list["e"] = format_list["t"] + ('-','_','.')
    format_list["u"] = format_list["e"] + ('&','?',':','.','/',)
    format_list["f"] = format_list["e"] + ('/',)
    format_list["F"] = format_list["f"] + ('\\','\n',)
    format_list["D"] = format_list["e"] + ("-",":","/",)
    format_list["d"] = format_list["n"] + ('.',)
    format_list["d"] = format_list["n"] + ('.',)
    format_list["i"] = format_list["n"] + ('.','-')
                     
    format_list["h"] = format_list["n"] + ('a','b','c','d','e','f',)
    format_list["s"] = ('.',',',':','|',)
    format_list["p"] = ('h')
    
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.text = ""
        self.textpos = 0
        self.textlen = 0

        
        self.format = ""
        self.formatpos = 0
        self.formatchar = ""
        self.formatlen = 0
        
        self.match = 1
        
    def validate(self, text, format, null=True):
        """return if result matches rules or not
            params
                text: value to validate
                format: format to validate against
                null: allow nulls
            return
                tuple: match type, result, original
            """
        self.reset()
        self.text = text
        self.textlen = len(text)
        if format == None:
            format = "t*"
        self.formatlen = len(format)-1
        self.format = format
        self.formatchar = format[0]
        result = ""
        
        #print "**********************Validateing***********************"
        #print "unvalidated value ="+str( self.text)
        while self.formatchar != "" and self.textpos < self.textlen:
            if self.format[self.formatpos] == "[":
                self.make_list()

            if self.format[self.formatpos] == "p":
                result = self.textparser()
            
            elif self.format_list.get(self.format[self.formatpos]):  
                result += self.handle_data()
            else:
                result += self.validate_list(format[self.formatpos:], (self.formatchar,))
                #self.format_pos_increment()
        #print "validation result ="+str(result)
                

        #how accurate was the match 
        #0 = exact match 
        #1 = inserted match, character was inserted like a space
        #2 = invalid characters removed
        #3 = stoped at invlaid match
        #4 = no Value when one required
        #5 = insecure
        #6 = too short
        #<10=fatal error no result returned or no result passed

        result_length=len(result)
        #empty fields not allowed so return an error message
        if null is False and result_length == 0 and self.textlen == 0:
            print("empty fields not allowed so return an error message")
            if result_length == 0:
                self.match = 10
            if self.textlen == 0:
                self.match = self.MATCH_NULL
            return self.match, result, self.text

        #empty fields allowed so dont return error
        if self.textlen != 0:
            if result == self.text:#result exactly matched input 100% match
                self.match = self.MATCH_EXACT     #passed validation exactly
            else:   
                self.match = self.MATCH_INSERTED  #characters removed
        else:
            self.match = 1
        return self.match, result, self.text

    def textparser(self):
        self.format_pos_increment()
        result = ''
        #if self.format[self.formatpos]=="h":
            #print "************** validate html parser started ***************"
            #parser=html_tags()
            #result=parser.scan(self.text)
            #print "************** validate html parser ended ***************"
            #self.textpos=self.textlen
        #print "parser result"+result
        return result

    #get data using list of values
    def handle_data(self):
        result = ""
        if self.format_list[self.format[self.formatpos]] == 'p':
            if self.textlen > 5:
                result += self.validate_list(self.format[self.formatpos:], self.alpha_simple)
            else:
                self.textpos = self.textlen + 1
        else:
            
            result+=self.validate_list(self.format[self.formatpos],self.format_list[self.format[self.formatpos]])
        return result

    def make_list(self):
        custom = ""
        pos = self.formatpos + 1
        tmp_format_pos = self.formatpos
        while pos<self.formatlen and self.format[pos] != ']':
            if self.format_list.get(self.format[pos]):
                self.format_list["z"] += self.format_list.get(self.format[pos])
            else:
                self.format_list["z"] += self.format[pos],
            pos += 1
        pos += 1
        
        self.format = "z" + self.format[pos:]

        #print "finished format " + str(self.format)
        self.formatpos = 0
        self.formatlen = len(self.format) - 1

    def format_pos_increment(self):
        if self.formatpos < self.formatlen:
            self.formatpos += 1
            self.formatchar = self.format[self.formatpos]
        else:
            self.formatchar = ""

    def text_pos_increment(self):
        if self.textpos < self.textlen:
            self.textpos += 1

    def validate_character(self):
        result = ""
        if self.formatchar == self.text[self.textpos]:
            result += self.text[self.textpos]
            self.text_pos_increment()
        self.format_pos_increment()
        return result

    def get_number(self):
        n = ""
        while self.formatchar in self.numeric:
            n += str(self.formatchar)
            self.format_pos_increment()
        self.formatpos -= 1
        if n == "":
            n = "0"
        return int(n)
        
    def validate_list(self, format, character_list):#validate a list of values
        result = ""
        self.format_pos_increment()
        if self.textpos < self.textlen:
            if self.formatchar == "*":
                result += self.loopmatch(character_list)
            elif self.formatchar in self.numeric:
                result += self.countmatch(character_list, self.get_number())
            else:          
                result += self.charmatch(character_list)
        return result
    
    def loopmatch(self, character_list):
        result = ""
        match = True
        for pos in range(self.textpos, self.textlen):
            if match == True:  
                if self.text[pos] in character_list:
                    result += self.text[self.textpos]
                    self.text_pos_increment()
                else:
                    match = False
        self.format_pos_increment()
        return result
    
    def countmatch(self, list, size):
        result = ""
        length = len(self.text[self.textpos:])
        if length > size:
            length = size

        #loop the specified number of charcter, or less if less characters exist
        match = True
        for pos in range(self.textpos, self.textpos + length):
            if match is True:                  #loop while still correct datatype
                if self.text[pos] in list:     #is this letter in the match list
                    result += self.text[pos]   #build up the return value
                    self.text_pos_increment()  #move to next character
                else:                          #not in match list so stop matching
                    match = False              #this character stopped matching move to next value
        self.format_pos_increment()            #move to next formatting character
        return result
    
    def seperator(self,let):
        result = ""
        self.format_pos_increment()
        if let not in self.alpha_numeric:
            result = self.formatchar
            self.text_pos_increment()
            self.format_pos_increment()
        return result
    
    def charmatch(self, character_list):
        if self.text[self.textpos] in character_list:
            result = self.text[self.textpos]
            self.text_pos_increment()
            return result
        else:
            return ""



