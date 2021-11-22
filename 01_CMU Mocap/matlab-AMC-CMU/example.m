%an example for reading and playing MOCAP data
skel=acclaimReadSkel('./data/01.asf');
[channels,skel ]=acclaimLoadChannels('./data/01_01.amc',skel);
skelPlayData(skel,channels,1/120)