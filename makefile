all: build share
	@echo 'Done'

build:
	@echo 'Building source...'
	mkdir -p extern/build
	g++ -shared -fPIC -O2 -c extern/src/square.cpp -o extern/build/square.o

share: extern/build/square.o
	@echo 'Building library...'
	mkdir -p extern/lib
	g++ -shared extern/build/square.o -o extern/lib/library.so

clean:
	rm -fr extern/build/
	rm -fr extern/lib/
