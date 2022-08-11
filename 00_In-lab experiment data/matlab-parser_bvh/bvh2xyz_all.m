% [skel, channels, frameLength] = bvhReadFile(fileName);
[skel, channels, frameLength] = bvhReadFile('data/09_bring somewhere to somewhere.bvh');
data = zeros(size(channels,1),72,3);
for i = 1:size(channels,1)
% data = zeros(500,27,3);
% for i = 1:500
     t = channels(i,:);  %351*62 --> 1*62
     xyz = bvh2xyz(skel,t);
     data(i,:,:) = xyz;
end
save('09_bring somewhere to somewhere.mat','data');