# Integrated-public-3D-skeleton-form-CML-library
Custom code in the generation of datasets
## Obtain reliable raw skeleton
To obtain reliable raw skeleton data, we manually selected and download available 3D skeleton sources form the official website of the institutions.<br/>
CMU Mocap dataset http://mocap.cs.cmu.edu<br/>
HMD05 Mocap dataset http://resources.mpi-inf.mpg.de/HDM05/<br/>
Berkeley MHAD https://tele-immersion.citris-uc.org/berkeley_mhad<br/>
NTU+RGBD 120 http://rose1.ntu.edu.sg/Datasets/actionRecognition.asp<br/>
SBU Kinect Interaction Dataset https://www3.cs.stonybrook.edu/~kyun/research/kinect_interaction/index.html<br/>
MSR Action3D Dataset https://sites.google.com/view/wanqingli/data-sets/msr-action3d<br/>
CAD60 Dataset http://pr.cs.cornell.edu/humanactivities/data.<br/>
UTKinect-Action3D Dataset http://cvrc.ece.utexas.edu/KinectDatasets/HOJ3D.html<br/>
UCF Dataset http://www.syedzainmasood.com/research.html<br/>
Microsoft Research Cambridge-12 https://www.microsoft.com/en-us/download/details.aspx?id=52283<br/>
Human 3.6 http://vision.imar.ro/human3.6m/description.php<br/>
PKU_MMD https://www.icst.pku.edu.cn/struct/Projects/PKUMMD.html?aimglfkfkfcjmopp<br/>
SYSU 3D https://www.iseeai.cn/~hujianfang/ProjectJOULE.html<br/>
UTD Multimodal Human Action Dataset(UTD MHAD1) https://personal.utdallas.edu/~kehtar/UTD-MHAD.html<br/>
UTD MHAD2 https://personal.utdallas.edu/~kehtar/UTD-MHAD.html<br/>
UTD MHAD3 https://personal.utdallas.edu/~kehtar/UTD-MHAD.html<br/>

## Equipment differences.
According to different collection equipment, human motion can be captured through two streams of technologies, including RGB/RGBD-based video processing and IMU-based wearable sensing. Differences in the choice of technologies will result in differences in the final data stored format.<br/> 
For example, the data format of RGB/RGBD-based dataset were stored in BVH or ASF/AMC, including NTU+RGBD 120, SBU Kinect Interaction Dataset, CAD 60 dataset. The data format of IMU-based dataset was stored in TXT or CSV, including CMU Motion Capture Dataset, HDM05 Mocap Database and Berkeley MHAD dataset<br/>

## General process of integrating data
(1)	Processing the number and position of joints<br/>
(2)	Processing the sampling rate<br/>
(3)	Processing the unit<br/>
(4)	Transformation coordinate system<br/>
(5)	Processing the file formats<br/>
## Case study
### (1) 00_In-lab experiment data
* The subjects wear Noitom Perception Neuron, a motion capturing system, while they were performing activities in both phases. The Perception Neuron system is able to wirelessly connect to a laptop computer and send data to the computer via Wi-Fi when both of them are connected to the same access point. Fig. 6 shows the Perception Neuron system we used to acquire data in the experiment.
* The predefined awkward postures in this experiment include working overhead (WO), kneeling (KN), back bending forward (BB), squatting (SQ), neck bending (NB) and reaching (RE). 


<img  src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/01_working%20oerheading.gif" width="800" height="615" >
<div align=center> Skeleton data visualized in Matlab
                                                                                                                                                      
<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/07ber.png" width="800" height="615" ><br/>
<div align=



### (1)IMU-based dataset------Berkeley_MHAD 

* Processing the number and position of joints<br/>
30joint -----15/20joint, Adjust the order of nodes and supplement missing data.<br/>
15nodes = [7,5,3,16,18,20,9,11,22,29,31,33,22,24,26]<br/>
20nodes= [7,5,3,16,18,20,9,11,22,29,31,33,22,24,26,1 missing wrist and ankle]<br/>
The missing joint data could be computed with neighbor joint interpolation. The nonlinear interpolation utilized the Multi-Layer Perceptron (MLP) model of the scikit-learn package.<br/>
* 480 frames per second (fps)-----30fps
* Millimeter-----meter
* Adopt Coordination transformation

<img  src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/%E5%9B%BE%E7%89%874.png" width="800" height="615" >
<div align=center> Skeleton data visualized in Matlab
                                                                                                                                                      
<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/07ber.png" width="800" height="615" ><br/>
<div align=center>Skeleton data visualized in Origin
</center>

### (2)RGB/RGBD-based video -----SUSY 3D dataset
* Processing the number and position of joints<br/>
20nodes = [4，3，2，9，10，12，5，6，8，13，14，16，17，18，20，1，11，15，7，19]<br/>
15nodes = [4，3，2，9，10，12，5，6，8，17，18，20，13，14，16]<br/>

* Adopt Coordination transformation

<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/06.png" width="800" height="615" ><br/>
<div align=center> Skeleton data visualized in Origin

