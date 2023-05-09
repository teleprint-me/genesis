#pragma once

#include <string>
#include "../submodules/cpr/include/cpr/cpr.h"
#include "../submodules/json/single_include/nlohmann/json.hpp"

using json = nlohmann::json;

class OpenAI
{
public:
	OpenAI(const std::string &api_key);

	std::string generate_text(const std::string &prompt, int max_tokens = 50);

private:
	std::string api_key_;
};
