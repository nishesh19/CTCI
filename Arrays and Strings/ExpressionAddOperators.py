class Solution:
    def addOperators(self, num: str, target: int) :
        if not num:
            return []
        
        self.target = target
        self.allOperations = []

        self.addOperatorsRecur(num,0,0,"",0,None)
        
        return self.allOperations
    
    def addOperatorsRecur(self,num,curr_value,prev_num,curr_expr,i,last_op):
        if i == len(num):
            if curr_value == self.target:
                self.allOperations.append(curr_expr)
            return 
        
        # for j in range(i,len(num)):
        #     if j!=i and num[j] == '0':
        #         break
        curr_num = num[i]
        self.addOperatorsRecur(num,curr_value+int(curr_num),int(curr_num),f"{curr_expr}+{curr_num}",i+1,"+")
        self.addOperatorsRecur(num,curr_value-int(curr_num),int(curr_num),f"{curr_expr}-{curr_num}",i+1,"-")
        
        if last_op == "-":
            curr_value += prev_num
            temp_value = int(curr_num)*prev_num
            curr_value -= temp_value
        elif last_op == "+":
            curr_value -= prev_num
            temp_value = int(curr_num)*prev_num
            curr_value += temp_value
        else:
            curr_value *= int(curr_num)
                
        self.addOperatorsRecur(num,curr_value,curr_num,f"{curr_expr}*{curr_num}",i+1,"*")

num = "105"
target = 5
print(Solution().addOperators(num,target))

