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

## Introduction

### Construction Dataset structure
#### 15 joints Skeleton data structure           
Frame #, P(1),P(2),P(3),...,P(15)，<br/>
 P(i)=>(x,y,z) position of ith joint，values are in meters <br/>
Joint number -> Joint name <br/>
            'Head': 0,  <br/>
            'ShoulderCenter': 1, <br/>
            'Spine': 2, <br/>
            'LeftShoulder': 3, <br/>
            'LeftElbow': 4, <br/>
            'LeftHand': 5, <br/>
            'RightShoulder': 6, <br/>
            'RightElbow': 7, <br/>
            'RightHand': 8, <br/>
            'LeftHip': 9, <br/>
            'LeftKnee': 10, <br/>
            'LeftFoot': 11, <br/>
            'RightHip': 12, <br/>
            'RightKnee': 13, <br/>
            'RightFoot': 14, <br/>

#### 20 joints Skeleton data structure   
Frame #, P(1),P(2),P(3),...,P(20)，<br/>
 P(i) =>(x,y,z) position of ith joint，values are in meters <br/>
Joint number -> Joint name <br/>
            'Head': 0,  <br/>
            'ShoulderCenter': 1, <br/>
            'Spine': 2, <br/>
            'LeftShoulder': 3, <br/>
            'LeftElbow': 4, <br/>
            'LeftHand': 5, <br/>
            'RightShoulder': 6, <br/>
            'RightElbow': 7, <br/>
            'RightHand': 8, <br/>
            'LeftHip': 9, <br/>
            'LeftKnee': 10, <br/>
            'LeftFoot': 11, <br/>
            'RightHip': 12, <br/>
            'RightKnee': 13, <br/>
            'RightFoot': 14, <br/>
            'HipCenter': 15, <br/>
            'LeftWrist': 16, <br/>
            'LeftAnkle': 17, <br/>
            'RightWrist': 18, <br/>
            'RightAnkle': 19, <br/>
# Environment
* windows 10
* anaconda 
* python 3.7
* numpy
# Case study
## Advantages 
* Existing datasets usually store activity as a separate file. However, many files have different enclosures, resulting in many labeled files having more than one activity and only having a rough tag.
* Visualization json file for check format in Blender.


## (1) 00_In-lab experiment data
* The subjects wear Noitom Perception Neuron, a motion capturing system, while they were performing activities in both phases. The Perception Neuron system is able to wirelessly connect to a laptop computer and send data to the computer via Wi-Fi when both of them are connected to the same access point.
* 

<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/01_working%20oerheading.gif" width="450" height="380" >    <img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/02_Squatting.gif" width="450" height="380"> <br/>
* Left picture: {"original label": "01_working overheading", "target label": "hand catch", "action type": 2} <br/>
* Right picture:  {"original label": "02_Squatting", "target label": "squats", "action type": 2} <br/>


<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/03_second%20complex%20work.gif" width="450" height="380" > <img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/04_reaching.gif" width="450" height="380" > 
* Left picture: {"original label": "03_second complex work", "target label": "moving object", "action type": 3} <br/>
* Right picture:  {"original label": "04_reaching", "target label": "hand catch", "action type": 2} <br/>

<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/05_neck%20bending.gif" width="450" height="380" > <img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/06_kneeling.gif" width="450" height="380" > 
* Left picture: {"original label": "05_neck bending", "target label": "bending", "action type": 2} <br/>
* Right picture:  {"original label": "06_kneeling", "target label": "lay down", "action type": 4} <br/>

<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/07_climb%20work_1.gif" width="450" height="380" > <img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/08_climb%20work.gif" width="450" height="380" > 
* Left picture: {"original label": "07_climb work_1", "target label": "climb up", "action type": 1} <br/>
* Right picture:  {"original label": "08_climb work", "target label": "climb up", "action type": 1} <br/>

<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/09_bring%20somewhere%20to%20somewhere.gif" width="450" height="380" > <img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/00_In-lab%20experiment%20data/gif/10_back%20bending.gif" width="450" height="380" > 
* Left picture: {"original label": "09_bring somewhere to somewhere", "target label": "carrying", "action type": 2} <br/>
* Right picture:  {"original label": "10_back bending", "target label": "bending", "action type": 2} <br/>

                                                                                     



