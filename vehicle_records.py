#Node of the Binary Tree
class TruckNode: 
 def __init__(self, Uid): 
  self.UId = Uid #Unique Id of vehicle
  self.chkoutCtr = 0 #Counter to check the total in/out of the vehicle
  self.left=None #left node 
  self.right=None #right node

#Class Operations is defined for calling different operations for the analysis
class Operations:
 #Recursive Search function that checks if the Uids are already loaded in the Binary Tree
 def search(self,Uid,tnode):
  if tnode.UId==Uid:
    return tnode,True
  if Uid<tnode.UId:
    if tnode.left:
      self.search(Uid,tnode.left)
    else:
      return None,False
  else:
    if tnode.right:
      self.search(Uid,tnode.right)
    else:
      return None,False
  return None,False

 #Recursive function for Inorder traversal - to get the data in the ascending order
 def traversal(self,tnode,node):
  if tnode:
        # First recur on left child
        self.traversal(tnode.left,node)
        # then store in a list
        node.append(tnode)
        # now recur on right child
        self.traversal(tnode.right,node)
  return node

 #Takes Data from the Input file and Loads it into Binary Tree - Recursive Function
 def _readTruckRec(self,Uid,tnode):
    node,stat=self.search(Uid,tnode) #gives the stat whether given Uid is already in the tree or not
    if stat:
      #Condition to check if the Uids have reached the max limit, else increment the counter to mark the in/out
      if int(node.chkoutCtr)/2>=maxchkout:
        print('vehicle id ',Uid,' is no longer available for service')
        return True
      else:
        node.chkoutCtr=node.chkoutCtr+1
    else:
      if tnode.UId>Uid:
        if tnode.left:
          self._readTruckRec(Uid,tnode.left)
        else:
          tnode.left=TruckNode(Uid)
      else:
        if tnode.right:
          self._readTruckRec(Uid,tnode.right)
        else:
          tnode.right=TruckNode(Uid)
    return False

 #Function to update the records into Binary tree
 def _updateTruckRec(self, Uid,tNode):
   task= self._readTruckRec(Uid,tNode)
   if task:
     log_out(log='------------- updateTruckRec:'+str(Uid)+'---------------')
     log_out(log='Warning--> Vehicle ID '+str(Uid)+' already reached maximum delivery.')
     log_out('----------------------------------------------\n')
   else:
     log_out(log='------------- updateTruckRec:'+str(Uid)+'---------------')
     log_out(log='Vehicle Id '+str(Uid)+' record updated')
     log_out('----------------------------------------------\n')

 #To print the every vehicle details in the Binary tree
 def  _printTruckRec(self, tnode):
   t='------------- printTruckRec ---------------'
   log_out(t)
   node=[]
   node=self.traversal(tnode,node) #inorder traversal to get the elements in the BT in ascending order
   log_out(log='Total number of vehicles entered in the warehouse: '+str(len(node)))
   for i,j in enumerate(node):
     log_out(log=str(j.UId)+','+str(j.chkoutCtr))
   return log_out('----------------------------------------------\n')
 
 #Checking the status of a particular truck warehouse
 def _checkTruckRec(self, Uid, tnode):
   node=[]
   node=self.traversal(tnode,node)
   log_out(log='------------- checkTruckRec: '+str(Uid)+' ---------------')
   for i,j in enumerate(node): 
     if j.UId==Uid:
       if j.chkoutCtr==0:
        log_out(log='Vehicle ID '+str(Uid)+' just reached the warehouse')
        return log_out('----------------------------------------------\n')
       elif j.chkoutCtr%2==0:
        log_out(log='Vehicle ID '+str(Uid)+' enters '+str(j.chkoutCtr)+' time(s) into the sytem.It just completed an order')
        return log_out('----------------------------------------------\n')
       elif j.chkoutCtr%2!=0:
        log_out(log='Vehicle ID '+str(Uid)+' enters '+str(j.chkoutCtr)+' time(s) into the sytem.It''s currently fulfilling an open order')
        return log_out('----------------------------------------------\n')
     else:
       continue
   log_out(log='Vehicle ID '+str(Uid)+' did not come to the warehouse today')
   return log_out('----------------------------------------------\n')
 
 #To check the whole status of orders based on the target orders
 def _printOrderStatus(self, targetorders):
   node=[]
   node=self.traversal(root,node)
   closed=0
   open=0
   for i,j in enumerate(node):
     if j.chkoutCtr>0 and j.chkoutCtr%2==0:
       closed+=1
     elif j.chkoutCtr>0 and j.chkoutCtr%2!=0:
       open+=1
   not_started=targetorders-(closed+open)
   log_out(log='------------- printOrderStatus: '+str(targetorders)+' ---------------')
   log_out(log='The following status of '+str(targetorders))
   log_out(log='Open Orders: '+str(open))
   log_out(log='Closed Orders: '+str(closed))
   log_out(log='Yet to be fulfilled: '+str(not_started))
   return log_out('----------------------------------------------\n')

 #To find the vehicles in the warehouse with equal to or more than given frequency
 def _highFreqTrucks(self, tnode, frequency): 
   node=[]
   node=self.traversal(tnode,node)
   counter=[]
   log_out(log='------------- highFreqTrucks: '+str(frequency)+' ---------------')
   for i,j in enumerate(node):
     if j.chkoutCtr>=frequency:
       counter.append(j)
     else:
       continue
   if len(counter):
      log_out(log='Vehicles that moved in/out more than '+str(frequency)+' times are:')
      for i,j in enumerate(counter):
        log_out(log=str(j.UId)+','+str(j.chkoutCtr))
        #+','+str(j.chkoutCtr)
   else:
     log_out('No such vehicle present in the system')
   return log_out('----------------------------------------------\n')
 
 #Checks the vehicles which reached the max delivery limit
 def _maxDeliveries(self, tnode):
   log_out('------------- maxDeliveries ---------------')
   node=[]
   counter=[]
   node=self.traversal(tnode,node)
   log_out(log='Max Deliveries are '+str(maxchkout))
   for i,j in enumerate(node):
     if int(j.chkoutCtr/2)>=maxchkout:
       counter.append(j)
     else:
       continue
   log_out(log=str(len(counter))+' Vehicle Id(s) did their maximum deliveries')
   for i,j in enumerate(counter):
     log_out(log=str(j.UId))
   return log_out('----------------------------------------------\n')    
 
 #To find the vehicles that are in the warehouse,and available to take the delivery
 def _availTrucks(self, tnode): 
   log_out('------------- availTrucks --------------- ')
   node=[]
   counter=0
   node=self.traversal(tnode,node)
   id=[]
   for i,j in enumerate(node):
     if j.chkoutCtr<maxchkout*2 and j.chkoutCtr%2==0:
       counter=counter+1
       id.append(j.UId)
     else:
       continue
   log_out(log=str(counter)+' Vehicle Id(s) that are currently available to deliver supplies:')
   for i,j in enumerate(id):
     log_out(str(j))
   return log_out('----------------------------------------------\n') 

