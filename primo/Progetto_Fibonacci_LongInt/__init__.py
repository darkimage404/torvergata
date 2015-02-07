class number:
    def __init__(self,numb):
        self.str=str()
        self.len=len(self.str)
    def somma(self,numb):
        a=number(numb)
        final=''
        if self.len>=a.len:
            carry=0
            for i in range(a.len-1,-1,-1):
                    resBit=str(int(self.str[i])+int(a.str[i])+carry)
                    if i!=0:
                        if len(resBit)>1:
                            final=final+resBit[0]
                            carry=resBit[1]
                        else:
                            final=final+resBit
                            carry=0
                    else:
                        final=final+resBit              
        else:
            carry=0
            for i in range(self.len-1,-1,-1):
                resBit=str(int(self.str[i])+int(a.str[i])+carry)
                if i!=0:
                    if len(resBit)>1:
                        final=final+resBit[0]
                        carry=resBit[1]
                    else:
                        self.string[i]=final+resBit
                        carry=0
                else:
                    final=final+resBit
                    
            
            
                

    
    
    
    
    