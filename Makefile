CXX = g++
CXXFLAGS = -I./imgui -I./submodules/imgui -I./submodules/imgui/backends -I./submodules/cpr/include -Wall -Wextra -std=c++11
LDFLAGS = -lglfw -lGLEW -lGL

TARGET = main
SOURCES = main.cpp \
	./submodules/imgui/imgui.cpp \
	./submodules/imgui/imgui_draw.cpp \
	./submodules/imgui/imgui_tables.cpp \
	./submodules/imgui/imgui_widgets.cpp \
	./submodules/imgui/backends/imgui_impl_glfw.cpp \
	./submodules/imgui/backends/imgui_impl_opengl3.cpp

OBJECTS = $(SOURCES:.cpp=.o)

all: $(TARGET)

$(TARGET): $(OBJECTS)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS) -L./submodules/cpr/build -lcpr

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

packages:
	./scripts/shell/install/dependencies.sh

clones:
	git clone https://github.com/ocornut/imgui.git submodules/imgui
	git clone --recursive https://github.com/whoshuu/cpr.git submodules/cpr
	git clone https://github.com/ggerganov/ggml.git submodules/ggml
	git clone https://github.com/ggerganov/llama.cpp.git submodules/llama.cpp

clean:
	rm -f $(TARGET) $(OBJECTS)

.PHONY: all packages clones clean
