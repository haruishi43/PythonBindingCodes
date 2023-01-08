#include <iostream>

#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <pybind11/eigen.h>

#include <Eigen/Core>

#include <opencv2/opencv.hpp>
#include <opencv2/core/eigen.hpp>

using namespace std;

using Eigen::Dynamic;
using Eigen::RowMajor;
using Eigen::Unaligned;

array<Eigen::Matrix<uint8_t, Eigen::Dynamic, Eigen::Dynamic, Eigen::RowMajor>, 3>
process_single_channel_image(array<Eigen::Matrix<uint8_t, Dynamic, Dynamic, RowMajor>, 3> src_img) {
    // convert to cv::Mat
    cv::Mat rgb[3];
    cv::Mat cv_src_img(src_img[0].rows(), src_img[0].cols(), CV_8UC3);
    for (int i=0;i<src_img.size();i++)
    {
        cv::Mat channel(src_img[i].rows(), src_img[i].cols(), CV_8UC1, src_img[i].data());
        rgb[i] = channel;
    }
    cv::merge(rgb, 3, cv_src_img);
    cv::imshow("window_cpp_1", cv_src_img);
    cv::waitKey();


    // do something with the image!

    cv::Mat cv_dst_img;
    cv::rotate(cv_src_img, cv_dst_img, cv::ROTATE_90_CLOCKWISE);

    cv::imshow("window_cpp_1", cv_dst_img);
    cv::waitKey();
    

    // convert to Eigen::Matrix
    cv::Mat split_img[3];
    cv::split(cv_dst_img, split_img);

    array<Eigen::Matrix<uint8_t, Dynamic, Dynamic, RowMajor>, 3> dst_array;
    using channel_stride = Eigen::Stride<Dynamic, 1>;

    for (int i=0;i<dst_array.size();i++)
    {
        channel_stride stride(split_img[i].cols, 1);
        auto channel_matrix = Eigen::Map<Eigen::Matrix<uint8_t, Dynamic, Dynamic, RowMajor>, Unaligned, channel_stride>(
            reinterpret_cast<uint8_t*>(split_img[i].data), split_img[i].rows, split_img[i].cols, stride);
        dst_array[i] = channel_matrix;
    }
    return dst_array;
}

PYBIND11_MODULE(process_in_cpp, m) {
    m.def("process_single_channel_image", &process_single_channel_image);
}
