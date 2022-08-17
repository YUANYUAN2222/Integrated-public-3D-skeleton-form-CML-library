# Integrated-public-3D-skeleton-form-CML-library


## Introduction

The purpose of our study is to establish a 3D skelelton dataset for recognizing constrcution workers. Through collecting 16 relatively small-scale motion dataset, aligning a standardized skeleton scheme and removing irrelevant data, the developed CML datasets not only ensure all samples are relevant to construction actives and properly tagged, but also constructed a huge dataset that has all samples have the same skeleton system, similar frame length, and same data structure. 

However, We have carefully reviewed the licenses of all the current datasets. We found more than half of the datasets did not specify their licenses and usage policy. Therefore, in this version, we only shared the tagged and processed dataset that clearly allows redistribution and modification. For the rest of the datasets, we highlighted their URL and doi (all of them are publicly accessible and free for use). Instead of providing processed datasets, we provides full preprocess codes in this repository, which could be used to align different skeleton data from 16 public 3D skeleton datasets. 
The code could retag and process (such as converting to predefined .bvh files) these datasets and allow all readers and users to process the source dataset by themselves.

Public version： Construction Motion Data Library(CML) contains contains 137 types of activities and 6131 samples(ALL_DATA); among them, 53 types of activities and 4333 samples are highly related to construction activities ( Construction_Related_Data). 

Downlaod CML DOI: https://doi.org/10.6084/m9.figshare.20480787.v1. 



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
* According to different collection equipment, human motion can be captured through two streams of technologies, including RGB/RGBD-based video processing and IMU-based wearable sensing. Differences in the choice of technologies will result in differences in the final data stored format.<br/> 
* For example, the data format of RGB/RGBD-based dataset were stored in BVH or ASF/AMC, including NTU+RGBD 120, SBU Kinect Interaction Dataset, CAD 60 dataset. The data format of IMU-based dataset was stored in TXT or CSV, including CMU Motion Capture Dataset, HDM05 Mocap Database and Berkeley MHAD dataset<br/>

## General process of integrating data
(1)	Processing the number and position of joints<br/>
(2)	Processing the sampling rate<br/>
(3)	Processing the unit<br/>
(4)	Transformation coordinate system<br/>
(5)	Processing the file formats<br/>


### Skeletal Structure Alignment
#### 15 joints Skeleton structure           
Frame #, P(1),P(2),P(3),...,P(15)，<br/>
 P(i)=>(x,y,z) position of ith joint，values are in meters <br/>
Joint number -> Joint name <br/>
            'Head': 1,  <br/>
            'ShoulderCenter': 2, <br/>
            'Spine': 3, <br/>
            'LeftShoulder': 4, <br/>
            'LeftElbow': 5, <br/>
            'LeftHand': 6, <br/>
            'RightShoulder': 7, <br/>
            'RightElbow': 8, <br/>
            'RightHand': 9, <br/>
            'LeftHip': 10, <br/>
            'LeftKnee': 11, <br/>
            'LeftFoot': 12, <br/>
            'RightHip': 13, <br/>
            'RightKnee': 14, <br/>
            'RightFoot': 15, <br/>

#### 20 joints Skeleton structure   
Frame #, P(1),P(2),P(3),...,P(20)，<br/>
 P(i) =>(x,y,z) position of ith joint，values are in meters <br/>
Joint number -> Joint name <br/>
            'Head': 1,  <br/>
            'ShoulderCenter': 2, <br/>
            'Spine': 3, <br/>
            'LeftShoulder': 4, <br/>
            'LeftElbow': 5, <br/>
            'LeftHand': 6, <br/>
            'RightShoulder': 7, <br/>
            'RightElbow': 8, <br/>
            'RightHand': 9, <br/>
            'LeftHip': 10, <br/>
            'LeftKnee': 11, <br/>
            'LeftFoot': 12, <br/>
            'RightHip': 13, <br/>
            'RightKnee': 14, <br/>
            'RightFoot': 15, <br/>
            'HipCenter': 16, <br/>
            'LeftWrist': 17, <br/>
            'LeftAnkle': 18, <br/>
            'RightWrist': 19, <br/>
            'RightAnkle': 20, <br/>
# Environment
* Windows 10
* anaconda 
* python 3.7
* numpy
* MATLAB

## Data Records Advantages 
* Existing datasets usually store activity as a separate file. However, many files have different enclosures, resulting in many labeled files having more than one activity and only having a rough tag.
* The CML data format for storage is JSON for sharing 
* The JSON file can be divided into two parts. 
* The first “meta-data” part only stores the information related to the data summary, the original dataset source, and the joint structure 
* The second “formal-data” part only includes “tdata” (an object encloses frames of all joints over time) and “bdata” (an object includes time-series data of each joint). 
<img src="https://github.com/YUANYUAN2222/Integrated-public-3D-skeleton-form-CML-library/blob/main/Json_Structure.png" width="900" height="300" >

# Case study
## 00_In-lab experiment data
* The subjects wear Noitom Perception Neuron, a motion capturing system, while they were performing activities in both phases. The Perception Neuron system is able to wirelessly connect to a laptop computer and send data to the computer via Wi-Fi when both of them are connected to the same access point.

## Dataset Alignment
* Skeletal Structure Alignment ------Cut down joint number into 15/20-joint system
* All samples’ units will be converted into meters
* Resampling,  125hz----30hz
* Coordination Transformation
## Visualize in MATLAB

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

                                                                                     



