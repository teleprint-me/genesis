#include <iostream>
#include <string>
#include <curl/curl.h>

size_t WriteCallback(char *contents, size_t size, size_t nmemb, std::string *response)
{
    size_t totalSize = size * nmemb;
    response->append(contents, totalSize);
    return totalSize;
}

int main()
{
    CURL *curl;
    CURLcode res;
    std::string response;

    curl_global_init(CURL_GLOBAL_DEFAULT);
    curl = curl_easy_init();

    if (curl)
    {
        // Set the URL to request
        curl_easy_setopt(curl, CURLOPT_URL, "https://api.example.com/endpoint");

        // Set the callback function for the response
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response);

        // Perform the request
        res = curl_easy_perform(curl);

        // Check for errors
        if (res != CURLE_OK)
        {
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(res));
        }

        // Cleanup
        curl_easy_cleanup(curl);
    }

    curl_global_cleanup();

    // Handle the response
    if (res == CURLE_OK)
    {
        // 'response' variable now contains the response data
        std::cout << "Response: " << response << std::endl;
    }

    return 0;
}
