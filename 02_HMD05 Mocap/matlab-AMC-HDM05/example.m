%an example for reading and playing MOCAP data
skel=acclaimReadSkel('./data/HDM_bd.asf');
[channels,skel ]=acclaimLoadChannels('./data/HDM_bd_01-01_01_120.amc',skel);
skelPlayData(skel,channels,1/120)