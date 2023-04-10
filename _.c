#include <iostream>
#include <complex>
#include <opencv2/opencv.hpp> // For image display

using namespace std;
using namespace cv;

int mandelbrot_recursive(complex<double> c, int max_iters, complex<double> z = 0, int iters = 0) {
    /*
     * Generate the Mandelbrot set for a given complex number c using recursion.
     */
    if (iters == max_iters) {
        return max_iters;
    } else if (abs(z) > 2) {
        return iters;
    } else {
        z = pow(z, 2) + c;
        iters++;
        return mandelbrot_recursive(c, max_iters, z, iters);
    }
}

void plot_mandelbrot_recursive(double xmin, double xmax, double ymin, double ymax, int width, int height, int max_iters) {
    /*
     * Plot the Mandelbrot set for a given range of x and y values using recursion.
     */
    Mat mandelbrot_set(height, width, CV_8UC1);
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            complex<double> c(xmin + j*(xmax-xmin)/width, ymin + i*(ymax-ymin)/height);
            mandelbrot_set.at<uchar>(i,j) = mandelbrot_recursive(c, max_iters);
        }
    }
    imshow("Mandelbrot Set (Recursive)", mandelbrot_set);
    waitKey(0);
}

int main() {
    // Example usage:
    plot_mandelbrot_recursive(-2, 2, -2, 2, 1000, 1000, 100);
    return 0;
}
