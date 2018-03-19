#include <opencv2/core/core.hpp>  
#include <opencv2/highgui/highgui.hpp>  
#include "cv.h"  
#include "highgui.h"  
  
using namespace cv;  
using namespace std;  
  
  
int main(int argc, char** argv)  
{  
	string srcfilename,dstfilename;
	string srcname,dstname;
	srcfilename="C:/Users/olivier/Desktop/S8/PAR/Jeudedonnee/bar_chart_resize/";
	dstfilename="C:/Users/olivier/Desktop/S8/PAR/Jeudedonnee/bar_chart_contour/";

	for (int i = 1; i < 21 ; i++)  
	{
	std::stringstream ss;  
    ss << i;  
	srcname = srcfilename + ss.str()  + ".jpg";
	Mat srcImage = imread(srcname);  
    Mat temImage, dstImage;  
    temImage = srcImage;

	Canny(temImage, dstImage, 150, 100);  

	dstname = dstfilename + ss.str()  + ".jpg";

	imwrite(dstname,dstImage);
	}

    return 0;  
}  