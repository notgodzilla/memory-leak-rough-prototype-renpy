
init python:
    
    #Inherits from Inventory class
    class Memento(Inventory):
        
        def __init__(self):
            Inventory.__init__(self, name)
            
    
    class Memory(Item):
        
        def __init__(self, name, desc, region):
            Item.__init__(self, name, desc)
            self.region = region 
            

    class Brain_Region(Inventory):
        def __init__(self, name):
            Inventory.__init__(self, name)
            self.region = name
        
    
        
    class Gestalt(Inventory):
        
        def __init__(self, name, max_size):
            Inventory.__init__(self, name)
            self.max_size = max_size
            self.current_size=0
            
        
        #Checks if memories in Gestalt fit the trigger
        def check_memories(self, trigger):
            pass
        
    
        def take(self, item):
            #renpy.show_screen("inventory_popup", message="TAKE IN GESTALT") 
            if not self.current_size == self.max_size:
                Inventory.take(self, item, 1)
                self.current_size+=1
            else:
                renpy.show_screen("inventory_popup", message="GESTALT IS FULL")


screen memento_screen(first_inventory, second_inventory=False, trade_mode=False, bank_mode=False):
    default crafting_screen = False
    tag menu
    modal False        
    frame:
        style_group "invstyle"          
        hbox:
            spacing 25
            vbox:
                label first_inventory.name                   
                #if second_inventory:
                    #use money(first_inventory, second_inventory, bank_mode) 
                use memento_view(first_inventory, second_inventory, trade_mode)                          
                use view_nav(first_inventory)
                #use sort_nav(first_inventory)
                #if not second_inventory:
                    #textbutton "Crafting Mode" action ToggleScreenVariable("crafting_screen")
                textbutton "Close" action Hide("memento_screen")
            if second_inventory:
                vbox:
                    label second_inventory.name  
                    #use money(second_inventory, first_inventory, bank_mode)                       
                    use memento_view(second_inventory, first_inventory, trade_mode)
                    use view_nav(second_inventory)
                    #use sort_nav(second_inventory)
            #if crafting_screen:
                #use crafting(first_inventory)


screen memento_view(inventory, second_inventory=False, trade_mode=False):     
    side "c r":
        style_group "invstyle"
        area (0, 0, 350, 400) 
        vpgrid id ("vp"+inventory.name):
            draggable True   
            mousewheel True
            xsize 350 ysize 400
            if inventory.grid_view:
                cols 3 spacing 10
            else:
                cols 1 spacing 25
            for item in inventory.inv:
                $ name = item[0].name
                $ desc = item[0].desc
                $ value = item[0].value
                $ qty = str(item[1])
                hbox:
                    if item[0].icon:
                        $ icon = item[0].icon
                        $ hover_icon = im.Sepia(icon)                              
                        imagebutton:
                            idle LiveComposite((100,100), (0,0), icon, (0,0), Text(qty))
                            hover LiveComposite((100,100), (0,0), hover_icon, (0,0), Text(qty))
                            #action (If(not second_inventory, item[0].act, (If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item)))))
                            #hovered Show("tooltip",item=item,seller=second_inventory)
                            #unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:
                                text name
                                if not trade_mode:
                                    text "List Value: [value]"                                        
                                    if second_inventory:                                            
                                        text ("Sell Value: " + str(calculate_price(item, second_inventory)) + ")")
                    
                    else:                               
                        textbutton "[name]" action (If(not second_inventory, item[0].act,(If(trade_mode, Function(trade,inventory, second_inventory, item), Function(transaction,inventory, second_inventory, item))))) hovered Show("tooltip",item=item,seller=second_inventory) unhovered Hide("tooltip")
                        if not inventory.grid_view:
                            vbox:                        
                                text "List Value: [value]"
                                if not trade_mode and second_inventory:
                                    text "Sell Value: " + str(calculate_price(item, second_inventory)) + ")"
            
            ## maintains spacing in empty inventories.
            if len(inventory.inv) == 0:
                add Null(height=100,width=100)
                                    
        vbar value YScrollValue("vp"+inventory.name)