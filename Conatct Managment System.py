#Creating a data structure for Contact Managment using trie 
class Node:
    #creating a node for each letter inserted using dictionary
    # the last character of the node simply tells us whether all letters to the last character exists 
    def __init__(self):
        self.children = {}
        self.lastword = False
    
class Contact:
    def __init__(self):
        self.root = Node()
    #create a root node containing no character
    def insert(self,first_name,middle_name,last_name):
        # initialize my pointer to my root
        current_ptr = self.root
        full_name = first_name + " "+ middle_name+" "+last_name
        for char in full_name:
            #if the character in full_name does not exit in our children dictionary we create a node for the letter
            # but if it exists set the pointer the exiting node
            if char not in current_ptr.children:
                current_ptr.children[char] = Node()
            current_ptr = current_ptr.children[char]
       # if the loop is done then we are at the last node so we set oour lastword to true     
        current_ptr.lastword= True

    def search(self,first_name,middle_name,last_name):
        full_name = first_name+" "+ middle_name + " "+ last_name
        
        #set the current pointer of the character of the name to our root and search until the characters in
        # the name we are searching is done 
        # therefore our searching algothm will take O(k) where k is the length of the name being searched.
        current_ptr= self.root
        for char in full_name:
            if char not in  current_ptr.children:
                return full_name+" does not exist!"
            current_ptr = current_ptr.children[char]
        self.root.lastword = True
        
        return full_name
        


            
                
def main():
    name = Contact()
    name.insert("Abebe" , "Kedu", "Beni")
    name.insert("Melki", "Tesfu","Simgh")
    print(name.search("Abebe" , "Kedu", "Beni"))
    print(name.search("Melki", "Tesfu","Simgh"))
    print(name.search("Abebe" , "Kedu", "Beni"))
    print(name.search("Abebe" , "Ked", "Beni"))
    

if __name__== "__main__":
    main()


