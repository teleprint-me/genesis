#include <iostream>
#include <string>
#include "../submodules/cpr/include/cpr/cpr.h"
#include "../submodules/json/single_include/nlohmann/json.hpp"
#include "openai.h"

using json = nlohmann::json;

OpenAI::OpenAI(const std::string &api_key) : api_key_(api_key) {}

std::string OpenAI::generate_text(const std::string &prompt, int max_tokens)
{
	const std::string url = "https://api.openai.com/v1/completions";

	auto response = cpr::Post(
		cpr::Url{url},
		cpr::Header{
			{"Authorization", "Bearer " + api_key_},
			{"Content-Type", "application/json"}},
		cpr::Body{json{{"model", "text-davinci-003"}, {"prompt", prompt}, {"max_tokens", max_tokens}}.dump()});

	if (response.status_code == 200)
	{
		json result = json::parse(response.text);
		return result["choices"][0]["text"].get<std::string>();
	}
	else
	{
		std::cerr << "Error: " << response.status_code << " - " << response.text << std::endl;
		return "";
	}
}
