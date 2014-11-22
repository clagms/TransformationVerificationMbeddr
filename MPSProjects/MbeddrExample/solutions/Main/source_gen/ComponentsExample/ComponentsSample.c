#include "ComponentsSample.h"


#include <stdio.h>

static int32_t  ComponentsSample_blockexpr_main_2(void);

static void  ComponentsSample_instances__init(void);

static inline void  ComponentsSample_instances_bserver__wire(void);

static inline void  ComponentsSample_instances_client__wire(void);

static inline void  ComponentsSample_instances_gserver__wire(void);

static ComponentsSample_Server__idata_t ComponentsSample_bserver_server__ops;

static ComponentsSample_Client__idata_t ComponentsSample_client_client__ops;

static ComponentsSample_Server__idata_t ComponentsSample_gserver_server__ops;

/* instance */
static ComponentsSample_BadServer__cdata_t ComponentsSample_instances_bserver__instance;

/* instance */
static ComponentsSample_ClientComponent__cdata_t ComponentsSample_instances_client__instance;

/* instance */
static ComponentsSample_GoodServer__cdata_t ComponentsSample_instances_gserver__instance;

char*  ComponentsSample_BadServer_server_process(char *request, void *___id) 
{
  ComponentsSample_BadServer__cdata_t *___cid = ((ComponentsSample_BadServer__cdata_t*)(___id));
  printf("$$BServerStart: Bad server started. (");
  printf(") @ComponentsSample:BadServer_server_process?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757789149\n");
  
  int32_t x = 0;
  while (x >= 0)
  {
    x = x + 1;
  }
  printf("$$BServerEnd: Bad server ended. (");
  printf("result=%s",(((char*)(request))));
  printf(") @ComponentsSample:BadServer_server_process:1?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757789151\n");
  
  return request;
  
  
}

void  ComponentsSample_ClientComponent_client_process(void *___id) 
{
  ComponentsSample_ClientComponent__cdata_t *___cid = ((ComponentsSample_ClientComponent__cdata_t*)(___id));
  printf("$$ClientStart: Client started. (");
  printf(") @ComponentsSample:ClientComponent_client_process?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757768527\n");
  
  (*___cid->server__ops->process)("Hello",___cid->server__port);
  printf("$$ClientEnd: Client ended. (");
  printf(") @ComponentsSample:ClientComponent_client_process:1?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757787073\n");
  
  return ;
  
  
}

char*  ComponentsSample_GoodServer_server_process(char *request, void *___id) 
{
  ComponentsSample_GoodServer__cdata_t *___cid = ((ComponentsSample_GoodServer__cdata_t*)(___id));
  printf("$$GServerStart: Good server started. (");
  printf(") @ComponentsSample:GoodServer_server_process?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757787685\n");
  
  printf("$$GServerEnd: Good server ended. (");
  printf("result=%s",(((char*)(request))));
  printf(") @ComponentsSample:GoodServer_server_process:1?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757788164\n");
  
  return request;
  
  
}

/* - - */
int32_t  ComponentsSample_Main(void) 
{
  int32_t ___failuresVal = 0;
  int32_t *___failures = &___failuresVal;
  printf("$$runningTest: running test (");
  printf(") @ComponentsSample:Main?r:05b27177-f968-4f4b-b363-323f6b133f5f(ComponentsExample)#3749681781757823876\n");
  
  ComponentsSample_instances__init();
  ComponentsSample_ClientComponent_client_process(&ComponentsSample_instances_client__instance);
  return ___failuresVal;
}

static int32_t  ComponentsSample_blockexpr_main_2(void) 
{
  int32_t ___failuresVal = 0;
  int32_t *___failures = &___failuresVal;
  *___failures = *___failures + ComponentsSample_Main();
  return ___failuresVal;
}

static void  ComponentsSample_instances__init(void) 
{
  void *___componentInstance = 0;
  
  ComponentsSample_instances_client__wire();
  ComponentsSample_instances_gserver__wire();
  ComponentsSample_instances_bserver__wire();
  
  
  
  {
    ___componentInstance = &ComponentsSample_instances_client__instance;
    
  }
  {
    ___componentInstance = &ComponentsSample_instances_gserver__instance;
    
  }
  {
    ___componentInstance = &ComponentsSample_instances_bserver__instance;
    
  }
  
}

static inline void  ComponentsSample_instances_bserver__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_bserver_server__ops.process = &ComponentsSample_BadServer_server_process;
}

static inline void  ComponentsSample_instances_client__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_client_client__ops.process = &ComponentsSample_ClientComponent_client_process;
  /* 
   * connected :1 req cs port
   */

  ComponentsSample_instances_client__instance.server__port = &ComponentsSample_instances_gserver__instance;
  /* 
   * required port ops
   */

  ComponentsSample_instances_client__instance.server__ops = &ComponentsSample_gserver_server__ops;
}

static inline void  ComponentsSample_instances_gserver__wire(void) 
{
  /* 
   * COMPONENT
   */

  /* 
   * prov port
   */

  ComponentsSample_gserver_server__ops.process = &ComponentsSample_GoodServer_server_process;
}

int32_t  main(int32_t argc, char *(argv[])) 
{
  return ComponentsSample_blockexpr_main_2();
}

