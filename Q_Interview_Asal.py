input =['ahmad.droobi1999@gmail.com','ahmaddroobi1999@gmail.com','ahmad_droobi1999@gmail.com','ahmad.droobi.1999@gmail.com','mohammad.aa@gmail.com']
# expected out = ahmaddroobi1999@gmail.com,mohammadaa@gmail.com

class Solution ():
   # splited_email =[]
   def uniqe_email(self,input):
       mail_Set = set()

       for email in input :
           splited_email =email.split('@')
           first_opp=splited_email[0].replace('.', "")
           first_opp=first_opp.replace('_', "")
           first_opp=first_opp+"@"+splited_email[1]
           mail_Set.add(first_opp)





       return mail_Set


s=Solution()
print (s.uniqe_email(input =['ahmad.droobi1999@gmail.com','ahmaddroobi1999@gmail.com','ahmad_droobi1999@gmail.com','ahmad.droobi.1999@gmail.com','mohammad.aa@gmail.com']
))
