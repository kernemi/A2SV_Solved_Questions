def solve(left,right,path):
       
        if len(path) == x :
            if path.count("+") == remainingplus:
                correct[0] += 1
                return
            
        for i in range(left,right+1):
            path.append("+")
            solve(i+1,right,path)
            path.pop()
            path.append("-")
            solve(i+1,right,path)
            path.pop()
            


    solve(0,x-1,[])
    ans = correct[0] / possibilty
    print(f"{ans:.12f}")