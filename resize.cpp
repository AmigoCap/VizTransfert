#include <opencv2/opencv.hpp>  
#include <opencv2/imgproc/imgproc.hpp>  
using namespace cv;  
  
int main()  
{  
	string srcfilename,dstfilename;
	string srcname,dstname;
	srcfilename="C:/Users/olivier/Desktop/S8/PAR/Github/google_pictures/line+chart/";
	dstfilename="C:/Users/olivier/Desktop/S8/PAR/Jeudedonnee/line+chart_resize/";

	//resize 
	for (int i = 12; i < 14 ; i++)  
	{
	std::stringstream ss;  
    ss << i;  
	srcname = srcfilename + "line+chart_"+ ss.str() + ".png";
    Mat srcImage = imread(srcname);  
    Mat temImage, dstImage;  
    temImage = srcImage;  

    resize(temImage, dstImage, Size(255, 255), 0, 0, CV_INTER_NN);  

	dstname = dstfilename + ss.str() + ".png";

	imwrite(dstname,dstImage);
	}

	//findcontour

	return 0;  
}  