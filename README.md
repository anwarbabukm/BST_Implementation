# BST ADT Implementation
**Binary Search Tree implementation**

**Given Problem Statement:**
Warehouse has certain number of trucks that transport supplies in and out of the warehouse. Each truck has a unique identifier and a counter to keep a track of how many orders did each truck fulfilled. Whenever a truck moves in/out of the warehouse its unique ID is recorded. The  warehouse  manager  requires  your  assistance  in  keeping  a  track  of  open  and  closed  orders through an automated system

**Goal:** 
The objective of the assignment is to implement the Binary Tree ADT for storing vehicle records entering and leaving a warehouse as part of the delivery service and run different analysis based on the prompts.

**Design:**
We have designed a Binary Tree ADT where each node can store the Vehicle Id and the counter to check the total in/out passage of the vehicles in the warehouse. The input is extracted from the inputps2.txt file where the first line represents the maximum delivery a vehicle is allowed to carry out in a day. The second line of the file is considered as the root node of the Binary Tree. If the vehicle Id is less than root node then it is fed to left node else it is fed to right node and the operation repeats for subsequent values as well. When the vehicle Id is already loaded to the tree, then counter variable is incremented for each in/out movement from the warehouse. Vehicles Ids are not allowed to enter the details when counter reaches the maximum delivery for a day. The time complexity of the Binary Tree in worst case scenario is O(n) which makes it reliable for operations to carry out.

**Operations:**

1. def _readTruckRec(self, tNode, Uid): This function reads vehicle ids entering and leaving 
the warehouse from the inputPS2.txt file. One ID should be populated per line (in the input 
text file) indicating entry or exit separated by comma. Input data is used to populate the tree.  
When truck arrives at the warehouse for the first time, the counter is set to 0. If a truck record 
is already added to the tree, then the counter is incremented for every subsequent occurrence 
of that truck in the input file.  
If the counter is odd, it means that the truck exited the warehouse and there is an open order 
against that truck ID in the system. On the other hand, if the counter is even the truck has 
arrived back to the warehouse and the order is closed. 
The  first  line  indicates  maximum  deliveries  a  vehicle  can  do.  Vehicle  entry  starts  from  the 
second  line.  If  vehicle  deliveries  exceed  the  maximum  allowed  deliveries,  then  display  a 
message ‘vehicle id xx no longer available for service’ and skip that entry. 
Use a trigger function to call this recursive function from the root node.  
Sample Input  
2 
34 
453 
56 
34 
643 
231 
31 
31 
453 
34 
34 
34 
 
2. def _updateTruckRec(self, tNode, Uid): This function updates the existing system with IDs 
entering and leaving the warehouse from the promptsPS2.txt file. If the truck arrives at the 
warehouse for the first time, the counter is set to 0. If the vehicle is already added to the tree, 
then the counter is incremented to update occurrence of that vehicle in the input file. If the 
counter is odd, it means that the truck exited the warehouse and if the counter is even the 
truck arrived back to the warehouse. Each exit marks an open order while each entry except 
the first indicates a closed order. 
updateTruckRec: 112 
updateTruckRec: 453 
 
3. def  _printTruckRec(self,  tNode):  The  input  should  be  read  from  the  promptsPS2.txt  file 
with the tag as shown below.  
printTruckRec  
This function counts the total number of vehicles that came to the warehouse for work and 
prints the list of vehicle ids added into the system and their counter separated by a ‘,’ in 
outputPS2.txt. ‘0’ counter indicates the vehicle arrived at the warehouse for the first time and 
has not started fulfilling any orders yet. The output file should show:  
 
Total number of vehicles entered in the warehouse: xx     
31, 1 
34, 4 
56, 0 
231, 0 
453, 1 
643, 0 
Use a traversal method that displays the current vehicles in ascending order of their id 
 
4. def _checkTruckRec(self, tNode, Uid): This function reads the vehicle id from the 
promptsPS2.txt file to be searched for availability in the system. The id is mentioned with the 
tag as shown below.  
checkTruckRec: 31 
checkTruckRec: 542 
The  search  function  is  called  for  every  checkTruckRec  tag  the  program  finds  in  the 
promptsPS2.txt file. 
If  the  vehicle  id  is  found  with  an  odd  counter,  the  below  string  is  output  to  the  into  the 
outputPS2.txt file 
Vehicle id xx entered yy times into the system. It is currently fulfilling an open order 
If  the  vehicle  id  is  found  with  an  even  counter,  the  below  string  is  output  to  the  into  the 
outputPS2.txt file 
Vehicle id xx entered yy times into the system. It just completed an order 
If the vehicle id is found but counter is 0, the below string is output into the outputPS2.txt file 
Vehicle id xx just reached the warehouse  
If the vehicle id is not found it outputs the below string into the outputPS2.txt file 
Vehicle id xx did not come to the warehouse today 
Use a trigger function to call this recursive function from the root node.  
 
5. def _printOrderStatus(self, targetorders): This function is triggered when the following tag 
is encountered in the promptsPS2.txt file 
printOrderStatus: 11 
This function prints the number of open, closed and yet to be fulfilled orders out of the total 
target orders into the outputPS2.txt file.  
The following status of xx orders: 
Open Orders: 2 
Closed Orders: 2 
Yet to be fulfilled: 7 
 
6. def _highFreqTrucks(self, tNode, frequency): This function generates the list of vehicles 
that have moved in/out of the warehouse more than ‘z’ number of times. This does not 
consider the scenario with counter ‘0’ i.e., entering warehouse for the first time. The function 
reads the x number from the file promptsPS2.txt with the tag as shown below.  
highFreqTrucks: 2 
The function outputs the vehicle ids and their entries into the outputPS2.txt file as:  
Vehicles that moved in/out more than xx times are: 
Vehicle id, counter 
If no qualifying vehicle print: ‘No such vehicle present in the system’ 
Use a trigger function to call this recursive function from the root node.  
 
7. def  _maxDeliveries(self, tNode):  This function prints the count  and  list of  vehicle  ids that 
have completed their maximum deliveries for the day. Allowed maximum deliveries per truck 
is determined by the first line of the inputPS2.txt and is triggered with the following tag in the 
promptsPS2.txt as shown below.  
maxDeliveries 
This function prints the list of qualifying vehicle ids into the file outputPS2.txt.  
 
If the maximum allowed orders to be fulfilled by each vehicle is 2, the output file should show:  
maxDeliveries: 2 
xx Vehicle Ids did their maximum deliveries: 
34 
Ensure that you use a traversal method that displays the sequence of vehicles in ascending 
order of vehicle id.  
 
8. def _availTrucks(self, tNode): This function prints the count and list of vehicle ids that are 
currently in the warehouse and available to deliver supplies. If a vehicle is in the warehouse 
but  already  completed  its  maximum  deliveries  for  the  day,  then  that  vehicle  is  no  longer 
available for service. It is triggered with the tag in promptsPS2.txt as shown below.  
availTrucks  
This function prints the qualifying ids into the file outputPS2.txt.  
 
If the maximum allowed orders to be fulfilled by each vehicle is 2, the output file should show:  
xx Vehicle Ids that are currently available to deliver supplies: 
56 
231 
643 
Ensure that you use a traversal method that displays the sequence of vehicles in ascending 
order of vehicle id.
