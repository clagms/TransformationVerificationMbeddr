#ifndef COMPONENTSSAMPLE_H
#define COMPONENTSSAMPLE_H


#include <stdint.h>

#include <stddef.h>

#include <stdbool.h>



#ifdef __cplusplus
extern "C" {
#endif

typedef struct ComponentsSample_Server__idata ComponentsSample_Server__idata_t;
typedef struct ComponentsSample_Client__idata ComponentsSample_Client__idata_t;
typedef struct ComponentsSample_BadServer__cdata ComponentsSample_BadServer__cdata_t;
typedef struct ComponentsSample_ClientComponent__cdata ComponentsSample_ClientComponent__cdata_t;
typedef struct ComponentsSample_GoodServer__cdata ComponentsSample_GoodServer__cdata_t;
struct ComponentsSample_BadServer__cdata {
  uint8_t aMemberSoTheStructIsNotEmpty;
};

struct ComponentsSample_ClientComponent__cdata {
    /* required ports */
void *serverInterface__port;
    /* Req port ops */
ComponentsSample_Server__idata_t *serverInterface__ops;
};

struct ComponentsSample_Client__idata {
  void (*process)(void*);
};

struct ComponentsSample_GoodServer__cdata {
  uint8_t aMemberSoTheStructIsNotEmpty;
};

struct ComponentsSample_Server__idata {
  char* (*process)(char*,void*);
};

char*  ComponentsSample_BadServer_serverInterface_process(char *request, void *___id);

void  ComponentsSample_ClientComponent_clientInterface_process(void *___id);

char*  ComponentsSample_GoodServer_serverInterface_process(char *request, void *___id);

int32_t  ComponentsSample_MainTest(void);

int32_t  ComponentsSample_main(int32_t argc, char *(argv[]));


#ifdef __cplusplus
} /* extern "C" */
#endif

#endif
