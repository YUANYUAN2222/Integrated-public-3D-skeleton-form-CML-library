%运行单个asf,和amc文件的程序

clc;clear;
skel=acclaimReadSkel('./data/HDM_bd.asf');
[channels,skel ]=acclaimLoadChannels('./data/HDM_bd_cartwheelLHandStart1Reps_001_120.amc',skel);
data = zeros(size(channels,1),31,3);
for i = 1:size(channels,1)
     t = channels(i,:);  %351*62 --> 1*62
     xyz = acclaim2xyz(skel,t);
     data(i,:,:) = xyz;
end
save('data1.mat','data');