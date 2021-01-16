import os                                                           #Import the os library that alows to create the directories.
i=0                                                                 #This int will contain the number of the folder that has to be created.
j="0000000000000000"                                                #This string  simply stores zeros.
k=""                                                                #The path of each folder will come from here.
count=1                                                             #This takes a count of the folders that have been created.
flag=True                                                           #This flag will end the next while loop when neccesary.
while flag:                                                         #The loop main loop.
    k=f"{j[0:(16-len(str(i)))]}{str(i)}"                            #This is the mos valuable thing, it converts i from int to string and add zeros to it depending of its lenght.
    os.makedirs(f"C:/Users/Valentino Amato/Desktop/Vault(10^16)/{k[0]}/{k[1]}/{k[2]}/{k[3]}/{k[4]}/{k[5]}/{k[6]}/{k[7]}/{k[8]}/{k[9]}/{k[10]}/{k[11]}/{k[12]}/{k[13]}/{k[14]}/{k[15]}")#This comand creates the folders.
    print(f"Folders created:{count}/10000000000000000 ")            #Prints how many folders were created.
    count+=1                                                        #Add one to count.
    i+=1                                                            #Add one to i.
    if i==9999999999999999:                                         #When all the folders are created.
        flag=False                                                  #It ends the loop.
        print("10000000000000000 Folders created successfully!")    #And prints a message.
#Have in mind that this process can take up to days and delete it may be impossible.
#This proyect was created by Valentino Amato: https://github.com/AMATO174/Folder-Generator . 