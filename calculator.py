class Equation():

    def __init__(self, equation, parts=[]):
        self.parts=parts
        self.equation = equation
        
    def split_equation(self):
        number=None
        equation=self.equation
        for symbol in range(len(equation)):
            if equation[symbol] in '!+-*/()':
                if number:
                    self.parts.append(number)
                    number=None
                self.parts.append(equation[symbol])
            elif equation[symbol]==' ':
                pass
            else:
                if number==None:
                    number=0
                number*=10
                number+=int(equation[symbol])
        if number:
            self.parts.append(number)   
                                       
    def subs(self):
        self.lefts=[]
        self.rights=[]
        for i in range(len(self.parts)):
            if self.parts[i] == '(':
                self.lefts.append(i)
            if self.parts[i] == ')':
                self.rights.append(i)
        self.pairs=[]
        for i in self.rights:
            for x in self.lefts[::-1]:
                if x!=None and i!=None and x<i:
                    self.pairs.append([x, i])
                    self.rights[self.rights.index(i)]=None
                    self.lefts[self.lefts.index(x)]=None
                    break
        for pair in self.pairs:
            move_k=0
            sub_equation = Equation(None, self.parts[pair[0]+1:pair[1]])
            self.parts = self.parts[:pair[0]] + [sub_equation] + self.parts[pair[1]+1:]
            move_k+=pair[1]-pair[0]
            for i in range(len(self.pairs)):
                if pair[1]<self.pairs[i][0]:
                    self.pairs[i][0]-=move_k
                if pair[1]<self.pairs[i][1]:
                    self.pairs[i][1]-=move_k              
    
    def solve(self):
        self.subs()
        parts=self.parts
        for i in range(len(parts)):
            if isinstance(parts[i], Equation):             
                parts[i] = parts[i].solve()
        move_k=0
        for i in range(len(parts)):
            i-=move_k
            if parts[i]=='!':
                new_part=1
                for x in range(parts[i-1]):
                    new_part*=(x+1)
                for z in range(2):
                    parts.pop(i-1)
                parts.insert(i-1, new_part)
                move_k+=1
        move_k=0
        for i in range(len(parts)):
            i-=move_k
            if parts[i]=='*':
                new_part=parts[i-1]*parts[i+1]
                for z in range(3):
                    parts.pop(i-1)
                parts.insert(i-1, new_part)
                move_k+=2
                i-=1
            if parts[i]=='/':
                new_part=parts[i-1]/parts[i+1]
                for z in range(3):
                    parts.pop(i-1)
                parts.insert(i-1, new_part)
                move_k+=2
        move_k=0
        for i in range(len(parts)):
            i-=move_k
            if parts[i]=='+':
                new_part=parts[i-1]+parts[i+1]
                for z in range(3):
                    parts.pop(i-1)
                parts.insert(i-1, new_part)
                move_k+=2
                i-=1
            if parts[i]=='-':
                new_part=parts[i-1]-parts[i+1]
                for z in range(3):
                    parts.pop(i-1)
                parts.insert(i-1, new_part)
                move_k+=2
        return parts[0]
      

task = Equation(input())
task.split_equation()
print(task.solve())