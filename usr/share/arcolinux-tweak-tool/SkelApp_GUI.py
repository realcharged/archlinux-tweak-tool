#=================================================================
#=                  Author: Brad Heffernan                       =
#=================================================================
def GUI(self, Gtk, GdkPixbuf, vboxStack9, skelapp, Functions):
    
    stack = Gtk.Stack()
    stack.set_transition_type(Gtk.StackTransitionType.SLIDE_UP_DOWN)
    stack.set_transition_duration(350)
    
    vboxStack1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
    vboxStack2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)

    stack_switcher = Gtk.StackSwitcher()
    stack_switcher.set_orientation(Gtk.Orientation.HORIZONTAL)
    stack_switcher.set_stack(stack)
    stack_switcher.set_homogeneous(True)
    
    
    #=======================TAB #1=============================
    
    stack.add_titled(vboxStack1, "main_stack", "Main")

    label = Gtk.Label()
    label.set_markup("<big>Under Construction!</big>")

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)

    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
    
    self.browse = Gtk.Button(label="ADD")
    self.browse.connect("clicked", self.on_browse_fixed)

    self.remove = Gtk.Button(label="REMOVE")
    self.remove.connect("clicked", self.on_remove_fixed)

    self.btn2 = Gtk.Button(label="Run Skel")
    self.btn2.connect("clicked", self.on_button_fetch_clicked)
  
    sw = Gtk.ScrolledWindow()
    sw.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
    sw.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    self.store = Gtk.ListStore(str)

    self.treeView = Gtk.TreeView(self.store)
    # treeView.connect("row-activated", self.on_activated)
    self.treeView.set_rules_hint(True)
    sw.set_size_request(270, 120)
    sw.add(self.treeView)
    self.create_columns(self.treeView)

    self.rbutton3 = Gtk.RadioButton(label="File")
    self.rbutton4 = Gtk.RadioButton.new_from_widget(self.rbutton3)
    self.rbutton4.set_label("Folder")

    vbox1.pack_start(self.browse, False, False, 0)
    vbox1.pack_start(self.remove, False, False, 10)

    hbox.pack_start(sw, True, True, 10)
    hbox.pack_start(vbox1, False, False, 10)

    hbox1.pack_end(self.rbutton4, False, False, 10)
    hbox1.pack_end(self.rbutton3, False, False, 10)
    
    hbox3.pack_start(label, True, False, 0)

    hbox2.pack_end(self.btn2, False, False, 0)

    vboxStack1.pack_start(hbox, False, False, 0)
    vboxStack1.pack_start(hbox1, False, False, 0)
    vboxStack1.pack_start(hbox3, False, False, 0)
    vboxStack1.pack_end(hbox2, False, False, 0)
    
    #=======================TAB #2=============================
    
    stack.add_titled(vboxStack2, "backup_stack", "Backups")

    label1 = Gtk.Label()
    label1.set_markup("<big>Under Construction!</big>")

    
    hbox4 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox5 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    vbox9 = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL, spacing=0)
    hbox10 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox11 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox12 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox13 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    hbox14 = Gtk.Box(
        orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
    vbox11 = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL, spacing=0)
    
    # ListRow 1 Elements
    self.backs = Gtk.ComboBoxText()
    
    skelapp.refresh(self)

    self.backs.set_active(0)
    self.backs.set_size_request(170, 0)
    self.btn4 = Gtk.Button(label="Refresh")
    self.btn5 = Gtk.Button(label="Delete")
    self.btn12 = Gtk.Button(label="Run Full Backup")
    self.btn12.set_size_request(0, 80)
    self.btn9 = Gtk.Button(label="Delete All Backups")
    

    sw2 = Gtk.ScrolledWindow()
    sw2.set_shadow_type(Gtk.ShadowType.ETCHED_IN)
    sw2.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)

    self.store2 = Gtk.ListStore(str)

    self.treeView2 = Gtk.TreeView(self.store2)
    # treeView.connect("row-activated", self.on_activated)
    self.treeView2.set_rules_hint(True)
    sw2.set_size_request(270, 120)
    sw2.add(self.treeView2)
    self.create_columns(self.treeView2)

    
    skelapp.refresh_inner(self)
    
    self.btn10 = Gtk.Button(label="Delete")
    self.btn11 = Gtk.Button(label="Restore")

    self.btn4.connect("clicked", self.on_refresh_clicked)
    self.btn5.connect("clicked", self.on_delete_clicked)
    self.btn9.connect("clicked", self.on_flush_clicked)
    self.btn12.connect("clicked", self.on_backup_clicked)
    self.btn10.connect("clicked", self.on_delete_inner_clicked)
    # btn11.connect("clicked", self.on_restore_inner_clicked)

    label4 = Gtk.Label(xalign=0)
    label4.set_markup("<b>Delete Backups</b>")

    self.progressbar = Gtk.ProgressBar()
    self.label_info = Gtk.Label("Idle ...")

    hbox5.pack_start(label4, True, True, 10)

    hbox4.pack_start(self.backs, True, True, 10)
    hbox4.pack_start(self.btn4, False, False, 0)
    hbox4.pack_end(self.btn5, True, True, 10)

    # hbox11.pack_start(self.backs_inner, True, True, 0)

    vbox11.pack_start(self.btn10, False, False, 0)
    vbox11.pack_start(self.btn11, False, False, 10)

    hbox10.pack_start(sw2, True, True, 10)
    hbox10.pack_start(vbox11, False, False, 10)
    
    vbox9.pack_start(self.btn12, True, True, 0)
    vbox9.pack_start(self.btn9, True, True, 0)
    
        
    hbox12.pack_start(label1, True, True, 5)

    hbox13.pack_start(self.label_info, False, False, 5)
    hbox14.pack_start(self.progressbar, True, True, 5)

    vboxStack2.pack_start(hbox5, False, False, 0)
    vboxStack2.pack_start(hbox4, False, False, 0)
    vboxStack2.pack_start(hbox10, False, False, 0)
    vboxStack2.pack_start(vbox9, False, False, 0) #
    vboxStack2.pack_start(hbox12, False, False, 0)

    vboxStack2.pack_end(hbox14, False, False, 0)
    vboxStack2.pack_end(hbox13, False, False, 0)

    self.backs.connect("changed", self.backs_changed)

    #=======================ADD STACKS=============================

    vboxStack9.pack_start(stack_switcher, False, True, 0)
    vboxStack9.pack_start(stack, True, True, 0)

    # vboxStack9.pack_start(hbox1, False, False, 0)
    # vboxStack9.pack_start(hbox, False, False, 0)