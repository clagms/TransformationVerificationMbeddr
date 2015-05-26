from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

class HmotherFather_CompleteLHS(HimesisPreConditionPatternLHS):
	def __init__(self):
		"""
		Creates the himesis graph representing the AToM3 model HmotherFather_CompleteLHS.
		"""
		# Flag this instance as compiled now
		self.is_compiled = True
		
		super(HmotherFather_CompleteLHS, self).__init__(name='HmotherFather_CompleteLHS', num_nodes=0, edges=[])
		
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
		self["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFather')
        
		# Nodes that represent match classes
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
		self.vs[2]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass2')
        
        
        #Nodes that represent apply classes
    	# match class CommunityRoot(motherFatherclass3) node
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
		self.vs[3]["mm__"] = """MT_pre__CommunityRoot"""  
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
		self.vs[3]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass3')
    	# match class Man(motherFatherclass4) node
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
		self.vs[4]["mm__"] = """MT_pre__Man"""  
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
		self.vs[4]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass4')
    	# match class Woman(motherFatherclass5) node
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
		self.vs[5]["mm__"] = """MT_pre__Woman"""  
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
		self.vs[5]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass5')
        
                
        # Nodes that represent the match associations of the property.
    	# match association Family--father-->Member node
		self.add_node()
		self.vs[6]["MT_subtypeMatching__"] = False
		self.vs[6]["MT_pre__associationType"] = """
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
		self.vs[6]["MT_label__"] = """7"""
		self.vs[6]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[6]["MT_dirty__"] = False
		self.vs[6]["mm__"] = """MT_pre__directLink_S"""
		self.vs[6]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0assoc6motherFatherclass1')
    	# match association Family--mother-->Member node
		self.add_node()
		self.vs[7]["MT_subtypeMatching__"] = False
		self.vs[7]["MT_pre__associationType"] = """
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
		self.vs[7]["MT_label__"] = """8"""
		self.vs[7]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[7]["MT_dirty__"] = False
		self.vs[7]["mm__"] = """MT_pre__directLink_S"""
		self.vs[7]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0assoc7motherFatherclass2')
        
        
        # Nodes that represent the apply associations of the property.
    	# apply association CommunityRoot--has-->Man node
		self.add_node()
		self.vs[8]["MT_subtypeMatching__"] = False
		self.vs[8]["MT_pre__associationType"] = """
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
		self.vs[8]["mm__"] = """MT_pre__directLink_T"""
		self.vs[8]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass3assoc8motherFatherclass4')
    	# apply association CommunityRoot--has-->Woman node
		self.add_node()
		self.vs[9]["MT_subtypeMatching__"] = False
		self.vs[9]["MT_pre__associationType"] = """
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
		self.vs[9]["mm__"] = """MT_pre__directLink_T"""
		self.vs[9]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass3assoc9motherFatherclass5')
        
		# Nodes that represent trace relations
		# backward association Member---->Man node
		self.add_node()
		self.vs[10]["MT_subtypeMatching__"] = False
		self.vs[10]["MT_label__"] = """11"""
		self.vs[10]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[10]["MT_dirty__"] = False
		self.vs[10]["mm__"] = """MT_pre__trace_link"""
		self.vs[10]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass1blink10motherFatherclass4')
		# backward association Member---->Woman node
		self.add_node()
		self.vs[11]["MT_subtypeMatching__"] = False
		self.vs[11]["MT_label__"] = """12"""
		self.vs[11]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[11]["MT_dirty__"] = False
		self.vs[11]["mm__"] = """MT_pre__trace_link"""
		self.vs[11]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass2blink11motherFatherclass5')
        
        
		# Nodes that represent match attributes
		# has match attribute lastName(motherFatherclass0attribute0) node
		self.add_node()
		self.vs[12]["MT_subtypeMatching__"] = False
		self.vs[12]["MT_label__"] = """13"""
		self.vs[12]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[12]["mm__"] = """MT_pre__hasAttr_S"""
		self.vs[12]["MT_dirty__"] = False
		self.vs[12]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass0attribute0')
    	
    	# match attribute lastName(motherFatherclass0attribute0) node
		self.add_node()
		self.vs[13]["MT_subtypeMatching__"] = False
		self.vs[13]["MT_label__"] = """14"""
		self.vs[13]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[13]["mm__"] = """MT_pre__Attribute"""
		self.vs[13]["MT_dirty__"] = False
		self.vs[13]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass0attribute0')
		# has match attribute firstName(motherFatherclass1attribute0) node
		self.add_node()
		self.vs[14]["MT_subtypeMatching__"] = False
		self.vs[14]["MT_label__"] = """15"""
		self.vs[14]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[14]["mm__"] = """MT_pre__hasAttr_S"""
		self.vs[14]["MT_dirty__"] = False
		self.vs[14]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass1attribute0')
    	
    	# match attribute firstName(motherFatherclass1attribute0) node
		self.add_node()
		self.vs[15]["MT_subtypeMatching__"] = False
		self.vs[15]["MT_label__"] = """16"""
		self.vs[15]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[15]["mm__"] = """MT_pre__Attribute"""
		self.vs[15]["MT_dirty__"] = False
		self.vs[15]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass1attribute0')
		# has match attribute firstName(motherFatherclass2attribute0) node
		self.add_node()
		self.vs[16]["MT_subtypeMatching__"] = False
		self.vs[16]["MT_label__"] = """17"""
		self.vs[16]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[16]["mm__"] = """MT_pre__hasAttr_S"""
		self.vs[16]["MT_dirty__"] = False
		self.vs[16]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass2attribute0')
    	
    	# match attribute firstName(motherFatherclass2attribute0) node
		self.add_node()
		self.vs[17]["MT_subtypeMatching__"] = False
		self.vs[17]["MT_label__"] = """18"""
		self.vs[17]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[17]["mm__"] = """MT_pre__Attribute"""
		self.vs[17]["MT_dirty__"] = False
		self.vs[17]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass2attribute0')
        
        
        #Nodes that represent apply attributes
    	# has apply attribute name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[18]["MT_subtypeMatching__"] = False
		self.vs[18]["MT_label__"] = """19"""
		self.vs[18]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[18]["mm__"] = """MT_pre__hasAttr_T"""
		self.vs[18]["MT_dirty__"] = False
		self.vs[18]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass4attribute0')
    	
    	# apply attribute name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[19]["MT_subtypeMatching__"] = False
		self.vs[19]["MT_label__"] = """20"""
		self.vs[19]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[19]["mm__"] = """MT_pre__Attribute"""
		self.vs[19]["MT_dirty__"] = False
		self.vs[19]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn attr_value = "name"\u000a
p1
.""")
		self.vs[19]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass4attribute0')
    	# apply attribute equation name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[20]["MT_subtypeMatching__"] = False
		self.vs[20]["MT_label__"] = """21"""
		self.vs[20]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[20]["mm__"] = """MT_pre__Equation"""
		self.vs[20]["MT_dirty__"] = False
		self.vs[20]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationmotherFatherclass4attribute0')
		# apply attribute equation left expr name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[21]["MT_subtypeMatching__"] = False
		self.vs[21]["MT_label__"] = """22"""
		self.vs[21]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[21]["mm__"] = """MT_pre__leftExpr"""
		self.vs[21]["MT_dirty__"] = False
		self.vs[21]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprmotherFatherclass4attribute0')
    	# apply attribute equation right expr name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[22]["MT_subtypeMatching__"] = False
		self.vs[22]["MT_label__"] = """23"""
		self.vs[22]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[22]["mm__"] = """MT_pre__rightExpr"""
		self.vs[22]["MT_dirty__"] = False
		self.vs[22]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprmotherFatherclass4attribute0')
		# attribute concat name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[23]["MT_subtypeMatching__"] = False
		self.vs[23]["MT_label__"] = """24"""
		self.vs[23]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[23]["mm__"] = """MT_pre__Concat"""
		self.vs[23]["MT_dirty__"] = False
		self.vs[23]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatmotherFatherclass4attribute023')
    	# apply attribute concat has left args name(motherFatherclass4attribute0) node
		self.add_node()
        
		self.vs[24]["MT_subtypeMatching__"] = False
		self.vs[24]["MT_label__"] = """25"""
		self.vs[24]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[24]["mm__"] = """MT_pre__hasArgs"""
		self.vs[24]["MT_dirty__"] = False
		self.vs[24]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgsmotherFatherclass4attribute024')
    	# apply attribute concat has right args name(motherFatherclass4attribute0) node
		self.add_node()
		self.vs[25]["MT_subtypeMatching__"] = False
		self.vs[25]["MT_label__"] = """26"""
		self.vs[25]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[25]["mm__"] = """MT_pre__hasArgs"""
		self.vs[25]["MT_dirty__"] = False
		self.vs[25]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgsmotherFatherclass4attribute025')
    	# has apply attribute name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[26]["MT_subtypeMatching__"] = False
		self.vs[26]["MT_label__"] = """27"""
		self.vs[26]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[26]["mm__"] = """MT_pre__hasAttr_T"""
		self.vs[26]["MT_dirty__"] = False
		self.vs[26]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'hasmotherFatherclass5attribute0')
    	
    	# apply attribute name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[27]["MT_subtypeMatching__"] = False
		self.vs[27]["MT_label__"] = """28"""
		self.vs[27]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[27]["mm__"] = """MT_pre__Attribute"""
		self.vs[27]["MT_dirty__"] = False
		self.vs[27]["MT_pre__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# This code is executed when evaluating if a node shall be matched by this rule.\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access any attribute x of this node by: this['x'].\u000a# If the constraint relies on attribute values from other nodes,\u000a# use the LHS/NAC constraint instead.\u000a# The given constraint must evaluate to a boolean expression.\u000a#===============================================================================\u000a\u000areturn attr_value = "name"\u000a
p1
.""")
		self.vs[27]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'motherFatherclass5attribute0')
    	# apply attribute equation name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[28]["MT_subtypeMatching__"] = False
		self.vs[28]["MT_label__"] = """29"""
		self.vs[28]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[28]["mm__"] = """MT_pre__Equation"""
		self.vs[28]["MT_dirty__"] = False
		self.vs[28]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationmotherFatherclass5attribute0')
		# apply attribute equation left expr name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[29]["MT_subtypeMatching__"] = False
		self.vs[29]["MT_label__"] = """30"""
		self.vs[29]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[29]["mm__"] = """MT_pre__leftExpr"""
		self.vs[29]["MT_dirty__"] = False
		self.vs[29]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationLeftExprmotherFatherclass5attribute0')
    	# apply attribute equation right expr name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[30]["MT_subtypeMatching__"] = False
		self.vs[30]["MT_label__"] = """31"""
		self.vs[30]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[30]["mm__"] = """MT_pre__rightExpr"""
		self.vs[30]["MT_dirty__"] = False
		self.vs[30]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'EquationRightExprmotherFatherclass5attribute0')
		# attribute concat name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[31]["MT_subtypeMatching__"] = False
		self.vs[31]["MT_label__"] = """32"""
		self.vs[31]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[31]["mm__"] = """MT_pre__Concat"""
		self.vs[31]["MT_dirty__"] = False
		self.vs[31]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatmotherFatherclass5attribute031')
    	# apply attribute concat has left args name(motherFatherclass5attribute0) node
		self.add_node()
        
		self.vs[32]["MT_subtypeMatching__"] = False
		self.vs[32]["MT_label__"] = """33"""
		self.vs[32]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[32]["mm__"] = """MT_pre__hasArgs"""
		self.vs[32]["MT_dirty__"] = False
		self.vs[32]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgsmotherFatherclass5attribute032')
    	# apply attribute concat has right args name(motherFatherclass5attribute0) node
		self.add_node()
		self.vs[33]["MT_subtypeMatching__"] = False
		self.vs[33]["MT_label__"] = """34"""
		self.vs[33]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
		self.vs[33]["mm__"] = """MT_pre__hasArgs"""
		self.vs[33]["MT_dirty__"] = False
		self.vs[33]["GUID__"] = uuid.uuid3(uuid.NAMESPACE_DNS,'ConcatHasLeftArgsmotherFatherclass5attribute033')
        
        
		# Add the edges
		self.add_edges([
    		(4,10), # apply_class Man(motherFatherclass4) -> backward_association
    		(10,1), #  backward_association -> apply_class Member(motherFatherclass1)
    		(5,11), # apply_class Woman(motherFatherclass5) -> backward_association
    		(11,2), #  backward_association -> apply_class Member(motherFatherclass2)
    		(0,12), # match_class Family(motherFatherclass0) -> has_match_attribute lastName (motherFatherclass0attribute0)
    		(12,13), #  has_match_attribute lastName (motherFatherclass0attribute0) -> match_attribute lastName (motherFatherclass0attribute0)
    		(1,14), # match_class Member(motherFatherclass1) -> has_match_attribute firstName (motherFatherclass1attribute0)
    		(14,15), #  has_match_attribute firstName (motherFatherclass1attribute0) -> match_attribute firstName (motherFatherclass1attribute0)
    		(2,16), # match_class Member(motherFatherclass2) -> has_match_attribute firstName (motherFatherclass2attribute0)
    		(16,17), #  has_match_attribute firstName (motherFatherclass2attribute0) -> match_attribute firstName (motherFatherclass2attribute0)
    		(4,18), # apply_class Man(motherFatherclass4) -> has_apply_attribute name (motherFatherclass4attribute0)
    		(18,19), #  has_apply_attribute name (motherFatherclass4attribute0) -> apply_attribute name (motherFatherclass4attribute0)
			(20,21), #  equation of apply attribute name (motherFatherclass4attribute0) -> left_expr
    		(21,19), #  left_expr -> apply_attribute name (motherFatherclass4attribute0)
    		(20,22), #  equation of apply attribute name (motherFatherclass4attribute0) -> right_expr
    		(23,24), #  apply attribute concat name (motherFatherclass4attribute0) -> left has_args  
    		(24,15), #  left has_args -> term
    		(23,25), #  apply attribute concat name (motherFatherclass4attribute0) -> right has_args  
    		(25,13), #  right has_args -> term
    		(22,23), # right_expr --> term
    		(5,26), # apply_class Woman(motherFatherclass5) -> has_apply_attribute name (motherFatherclass5attribute0)
    		(26,27), #  has_apply_attribute name (motherFatherclass5attribute0) -> apply_attribute name (motherFatherclass5attribute0)
			(28,29), #  equation of apply attribute name (motherFatherclass5attribute0) -> left_expr
    		(29,27), #  left_expr -> apply_attribute name (motherFatherclass5attribute0)
    		(28,30), #  equation of apply attribute name (motherFatherclass5attribute0) -> right_expr
    		(31,32), #  apply attribute concat name (motherFatherclass5attribute0) -> left has_args  
    		(32,17), #  left has_args -> term
    		(31,33), #  apply attribute concat name (motherFatherclass5attribute0) -> right has_args  
    		(33,13), #  right has_args -> term
    		(30,31), # right_expr --> term
    		(3,8), # apply_class CommunityRoot(motherFatherclass3) -> association has
    		(8,4), # association has  -> apply_class Man(motherFatherclass4)
    		(3,9), # apply_class CommunityRoot(motherFatherclass3) -> association has
    		(9,5), # association has  -> apply_class Woman(motherFatherclass5)
    		(0,6), # match_class Family(motherFatherclass0) -> association father
    		(6,1), # association father  -> match_class Member(motherFatherclass1)
    		(0,7), # match_class Family(motherFatherclass0) -> association mother
    		(7,2) # association mother  -> match_class Member(motherFatherclass2)
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

        
		def eval_associationType7(self, attr_value, this):
			
			#===============================================================================
			# This code is executed when evaluating if a node shall be matched by this rule.
			# You can access the value of the current node's attribute value by: attr_value.
			# You can access any attribute x of this node by: this['x'].
			# If the constraint relies on attribute values from other nodes,
			# use the LHS/NAC constraint instead.
			# The given constraint must evaluate to a boolean expression.
			#===============================================================================
			
			return attr_value == "father"
			

		def eval_associationType8(self, attr_value, this):
			
			#===============================================================================
			# This code is executed when evaluating if a node shall be matched by this rule.
			# You can access the value of the current node's attribute value by: attr_value.
			# You can access any attribute x of this node by: this['x'].
			# If the constraint relies on attribute values from other nodes,
			# use the LHS/NAC constraint instead.
			# The given constraint must evaluate to a boolean expression.
			#===============================================================================
			
			return attr_value == "mother"
			

        
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

