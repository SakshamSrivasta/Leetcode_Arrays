class Solution:
    def interpret(self, command: str) -> str:
        res=""
        for i in range(len(command)):
            if command[i] =="(" and command[i+1]==")":
                res+="o"
            elif command[i]=="(" and command[i+1]!=")":
                res+="al"
            elif command[i]=="G":
                res+="G"
        return res
        