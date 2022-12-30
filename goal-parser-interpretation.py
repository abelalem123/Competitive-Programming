class Solution:
    def interpret(self, command: str) -> str:
        ans=""
        for i in range(len(command)):
           if command[i]=="G":
               ans=ans+command[i]
           elif command[i]=="(":
               if command[i+1]==")":
                   ans=ans+"o"
               else:
                   ans=ans+"al"
           else:
               pass
        return ans
                
       
