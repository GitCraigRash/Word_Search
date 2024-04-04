class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def find_possibilities(board,word):
            possible_starts=[]
            for i,n in enumerate(board):
                for j,k in enumerate(n):
                    if k == word[0]:
                        possible_starts.append((i,j))
            return possible_starts


        def neighborhood(board,start,letter):
            neighborhood = []
            print(start,letter)
            if start[0] != len(board)-1:
                if board[start[0]+1][start[1]] == letter:
                    neighborhood.append((start[0]+1,start[1]))
                    print("down", board[start[0]+1][start[1]])
            if start[1] != len(board[0])-1:
                if board[start[0]][start[1]+1] == letter:
                    neighborhood.append((start[0],start[1]+1))
                    print("right", board[start[0]+1][start[1]])
            if start[0] != 0:
                if board[start[0]-1][start[1]] == letter:
                    neighborhood.append((start[0]-1,start[1]))
                    print("up", board[start[0]+1][start[1]])
            if start[1] != 0:
                if board[start[0]][start[1]-1] == letter:
                    neighborhood.append((start[0],start[1]-1))
                    print("left", board[start[0]+1][start[1]])
            return neighborhood


        def end_of_options(board,neighbors,word,visited):
            if len(word)!=len(visited):
                return False
            for n,o in enumerate(word):
                print("checking", board [visited[n][0]] [visited[n][1]], word[n])
                if board[visited[n][0]][visited[n][1]] != word[n]:
                    return False
            return True


        def search(board,visited,start,word,count):
            if visited is None:
                visited = set()
            if count is None: 
                count = 0
            visited.add(start)
            count = count + 1
            if count >= len(word)
                    
                letter = word[count]
                neighbors = neighborhood(board,start,letter)
                print(letter," ", visited," ", neighbors)
                
                if neighbors == []:
                    return end_of_options(board,neighbors,word,visited)
                
                    return search(board,visited,start,word,count)
            return False
        
        possible_starts = find_possibilities(board,word)
        print(possible_starts)
        visited = set()
        count = 0
        for l in possible_starts:
            print(l)
            result = search(board,visited,l,word,count)
            if result == True:
                return True
        return False


        #route
        #record
            #cannot record letter
            #must record position
        #reconize
            #list possible options
            #loop for target letter
        #report
    

    
 
