from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HfourMembers_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HfourMembers_CompleteLHS.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True
		
		super(HfourMembers_CompleteLHS, self).__init__(name='HfourMembers_CompleteLHS', num_nodes=0, edges=[])
		
		# Set the graph attributes
		self["mm__"] = pickle.loads("""(lp1
S'MT_pre__HimesisMM'
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
        
		# Nodes that represent match classes
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
        
        
        #Nodes that represent apply classes
    	# match class Community(fourMembersclass5) node
		self.add_node()
		self.vs[5]["MT_subtypeMatching__"] = False
		self.vs[5]["MT_pre__classtype"] = """
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
		self.vs[5]["MT_label__"] = """6"""  
		self.vs[5]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[5]["MT_dirty__"] = False
		self.vs[5]["mm__"] = """MT_pre__Community"""  
		self.vs[5]["MT_pre__classtype"] = """
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
		self.vs[5]["MT_pre__name"] = """
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
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass5')
    	# match class Man(fourMembersclass6) node
		self.add_node()
		self.vs[6]["MT_subtypeMatching__"] = False
		self.vs[6]["MT_pre__classtype"] = """
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
		self.vs[6]["MT_label__"] = """7"""  
		self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[6]["MT_dirty__"] = False
		self.vs[6]["mm__"] = """MT_pre__Man"""  
		self.vs[6]["MT_pre__classtype"] = """
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
		self.vs[6]["MT_pre__name"] = """
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
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass6')
    	# match class Man(fourMembersclass7) node
		self.add_node()
		self.vs[7]["MT_subtypeMatching__"] = False
		self.vs[7]["MT_pre__classtype"] = """
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
		self.vs[7]["MT_label__"] = """8"""  
		self.vs[7]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[7]["MT_dirty__"] = False
		self.vs[7]["mm__"] = """MT_pre__Man"""  
		self.vs[7]["MT_pre__classtype"] = """
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
		self.vs[7]["MT_pre__name"] = """
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
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass7')
    	# match class Female(fourMembersclass8) node
		self.add_node()
		self.vs[8]["MT_subtypeMatching__"] = False
		self.vs[8]["MT_pre__classtype"] = """
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
		self.vs[8]["MT_label__"] = """9"""  
		self.vs[8]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[8]["MT_dirty__"] = False
		self.vs[8]["mm__"] = """MT_pre__Female"""  
		self.vs[8]["MT_pre__classtype"] = """
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
		self.vs[8]["MT_pre__name"] = """
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
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass8')
    	# match class Female(fourMembersclass9) node
		self.add_node()
		self.vs[9]["MT_subtypeMatching__"] = False
		self.vs[9]["MT_pre__classtype"] = """
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
		self.vs[9]["MT_label__"] = """10"""  
		self.vs[9]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[9]["MT_dirty__"] = False
		self.vs[9]["mm__"] = """MT_pre__Female"""  
		self.vs[9]["MT_pre__classtype"] = """
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
		self.vs[9]["MT_pre__name"] = """
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
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass9')
        
                
        # Nodes that represent the match associations of the property.
    	# match association Family--father-->Member node
		self.add_node()
		self.vs[10]["MT_subtypeMatching__"] = False
		self.vs[10]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "father"
"""
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[10]["MT_dirty__"] = False
		self.vs[10]["mm__"] = """MT_pre__directLink_S"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc10fourMembersclass2')
    	# match association Family--mother-->Member node
		self.add_node()
		self.vs[11]["MT_subtypeMatching__"] = False
		self.vs[11]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "mother"
"""
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[11]["MT_dirty__"] = False
		self.vs[11]["mm__"] = """MT_pre__directLink_S"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc11fourMembersclass1')
    	# match association Family--son-->Member node
		self.add_node()
		self.vs[12]["MT_subtypeMatching__"] = False
		self.vs[12]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "son"
"""
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[12]["MT_dirty__"] = False
		self.vs[12]["mm__"] = """MT_pre__directLink_S"""
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc12fourMembersclass4')
    	# match association Family--daughter-->Member node
		self.add_node()
		self.vs[13]["MT_subtypeMatching__"] = False
		self.vs[13]["MT_pre__associationType"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access any attribute x of this node by: this['x'].
# If the constraint relies on attribute values from other nodes,
# use the LHS/NAC constraint instead.
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return attr_value == "daughter"
"""
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[13]["MT_dirty__"] = False
		self.vs[13]["mm__"] = """MT_pre__directLink_S"""
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0assoc13fourMembersclass3')
        
        
        # Nodes that represent the apply associations of the property.
    	# apply association Community--has-->Man node
		self.add_node()
		self.vs[14]["MT_subtypeMatching__"] = False
		self.vs[14]["MT_pre__associationType"] = """
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
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[14]["MT_dirty__"] = False
		self.vs[14]["mm__"] = """MT_pre__directLink_T"""
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass5assoc14fourMembersclass6')
    	# apply association Community--has-->Man node
		self.add_node()
		self.vs[15]["MT_subtypeMatching__"] = False
		self.vs[15]["MT_pre__associationType"] = """
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
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[15]["MT_dirty__"] = False
		self.vs[15]["mm__"] = """MT_pre__directLink_T"""
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass5assoc15fourMembersclass7')
    	# apply association Community--has-->Female node
		self.add_node()
		self.vs[16]["MT_subtypeMatching__"] = False
		self.vs[16]["MT_pre__associationType"] = """
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
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[16]["MT_dirty__"] = False
		self.vs[16]["mm__"] = """MT_pre__directLink_T"""
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass5assoc16fourMembersclass8')
    	# apply association Community--has-->Female node
		self.add_node()
		self.vs[17]["MT_subtypeMatching__"] = False
		self.vs[17]["MT_pre__associationType"] = """
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
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[17]["MT_dirty__"] = False
		self.vs[17]["mm__"] = """MT_pre__directLink_T"""
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass5assoc17fourMembersclass9')
        
		# Nodes that represent trace relations
		# backward association Family---->Community node
		self.add_node()
		self.vs[18]["MT_subtypeMatching__"] = False
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[18]["MT_dirty__"] = False
		self.vs[18]["mm__"] = """MT_pre__trace_link"""
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass0blink18fourMembersclass5')
		# backward association Member---->Man node
		self.add_node()
		self.vs[19]["MT_subtypeMatching__"] = False
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[19]["MT_dirty__"] = False
		self.vs[19]["mm__"] = """MT_pre__trace_link"""
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass4blink19fourMembersclass7')
		# backward association Member---->Man node
		self.add_node()
		self.vs[20]["MT_subtypeMatching__"] = False
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[20]["MT_dirty__"] = False
		self.vs[20]["mm__"] = """MT_pre__trace_link"""
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass2blink20fourMembersclass6')
		# backward association Member---->Female node
		self.add_node()
		self.vs[21]["MT_subtypeMatching__"] = False
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[21]["MT_dirty__"] = False
		self.vs[21]["mm__"] = """MT_pre__trace_link"""
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass3blink21fourMembersclass8')
		# backward association Member---->Female node
		self.add_node()
		self.vs[22]["MT_subtypeMatching__"] = False
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[22]["MT_dirty__"] = False
		self.vs[22]["mm__"] = """MT_pre__trace_link"""
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'fourMembersclass1blink22fourMembersclass9')
        
        
		# Nodes that represent match attributes
        
        
        #Nodes that represent apply attributes
        
        
		# Add the edges
		self.add_edges([
    		(5,18), # apply_class Community(fourMembersclass5) -> backward_association
    		(18,0), #  backward_association -> apply_class Family(fourMembersclass0)
    		(7,19), # apply_class Man(fourMembersclass7) -> backward_association
    		(19,4), #  backward_association -> apply_class Member(fourMembersclass4)
    		(6,20), # apply_class Man(fourMembersclass6) -> backward_association
    		(20,2), #  backward_association -> apply_class Member(fourMembersclass2)
    		(8,21), # apply_class Female(fourMembersclass8) -> backward_association
    		(21,3), #  backward_association -> apply_class Member(fourMembersclass3)
    		(9,22), # apply_class Female(fourMembersclass9) -> backward_association
    		(22,1), #  backward_association -> apply_class Member(fourMembersclass1)
    		(5,14), # apply_class Community(fourMembersclass5) -> association has
    		(14,6), # association has  -> apply_class Man(fourMembersclass6)
    		(5,15), # apply_class Community(fourMembersclass5) -> association has
    		(15,7), # association has  -> apply_class Man(fourMembersclass7)
    		(5,16), # apply_class Community(fourMembersclass5) -> association has
    		(16,8), # association has  -> apply_class Female(fourMembersclass8)
    		(5,17), # apply_class Community(fourMembersclass5) -> association has
    		(17,9), # association has  -> apply_class Female(fourMembersclass9)
    		(0,10), # match_class Family(fourMembersclass0) -> association father
    		(10,2), # association father  -> match_class Member(fourMembersclass2)
    		(0,11), # match_class Family(fourMembersclass0) -> association mother
    		(11,1), # association mother  -> match_class Member(fourMembersclass1)
    		(0,12), # match_class Family(fourMembersclass0) -> association son
    		(12,4), # association son  -> match_class Member(fourMembersclass4)
    		(0,13), # match_class Family(fourMembersclass0) -> association daughter
    		(13,3) # association daughter  -> match_class Member(fourMembersclass3)
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

        
		def eval_associationType11(self, attr_value, this):
			
			#===============================================================================
			# This code is executed when evaluating if a node shall be matched by this rule.
			# You can access the value of the current node's attribute value by: attr_value.
			# You can access any attribute x of this node by: this['x'].
			# If the constraint relies on attribute values from other nodes,
			# use the LHS/NAC constraint instead.
			# The given constraint must evaluate to a boolean expression.
			#===============================================================================
			
			return attr_value == "father"
			

		def eval_associationType12(self, attr_value, this):
			
			#===============================================================================
			# This code is executed when evaluating if a node shall be matched by this rule.
			# You can access the value of the current node's attribute value by: attr_value.
			# You can access any attribute x of this node by: this['x'].
			# If the constraint relies on attribute values from other nodes,
			# use the LHS/NAC constraint instead.
			# The given constraint must evaluate to a boolean expression.
			#===============================================================================
			
			return attr_value == "mother"
			

		def eval_associationType13(self, attr_value, this):
			
			#===============================================================================
			# This code is executed when evaluating if a node shall be matched by this rule.
			# You can access the value of the current node's attribute value by: attr_value.
			# You can access any attribute x of this node by: this['x'].
			# If the constraint relies on attribute values from other nodes,
			# use the LHS/NAC constraint instead.
			# The given constraint must evaluate to a boolean expression.
			#===============================================================================
			
			return attr_value == "son"
			

		def eval_associationType14(self, attr_value, this):
			
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

