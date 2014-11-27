<?xml version="1.0" encoding="UTF-8"?>
<model modelUID="r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)">
  <persistence version="8" />
  <language namespace="54f2a59b-97bb-4c09-af92-928ebf9c5966(com.mbeddr.ext.compositecomponents)" />
  <language namespace="028899e1-bfee-4db6-b470-ed0f9ee5f662(com.mbeddr.ext.components.embedded)" />
  <language namespace="97d24244-51db-4e2e-97fc-7bd73b1f5f40(com.mbeddr.ext.components)" />
  <devkit namespace="d2a9c55c-6bdc-4cc2-97e1-4ba7552f5584(com.mbeddr.core)" />
  <devkit namespace="24565007-e59f-42fc-ac10-da3836deec1c(com.mbeddr.components)" />
  <devkit namespace="315c0ec2-38ff-4e9c-9d15-fd0848b5f062(com.mbeddr.analyses.components)" />
  <import index="tpck" modelUID="r:00000000-0000-4000-0000-011c89590288(jetbrains.mps.lang.core.structure)" version="0" implicit="yes" />
  <import index="x27k" modelUID="r:75ecab8a-8931-4140-afc6-4b46398710fc(com.mbeddr.core.modules.structure)" version="9" implicit="yes" />
  <import index="v7ag" modelUID="r:9596407c-f27a-49d3-abde-3a66293c5b61(com.mbeddr.ext.components.structure)" version="19" implicit="yes" />
  <import index="mj1l" modelUID="r:c371cf98-dcc8-4a43-8eb8-8a8096de18b2(com.mbeddr.core.expressions.structure)" version="36" implicit="yes" />
  <import index="yq40" modelUID="r:152b3fc0-83a1-4bab-a8cd-565eb8483785(com.mbeddr.core.pointers.structure)" version="5" implicit="yes" />
  <import index="c4fa" modelUID="r:9f0e84b6-2ec7-4f9e-83e0-feedc77b63a3(com.mbeddr.core.statements.structure)" version="11" implicit="yes" />
  <import index="k146" modelUID="r:5209fc71-bade-45c9-9079-f2d474f0d6ca(com.mbeddr.core.util.structure)" version="21" implicit="yes" />
  <import index="yz9a" modelUID="r:734c02dd-cc16-4184-99eb-5fd9f43aa37e(com.mbeddr.core.unittest.structure)" version="0" implicit="yes" />
  <import index="51wr" modelUID="r:b31f1c3c-99aa-4f1e-a329-cba27efb1a6b(com.mbeddr.core.buildconfig.structure)" version="1" implicit="yes" />
  <import index="vs0r" modelUID="r:f7764ca4-8c75-4049-922b-08516400a727(com.mbeddr.core.base.structure)" version="25" implicit="yes" />
  <import index="p7vm" modelUID="r:28fa862e-f94d-4c39-bdf7-a4bdbc773888(com.mbeddr.ext.components.gen_nomw.structure)" version="0" implicit="yes" />
  <root type="x27k.ImplementationModule" typeId="x27k.6437088627575722830" id="3749681781757542307" nodeInfo="ng">
    <property name="name" nameId="tpck.1169194664001" value="ComponentsSample" />
    <node role="contents" roleId="x27k.6437088627575722833" type="v7ag.ClientServerInterface" typeId="v7ag.4491876417845484922" id="3749681781757728357" nodeInfo="ng">
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="Client" />
      <node role="contents" roleId="v7ag.4491876417845484926" type="v7ag.Operation" typeId="v7ag.4491876417845484924" id="3749681781757728457" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="process" />
        <node role="type" roleId="mj1l.318113533128716676" type="mj1l.VoidType" typeId="mj1l.7892328519581699353" id="3749681781757728455" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757728366" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416672008719_10" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="v7ag.ClientServerInterface" typeId="v7ag.4491876417845484922" id="3749681781757728345" nodeInfo="ng">
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="Server" />
      <node role="contents" roleId="v7ag.4491876417845484926" type="v7ag.Operation" typeId="v7ag.4491876417845484924" id="3749681781757728529" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="process" />
        <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="3749681781757737393" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
        <node role="arguments" roleId="x27k.5708867820623310661" type="v7ag.OperationParameter" typeId="v7ag.4491876417845683828" id="3749681781757728583" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="request" />
          <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="3749681781757728582" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757728375" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416672011371_11" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="v7ag.AtomicComponent" typeId="v7ag.4491876417845649011" id="3749681781757728399" nodeInfo="ng">
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="ClientComponent" />
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.ProvidedPort" typeId="v7ag.4491876417845628840" id="3749681781757728416" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="clientInterface" />
        <link role="intf" roleId="v7ag.4491876417845484932" targetNodeId="3749681781757728357" resolveInfo="Client" />
      </node>
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.RequiredPort" typeId="v7ag.4491876417845628841" id="3749681781757728432" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="serverInterface" />
        <link role="intf" roleId="v7ag.4491876417845484932" targetNodeId="3749681781757728345" resolveInfo="Server" />
      </node>
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.EmptyComponentContent" typeId="v7ag.8515777736166878876" id="3749681781757729360" nodeInfo="ng" />
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.Runnable" typeId="v7ag.4491876417845641670" id="3749681781757729830" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="clientInterface_process" />
        <node role="body" roleId="v7ag.4491876417845689763" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="3749681781757729831" nodeInfo="ng">
          <node role="statements" roleId="c4fa.4185783222026475862" type="k146.ReportStatement" typeId="k146.2688792604367964821" id="3749681781757768527" nodeInfo="ng">
            <node role="msgref" roleId="k146.2688792604367973273" type="k146.MessageRef" typeId="k146.2688792604367964823" id="3749681781757768529" nodeInfo="ng">
              <link role="msg" roleId="k146.2688792604367964825" targetNodeId="3749681781757776782" resolveInfo="ClientStart" />
              <link role="table" roleId="k146.2688792604367964824" targetNodeId="3749681781757773498" resolveInfo="messages" />
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.ExpressionStatement" typeId="c4fa.7254843406768833938" id="3749681781757730378" nodeInfo="ng">
            <node role="expr" roleId="c4fa.7254843406768833939" type="v7ag.RequiredPortOpCallExpr" typeId="v7ag.466603768608442377" id="3749681781757730394" nodeInfo="ng">
              <link role="operation" roleId="v7ag.8105003328815071752" targetNodeId="3749681781757728529" resolveInfo="process" />
              <node role="expression" roleId="mj1l.7254843406768839760" type="v7ag.PortRefExpr" typeId="v7ag.8105003328815208362" id="3749681781757730377" nodeInfo="ng">
                <link role="port" roleId="v7ag.8105003328815208363" targetNodeId="3749681781757728432" resolveInfo="serverInterface" />
              </node>
              <node role="actuals" roleId="v7ag.8105003328815091213" type="yq40.StringLiteral" typeId="yq40.6113173064526131575" id="3749681781757730429" nodeInfo="ng">
                <property name="value" nameId="yq40.6113173064526131578" value="Hello" />
              </node>
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="k146.ReportStatement" typeId="k146.2688792604367964821" id="3749681781757787073" nodeInfo="ng">
            <node role="msgref" roleId="k146.2688792604367973273" type="k146.MessageRef" typeId="k146.2688792604367964823" id="3749681781757787074" nodeInfo="ng">
              <link role="table" roleId="k146.2688792604367964824" targetNodeId="3749681781757773498" resolveInfo="messages" />
              <link role="msg" roleId="k146.2688792604367964825" targetNodeId="3749681781757787158" resolveInfo="ClientEnd" />
            </node>
          </node>
        </node>
        <node role="trigger" roleId="v7ag.4491876417845643892" type="v7ag.OperationTrigger" typeId="v7ag.4491876417845641677" id="3749681781757729863" nodeInfo="ng">
          <link role="providedPort" roleId="v7ag.4514118643321592184" targetNodeId="3749681781757728416" resolveInfo="clientInterface" />
          <link role="calledOperation" roleId="v7ag.4514118643321619583" targetNodeId="3749681781757728457" resolveInfo="process" />
        </node>
        <node role="type" roleId="mj1l.318113533128716676" type="mj1l.VoidType" typeId="mj1l.7892328519581699353" id="2439180850586847339" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757731919" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416672398341_13" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757770268" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416672887896_18" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="v7ag.AtomicComponent" typeId="v7ag.4491876417845649011" id="3749681781757732249" nodeInfo="ng">
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="GoodServer" />
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.ProvidedPort" typeId="v7ag.4491876417845628840" id="3749681781757732390" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="serverInterface" />
        <link role="intf" roleId="v7ag.4491876417845484932" targetNodeId="3749681781757728345" resolveInfo="Server" />
      </node>
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.Runnable" typeId="v7ag.4491876417845641670" id="3749681781757732859" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="serverInterface_process" />
        <node role="body" roleId="v7ag.4491876417845689763" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="3749681781757732860" nodeInfo="ng">
          <node role="statements" roleId="c4fa.4185783222026475862" type="k146.ReportStatement" typeId="k146.2688792604367964821" id="3749681781757787685" nodeInfo="ng">
            <node role="msgref" roleId="k146.2688792604367973273" type="k146.MessageRef" typeId="k146.2688792604367964823" id="3749681781757787686" nodeInfo="ng">
              <link role="msg" roleId="k146.2688792604367964825" targetNodeId="3749681781757787473" resolveInfo="GServerStart" />
              <link role="table" roleId="k146.2688792604367964824" targetNodeId="3749681781757773498" resolveInfo="messages" />
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="k146.ReportStatement" typeId="k146.2688792604367964821" id="3749681781757788164" nodeInfo="ng">
            <node role="msgref" roleId="k146.2688792604367973273" type="k146.MessageRef" typeId="k146.2688792604367964823" id="3749681781757788165" nodeInfo="ng">
              <link role="msg" roleId="k146.2688792604367964825" targetNodeId="3749681781757787485" resolveInfo="GServerEnd" />
              <link role="table" roleId="k146.2688792604367964824" targetNodeId="3749681781757773498" resolveInfo="messages" />
              <node role="propVals" roleId="k146.767515563077221084" type="x27k.ArgumentRef" typeId="x27k.2093108837558505658" id="2439180850586948192" nodeInfo="ng">
                <link role="arg" roleId="x27k.2093108837558505659" targetNodeId="2439180850586940794" resolveInfo="request" />
              </node>
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="x27k.ReturnStatement" typeId="x27k.8967919205527146149" id="3749681781757733021" nodeInfo="ng">
            <node role="expression" roleId="x27k.8967919205527146150" type="x27k.ArgumentRef" typeId="x27k.2093108837558505658" id="2439180850586948263" nodeInfo="ng">
              <link role="arg" roleId="x27k.2093108837558505659" targetNodeId="2439180850586940794" resolveInfo="request" />
            </node>
          </node>
        </node>
        <node role="trigger" roleId="v7ag.4491876417845643892" type="v7ag.OperationTrigger" typeId="v7ag.4491876417845641677" id="3749681781757732898" nodeInfo="ng">
          <link role="providedPort" roleId="v7ag.4514118643321592184" targetNodeId="3749681781757732390" resolveInfo="serverInterface" />
          <link role="calledOperation" roleId="v7ag.4514118643321619583" targetNodeId="3749681781757728529" resolveInfo="process" />
        </node>
        <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="2439180850586940793" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
        <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="2439180850586940794" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="request" />
          <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="2439180850586940795" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757734603" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416672546635_15" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="v7ag.AtomicComponent" typeId="v7ag.4491876417845649011" id="3749681781757736867" nodeInfo="ng">
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="BadServer" />
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.ProvidedPort" typeId="v7ag.4491876417845628840" id="3749681781757737956" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="serverInterface" />
        <link role="intf" roleId="v7ag.4491876417845484932" targetNodeId="3749681781757728345" resolveInfo="Server" />
      </node>
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.Runnable" typeId="v7ag.4491876417845641670" id="3749681781757739180" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="serverInterface_process" />
        <node role="body" roleId="v7ag.4491876417845689763" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="3749681781757739181" nodeInfo="ng">
          <node role="statements" roleId="c4fa.4185783222026475862" type="k146.ReportStatement" typeId="k146.2688792604367964821" id="3749681781757789149" nodeInfo="ng">
            <node role="msgref" roleId="k146.2688792604367973273" type="k146.MessageRef" typeId="k146.2688792604367964823" id="3749681781757789150" nodeInfo="ng">
              <link role="msg" roleId="k146.2688792604367964825" targetNodeId="3749681781757787504" resolveInfo="BServerStart" />
              <link role="table" roleId="k146.2688792604367964824" targetNodeId="3749681781757773498" resolveInfo="messages" />
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.LocalVariableDeclaration" typeId="c4fa.4185783222026475238" id="3749681781757740200" nodeInfo="ng">
            <property name="name" nameId="tpck.1169194664001" value="x" />
            <node role="type" roleId="mj1l.318113533128716676" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="3749681781757740198" nodeInfo="ng">
              <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
              <property name="const" nameId="mj1l.2941277002445651368" value="false" />
            </node>
            <node role="init" roleId="c4fa.4185783222026502647" type="mj1l.NumberLiteral" typeId="mj1l.8860443239512128103" id="3749681781757741875" nodeInfo="ng">
              <property name="value" nameId="mj1l.2212975673976043696" value="0" />
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.WhileStatement" typeId="c4fa.8441331188640771826" id="3749681781757739409" nodeInfo="ng">
            <node role="body" roleId="c4fa.8441331188640771828" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="3749681781757739410" nodeInfo="ng">
              <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.ExpressionStatement" typeId="c4fa.7254843406768833938" id="3749681781757749913" nodeInfo="ng">
                <node role="expr" roleId="c4fa.7254843406768833939" type="mj1l.AssignmentExpr" typeId="mj1l.22102029902365709" id="3749681781757750307" nodeInfo="ng">
                  <node role="right" roleId="mj1l.8860443239512128065" type="mj1l.PlusExpression" typeId="mj1l.5763383285156373013" id="3749681781757755340" nodeInfo="ng">
                    <node role="left" roleId="mj1l.8860443239512128064" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="3749681781757755343" nodeInfo="ng">
                      <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="3749681781757740200" resolveInfo="x" />
                    </node>
                    <node role="right" roleId="mj1l.8860443239512128065" type="mj1l.NumberLiteral" typeId="mj1l.8860443239512128103" id="3749681781757755342" nodeInfo="ng">
                      <property name="value" nameId="mj1l.2212975673976043696" value="1" />
                    </node>
                  </node>
                  <node role="left" roleId="mj1l.8860443239512128064" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="3749681781757749912" nodeInfo="ng">
                    <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="3749681781757740200" resolveInfo="x" />
                  </node>
                </node>
              </node>
            </node>
            <node role="condition" roleId="c4fa.8441331188640771827" type="mj1l.GreaterEqualsExpression" typeId="mj1l.8860443239512147447" id="3749681781757762643" nodeInfo="ng">
              <node role="left" roleId="mj1l.8860443239512128064" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="3749681781757762646" nodeInfo="ng">
                <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="3749681781757740200" resolveInfo="x" />
              </node>
              <node role="right" roleId="mj1l.8860443239512128065" type="mj1l.NumberLiteral" typeId="mj1l.8860443239512128103" id="3749681781757762645" nodeInfo="ng">
                <property name="value" nameId="mj1l.2212975673976043696" value="0" />
              </node>
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="k146.ReportStatement" typeId="k146.2688792604367964821" id="3749681781757789151" nodeInfo="ng">
            <node role="msgref" roleId="k146.2688792604367973273" type="k146.MessageRef" typeId="k146.2688792604367964823" id="3749681781757789152" nodeInfo="ng">
              <link role="msg" roleId="k146.2688792604367964825" targetNodeId="3749681781757787505" resolveInfo="BServerEnd" />
              <link role="table" roleId="k146.2688792604367964824" targetNodeId="3749681781757773498" resolveInfo="messages" />
              <node role="propVals" roleId="k146.767515563077221084" type="x27k.ArgumentRef" typeId="x27k.2093108837558505658" id="2439180850586948334" nodeInfo="ng">
                <link role="arg" roleId="x27k.2093108837558505659" targetNodeId="2439180850586941041" resolveInfo="request" />
              </node>
            </node>
          </node>
          <node role="statements" roleId="c4fa.4185783222026475862" type="x27k.ReturnStatement" typeId="x27k.8967919205527146149" id="3749681781757739588" nodeInfo="ng">
            <node role="expression" roleId="x27k.8967919205527146150" type="x27k.ArgumentRef" typeId="x27k.2093108837558505658" id="2439180850586947934" nodeInfo="ng">
              <link role="arg" roleId="x27k.2093108837558505659" targetNodeId="2439180850586941041" resolveInfo="request" />
            </node>
          </node>
        </node>
        <node role="trigger" roleId="v7ag.4491876417845643892" type="v7ag.OperationTrigger" typeId="v7ag.4491876417845641677" id="3749681781757739298" nodeInfo="ng">
          <link role="providedPort" roleId="v7ag.4514118643321592184" targetNodeId="3749681781757737956" resolveInfo="serverInterface" />
          <link role="calledOperation" roleId="v7ag.4514118643321619583" targetNodeId="3749681781757728529" resolveInfo="process" />
        </node>
        <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="2439180850586941040" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
        <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="2439180850586941041" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="request" />
          <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="2439180850586941042" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
      <node role="contents" roleId="v7ag.6041318036221669720" type="v7ag.EmptyComponentContent" typeId="v7ag.8515777736166878876" id="3749681781757739345" nodeInfo="ng" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757812424" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416673739229_22" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="k146.MessageDefinitionTable" typeId="k146.2688792604367903085" id="3749681781757773498" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="messages" />
      <node role="messages" roleId="k146.2688792604367903095" type="k146.MessageDefinition" typeId="k146.2688792604367903087" id="3749681781757776782" nodeInfo="ng">
        <property name="active" nameId="k146.2688792604367947988" value="true" />
        <property name="kind" nameId="k146.2688792604367903094" value="1" />
        <property name="name" nameId="tpck.1169194664001" value="ClientStart" />
        <property name="text" nameId="k146.2688792604367903089" value="Client started." />
      </node>
      <node role="messages" roleId="k146.2688792604367903095" type="k146.MessageDefinition" typeId="k146.2688792604367903087" id="3749681781757787158" nodeInfo="ng">
        <property name="active" nameId="k146.2688792604367947988" value="true" />
        <property name="kind" nameId="k146.2688792604367903094" value="1" />
        <property name="name" nameId="tpck.1169194664001" value="ClientEnd" />
        <property name="text" nameId="k146.2688792604367903089" value="Client ended." />
      </node>
      <node role="messages" roleId="k146.2688792604367903095" type="k146.MessageDefinition" typeId="k146.2688792604367903087" id="3749681781757787473" nodeInfo="ng">
        <property name="active" nameId="k146.2688792604367947988" value="true" />
        <property name="kind" nameId="k146.2688792604367903094" value="1" />
        <property name="name" nameId="tpck.1169194664001" value="GServerStart" />
        <property name="text" nameId="k146.2688792604367903089" value="Good server started." />
      </node>
      <node role="messages" roleId="k146.2688792604367903095" type="k146.MessageDefinition" typeId="k146.2688792604367903087" id="3749681781757787485" nodeInfo="ng">
        <property name="active" nameId="k146.2688792604367947988" value="true" />
        <property name="kind" nameId="k146.2688792604367903094" value="1" />
        <property name="name" nameId="tpck.1169194664001" value="GServerEnd" />
        <property name="text" nameId="k146.2688792604367903089" value="Good server ended." />
        <node role="properties" roleId="k146.767515563077204474" type="k146.MessageProperty" typeId="k146.767515563077204464" id="3749681781757788627" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="result" />
          <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="3749681781757788626" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
      <node role="messages" roleId="k146.2688792604367903095" type="k146.MessageDefinition" typeId="k146.2688792604367903087" id="3749681781757787504" nodeInfo="ng">
        <property name="active" nameId="k146.2688792604367947988" value="true" />
        <property name="kind" nameId="k146.2688792604367903094" value="1" />
        <property name="name" nameId="tpck.1169194664001" value="BServerStart" />
        <property name="text" nameId="k146.2688792604367903089" value="Bad server started." />
      </node>
      <node role="messages" roleId="k146.2688792604367903095" type="k146.MessageDefinition" typeId="k146.2688792604367903087" id="3749681781757787505" nodeInfo="ng">
        <property name="active" nameId="k146.2688792604367947988" value="true" />
        <property name="kind" nameId="k146.2688792604367903094" value="1" />
        <property name="name" nameId="tpck.1169194664001" value="BServerEnd" />
        <property name="text" nameId="k146.2688792604367903089" value="Bad server ended." />
        <node role="properties" roleId="k146.767515563077204474" type="k146.MessageProperty" typeId="k146.767515563077204464" id="3749681781757788943" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="result" />
          <node role="type" roleId="mj1l.318113533128716676" type="yq40.StringType" typeId="yq40.6113173064528067332" id="3749681781757788942" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757816121" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416673744631_24" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="v7ag.InstanceConfiguration" typeId="v7ag.4491876417845649024" id="3749681781757817638" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="instances" />
      <node role="contents" roleId="v7ag.7780999115923944213" type="v7ag.ComponentInstance" typeId="v7ag.4491876417845649014" id="3749681781757819453" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="clientComponent" />
        <link role="component" roleId="v7ag.4491876417845649015" targetNodeId="3749681781757728399" resolveInfo="ClientComponent" />
      </node>
      <node role="contents" roleId="v7ag.7780999115923944213" type="v7ag.ComponentInstance" typeId="v7ag.4491876417845649014" id="3749681781757819578" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="gserverComponent" />
        <link role="component" roleId="v7ag.4491876417845649015" targetNodeId="3749681781757732249" resolveInfo="GoodServer" />
      </node>
      <node role="contents" roleId="v7ag.7780999115923944213" type="v7ag.ComponentInstance" typeId="v7ag.4491876417845649014" id="3749681781757819627" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="bserverComponent" />
        <link role="component" roleId="v7ag.4491876417845649015" targetNodeId="3749681781757736867" resolveInfo="BadServer" />
      </node>
      <node role="contents" roleId="v7ag.7780999115923944213" type="v7ag.AssemblyConnector" typeId="v7ag.4491876417845649016" id="2439180850586940486" nodeInfo="ng">
        <node role="source" roleId="v7ag.4491876417845649020" type="v7ag.InstancePortRef" typeId="v7ag.4491876417845649017" id="2439180850586940487" nodeInfo="ng">
          <link role="port" roleId="v7ag.3444913373458569211" targetNodeId="3749681781757728432" resolveInfo="serverInterface" />
          <link role="instance" roleId="v7ag.4491876417845649018" targetNodeId="3749681781757819453" resolveInfo="clientComponent" />
        </node>
        <node role="target" roleId="v7ag.4491876417845649021" type="v7ag.InstancePortRef" typeId="v7ag.4491876417845649017" id="2439180850586940488" nodeInfo="ng">
          <link role="port" roleId="v7ag.3444913373458569211" targetNodeId="3749681781757732390" resolveInfo="serverInterface" />
          <link role="instance" roleId="v7ag.4491876417845649018" targetNodeId="3749681781757819578" resolveInfo="gserverComponent" />
        </node>
      </node>
      <node role="contents" roleId="v7ag.7780999115923944213" type="v7ag.PortAdapter" typeId="v7ag.5172178961828157634" id="3749681781757826094" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="clientPort" />
        <node role="portRef" roleId="v7ag.6616025724454701213" type="v7ag.AdapterInstancePortRef" typeId="v7ag.6616025724454668918" id="3749681781757826095" nodeInfo="ng">
          <link role="instance" roleId="v7ag.6616025724454668919" targetNodeId="3749681781757819453" resolveInfo="clientComponent" />
          <link role="port" roleId="v7ag.6616025724454668920" targetNodeId="3749681781757728416" resolveInfo="clientInterface" />
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757820896" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416674057008_26" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="yz9a.TestCase" typeId="yz9a.6275792049641586523" id="3749681781757823876" nodeInfo="ng">
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="MainTest" />
      <node role="type" roleId="mj1l.318113533128716676" type="mj1l.VoidType" typeId="mj1l.7892328519581699353" id="3749681781757823877" nodeInfo="ng">
        <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
        <property name="const" nameId="mj1l.2941277002445651368" value="false" />
      </node>
      <node role="body" roleId="yz9a.6275792049641586525" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="3749681781757823879" nodeInfo="ng">
        <node role="statements" roleId="c4fa.4185783222026475862" type="v7ag.InitializeConfiguration" typeId="v7ag.591155063063570513" id="3749681781757825750" nodeInfo="ng">
          <link role="config" roleId="v7ag.591155063063570514" targetNodeId="3749681781757817638" resolveInfo="instances" />
        </node>
        <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.ExpressionStatement" typeId="c4fa.7254843406768833938" id="3749681781757826277" nodeInfo="ng">
          <node role="expr" roleId="c4fa.7254843406768833939" type="v7ag.PortAdapterOpCallExpr" typeId="v7ag.466603768608410221" id="3749681781757826295" nodeInfo="ng">
            <link role="operation" roleId="v7ag.8105003328815071752" targetNodeId="3749681781757728457" resolveInfo="process" />
            <node role="expression" roleId="mj1l.7254843406768839760" type="v7ag.PortAdapterRefExpr" typeId="v7ag.8105003328815039001" id="2439180850586910739" nodeInfo="ng">
              <link role="portAdater" roleId="v7ag.8105003328815039002" targetNodeId="3749681781757826094" resolveInfo="clientPort" />
            </node>
          </node>
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781758031105" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416674391010_28" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.Function" typeId="x27k.6437088627575724001" id="9141254329931944223" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="main" />
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <node role="body" roleId="x27k.4185783222026475860" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="9141254329931944224" nodeInfo="ng">
        <node role="statements" roleId="c4fa.4185783222026475862" type="x27k.ReturnStatement" typeId="x27k.8967919205527146149" id="9141254329931944225" nodeInfo="ng">
          <node role="expression" roleId="x27k.8967919205527146150" type="yz9a.ExecuteTestExpression" typeId="yz9a.186853311768094629" id="9141254329931944226" nodeInfo="ng">
            <node role="tests" roleId="yz9a.5686538669182341016" type="yz9a.TestCaseRef" typeId="yz9a.5686538669182340985" id="3749681781758040689" nodeInfo="ng">
              <link role="testcase" roleId="yz9a.5686538669182340986" targetNodeId="3749681781757823876" resolveInfo="MainTest" />
            </node>
          </node>
        </node>
      </node>
      <node role="type" roleId="mj1l.318113533128716676" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="9141254329931944228" nodeInfo="ng">
        <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
        <property name="const" nameId="mj1l.2941277002445651368" value="false" />
      </node>
      <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="9141254329931944229" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="argc" />
        <node role="type" roleId="mj1l.318113533128716676" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="9141254329931944230" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
      </node>
      <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="9141254329931944231" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="argv" />
        <node role="type" roleId="mj1l.318113533128716676" type="yq40.ArrayType" typeId="yq40.5679441017214012545" id="9141254329931944232" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          <node role="baseType" roleId="c4fa.7763322639126652758" type="yq40.StringType" typeId="yq40.6113173064528067332" id="9141254329931944234" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.EmptyModuleContent" typeId="x27k.8934095934011938595" id="3749681781757812575" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="empty_1416673739383_23" />
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.Function" typeId="x27k.6437088627575724001" id="8001866789944361800" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="someCFunction" />
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <node role="body" roleId="x27k.4185783222026475860" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="8001866789944361802" nodeInfo="ng">
        <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.LocalVariableDeclaration" typeId="c4fa.4185783222026475238" id="8001866789944364431" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="cid" />
          <node role="type" roleId="mj1l.318113533128716676" type="yq40.PointerType" typeId="yq40.279446265608459824" id="8001866789944365319" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
            <node role="baseType" roleId="c4fa.7763322639126652758" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="8001866789944364430" nodeInfo="ng">
              <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
              <property name="const" nameId="mj1l.2941277002445651368" value="false" />
            </node>
          </node>
          <node role="init" roleId="c4fa.4185783222026502647" type="mj1l.ParensExpression" typeId="mj1l.5763383285156533447" id="8001866789944366335" nodeInfo="ng">
            <node role="expression" roleId="mj1l.7254843406768839760" type="mj1l.CastExpression" typeId="mj1l.6610873504380029780" id="8001866789944367140" nodeInfo="ng">
              <node role="expr" roleId="mj1l.6610873504380029782" type="x27k.ArgumentRef" typeId="x27k.2093108837558505658" id="8001866789944368320" nodeInfo="ng">
                <link role="arg" roleId="x27k.2093108837558505659" targetNodeId="8001866789944363442" resolveInfo="id" />
              </node>
              <node role="targetType" roleId="mj1l.6610873504380029790" type="yq40.PointerType" typeId="yq40.279446265608459824" id="8001866789944369445" nodeInfo="ng">
                <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
                <property name="const" nameId="mj1l.2941277002445651368" value="false" />
                <node role="baseType" roleId="c4fa.7763322639126652758" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="8001866789944367633" nodeInfo="ng">
                  <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
                  <property name="const" nameId="mj1l.2941277002445651368" value="false" />
                </node>
              </node>
            </node>
          </node>
        </node>
        <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.LocalVariableDeclaration" typeId="c4fa.4185783222026475238" id="8001866789944371306" nodeInfo="ng">
          <property name="name" nameId="tpck.1169194664001" value="x" />
          <node role="type" roleId="mj1l.318113533128716676" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="8001866789944371304" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
          <node role="init" roleId="c4fa.4185783222026502647" type="mj1l.NumberLiteral" typeId="mj1l.8860443239512128103" id="8001866789944375718" nodeInfo="ng">
            <property name="value" nameId="mj1l.2212975673976043696" value="0" />
          </node>
        </node>
        <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.WhileStatement" typeId="c4fa.8441331188640771826" id="8001866789944378632" nodeInfo="ng">
          <node role="body" roleId="c4fa.8441331188640771828" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="8001866789944378633" nodeInfo="ng">
            <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.ExpressionStatement" typeId="c4fa.7254843406768833938" id="8001866789944386463" nodeInfo="ng">
              <node role="expr" roleId="c4fa.7254843406768833939" type="mj1l.AssignmentExpr" typeId="mj1l.22102029902365709" id="8001866789944387533" nodeInfo="ng">
                <node role="right" roleId="mj1l.8860443239512128065" type="mj1l.PlusExpression" typeId="mj1l.5763383285156373013" id="8001866789944390901" nodeInfo="ng">
                  <node role="right" roleId="mj1l.8860443239512128065" type="mj1l.NumberLiteral" typeId="mj1l.8860443239512128103" id="8001866789944390904" nodeInfo="ng">
                    <property name="value" nameId="mj1l.2212975673976043696" value="1" />
                  </node>
                  <node role="left" roleId="mj1l.8860443239512128064" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="8001866789944389692" nodeInfo="ng">
                    <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="8001866789944371306" resolveInfo="x" />
                  </node>
                </node>
                <node role="left" roleId="mj1l.8860443239512128064" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="8001866789944386462" nodeInfo="ng">
                  <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="8001866789944371306" resolveInfo="x" />
                </node>
              </node>
            </node>
          </node>
          <node role="condition" roleId="c4fa.8441331188640771827" type="mj1l.GreaterEqualsExpression" typeId="mj1l.8860443239512147447" id="8001866789944381931" nodeInfo="ng">
            <node role="right" roleId="mj1l.8860443239512128065" type="mj1l.NumberLiteral" typeId="mj1l.8860443239512128103" id="8001866789944383849" nodeInfo="ng">
              <property name="value" nameId="mj1l.2212975673976043696" value="0" />
            </node>
            <node role="left" roleId="mj1l.8860443239512128064" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="8001866789944379658" nodeInfo="ng">
              <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="8001866789944371306" resolveInfo="x" />
            </node>
          </node>
        </node>
        <node role="statements" roleId="c4fa.4185783222026475862" type="c4fa.ExpressionStatement" typeId="c4fa.7254843406768833938" id="8001866789944432933" nodeInfo="ng">
          <node role="expr" roleId="c4fa.7254843406768833939" type="x27k.FunctionCall" typeId="x27k.5950410542643524492" id="8001866789944432931" nodeInfo="ng">
            <link role="function" roleId="x27k.5950410542643524493" targetNodeId="8001866789944424009" resolveInfo="someCFunction2BeCalled" />
            <node role="actuals" roleId="x27k.5950410542643524495" type="c4fa.LocalVarRef" typeId="c4fa.2093108837558113914" id="8001866789944436071" nodeInfo="ng">
              <link role="var" roleId="c4fa.2093108837558124071" targetNodeId="8001866789944371306" resolveInfo="x" />
            </node>
          </node>
        </node>
        <node role="statements" roleId="c4fa.4185783222026475862" type="x27k.ReturnStatement" typeId="x27k.8967919205527146149" id="8001866789944396641" nodeInfo="ng">
          <node role="expression" roleId="x27k.8967919205527146150" type="x27k.ArgumentRef" typeId="x27k.2093108837558505658" id="8001866789944399526" nodeInfo="ng">
            <link role="arg" roleId="x27k.2093108837558505659" targetNodeId="8001866789944363162" resolveInfo="request" />
          </node>
        </node>
      </node>
      <node role="type" roleId="mj1l.318113533128716676" type="yq40.PointerType" typeId="yq40.279446265608459824" id="8001866789944360971" nodeInfo="ng">
        <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
        <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        <node role="baseType" roleId="c4fa.7763322639126652758" type="mj1l.CharType" typeId="mj1l.1664480272136207708" id="8001866789944359749" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
      </node>
      <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="8001866789944363162" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="request" />
        <node role="type" roleId="mj1l.318113533128716676" type="yq40.PointerType" typeId="yq40.279446265608459824" id="8001866789944363349" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          <node role="baseType" roleId="c4fa.7763322639126652758" type="mj1l.CharType" typeId="mj1l.1664480272136207708" id="8001866789944363161" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
      <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="8001866789944363442" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="id" />
        <node role="type" roleId="mj1l.318113533128716676" type="yq40.PointerType" typeId="yq40.279446265608459824" id="8001866789944363507" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          <node role="baseType" roleId="c4fa.7763322639126652758" type="mj1l.VoidType" typeId="mj1l.7892328519581699353" id="8001866789944363440" nodeInfo="ng">
            <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
            <property name="const" nameId="mj1l.2941277002445651368" value="false" />
          </node>
        </node>
      </node>
    </node>
    <node role="contents" roleId="x27k.6437088627575722833" type="x27k.Function" typeId="x27k.6437088627575724001" id="8001866789944424009" nodeInfo="ng">
      <property name="name" nameId="tpck.1169194664001" value="someCFunction2BeCalled" />
      <property name="exported" nameId="x27k.1317894735999272944" value="true" />
      <node role="body" roleId="x27k.4185783222026475860" type="c4fa.StatementList" typeId="c4fa.4185783222026475861" id="8001866789944424011" nodeInfo="ng">
        <node role="statements" roleId="c4fa.4185783222026475862" type="x27k.ReturnStatement" typeId="x27k.8967919205527146149" id="8001866789944429980" nodeInfo="ng" />
      </node>
      <node role="type" roleId="mj1l.318113533128716676" type="mj1l.VoidType" typeId="mj1l.7892328519581699353" id="8001866789944418728" nodeInfo="ng">
        <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
        <property name="const" nameId="mj1l.2941277002445651368" value="false" />
      </node>
      <node role="arguments" roleId="x27k.5708867820623310661" type="x27k.Argument" typeId="x27k.7892328519581704407" id="8001866789944428756" nodeInfo="ng">
        <property name="name" nameId="tpck.1169194664001" value="v" />
        <node role="type" roleId="mj1l.318113533128716676" type="mj1l.Int32tType" typeId="mj1l.8463282783691618440" id="8001866789944428755" nodeInfo="ng">
          <property name="volatile" nameId="mj1l.2941277002448691247" value="false" />
          <property name="const" nameId="mj1l.2941277002445651368" value="false" />
        </node>
      </node>
    </node>
  </root>
  <root type="51wr.BuildConfiguration" typeId="51wr.7717755763392524104" id="3749681781758022709" nodeInfo="ng">
    <node role="target" roleId="51wr.5323740605968447026" type="51wr.DesktopPlatform" typeId="51wr.5323740605968447022" id="3749681781758022710" nodeInfo="ng">
      <property name="compiler" nameId="51wr.5323740605968447024" value="gcc" />
      <property name="gdb" nameId="51wr.3963667026125442601" value="gdb" />
      <property name="make" nameId="51wr.3963667026125442676" value="make" />
      <property name="compilerOptions" nameId="51wr.5323740605968447025" value="-std=c99" />
      <property name="debugOptions" nameId="51wr.2736179788492003937" value="-g" />
    </node>
    <node role="configurationItems" roleId="vs0r.4459718605982007338" type="k146.ReportingConfiguration" typeId="k146.4459718605982051949" id="3749681781758028745" nodeInfo="ng">
      <node role="strategy" roleId="k146.4459718605982051999" type="k146.PrintfReportingStrategy" typeId="k146.4459718605982051980" id="3749681781758028746" nodeInfo="ng" />
    </node>
    <node role="configurationItems" roleId="vs0r.4459718605982007338" type="v7ag.ComponentsConfigItem" typeId="v7ag.2103658896110121032" id="3749681781758028758" nodeInfo="ng">
      <node role="genStrategy" roleId="v7ag.2103658896110238743" type="p7vm.NoMwComponentsGenStrategy" typeId="p7vm.2103658896110278831" id="3749681781758028770" nodeInfo="ng">
        <property name="generateContracts" nameId="p7vm.4768833643347725006" value="true" />
      </node>
    </node>
    <node role="binaries" roleId="51wr.5046689135694070731" type="51wr.Executable" typeId="51wr.5046689135693761554" id="3749681781758028952" nodeInfo="ng">
      <property name="isTest" nameId="51wr.3431613015799084476" value="true" />
      <property name="name" nameId="tpck.1169194664001" value="ComponentsExec" />
      <node role="referencedModules" roleId="51wr.5046689135693761559" type="51wr.ModuleRef" typeId="51wr.7717755763392524107" id="3749681781758028955" nodeInfo="ng">
        <link role="module" roleId="51wr.7717755763392524108" targetNodeId="3749681781757542307" resolveInfo="ComponentsSample" />
      </node>
    </node>
  </root>
</model>

