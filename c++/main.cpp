#include <iostream>
#include <opencv2/opencv.hpp>

int main(int argc, char* argv[]) {
    if (argc != 5) {
        return 1;
    }

    std::string input_dir = argv[1];
    std::string output_dir = argv[2];
    int width = std::stoi(argv[3]);
    int height = std::stoi(argv[4]);

    cv::Mat img;
    for (const auto& entry : std::filesystem::directory_iterator(input_dir)) {
        std::string file = entry.path().string();
        img = cv::imread(file);

        if (img.empty()) {
            std::cerr << "Failed to open image: " << file << std::endl;
            continue;
        }

        cv::resize(img, img, cv::Size(width, height), 0, 0, cv::INTER_LINEAR);

        std::string output_path = output_dir + "/" + entry.path().filename().string();
        cv::imwrite(output_path, img);

        cv::imshow("Resized Image", img);
        cv::waitKey(0);
    }

    return 0;
}
