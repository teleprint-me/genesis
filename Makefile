CXX = g++
CXXFLAGS = -I./imgui -Wall -Wextra -std=c++11
LDFLAGS = -lglfw -lGLEW -lGL

TARGET = main
SOURCES = main.cpp ./imgui/imgui.cpp ./imgui/imgui_draw.cpp ./imgui/imgui_tables.cpp ./imgui/imgui_widgets.cpp ./imgui/backends/imgui_impl_glfw.cpp ./imgui/backends/imgui_impl_opengl3.cpp

all: $(TARGET)

$(TARGET): $(SOURCES)
	$(CXX) $(CXXFLAGS) -o $@ $^ $(LDFLAGS)

deps:
	./make.sh
	git clone https://github.com/ocornut/imgui.git imgui
	git clone --recursive https://github.com/whoshuu/cpr.git
	git clone git@github.com:teleprint-me/llama.cpp.git

clean:
	rm -f $(TARGET)

.PHONY: all deps clean
