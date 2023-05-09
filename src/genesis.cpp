#include <stdio.h>
#include <cstdlib>
#include <iostream>
#include <GL/glew.h>
#include <GLFW/glfw3.h>
#include "../submodules/imgui/imgui.h"
#include "../submodules/imgui/backends/imgui_impl_glfw.h"
#include "../submodules/imgui/backends/imgui_impl_opengl3.h"
#include "openai.h"

int main(void)
{
    if (!glfwInit())
    {
        fprintf(stderr, "Failed to initialize GLFW\n");
        return -1;
    }

    GLFWwindow *window = glfwCreateWindow(1280, 720, "ImGui GLFW OpenGL3 example", NULL, NULL);

    if (window == NULL)
    {
        fprintf(stderr, "Failed to create a GLFW window\n");
        glfwTerminate();
        return -1;
    }
    
	glfwMakeContextCurrent(window);
    glfwSwapInterval(0); // Enable vsync

    if (glewInit() != GLEW_OK)
    {
        fprintf(stderr, "Failed to initialize GLEW\n");
        glfwTerminate();
        return -1;
    }

    IMGUI_CHECKVERSION();
    ImGui::CreateContext();
    ImGuiIO &io = ImGui::GetIO();
    ImGui::StyleColorsDark();

    ImGui_ImplGlfw_InitForOpenGL(window, true);
    ImGui_ImplOpenGL3_Init("#version 130");

	// Read the API key from the environment variable
	const char *api_key = std::getenv("OPENAI_API_KEY");

	if (!api_key)
	{
		std::cerr << "Error: OPENAI_API_KEY environment variable is not set." << std::endl;
		return 1;
	}

	OpenAI openai(api_key);

	std::string prompt = "Once upon a time";
	std::string generated_text = openai.generate_text(prompt);
	std::cout << "Generated text: " << generated_text << std::endl;

	while (!glfwWindowShouldClose(window))
	{
		glfwPollEvents();

		ImGui_ImplOpenGL3_NewFrame();
		ImGui_ImplGlfw_NewFrame();
		ImGui::NewFrame();

		ImGui::Begin("Hello, ImGui!");

		// Test OpenAI completion
		ImGui::Text("Prompt: %s", prompt.c_str());
		ImGui::Text("Completion: %s", generated_text.c_str());

		ImGui::End();

		ImGui::Render();
        int display_w, display_h;
        glfwGetFramebufferSize(window, &display_w, &display_h);
        glViewport(0, 0, display_w, display_h);
        glClearColor(0.1f, 0.1f, 0.1f, 1.00f);
        glClear(GL_COLOR_BUFFER_BIT);
        ImGui_ImplOpenGL3_RenderDrawData(ImGui::GetDrawData());
        glfwSwapBuffers(window);
	}

	ImGui_ImplOpenGL3_Shutdown();
    ImGui_ImplGlfw_Shutdown();
    ImGui::DestroyContext();

    glfwDestroyWindow(window);
    glfwTerminate();
    return 0;
}
