CXX = g++

CXXFLAGS = -I./imgui -I./submodules/imgui \
	-I./submodules/imgui/backends \
	-I./submodules/cpr/include/cpr \
	-Wall -Wextra -std=c++11

LDFLAGS = -L$(CURDIR)/submodules/cpr/build/lib \
	-Wl,-rpath=$(CURDIR)/submodules/cpr/build/lib \
	-lglfw -lGLEW -lGL -lcpr

TARGET = genesis

SOURCES = src/genesis.cpp \
	./submodules/imgui/imgui.cpp \
	./submodules/imgui/imgui_draw.cpp \
	./submodules/imgui/imgui_tables.cpp \
	./submodules/imgui/imgui_widgets.cpp \
	./submodules/imgui/backends/imgui_impl_glfw.cpp \
	./submodules/imgui/backends/imgui_impl_opengl3.cpp

OBJECTS = $(SOURCES:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS) submodules/cpr/build/lib/libcpr.so
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

packages:
	./scripts/shell/install/dependencies.sh

clones:
	git submodule add https://github.com/ocornut/imgui.git submodules/imgui
	git submodule add https://github.com/whoshuu/cpr.git submodules/cpr
	git submodule add https://github.com/ggerganov/ggml.git submodules/ggml
	git submodule add https://github.com/ggerganov/llama.cpp.git submodules/llama.cpp
	git submodule init
	git submodule update

modules:
	git submodule update --init

submodules/cpr/build/lib/libcpr.so: submodules/cpr
	cd submodules/cpr && mkdir -p build && cd build && cmake .. && make

clean:
	rm -f $(TARGET) $(OBJECTS)

.PHONY: all packages clones clean modules
