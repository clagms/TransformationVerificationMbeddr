from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
import uuid

class HmotherFather_IsolatedLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
        Creates the himesis graph representing the AToM3 model HmotherFather_IsolatedLHS.
		"""
        # Flag this instance as compiled now
		self.is_compiled = True
        
		super(HmotherFather_IsolatedLHS, self).__init__(name='HmotherFather_IsolatedLHS', num_nodes=0, edges=[])
        
        # Add the edges
		self.add_edges([])
        
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
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFather')
        
        # Set the node attributes
        
        # match class Family(motherFatherclass0) node
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
		self.vs[0]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0')
        # match class Member(motherFatherclass1) node
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
		self.vs[1]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass1')
        # match class Member(motherFatherclass2) node
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
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass2')
        
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
        
        