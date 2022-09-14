
import pyautogui
import time

time.sleep(3)
##failsafe limit
i=0
## round counter / limit to go to the next level
r=0
## limit on how many clicks can be possible
l=0
## goes back a level
b=0
## number to add to "b" in order to extend the variable
a=0
y=0
while True:
    ## clicks the first hero
    first= pyautogui.pixelMatchesColor(97,501, (111,197,255), tolerance= 19)
    ##clicks the next level
    level_check=pyautogui.pixelMatchesColor(1544,171, (255,212,52), tolerance= 19)
    ##second hero
    second=pyautogui.pixelMatchesColor(235,686,(111,197,255),tolerance=19)
    ##third hero
    third=pyautogui.pixelMatchesColor(232,868,(111,197,255), tolerance=19)



    if level_check == True and r>=1:
        pyautogui.click(1544,171)
        r=0
        b=0
    else:
        b=b+1
     
    second=pyautogui.pixelMatchesColor(235,686,(111,197,255),tolerance=19)
    third=pyautogui.pixelMatchesColor(232,868,(111,197,255), tolerance=19)

    x=200
    #Supposed to scan along set x and y values
    #scan = pyautogui.pixelMatchesColor(x,y,(111,197,255), tolerance=5)
    
    while first == True:
        pyautogui.click(97,501,interval=0.0005, _pause=False)
        first= pyautogui.pixelMatchesColor(97,501, (111,197,255), tolerance= 19)
        l=0
        
    #clicks the second hero   
    while second == True:
        pyautogui.click(235,686)
        second=pyautogui.pixelMatchesColor(235,686,(111,197,255),tolerance=19)
   #Clicks the third hero
    while third == True:
        pyautogui.click(232,868)
        third=pyautogui.pixelMatchesColor(232,868,(111,197,255), tolerance=19)
    #clicks the enemies
    while first == False:
        pyautogui.click(1438,680,interval=0.0005, _pause=False)
        first= pyautogui.pixelMatchesColor(97,501, (111,197,255), tolerance= 19)
        second=pyautogui.pixelMatchesColor(235,686,(111,197,255),tolerance=19)
        third=pyautogui.pixelMatchesColor(232,868,(111,197,255), tolerance=19)
        if l == 50:
            l=0
            break
            
        l=l+1
        
    if b>=15 + a:
        pyautogui.click(1326,177,interval=0.0005, _pause=False)
        for x in range(200):
            pyautogui.click(1438,680,interval=0.0005, _pause=False)
        
        pyautogui.click(1544,171)
        b=0
    
    if y ==1279:
        y=0
    l=0
    i=i+1
    r=r+1
    a=a+0.05
    print(b)
    print(r)
    print(a)
    
print(i)
print(r)
print(l)