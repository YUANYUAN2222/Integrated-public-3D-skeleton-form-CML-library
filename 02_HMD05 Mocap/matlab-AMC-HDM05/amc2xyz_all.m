% 处理所有文件的程序
clc; clear;
data_path = '../HDM05_cut_amc/';
save_path = './processed/';
if exist(save_path,'dir') ==0 % 和python一样，exist(),返回值ture or false 或者0/1
    mkdir(save_path); 
end                    %需要注意的是，dir()会返回两个.和..的文件夹
fdrs = dir(data_path); %Matlab使用dir函数获得指定文件夹下的所有子文件夹和文件,并存放在在一种为文件结构体数组中.
for i=3:length(fdrs) %matlab计数从1开始，python从0开始，所以第一个文件夹是.第二个文件夹是..
    act = fdrs(i).name; %提取name那一栏内容
%     person_id = str2num(fdr);
    act_fdr = [data_path,act,'/']; %拼接字符串
    save_act_fdr = [save_path,act,'/'];
    if exist(save_act_fdr,'dir')==0  
        mkdir(save_act_fdr);
    end
    files = dir(act_fdr);
    for j=3:length(files)
        filename_all = files(j).name; %提取文件夹的名字
        file_ap = strsplit(filename_all,'.');%把文件夹名字进行分割
        filename = file_ap{1};% 提取名字
        ap = file_ap{2};%提取后缀
        if ap=='asf'
            skel_path = [act_fdr,filename_all]
            skel = acclaimReadSkel(skel_path);
        end
        if ap=='amc'
            file_path = [act_fdr,filename_all]
            save_file_path = [save_act_fdr,filename,'.mat'];
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
end
