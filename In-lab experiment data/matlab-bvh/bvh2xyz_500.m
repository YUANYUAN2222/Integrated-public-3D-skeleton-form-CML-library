% [skel, channels, frameLength] = bvhReadFile(fileName);
[skel, channels, frameLength] = bvhReadFile('./data/swagger.bvh');
% data = zeros(size(channels,1),27,3);
% for i = 1:size(channels,1)
data = zeros(500,27,3);
for i = 1:500
     t = channels(i,:);  %351*62 --> 1*62
     xyz = bvh2xyz(skel,t);
     data(i,:,:) = xyz;
end
save('data2.mat','data');