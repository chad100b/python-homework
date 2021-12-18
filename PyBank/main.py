#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pathlib import Path
import csv
#imports for exercise


# In[2]:


filepath = Path("budget_data.csv")
#created path to data file


# In[3]:


profit_loss_net_change = []
total_months = 0
net_total_amount = 0
net_change = 0
avg_changes = 0
increasepl = ["",0]
decreasepl = ["",99999999]
#created my variables, and two lists, that I will be using to calculate and analys the data

with open(filepath, "r") as file:
    csvreader = csv.reader(file,delimiter=",")
    header = next(csvreader)
#used 'with open' and 'csvreader' to open the data file and read the csv file
    
    first_row = next(csvreader)
    total_months += 1
    net_total_amount += int(first_row[1])
    prev_amount = int(first_row[1])
#addressed the header by 'next', started month count at 1, net_total_amount set to index [1] and output as an 'int'

    
    for row in csvreader:
        # print(row[1])
        # pl.append(int(row[1]))
        total_months += 1
        net_total_amount += int(row[1])
#started a 'for' loop and again output will be an 'int'        
        net_change = int(row[1]) - prev_amount
        profit_loss_net_change.append(net_change)
        prev_amount = int(row[1])
#the logic here is to calculate the difference from the previous net_change or row and append that change to the list profit_loss_net_change 
        if net_change > increasepl[1]:
            increasepl[1] = (net_change)
            increasepl[0] = (row[0])  
#this is the logic/code to determine the greatest net change
#used if then statement to check if the change was greater than the previous int within the increasepl list i created for the entirety of the loop           
        if net_change < decreasepl[1]:
            decreasepl[1] = net_change
            decreasepl[0] = row[0]
#same logic as greated net change just the inverse, or greatest decrease
#this is the reason i set the two lists at ["",0] for increase and ["",999999] for decrease
        
avg_change = round(sum(profit_loss_net_change) / len(profit_loss_net_change),2)

#print(total_months)
#print(net_total_amount)
#print(avg_change)
#print(profit_loss_net_change)
#print(increasepl)
#print(decreasepl)


# In[6]:


out_put = Path("Analysis_File.txt")
with open(out_put, "w") as f:
    f.write("Financial Analysis \n")
    f.write("----------------------------- \n")
    f.write(f"Total Months: ${total_months} \n")
    f.write(f"Total: ${net_total_amount} \n")
    f.write(f"Average Change: ${avg_change} \n")
    f.write(f"Greatest Increase in Profits: {increasepl[0]}, (${increasepl[1]}) \n")
    f.write(f"Greatest Decrease in Profits: {decreasepl[0]}, (${decreasepl[1]})")


# In[36]:





# In[ ]:




