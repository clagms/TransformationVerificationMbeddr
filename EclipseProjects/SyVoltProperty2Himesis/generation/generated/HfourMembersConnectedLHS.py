from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
import uuid

class HfourMembers_ConnectedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HfourMembers_ConnectedLHS.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True
        
		super(HfourMembers_ConnectedLHS, self).__init__(name='HfourMembers_ConnectedLHS', num_nodes=0, edges=[])
        
		# Set the graph attributes
		self["mm__"] = pickle.loads("""(lp1
S'MT_pre__FamiliesToPersonsMM'
p2
aS'MoTifRule'
p3
a.""")
		self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the LHS have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True enables the rule to be applied,
#    returning False forbids the rule from being applied.
#===============================================================================

return True
"""
		self["name"] = """"""
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembers')
        
		# Set the node attributes
        
		# match class Family(fourMembersclass0) node
		self.add_node()
		self.vs[0]["MT_subtypeMatching__"] = False
		self.vs[0]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["MT_label__"] = """1"""  
		self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[0]["MT_dirty__"] = False
		self.vs[0]["mm__"] = """MT_pre__Family"""  
		self.vs[0]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0')
		# match class Member(fourMembersclass1) node
		self.add_node()
		self.vs[1]["MT_subtypeMatching__"] = False
		self.vs[1]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["MT_label__"] = """2"""  
		self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[1]["MT_dirty__"] = False
		self.vs[1]["mm__"] = """MT_pre__Member"""  
		self.vs[1]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass1')
		# match class Member(fourMembersclass2) node
		self.add_node()
		self.vs[2]["MT_subtypeMatching__"] = False
		self.vs[2]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["MT_label__"] = """3"""  
		self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[2]["MT_dirty__"] = False
		self.vs[2]["mm__"] = """MT_pre__Member"""  
		self.vs[2]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass2')
		# match class Member(fourMembersclass3) node
		self.add_node()
		self.vs[3]["MT_subtypeMatching__"] = False
		self.vs[3]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[3]["MT_label__"] = """4"""  
		self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[3]["MT_dirty__"] = False
		self.vs[3]["mm__"] = """MT_pre__Member"""  
		self.vs[3]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[3]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[3]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass3')
		# match class Member(fourMembersclass4) node
		self.add_node()
		self.vs[4]["MT_subtypeMatching__"] = False
		self.vs[4]["MT_pre__classtype"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[4]["MT_label__"] = """5"""  
		self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[4]["MT_dirty__"] = False
		self.vs[4]["mm__"] = """MT_pre__Member"""  
		self.vs[4]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[4]["MT_pre__cardinality"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[4]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass4')
        
        # Nodes that represent the edges of the property.
    	# match association Family--father-->Member node
		self.add_node()
		self.vs[5]["MT_label__"] = """6"""
		self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[5]["MT_dirty__"] = False
		self.vs[5]["mm__"] = """MT_pre__directLink_S"""
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc5fourMembersclass2')
    	# match association Family--mother-->Member node
		self.add_node()
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[6]["MT_dirty__"] = False
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc6fourMembersclass1')
    	# match association Family--son-->Member node
		self.add_node()
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[7]["MT_dirty__"] = False
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc7fourMembersclass4')
    	# match association Family--daughter-->Member node
		self.add_node()
		self.vs[8]["MT_label__"] = """9"""
		self.vs[8]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[8]["MT_dirty__"] = False
		self.vs[8]["mm__"] = """MT_pre__directLink_S"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc8fourMembersclass3')
        
        # Add the edges
		self.add_edges([
    		(0,5), # match_class Family(fourMembersclass0) -> association father
    		(5,2), # association father  -> match_class Member(fourMembersclass2)
    		(0,6), # match_class Family(fourMembersclass0) -> association mother
    		(6,1), # association mother  -> match_class Member(fourMembersclass1)
    		(0,7), # match_class Family(fourMembersclass0) -> association son
    		(7,4), # association son  -> match_class Member(fourMembersclass4)
    		(0,8), # match_class Family(fourMembersclass0) -> association daughter
    		(8,3) # association daughter  -> match_class Member(fourMembersclass3)
        ])
        
		def eval_classtype1(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================

			return True
        
        
		def eval_cardinality1(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True

        
		def eval_name1(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True
        
        
		def eval_classtype2(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================

			return True
        
        
		def eval_cardinality2(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True

        
		def eval_name2(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True
        
        
		def eval_classtype3(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================

			return True
        
        
		def eval_cardinality3(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True

        
		def eval_name3(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True
        
        
		def eval_classtype4(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================

			return True
        
        
		def eval_cardinality4(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True

        
		def eval_name4(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True
        
        
		def eval_classtype5(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================

			return True
        
        
		def eval_cardinality5(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True

        
		def eval_name5(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return True
        
        
		def eval_associationType6(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return attr_value == "father"
	        
	        
		def eval_associationType7(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return attr_value == "mother"
	        
	        
		def eval_associationType8(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return attr_value == "son"
	        
	        
		def eval_associationType9(self, attr_value, this):
        
	        #===============================================================================
	        # This code is executed when evaluating if a node shall be matched by this rule.
	        # You can access the value of the current node's attribute value by: attr_value.
	        # You can access any attribute x of this node by: this['x'].
	        # If the constraint relies on attribute values from other nodes,
	        # use the LHS/NAC constraint instead.
	        # The given constraint must evaluate to a boolean expression.
	        #===============================================================================
	        
			return attr_value == "daughter"
	        
	        
        
		def constraint(self, PreNode, graph):
			"""
			Executable constraint code. 
			@param PreNode: Function taking an integer as parameter
				and returns the node corresponding to that label.
			"""
	        #===============================================================================
	        # This code is executed after the nodes in the LHS have been matched.
	        # You can access a matched node labelled n by: PreNode('n').
	        # To access attribute x of node n, use: PreNode('n')['x'].
	        # The given constraint must evaluate to a boolean expression:
	        #    returning True enables the rule to be applied,
	        #    returning False forbids the rule from being applied.
	        #===============================================================================
	        
			return True
        
        