clc; clear;
data_path = '../CMUallamcasf_data/';
save_path = './processed11/';
if exist(save_path,'dir') ==0
    mkdir(save_path); % Matlab使用dir函数获得指定文件夹下的所有子文件夹和文件,并存放在在一种为文件结构体数组中.
end
fdrs = dir(data_path);
for i=3:length(fdrs)
    fdr = fdrs(i).name;
    person_id = str2num(fdr);
    person_fdr = [data_path,fdr,'/'];
    person_skel_path = [person_fdr,fdr,'.asf'];
    save_person_fdr = [save_path,fdr,'/'];
    if exist(save_person_fdr,'dir')==0
        mkdir(save_person_fdr);
    end
    skel = acclaimReadSkel(person_skel_path);
    files = dir(person_fdr);
    for j=4:length(files)
        file_name = files(j).name
        file_path = [person_fdr,file_name];
        file_name_f = strsplit(file_name,'.');
        file_name_f = file_name_f{1}; %filename without appendix
        save_file_path = [save_person_fdr,file_name_f,'.mat'];
        [channels,skel ]=acclaimLoadChannels(file_path,skel);
        data = zeros(size(channels,1),31,3);
        for k = 1:size(channels,1)
            t = channels(k,:);  %351*62 --> 1*62
            xyz = acclaim2xyz(skel,t);
            data(k,:,:) = xyz;
        end
        save(save_file_path,'data'); 
    end  
end
% skel=acclaimReadSkel('./data/01.asf');
% [channels,skel ]=acclaimLoadChannels('./data/01_01.amc',skel);
% data = zeros(size(channels,1),31,3);
% for i = 1:size(channels,1)
%      t = channels(i,:);  %351*62 --> 1*62
%      xyz = acclaim2xyz(skel,t);
%      data(i,:,:) = xyz;
% end
% save('9.23data.mat','data');