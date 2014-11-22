CC=gcc
CFLAGS=-std=c99
ODIR=./bin
_OBJ_ComponentsExec=ComponentsSample.o
OBJ_ComponentsExec=$(patsubst %,$(ODIR)/%,$(_OBJ_ComponentsExec))


all: removeStuffFromLibraries clean ComponentsExec 
.PHONY: removeStuffFromLibraries all clean
removeStuffFromLibraries: 
	
$(ODIR)/%.o: %.c
		mkdir -p $(ODIR) 
	$(CC) $(CFLAGS)   -c -o $@ $<  
$(ODIR)/%.o: %.cpp
		mkdir -p $(ODIR) 
	$(CC) $(CFLAGS)   -c -o $@ $<  
debug: CFLAGS +=-g
debug: clean ComponentsExec
ComponentsExec: $(OBJ_ComponentsExec)
	$(CC) $(CFLAGS) -o $@ $^   
test: ComponentsExec
	./ComponentsExec.exe
	 
clean: 
	rm -rf $(ODIR) 
