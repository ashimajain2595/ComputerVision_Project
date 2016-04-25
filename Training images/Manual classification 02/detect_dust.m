list = dir; %reads all files in the directory%
for i=3:size(list,1)-1
    if mod(i,2)~=0
        c0 = imread(list(i).name); %read c0 image%
        c1 = imread(list(i+1).name); %read c1 image%
        sub = abs(c1-c0); %subtract c0 and c1 images%
        gray = rgb2gray(sub); %convert into grayscale%
        bw=gray;
        bw(gray>150)=255; %thresholding the image%
        bw(gray<=150)=0;
        bw2 = bwareaopen(bw,250); %remove the smaller components connected by less than 250 pixels%
        se = strel('disk',2); %structuring element%
        bw3 = imopen(bw2,se); %open the image%
        subplot(1,3,1)
        imshow(c0)
        subplot(1,3,2)
        imshow(c1)
        subplot(1,3,3)
        imshow(bw3)
        name = list(i).name(1:end-6);
        name = strcat(name,'anno.bmp');
        imwrite(bw3,name); %saving the image with fault area highlighted%
    end
end
b1 = gray;
b1(gray<=10)=255;
b1(gray>10) = 0;
add = c1+c0;
g = rgb2gray(add);
b2=g;
b2(g<150)=0;
b2(g>=150)=255;
x = xor(b1,b2);
x1 = bwareaopen(x,250);
x2 = imopen(x1,se);