#Function to read the elements from text file and load to Binary Tree
def insert():
    f = open('inputPS2.txt','r') #Reading the file in read mode
    data=[]
    for i in f:
      data.append(int(i))
    global maxchkout,root
    v=Operations()
    if data[0]>0:
      print('\nThe elements to load are:\n',data[1:])
      maxchkout= data[0] #Max delivery limit for a vehicle
      for j in range(len(data[1:])):
          j+=1
          if data[j]>0:
            print('\n---Values are loading into Binary Tree---\n')
            root=TruckNode(data[j]) #Setting the root node of Binary tree
            for Uid in data[j+1:]: 
             if Uid<0:
              print(Uid,'is an invalid Input')
             else:
              v._readTruckRec(Uid,root) #Loading the binary tree
            return True
          else:
            print(data[j],'is an invalid Input. It will not be considered as an input entry')
            continue
    else:
      print('Invalid input for Maximum delivery\n')
      print('Loading Failed!!\n')
      return False
    print('\n---Finished Loading the Binary Tree---\n\n')
    return True

#Extract all the prompts to be executed, from the prompt file 
def extracting_prompts():
  files=[]
  # Using readlines()
  file = open('promptsPS2.txt', 'r')
  Lines = file.readlines()
  #reading each prompt and save it to a list with prompts and numerical arguements separated
  for line in Lines:
      # Strips the newline character
      text=line.strip()
      #condition to check the prompt type
      if text.isalpha():
        files.append((text,0,0)) #
      else:
        t=[]
        d=[]
        counter=0
        for j,k in enumerate(line):
          #print(j,k)
          if k.isalpha():
            t.append(k) #stores the text characters from the prompt
          elif k.isdigit():
            d.append(k) #stores the numerical arguements from the prompt
          elif k=='-':
            counter+=1
            continue
        t=''.join(t)
        d=''.join(d)
        files.append((t,int(d),counter))
  return files

#Executes all the prompts extracted from the text file sequentially
def reading_prompts(file):
  v=Operations()
  for i,items in enumerate(file):
    #print(items)
    if items[2]==0:
      if items[1]==0:
        if items[0]=='printTruckRec':
          v._printTruckRec(root)
        elif items[0]=='maxDeliveries':
          v._maxDeliveries(root)
        elif items[0]=='availTrucks':
          v._availTrucks(root)
        else:
          log_out('Error!')
          log_out(log=str(items[0])+' is an invalid Operation!!')
          log_out('----------------------------------------------\n')
      else:
        if items[0]=='updateTruckRec':
          v._updateTruckRec(items[1],root)
        elif items[0]=='checkTruckRec':
          v._checkTruckRec(items[1],root)
        elif items[0]=='printOrderStatus':
          v._printOrderStatus(items[1])
        elif items[0]=='highFreqTrucks':
          v._highFreqTrucks(root,items[1])
        else:
          log_out('Error!')
          log_out(log=str(items[0])+' '+str(items[1])+' is an invalid Operation!!')
          log_out('----------------------------------------------\n')
    else:

      log_out(log='-------------'+str(items[0])+': -'+str(items[1])+'-------------')
      log_out('Error!')
      log_out('Invalid Entry!!')
      log_out('----------------------------------------------\n')
  return 

#store the logs to output file
def log_out(log):
  output.write(log + '\n')

#Main function to give trigger to populate the elements into the binary tree
def main():
  print('Do you want to load the Binary Tree? \n')
  stat=input('Answer: Yes or No\n\n')
  if stat.lower()=='yes':
   if insert():
    return True
   else:
    return False
  else:
    return False
   
if __name__ == '__main__':
  global output
  output=open('outputPS2.txt', 'w')
  if main():
    print('\nDo you want to execute the prompts? \n')
    stat=input('Answer: Yes or No\n\n')
    if stat.lower()=='yes':
      print('\n****Reading prompts from the file for execution****\n')
      info=extracting_prompts() #Extraction of prompts from text file
      reading_prompts(info) #Reading the prompts from extracted file
      #log_out('----------------------------------------------\n')
      print('Execution Finished!!!\n\n')
    else:
      print('No prompts Executed!!')
  else:
    print('\nNo operations Executed\n\n--Completed--')
  output.close()