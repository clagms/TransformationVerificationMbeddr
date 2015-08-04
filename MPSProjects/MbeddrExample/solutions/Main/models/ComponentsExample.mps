<?xml version="1.0" encoding="UTF-8"?>
<model ref="r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)">
  <persistence version="9" />
  <languages>
    <use id="54f2a59b-97bb-4c09-af92-928ebf9c5966" name="com.mbeddr.ext.compositecomponents" version="-1" />
    <use id="028899e1-bfee-4db6-b470-ed0f9ee5f662" name="com.mbeddr.ext.components.embedded" version="-1" />
    <use id="97d24244-51db-4e2e-97fc-7bd73b1f5f40" name="com.mbeddr.ext.components" version="-1" />
    <devkit ref="d2a9c55c-6bdc-4cc2-97e1-4ba7552f5584(com.mbeddr.core)" />
    <devkit ref="24565007-e59f-42fc-ac10-da3836deec1c(com.mbeddr.components)" />
    <devkit ref="315c0ec2-38ff-4e9c-9d15-fd0848b5f062(com.mbeddr.analyses.components)" />
  </languages>
  <imports />
  <registry>
    <language id="a9d69647-0840-491e-bf39-2eb0805d2011" name="com.mbeddr.core.statements">
      <concept id="8441331188640771826" name="com.mbeddr.core.statements.structure.WhileStatement" flags="ng" index="27v$Wf">
        <child id="8441331188640771828" name="body" index="27v$W9" />
        <child id="8441331188640771827" name="condition" index="27v$We" />
      </concept>
      <concept id="7763322639126652757" name="com.mbeddr.core.statements.structure.ITypeContainingType" flags="ng" index="2umbIr">
        <child id="7763322639126652758" name="baseType" index="2umbIo" />
      </concept>
      <concept id="7254843406768833938" name="com.mbeddr.core.statements.structure.ExpressionStatement" flags="ng" index="1_9egQ">
        <child id="7254843406768833939" name="expr" index="1_9egR" />
      </concept>
      <concept id="4185783222026475238" name="com.mbeddr.core.statements.structure.LocalVariableDeclaration" flags="ng" index="3XIRlf">
        <child id="4185783222026502647" name="init" index="3XIe9u" />
      </concept>
      <concept id="4185783222026475861" name="com.mbeddr.core.statements.structure.StatementList" flags="ng" index="3XIRFW">
        <child id="4185783222026475862" name="statements" index="3XIRFZ" />
      </concept>
      <concept id="2093108837558113914" name="com.mbeddr.core.statements.structure.LocalVarRef" flags="ng" index="3ZVu4v">
        <reference id="2093108837558124071" name="var" index="3ZVs_2" />
      </concept>
    </language>
    <language id="2d7fadf5-33f6-4e80-a78f-0f739add2bde" name="com.mbeddr.core.buildconfig">
      <concept id="5046689135693761556" name="com.mbeddr.core.buildconfig.structure.Binary" flags="ng" index="2eOfOj">
        <child id="5046689135693761559" name="referencedModules" index="2eOfOg" />
      </concept>
      <concept id="5046689135693761554" name="com.mbeddr.core.buildconfig.structure.Executable" flags="ng" index="2eOfOl">
        <property id="3431613015799084476" name="isTest" index="iO3LB" />
      </concept>
      <concept id="7717755763392524104" name="com.mbeddr.core.buildconfig.structure.BuildConfiguration" flags="ng" index="2v9HqL">
        <child id="5046689135694070731" name="binaries" index="2ePNbc" />
        <child id="5323740605968447026" name="target" index="2AWWZH" />
      </concept>
      <concept id="7717755763392524107" name="com.mbeddr.core.buildconfig.structure.ModuleRef" flags="ng" index="2v9HqM">
        <reference id="7717755763392524108" name="module" index="2v9HqP" />
      </concept>
      <concept id="5323740605968447022" name="com.mbeddr.core.buildconfig.structure.DesktopPlatform" flags="ng" index="2AWWZL">
        <property id="5323740605968447025" name="compilerOptions" index="2AWWZI" />
        <property id="5323740605968447024" name="compiler" index="2AWWZJ" />
        <property id="3963667026125442601" name="gdb" index="3r8Kw1" />
        <property id="3963667026125442676" name="make" index="3r8Kxs" />
      </concept>
      <concept id="2736179788492003936" name="com.mbeddr.core.buildconfig.structure.IDebuggablePlatform" flags="ng" index="1FkSt_">
        <property id="2736179788492003937" name="debugOptions" index="1FkSt$" />
      </concept>
    </language>
    <language id="3bf5377a-e904-4ded-9754-5a516023bfaa" name="com.mbeddr.core.pointers">
      <concept id="6113173064526131575" name="com.mbeddr.core.pointers.structure.StringLiteral" flags="ng" index="PhEJO">
        <property id="6113173064526131578" name="value" index="PhEJT" />
      </concept>
      <concept id="6113173064528067332" name="com.mbeddr.core.pointers.structure.StringType" flags="ng" index="Pu267" />
      <concept id="5679441017214012545" name="com.mbeddr.core.pointers.structure.ArrayType" flags="ng" index="3J0A42" />
    </language>
    <language id="bd640b8f-4be4-42b6-8dc0-2c94d1ddf606" name="com.mbeddr.ext.components.gen_nomw">
      <concept id="2103658896110278831" name="com.mbeddr.ext.components.gen_nomw.structure.NoMwComponentsGenStrategy" flags="ng" index="3i3YCL">
        <property id="4768833643347725006" name="generateContracts" index="3Ewwow" />
      </concept>
    </language>
    <language id="2693fc71-9b0e-4b05-ab13-f57227d675f2" name="com.mbeddr.core.util">
      <concept id="767515563077204464" name="com.mbeddr.core.util.structure.MessageProperty" flags="ng" index="2qqzEA" />
      <concept id="2688792604367903085" name="com.mbeddr.core.util.structure.MessageDefinitionTable" flags="ng" index="2vmPJd">
        <child id="2688792604367903095" name="messages" index="2vmPJn" />
      </concept>
      <concept id="2688792604367903087" name="com.mbeddr.core.util.structure.MessageDefinition" flags="ng" index="2vmPJf">
        <property id="2688792604367903089" name="text" index="2vmPJh" />
        <property id="2688792604367903094" name="kind" index="2vmPJm" />
        <property id="2688792604367947988" name="active" index="2vn0DO" />
        <child id="767515563077204474" name="properties" index="2qqzEG" />
      </concept>
      <concept id="2688792604367964821" name="com.mbeddr.core.util.structure.ReportStatement" flags="ng" index="2vn4wP">
        <child id="2688792604367973273" name="msgref" index="2vn6$T" />
      </concept>
      <concept id="2688792604367964823" name="com.mbeddr.core.util.structure.MessageRef" flags="ng" index="2vn4wR">
        <reference id="2688792604367964824" name="table" index="2vn4wS" />
        <reference id="2688792604367964825" name="msg" index="2vn4wT" />
        <child id="767515563077221084" name="propVals" index="2qqZAa" />
      </concept>
      <concept id="4459718605982051949" name="com.mbeddr.core.util.structure.ReportingConfiguration" flags="ng" index="2Q9Fgs">
        <child id="4459718605982051999" name="strategy" index="2Q9FjI" />
      </concept>
      <concept id="4459718605982051980" name="com.mbeddr.core.util.structure.PrintfReportingStrategy" flags="ng" index="2Q9FjX" />
    </language>
    <language id="d4280a54-f6df-4383-aa41-d1b2bffa7eb1" name="com.mbeddr.core.base">
      <concept id="4459718605982007337" name="com.mbeddr.core.base.structure.IConfigurationContainer" flags="ng" index="2Q9xDo">
        <child id="4459718605982007338" name="configurationItems" index="2Q9xDr" />
      </concept>
    </language>
    <language id="6d11763d-483d-4b2b-8efc-09336c1b0001" name="com.mbeddr.core.modules">
      <concept id="8967919205527146149" name="com.mbeddr.core.modules.structure.ReturnStatement" flags="ng" index="2BFjQ_">
        <child id="8967919205527146150" name="expression" index="2BFjQA" />
      </concept>
      <concept id="8105003328814797298" name="com.mbeddr.core.modules.structure.IFunctionLike" flags="ng" index="2H9T1B">
        <child id="5708867820623310661" name="arguments" index="1UOdpc" />
      </concept>
      <concept id="6437088627575722813" name="com.mbeddr.core.modules.structure.Module" flags="ng" index="N3F4X">
        <child id="6437088627575722833" name="contents" index="N3F5h" />
      </concept>
      <concept id="6437088627575722830" name="com.mbeddr.core.modules.structure.ImplementationModule" flags="ng" index="N3F5e" />
      <concept id="6437088627575722831" name="com.mbeddr.core.modules.structure.IModuleContent" flags="ng" index="N3F5f">
        <property id="1317894735999272944" name="exported" index="2OOxQR" />
      </concept>
      <concept id="6437088627575724001" name="com.mbeddr.core.modules.structure.Function" flags="ng" index="N3Fnx">
        <child id="4185783222026475860" name="body" index="3XIRFX" />
      </concept>
      <concept id="8934095934011938595" name="com.mbeddr.core.modules.structure.EmptyModuleContent" flags="ng" index="2NXPZ9" />
      <concept id="7892328519581704407" name="com.mbeddr.core.modules.structure.Argument" flags="ng" index="19RgSI" />
      <concept id="2093108837558505658" name="com.mbeddr.core.modules.structure.ArgumentRef" flags="ng" index="3ZUYvv">
        <reference id="2093108837558505659" name="arg" index="3ZUYvu" />
      </concept>
    </language>
    <language id="06d68b77-b699-4918-83b8-857e63787800" name="com.mbeddr.core.unittest">
      <concept id="6275792049641586523" name="com.mbeddr.core.unittest.structure.TestCase" flags="ng" index="c0Qz5">
        <child id="6275792049641586525" name="body" index="c0Qz3" />
      </concept>
      <concept id="5686538669182340985" name="com.mbeddr.core.unittest.structure.TestCaseRef" flags="ng" index="3cM6IN">
        <reference id="5686538669182340986" name="testcase" index="3cM6IK" />
      </concept>
      <concept id="186853311768094629" name="com.mbeddr.core.unittest.structure.ExecuteTestExpression" flags="ng" index="3rBj6X">
        <child id="5686538669182341016" name="tests" index="3cM6Hi" />
      </concept>
    </language>
    <language id="ceab5195-25ea-4f22-9b92-103b95ca8c0c" name="jetbrains.mps.lang.core">
      <concept id="1169194658468" name="jetbrains.mps.lang.core.structure.INamedConcept" flags="ng" index="TrEIO">
        <property id="1169194664001" name="name" index="TrG5h" />
      </concept>
    </language>
    <language id="97d24244-51db-4e2e-97fc-7bd73b1f5f40" name="com.mbeddr.ext.components">
      <concept id="6616025724454668918" name="com.mbeddr.ext.components.structure.AdapterInstancePortRef" flags="ng" index="219P8x">
        <reference id="6616025724454668919" name="instance" index="219P8w" />
        <reference id="6616025724454668920" name="port" index="219P8J" />
      </concept>
      <concept id="5172178961828157634" name="com.mbeddr.ext.components.structure.PortAdapter" flags="ng" index="21gPQu">
        <child id="6616025724454701213" name="portRef" index="21ad3a" />
      </concept>
      <concept id="7780999115923942144" name="com.mbeddr.ext.components.structure.AbstractInstanceConfiguration" flags="ng" index="5Js9S">
        <child id="7780999115923944213" name="contents" index="5JtDH" />
      </concept>
      <concept id="4491876417845649024" name="com.mbeddr.ext.components.structure.InstanceConfiguration" flags="ng" index="2EWCtd" />
      <concept id="4491876417845649017" name="com.mbeddr.ext.components.structure.InstancePortRef" flags="ng" index="2EWCuO">
        <reference id="4491876417845649018" name="instance" index="2EWCuR" />
        <reference id="3444913373458569211" name="port" index="XcPQd" />
      </concept>
      <concept id="4491876417845649016" name="com.mbeddr.ext.components.structure.AssemblyConnector" flags="ng" index="2EWCuP">
        <child id="4491876417845649021" name="target" index="2EWCuK" />
        <child id="4491876417845649020" name="source" index="2EWCuL" />
      </concept>
      <concept id="4491876417845649014" name="com.mbeddr.ext.components.structure.ComponentInstance" flags="ng" index="2EWCuV">
        <reference id="4491876417845649015" name="component" index="2EWCuU" />
      </concept>
      <concept id="4491876417845649011" name="com.mbeddr.ext.components.structure.AtomicComponent" flags="ng" index="2EWCuY" />
      <concept id="4491876417845641677" name="com.mbeddr.ext.components.structure.OperationTrigger" flags="ng" index="2EWDw0" />
      <concept id="4491876417845641670" name="com.mbeddr.ext.components.structure.Runnable" flags="ng" index="2EWDwb">
        <child id="4491876417845643892" name="trigger" index="2EWDeT" />
        <child id="4491876417845689763" name="body" index="2EWMhI" />
      </concept>
      <concept id="4491876417845628841" name="com.mbeddr.ext.components.structure.RequiredPort" flags="ng" index="2EWHp$" />
      <concept id="4491876417845628840" name="com.mbeddr.ext.components.structure.ProvidedPort" flags="ng" index="2EWHp_" />
      <concept id="4491876417845683828" name="com.mbeddr.ext.components.structure.OperationParameter" flags="ng" index="2EWNYT" />
      <concept id="4491876417845484930" name="com.mbeddr.ext.components.structure.Port" flags="ng" index="2EX0hf">
        <reference id="4491876417845484932" name="intf" index="2EX0h9" />
      </concept>
      <concept id="4491876417845484924" name="com.mbeddr.ext.components.structure.Operation" flags="ng" index="2EX0iL" />
      <concept id="4491876417845484922" name="com.mbeddr.ext.components.structure.ClientServerInterface" flags="ng" index="2EX0iR">
        <child id="4491876417845484926" name="contents" index="2EX0iN" />
      </concept>
      <concept id="4491876417845474761" name="com.mbeddr.ext.components.structure.Component" flags="ng" index="2EX6K4">
        <child id="6041318036221669720" name="contents" index="2RW2fA" />
      </concept>
      <concept id="8105003328815208362" name="com.mbeddr.ext.components.structure.PortRefExpr" flags="ng" index="2H6loZ">
        <reference id="8105003328815208363" name="port" index="2H6loY" />
      </concept>
      <concept id="8105003328815071749" name="com.mbeddr.ext.components.structure.InterfaceOperationCallExpr" flags="ng" index="2H6Oeg">
        <reference id="8105003328815071752" name="operation" index="2H6Oet" />
        <child id="8105003328815091213" name="actuals" index="2H6KYo" />
      </concept>
      <concept id="8105003328815039001" name="com.mbeddr.ext.components.structure.PortAdapterRefExpr" flags="ng" index="2H6Wec">
        <reference id="8105003328815039002" name="portAdater" index="2H6Wef" />
      </concept>
      <concept id="466603768608442377" name="com.mbeddr.ext.components.structure.RequiredPortOpCallExpr" flags="ng" index="30IBQI" />
      <concept id="466603768608410221" name="com.mbeddr.ext.components.structure.PortAdapterOpCallExpr" flags="ng" index="30IJZa" />
      <concept id="2103658896110121032" name="com.mbeddr.ext.components.structure.ComponentsConfigItem" flags="ng" index="3i2$bm">
        <child id="2103658896110238743" name="genStrategy" index="3i30U9" />
      </concept>
      <concept id="591155063063570513" name="com.mbeddr.ext.components.structure.InitializeConfiguration" flags="ng" index="3t9XKO">
        <reference id="591155063063570514" name="config" index="3t9XKR" />
      </concept>
      <concept id="8515777736166878876" name="com.mbeddr.ext.components.structure.EmptyComponentContent" flags="ng" index="3Khz0B" />
      <concept id="4514118643321588318" name="com.mbeddr.ext.components.structure.IOperationTriggerLike" flags="ng" index="1ZwTiz">
        <reference id="4514118643321619583" name="calledOperation" index="1ZwxE2" />
        <reference id="4514118643321592184" name="providedPort" index="1ZwSu5" />
      </concept>
    </language>
    <language id="61c69711-ed61-4850-81d9-7714ff227fb0" name="com.mbeddr.core.expressions">
      <concept id="8463282783691618440" name="com.mbeddr.core.expressions.structure.Int32tType" flags="ng" index="26Vqph" />
      <concept id="3005510381523579442" name="com.mbeddr.core.expressions.structure.UnaryExpression" flags="ng" index="2aKSnQ">
        <child id="7254843406768839760" name="expression" index="1_9fRO" />
      </concept>
      <concept id="2212975673976017893" name="com.mbeddr.core.expressions.structure.NumericLiteral" flags="ng" index="2hns93">
        <property id="2212975673976043696" name="value" index="2hmy$m" />
      </concept>
      <concept id="5763383285156373013" name="com.mbeddr.core.expressions.structure.PlusExpression" flags="ng" index="2BOciq" />
      <concept id="318113533128716675" name="com.mbeddr.core.expressions.structure.ITyped" flags="ng" index="2C2TGh">
        <child id="318113533128716676" name="type" index="2C2TGm" />
      </concept>
      <concept id="7892328519581699353" name="com.mbeddr.core.expressions.structure.VoidType" flags="ng" index="19Rifw" />
      <concept id="22102029902365709" name="com.mbeddr.core.expressions.structure.AssignmentExpr" flags="ng" index="3pqW6w" />
      <concept id="8860443239512147447" name="com.mbeddr.core.expressions.structure.GreaterEqualsExpression" flags="ng" index="3Tl9Jp" />
      <concept id="8860443239512128054" name="com.mbeddr.core.expressions.structure.Type" flags="ng" index="3TlMgo">
        <property id="2941277002445651368" name="const" index="2c7vTL" />
        <property id="2941277002448691247" name="volatile" index="2caQfQ" />
      </concept>
      <concept id="8860443239512128052" name="com.mbeddr.core.expressions.structure.BinaryExpression" flags="ng" index="3TlMgq">
        <child id="8860443239512128064" name="left" index="3TlMhI" />
        <child id="8860443239512128065" name="right" index="3TlMhJ" />
      </concept>
      <concept id="8860443239512128103" name="com.mbeddr.core.expressions.structure.NumberLiteral" flags="ng" index="3TlMh9" />
    </language>
  </registry>
  <node concept="N3F5e" id="3g9yVqYqnYz">
    <property role="TrG5h" value="ComponentsSample" />
    <node concept="2EX0iR" id="3g9yVqYr5p_" role="N3F5h">
      <property role="2OOxQR" value="true" />
      <property role="TrG5h" value="Client" />
      <node concept="2EX0iL" id="3g9yVqYr5r9" role="2EX0iN">
        <property role="TrG5h" value="client_process" />
        <node concept="19Rifw" id="3g9yVqYr5r7" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="6cEg21zqGiW" role="N3F5h">
      <property role="TrG5h" value="empty_1417129228519_8" />
    </node>
    <node concept="2EX0iR" id="3g9yVqYr5pp" role="N3F5h">
      <property role="2OOxQR" value="true" />
      <property role="TrG5h" value="Server" />
      <node concept="2EX0iL" id="3g9yVqYr5sh" role="2EX0iN">
        <property role="TrG5h" value="server_process" />
        <node concept="Pu267" id="3g9yVqYr7AL" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
        </node>
        <node concept="2EWNYT" id="3g9yVqYr5t7" role="1UOdpc">
          <property role="TrG5h" value="request" />
          <node concept="Pu267" id="3g9yVqYr5t6" role="2C2TGm">
            <property role="2caQfQ" value="false" />
            <property role="2c7vTL" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="3g9yVqYr5pR" role="N3F5h">
      <property role="TrG5h" value="empty_1416672011371_11" />
    </node>
    <node concept="2EWCuY" id="3g9yVqYr5qf" role="N3F5h">
      <property role="2OOxQR" value="true" />
      <property role="TrG5h" value="ClientComponent" />
      <node concept="2EWHp_" id="3g9yVqYr5qw" role="2RW2fA">
        <property role="TrG5h" value="clientInterface" />
        <ref role="2EX0h9" node="3g9yVqYr5p_" resolve="Client" />
      </node>
      <node concept="2EWHp$" id="3g9yVqYr5qK" role="2RW2fA">
        <property role="TrG5h" value="clientcomp_serverInterface" />
        <ref role="2EX0h9" node="3g9yVqYr5pp" resolve="Server" />
      </node>
      <node concept="3Khz0B" id="3g9yVqYr5Dg" role="2RW2fA" />
      <node concept="2EWDwb" id="3g9yVqYr5KA" role="2RW2fA">
        <property role="TrG5h" value="clientInterface_client_process" />
        <node concept="3XIRFW" id="3g9yVqYr5KB" role="2EWMhI">
          <node concept="2vn4wP" id="3g9yVqYrfdf" role="3XIRFZ">
            <node concept="2vn4wR" id="3g9yVqYrfdh" role="2vn6$T">
              <ref role="2vn4wT" node="3g9yVqYrhee" resolve="ClientStart" />
              <ref role="2vn4wS" node="3g9yVqYrgqU" resolve="messages" />
            </node>
          </node>
          <node concept="1_9egQ" id="3g9yVqYr5Ta" role="3XIRFZ">
            <node concept="30IBQI" id="3g9yVqYr5Tq" role="1_9egR">
              <ref role="2H6Oet" node="3g9yVqYr5sh" resolve="server_process" />
              <node concept="2H6loZ" id="3g9yVqYr5T9" role="1_9fRO">
                <ref role="2H6loY" node="3g9yVqYr5qK" resolve="clientcomp_serverInterface" />
              </node>
              <node concept="PhEJO" id="3g9yVqYr5TX" role="2H6KYo">
                <property role="PhEJT" value="Hello" />
              </node>
            </node>
          </node>
          <node concept="2vn4wP" id="3g9yVqYrjJ1" role="3XIRFZ">
            <node concept="2vn4wR" id="3g9yVqYrjJ2" role="2vn6$T">
              <ref role="2vn4wS" node="3g9yVqYrgqU" resolve="messages" />
              <ref role="2vn4wT" node="3g9yVqYrjKm" resolve="ClientEnd" />
            </node>
          </node>
        </node>
        <node concept="2EWDw0" id="3g9yVqYr5L7" role="2EWDeT">
          <ref role="1ZwSu5" node="3g9yVqYr5qw" resolve="clientInterface" />
          <ref role="1ZwxE2" node="3g9yVqYr5r9" resolve="client_process" />
        </node>
        <node concept="19Rifw" id="7RjEbnpyNR_" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="3g9yVqYrfCs" role="N3F5h">
      <property role="TrG5h" value="empty_1416672887896_18" />
    </node>
    <node concept="2EWCuY" id="3g9yVqYr6mp" role="N3F5h">
      <property role="2OOxQR" value="true" />
      <property role="TrG5h" value="GoodServer" />
      <node concept="2EWHp_" id="3g9yVqYr6oA" role="2RW2fA">
        <property role="TrG5h" value="serverInterface" />
        <ref role="2EX0h9" node="3g9yVqYr5pp" resolve="Server" />
      </node>
      <node concept="2EWDwb" id="3g9yVqYr6vV" role="2RW2fA">
        <property role="TrG5h" value="serverInterface_server_process" />
        <node concept="3XIRFW" id="3g9yVqYr6vW" role="2EWMhI">
          <node concept="2vn4wP" id="3g9yVqYrjS_" role="3XIRFZ">
            <node concept="2vn4wR" id="3g9yVqYrjSA" role="2vn6$T">
              <ref role="2vn4wT" node="3g9yVqYrjPh" resolve="GServerStart" />
              <ref role="2vn4wS" node="3g9yVqYrgqU" resolve="messages" />
            </node>
          </node>
          <node concept="2vn4wP" id="3g9yVqYrk04" role="3XIRFZ">
            <node concept="2vn4wR" id="3g9yVqYrk05" role="2vn6$T">
              <ref role="2vn4wT" node="3g9yVqYrjPt" resolve="GServerEnd" />
              <ref role="2vn4wS" node="3g9yVqYrgqU" resolve="messages" />
              <node concept="3ZUYvv" id="7RjEbnpyQQU" role="2qqZAa">
                <ref role="3ZUYvu" node="7RjEbnpyO4w" resolve="request" />
              </node>
            </node>
          </node>
          <node concept="2BFjQ_" id="3g9yVqYr6yt" role="3XIRFZ">
            <node concept="3ZUYvv" id="7RjEbnpyQSj" role="2BFjQA">
              <ref role="3ZUYvu" node="7RjEbnpyO4w" resolve="request" />
            </node>
          </node>
        </node>
        <node concept="2EWDw0" id="3g9yVqYr6wy" role="2EWDeT">
          <ref role="1ZwSu5" node="3g9yVqYr6oA" resolve="serverInterface" />
          <ref role="1ZwxE2" node="3g9yVqYr5sh" resolve="server_process" />
        </node>
        <node concept="Pu267" id="7RjEbnpyO4v" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
        </node>
        <node concept="19RgSI" id="7RjEbnpyO4w" role="1UOdpc">
          <property role="TrG5h" value="request" />
          <node concept="Pu267" id="7RjEbnpyO4x" role="2C2TGm">
            <property role="2caQfQ" value="false" />
            <property role="2c7vTL" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="3g9yVqYr6Vb" role="N3F5h">
      <property role="TrG5h" value="empty_1416672546635_15" />
    </node>
    <node concept="2EWCuY" id="3g9yVqYr7uz" role="N3F5h">
      <property role="2OOxQR" value="true" />
      <property role="TrG5h" value="BadServer" />
      <node concept="2EWHp_" id="3g9yVqYr7J$" role="2RW2fA">
        <property role="TrG5h" value="serverInterface" />
        <ref role="2EX0h9" node="3g9yVqYr5pp" resolve="Server" />
      </node>
      <node concept="2EWDwb" id="3g9yVqYr82G" role="2RW2fA">
        <property role="TrG5h" value="serverInterface_server_process" />
        <node concept="3XIRFW" id="3g9yVqYr82H" role="2EWMhI">
          <node concept="2vn4wP" id="3g9yVqYrkft" role="3XIRFZ">
            <node concept="2vn4wR" id="3g9yVqYrkfu" role="2vn6$T">
              <ref role="2vn4wT" node="3g9yVqYrjPK" resolve="BServerStart" />
              <ref role="2vn4wS" node="3g9yVqYrgqU" resolve="messages" />
            </node>
          </node>
          <node concept="3XIRlf" id="3g9yVqYr8iC" role="3XIRFZ">
            <property role="TrG5h" value="x" />
            <node concept="26Vqph" id="3g9yVqYr8iA" role="2C2TGm">
              <property role="2caQfQ" value="false" />
              <property role="2c7vTL" value="false" />
            </node>
            <node concept="3TlMh9" id="3g9yVqYr8GN" role="3XIe9u">
              <property role="2hmy$m" value="0" />
            </node>
          </node>
          <node concept="27v$Wf" id="3g9yVqYr86h" role="3XIRFZ">
            <node concept="3XIRFW" id="3g9yVqYr86i" role="27v$W9">
              <node concept="1_9egQ" id="3g9yVqYraEp" role="3XIRFZ">
                <node concept="3pqW6w" id="3g9yVqYraKz" role="1_9egR">
                  <node concept="2BOciq" id="3g9yVqYrbZc" role="3TlMhJ">
                    <node concept="3ZVu4v" id="3g9yVqYrbZf" role="3TlMhI">
                      <ref role="3ZVs_2" node="3g9yVqYr8iC" resolve="x" />
                    </node>
                    <node concept="3TlMh9" id="3g9yVqYrbZe" role="3TlMhJ">
                      <property role="2hmy$m" value="1" />
                    </node>
                  </node>
                  <node concept="3ZVu4v" id="3g9yVqYraEo" role="3TlMhI">
                    <ref role="3ZVs_2" node="3g9yVqYr8iC" resolve="x" />
                  </node>
                </node>
              </node>
            </node>
            <node concept="3Tl9Jp" id="3g9yVqYrdLj" role="27v$We">
              <node concept="3ZVu4v" id="3g9yVqYrdLm" role="3TlMhI">
                <ref role="3ZVs_2" node="3g9yVqYr8iC" resolve="x" />
              </node>
              <node concept="3TlMh9" id="3g9yVqYrdLl" role="3TlMhJ">
                <property role="2hmy$m" value="0" />
              </node>
            </node>
          </node>
          <node concept="2vn4wP" id="3g9yVqYrkfv" role="3XIRFZ">
            <node concept="2vn4wR" id="3g9yVqYrkfw" role="2vn6$T">
              <ref role="2vn4wT" node="3g9yVqYrjPL" resolve="BServerEnd" />
              <ref role="2vn4wS" node="3g9yVqYrgqU" resolve="messages" />
              <node concept="3ZUYvv" id="7RjEbnpyQTy" role="2qqZAa">
                <ref role="3ZUYvu" node="7RjEbnpyO4q" resolve="request" />
              </node>
            </node>
          </node>
          <node concept="2BFjQ_" id="3g9yVqYr894" role="3XIRFZ">
            <node concept="3ZUYvv" id="7RjEbnpyQXT" role="2BFjQA">
              <ref role="3ZUYvu" node="7RjEbnpyO4q" resolve="request" />
            </node>
          </node>
        </node>
        <node concept="2EWDw0" id="3g9yVqYr84y" role="2EWDeT">
          <ref role="1ZwSu5" node="3g9yVqYr7J$" resolve="serverInterface" />
          <ref role="1ZwxE2" node="3g9yVqYr5sh" resolve="server_process" />
        </node>
        <node concept="Pu267" id="7RjEbnpyO4p" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
        </node>
        <node concept="19RgSI" id="7RjEbnpyO4q" role="1UOdpc">
          <property role="TrG5h" value="request" />
          <node concept="Pu267" id="7RjEbnpyO4r" role="2C2TGm">
            <property role="2caQfQ" value="false" />
            <property role="2c7vTL" value="false" />
          </node>
        </node>
      </node>
      <node concept="3Khz0B" id="3g9yVqYr85h" role="2RW2fA" />
    </node>
    <node concept="2NXPZ9" id="3g9yVqYrpV8" role="N3F5h">
      <property role="TrG5h" value="empty_1416673739229_22" />
    </node>
    <node concept="2vmPJd" id="3g9yVqYrgqU" role="N3F5h">
      <property role="TrG5h" value="messages" />
      <node concept="2vmPJf" id="3g9yVqYrhee" role="2vmPJn">
        <property role="2vn0DO" value="true" />
        <property role="2vmPJm" value="1" />
        <property role="TrG5h" value="ClientStart" />
        <property role="2vmPJh" value="Client started." />
      </node>
      <node concept="2vmPJf" id="3g9yVqYrjKm" role="2vmPJn">
        <property role="2vn0DO" value="true" />
        <property role="2vmPJm" value="1" />
        <property role="TrG5h" value="ClientEnd" />
        <property role="2vmPJh" value="Client ended." />
      </node>
      <node concept="2vmPJf" id="3g9yVqYrjPh" role="2vmPJn">
        <property role="2vn0DO" value="true" />
        <property role="2vmPJm" value="1" />
        <property role="TrG5h" value="GServerStart" />
        <property role="2vmPJh" value="Good server started." />
      </node>
      <node concept="2vmPJf" id="3g9yVqYrjPt" role="2vmPJn">
        <property role="2vn0DO" value="true" />
        <property role="2vmPJm" value="1" />
        <property role="TrG5h" value="GServerEnd" />
        <property role="2vmPJh" value="Good server ended." />
        <node concept="2qqzEA" id="3g9yVqYrk7j" role="2qqzEG">
          <property role="TrG5h" value="result" />
          <node concept="Pu267" id="3g9yVqYrk7i" role="2C2TGm">
            <property role="2caQfQ" value="false" />
            <property role="2c7vTL" value="false" />
          </node>
        </node>
      </node>
      <node concept="2vmPJf" id="3g9yVqYrjPK" role="2vmPJn">
        <property role="2vn0DO" value="true" />
        <property role="2vmPJm" value="1" />
        <property role="TrG5h" value="BServerStart" />
        <property role="2vmPJh" value="Bad server started." />
      </node>
      <node concept="2vmPJf" id="3g9yVqYrjPL" role="2vmPJn">
        <property role="2vn0DO" value="true" />
        <property role="2vmPJm" value="1" />
        <property role="TrG5h" value="BServerEnd" />
        <property role="2vmPJh" value="Bad server ended." />
        <node concept="2qqzEA" id="3g9yVqYrkcf" role="2qqzEG">
          <property role="TrG5h" value="result" />
          <node concept="Pu267" id="3g9yVqYrkce" role="2C2TGm">
            <property role="2caQfQ" value="false" />
            <property role="2c7vTL" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="3g9yVqYrqOT" role="N3F5h">
      <property role="TrG5h" value="empty_1416673744631_24" />
    </node>
    <node concept="2EWCtd" id="3g9yVqYrrcA" role="N3F5h">
      <property role="TrG5h" value="instances" />
      <node concept="2EWCuV" id="3g9yVqYrrCX" role="5JtDH">
        <property role="TrG5h" value="clientComponent" />
        <ref role="2EWCuU" node="3g9yVqYr5qf" resolve="ClientComponent" />
      </node>
      <node concept="2EWCuV" id="3g9yVqYrrEU" role="5JtDH">
        <property role="TrG5h" value="gserverComponent" />
        <ref role="2EWCuU" node="3g9yVqYr6mp" resolve="GoodServer" />
      </node>
      <node concept="2EWCuV" id="3g9yVqYrrFF" role="5JtDH">
        <property role="TrG5h" value="bserverComponent" />
        <ref role="2EWCuU" node="3g9yVqYr7uz" resolve="BadServer" />
      </node>
      <node concept="2EWCuP" id="27pHwXIaRh6" role="5JtDH">
        <node concept="2EWCuO" id="27pHwXIaRh7" role="2EWCuL">
          <ref role="XcPQd" node="3g9yVqYr5qK" resolve="clientcomp_serverInterface" />
          <ref role="2EWCuR" node="3g9yVqYrrCX" resolve="clientComponent" />
        </node>
        <node concept="2EWCuO" id="27pHwXIaRh8" role="2EWCuK">
          <ref role="XcPQd" node="3g9yVqYr6oA" resolve="serverInterface" />
          <ref role="2EWCuR" node="3g9yVqYrrEU" resolve="gserverComponent" />
        </node>
      </node>
      <node concept="21gPQu" id="3g9yVqYrtgI" role="5JtDH">
        <property role="TrG5h" value="clientPort" />
        <node concept="219P8x" id="3g9yVqYrtgJ" role="21ad3a">
          <ref role="219P8w" node="3g9yVqYrrCX" resolve="clientComponent" />
          <ref role="219P8J" node="3g9yVqYr5qw" resolve="clientInterface" />
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="3GSXuMfTDx5" role="N3F5h">
      <property role="TrG5h" value="empty_1419593284711_1" />
    </node>
    <node concept="c0Qz5" id="3g9yVqYrsI4" role="N3F5h">
      <property role="2OOxQR" value="true" />
      <property role="TrG5h" value="MainTest" />
      <node concept="19Rifw" id="3g9yVqYrsI5" role="2C2TGm">
        <property role="2caQfQ" value="false" />
        <property role="2c7vTL" value="false" />
      </node>
      <node concept="3XIRFW" id="3g9yVqYrsI7" role="c0Qz3">
        <node concept="3t9XKO" id="3g9yVqYrtbm" role="3XIRFZ">
          <ref role="3t9XKR" node="3g9yVqYrrcA" resolve="instances" />
        </node>
        <node concept="1_9egQ" id="3g9yVqYrtj_" role="3XIRFZ">
          <node concept="30IJZa" id="3g9yVqYrtjR" role="1_9egR">
            <ref role="2H6Oet" node="3g9yVqYr5r9" resolve="client_process" />
            <node concept="2H6Wec" id="27pHwXIaK0j" role="1_9fRO">
              <ref role="2H6Wef" node="3g9yVqYrtgI" resolve="clientPort" />
            </node>
          </node>
        </node>
      </node>
    </node>
    <node concept="2NXPZ9" id="3g9yVqYsfk1" role="N3F5h">
      <property role="TrG5h" value="empty_1416674391010_28" />
    </node>
    <node concept="N3Fnx" id="7VsgA5L654v" role="N3F5h">
      <property role="TrG5h" value="main" />
      <property role="2OOxQR" value="true" />
      <node concept="3XIRFW" id="7VsgA5L654w" role="3XIRFX">
        <node concept="2BFjQ_" id="7VsgA5L654x" role="3XIRFZ">
          <node concept="3rBj6X" id="7VsgA5L654y" role="2BFjQA">
            <node concept="3cM6IN" id="3g9yVqYshDL" role="3cM6Hi">
              <ref role="3cM6IK" node="3g9yVqYrsI4" resolve="MainTest" />
            </node>
          </node>
        </node>
      </node>
      <node concept="26Vqph" id="7VsgA5L654$" role="2C2TGm">
        <property role="2caQfQ" value="false" />
        <property role="2c7vTL" value="false" />
      </node>
      <node concept="19RgSI" id="7VsgA5L654_" role="1UOdpc">
        <property role="TrG5h" value="argc" />
        <node concept="26Vqph" id="7VsgA5L654A" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
        </node>
      </node>
      <node concept="19RgSI" id="7VsgA5L654B" role="1UOdpc">
        <property role="TrG5h" value="argv" />
        <node concept="3J0A42" id="7VsgA5L654C" role="2C2TGm">
          <property role="2caQfQ" value="false" />
          <property role="2c7vTL" value="false" />
          <node concept="Pu267" id="7VsgA5L654E" role="2umbIo">
            <property role="2caQfQ" value="false" />
            <property role="2c7vTL" value="false" />
          </node>
        </node>
      </node>
    </node>
  </node>
  <node concept="2v9HqL" id="3g9yVqYsdgP">
    <node concept="2AWWZL" id="3g9yVqYsdgQ" role="2AWWZH">
      <property role="2AWWZJ" value="gcc" />
      <property role="3r8Kw1" value="gdb" />
      <property role="3r8Kxs" value="make" />
      <property role="2AWWZI" value="-std=c99" />
      <property role="1FkSt$" value="-g" />
    </node>
    <node concept="2Q9Fgs" id="3g9yVqYseJ9" role="2Q9xDr">
      <node concept="2Q9FjX" id="3g9yVqYseJa" role="2Q9FjI" />
    </node>
    <node concept="3i2$bm" id="3g9yVqYseJm" role="2Q9xDr">
      <node concept="3i3YCL" id="3g9yVqYseJy" role="3i30U9">
        <property role="3Ewwow" value="true" />
      </node>
    </node>
    <node concept="2eOfOl" id="3g9yVqYseMo" role="2ePNbc">
      <property role="iO3LB" value="true" />
      <property role="TrG5h" value="ComponentsExec" />
      <node concept="2v9HqM" id="3g9yVqYseMr" role="2eOfOg">
        <ref role="2v9HqP" node="3g9yVqYqnYz" resolve="ComponentsSample" />
      </node>
    </node>
  </node>
</model>

