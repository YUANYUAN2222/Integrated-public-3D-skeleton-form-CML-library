% [skel, channels, frameLength] = bvhReadFile(fileName);
clc;clear;
data_path = '../skeletondata/SkeletalData/';
save_root = './processed'
if exist(save_root,'dir')==0
    mkdir(save_root);
end
files = dir(data_path);%返回所有文件夹和文件
for i=3:length(files)
    disp(i);
    file_name = files(i).name;
    sp = strsplit(file_name,'_');
    if size(sp,2)~=4
        continue
    end
    act = sp{3};
    sp = strsplit(file_name,'.');
    file_name_f = sp{1};
    save_path = [save_root,'/',act];
    if exist(save_path,'dir')==0
        mkdir(save_path);
    end
    save_file_path = [save_path,'/',file_name_f,'.mat'];
    [skel, channels, frameLength] = bvhReadFile(file_name);
    data = zeros(size(channels,1),35,3);
    for j=1:size(channels,1)
        t = channels(j,:);
        xyz = bvh2xyz(skel,t);
        data(j,:,:) = xyz;
    end
    save(save_file_path,'data');
end
