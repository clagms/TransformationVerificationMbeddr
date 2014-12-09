#include "ComponentsSample.h"


#include <stdio.h>

static int32_t  ComponentsSample_blockexpr_main_2(void);

static void  ComponentsSample_instances__init(void);

static inline void  ComponentsSample_instances_bserverComponent__wire(void);

static inline void  ComponentsSample_instances_clientComponent2__wire(void);

static inline void  ComponentsSample_instances_clientComponent__wire(void);

static inline void  ComponentsSample_instances_gserverComponent__wire(void);

static ComponentsSample_Server__idata_t ComponentsSample_bserverComponent_serverInterface__ops;

static ComponentsSample_Client__idata_t ComponentsSample_clientComponent2_clientInterface__ops;

static ComponentsSample_Client__idata_t ComponentsSample_clientComponent_clientInterface__ops;

static ComponentsSample_Server__idata_t ComponentsSample_gserverComponent_serverInterface__ops;

/* instance */
static ComponentsSample_BadServer__cdata_t ComponentsSample_instances_bserverComponent__instance;

/* instance */
static ComponentsSample_ClientComponent__cdata_t ComponentsSample_instances_clientComponent2__instance;

/* instance */
static ComponentsSample_ClientComponent__cdata_t ComponentsSample_instances_clientComponent__instance;

/* instance */
static ComponentsSample_GoodServer__cdata_t ComponentsSample_instances_gserverComponent__instance;

char*  ComponentsSample_BadServer_serverInterface_server_process(char *request, void *___id) 
{
  ComponentsSample_BadServer__cdata_t *___cid = ((ComponentsSample_BadServer__cdata_t*)(___id));
  printf("$$BServerStart: Bad server started. (");
  printf(") @ComponentsSample:BadServer_serverInterface_server_process?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757789149\n");
  
  int32_t x = 0;
  while (x >= 0)
  {
    x = x + 1;
  }
  printf("$$BServerEnd: Bad server ended. (");
  printf("result=%s",(((char*)(request))));
  printf(") @ComponentsSample:BadServer_serverInterface_server_process:1?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757789151\n");
  
  return request;
  
  
}

void  ComponentsSample_ClientComponent_clientInterface_client_process(void *___id) 
{
  ComponentsSample_ClientComponent__cdata_t *___cid = ((ComponentsSample_ClientComponent__cdata_t*)(___id));
  printf("$$ClientStart: Client started. (");
  printf(") @ComponentsSample:ClientComponent_clientInterface_client_process?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757768527\n");
  
  (*___cid->clientcomp_serverInterface__ops->server_process)("Hello",___cid->clientcomp_serverInterface__port);
  printf("$$ClientEnd: Client ended. (");
  printf(") @ComponentsSample:ClientComponent_clientInterface_client_process:1?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757787073\n");
  
  return ;
  
  
}

char*  ComponentsSample_GoodServer_serverInterface_server_process(char *request, void *___id) 
{
  ComponentsSample_GoodServer__cdata_t *___cid = ((ComponentsSample_GoodServer__cdata_t*)(___id));
  printf("$$GServerStart: Good server started. (");
  printf(") @ComponentsSample:GoodServer_serverInterface_server_process?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757787685\n");
  
  printf("$$GServerEnd: Good server ended. (");
  printf("result=%s",(((char*)(request))));
  printf(") @ComponentsSample:GoodServer_serverInterface_server_process:1?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757788164\n");
  
  return request;
  
  
}

/* - - */
int32_t  ComponentsSample_MainTest(void) 
{
  int32_t ___failuresVal = 0;
  int32_t *___failures = &___failuresVal;
  printf("$$runningTest: running test (");
  printf(") @ComponentsSample:MainTest?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757823876\n");
  
  ComponentsSample_instances__init();
  ComponentsSample_ClientComponent_clientInterface_client_process(&ComponentsSample_instances_clientComponent__instance);
  return ___failuresVal;
}

static int32_t  ComponentsSample_blockexpr_main_2(void) 
{
  int32_t ___failuresVal = 0;
  int32_t *___failures = &___failuresVal;
  *___failures = *___failures + ComponentsSample_MainTest();
  return ___failuresVal;
}

static void  ComponentsSample_instances__init(void) 
{
  void *___componentInstance = 0;
  
  ComponentsSample_instances_clientComponent__wire();
  ComponentsSample_instances_clientComponent2__wire();
  ComponentsSample_instances_gserverComponent__wire();
  ComponentsSample_instances_bserverComponent__wire();
  
  
  
  {
    ___componentInstance = &ComponentsSample_instances_clientComponent__instance;
    
  }
  {
    ___componentInstance = &ComponentsSample_instances_clientComponent2__instance;
    
  }
  {
    ___componentInstance = &ComponentsSample_instances_gserverComponent__instance;
    
  }
  {
    ___componentInstance = &ComponentsSample_instances_bserverComponent__instance;
    
  }
  
}

static inline void  ComponentsSample_instances_bserverComponent__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_bserverComponent_serverInterface__ops.server_process = &ComponentsSample_BadServer_serverInterface_server_process;
}

static inline void  ComponentsSample_instances_clientComponent2__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_clientComponent2_clientInterface__ops.client_process = &ComponentsSample_ClientComponent_clientInterface_client_process;
  /* 
   * connected :1 req cs port
   */

  ComponentsSample_instances_clientComponent2__instance.clientcomp_serverInterface__port = &ComponentsSample_instances_bserverComponent__instance;
  /* 
   * required port ops
   */

  ComponentsSample_instances_clientComponent2__instance.clientcomp_serverInterface__ops = &ComponentsSample_bserverComponent_serverInterface__ops;
}

static inline void  ComponentsSample_instances_clientComponent__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_clientComponent_clientInterface__ops.client_process = &ComponentsSample_ClientComponent_clientInterface_client_process;
  /* 
   * connected :1 req cs port
   */

  ComponentsSample_instances_clientComponent__instance.clientcomp_serverInterface__port = &ComponentsSample_instances_gserverComponent__instance;
  /* 
   * required port ops
   */

  ComponentsSample_instances_clientComponent__instance.clientcomp_serverInterface__ops = &ComponentsSample_gserverComponent_serverInterface__ops;
}

static inline void  ComponentsSample_instances_gserverComponent__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_gserverComponent_serverInterface__ops.server_process = &ComponentsSample_GoodServer_serverInterface_server_process;
}

int32_t  main(int32_t argc, char *(argv[])) 
{
  return ComponentsSample_blockexpr_main_2();
}

