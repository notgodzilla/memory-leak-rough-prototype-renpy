define a = Character("Ada")
image ada normal = "images/ada.png"
define ax  = Character("Alyx") 
image bg e-den = "images/afterlife.png" 
 
label start:  
    ### Boolean for meeting ada
    $ met_ada = False

    ## If using the crafting feature, add an empty cookbook list after start to keep track of recipes
    $ cookbook = list() 
  
    
    $ parietal = Brain_Region("PARIETAL") 
    $ parietal_mem = Memory("memory","A memory from your parietal lobe", "PARIETAL")
    $ parietal.take(parietal_mem) 
    
    $ frontal = Brain_Region("FRONTAL") 
    $ frontal_mem = Memory("memory","A memory from your frontal lobe","FRONTAL")
    $ frontal_mem1 = Memory("memory","A memory from your frontal lobe","FRONTAL")
    $ frontal.take(frontal_mem)
    $ frontal.take(frontal_mem1) 
    
    $ gestalt = Gestalt("GESTALT",8)
    jump meeting_ada

label meeting_ada:
    show screen memento_overlay
    show screen test_other_screens
    show screen other_hbox
    
    scene bg e-den
    
    if not met_ada:
        show ada normal
        a "Hello, world"
        $ met_ada = True
        
    else:
        show ada normal
        a "Oh, you again?"
    
    $ parietal = Brain_Region("PARIETAL") 
    $ parietal_mem = Memory("memory","A memory from your parietal lobe", "PARIETAL")
    $ parietal.take(parietal_mem) 
    
    $ frontal = Brain_Region("FRONTAL") 
    $ frontal_mem = Memory("memory","A memory from your frontal lobe","FRONTAL")
    $ frontal_mem1 = Memory("memory","A memory from your frontal lobe","FRONTAL")
    $ frontal.take(frontal_mem)
    $ frontal.take(frontal_mem1) 
    
    $ gestalt = Gestalt("GESTALT",8)
    
    show screen test_other_screens
    show screen other_hbox
      
    jump meeting_ada
    
label conditions_met: 
   a "Test passed - having three memories in Gestalt triggers this label option"
   jump bedroom_sstart 

screen memento_overlay:
    frame:
        yalign 0.0 xalign 0.0
        hbox:
            textbutton "FRONTAL" action Show("memento_screen", first_inventory=frontal, second_inventory=gestalt, trade_mode=True) 
            textbutton "PARIETAL" action Show("memento_screen", first_inventory=parietal, second_inventory=gestalt, trade_mode=True)

screen test_other_screens:
    add "images/memento-button.png" yalign 0.0 xalign 1.0

screen other_hbox: 
    frame: 
        yalign 0.0 xalign 0.5
        hbox:
            textbutton "TESTING" action Jump("show_ada_menu") 

label show_ada_menu:
    menu:
        "Option 1":
            jump meeting_ada
        "Option 2":
            jump meeting_ada
        "Option 3" if gestalt.current_size == 3:
            jump bedroom_start 
        "Back":
            jump meeting_ada 
            

screen overlay:
    frame:
        yalign 0.0 xalign 0.0
        hbox:
            textbutton "Inventory" action Show("inventory_screen", first_inventory=jane_inv)
            textbutton "Vendor" action Show("inventory_screen", first_inventory=jane_inv, second_inventory=mindy_inv)
            textbutton "Trade" action Show("inventory_screen", first_inventory=jane_inv, second_inventory=mindy_inv, trade_mode=True)
            textbutton "Storage/Bank" action Show("inventory_screen", first_inventory=jane_inv, second_inventory=chest, trade_mode=True, bank_mode=True) 
            textbutton "Exit" action Quit(confirm=False)