
% Author: Morag Brown
% These sections plot the various waveforms, spectra, and spectrograms
% used in Chapter 4 of my final year report

%%
%Sustain waveform, frequency spectrum, spectrogram 
file = 'D6.wav';
[y, Fs] = audioread(file);      % y is sound data, Fs is sample frequency.
t = (1:length(y))/Fs;           % time
L = length(y);

figure; 

% %Waveform
% i = find(t>0.0 & t<0.005);   % set time duration for waveform plot
% subplot(3,1,1)
% plot(t(i),y(i))  
% axis tight         
% title(['Waveform of ' file])
% xlabel('Time (s)')
% ylabel('Sample Value Ratio')

%Frequency spectrum
N = 2^17;                     % number of points to analyze
c = abs(fft(y(1:N))/N);       % compute fft of sound data
f = (1:N)*Fs/N;           % frequency corresponding to c

subplot(1,1,1)
plot(f,c)
axis([0 4000 0.00001 0.008])                
title(['Frequency Spectrum of ' file])
xlabel('Frequency (Hz)')
ylabel('Magnitude')

% %Spectrogram with Hann windowing
% subplot(3,1,3)
% spectrogram(y, hann(4000), [], 0:9000, Fs, 'yaxis');
% title(['Spectrogram of ' file])

%%
%Sustain, staccato and detached waveform, frequency spectrum and
%spectrogram
file = 'C8.wav';                %sustain
file1 = 'C8 - Staccato.wav' ;   %staccato
file2 = 'C8 - Detached.wav';    %detached
[y, Fs] = audioread(file);      % y is sound data, Fs is sample frequency.
[z, Fs1] = audioread(file1);    %staccato 
[x, Fs2] = audioread(file2);    %detached 
t = (1:length(y))/Fs;           % time of sustain recording   
t1 = (1:length(z))/Fs;
t2 = (1:length(x))/Fs;
figure; 
%================================Sustain===================================
%Waveform
i = find(t>0.00 & t<25);  % set time duration for waveform plot
subplot(3,1,1)
plot(t,y)  
axis tight         
title(['Waveform of ' file])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

% %Spectrogram with Hann windowing
% subplot(2,3,4)
% spectrogram(y, hann(4000), [], 0:5000, Fs, 'yaxis');
% title(['Spectrogram of ' file])
%================================Staccato==================================
i = find(t>0.00 & t<2);  % set time duration for waveform plot
subplot(3,1,2)
plot(t1,z)  
axis tight         
title(['Waveform of ' file1])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

% %Spectrogram with Hann windowing
% subplot(2,3,5)
% spectrogram(z, hann(4000), [], 0:5000, Fs1, 'yaxis');
% title(['Spectrogram of ' file1])
%================================Detached==================================
i = find(t>0.00 & t<5);  % set time duration for waveform plot
subplot(3,1,3)
plot(t2,x)  
axis tight         
title(['Waveform of ' file2])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

% %Spectrogram with Hann windowing
% subplot(2,3,6)
% spectrogram(x, hann(4000), [], 0:5000, Fs2, 'yaxis');
% title(['Spectrogram of ' file2])

%==========================================================================






%%
%Transients of one of the nine base notes and a semitone above and below
file = 'C8.wav';                %sustain
file1 = 'B7.wav' ;   %semitone below
file2 = 'G#1.wav';    %semitone above
[y, Fs] = audioread(file);      % y is sound data, Fs is sample frequency.
[z, ~] = audioread(file1);    %below
[x, ~] = audioread(file2);    %above
t = (1:length(y))/Fs;           % time of sustain recording              

figure; 
%=================================Below====================================
%Waveform
i1 = find(t>0.0 & t<0.0025);  % set time duration for waveform plot
subplot(2,1,1)
plot(t(i1),z(i1))  
axis tight         
title(['Steady-state of ' file1 ' (1 semitone below ' file ' )'])
xlabel('Time (s)')
ylabel('Sample Value Ratio')
%================================Sustain===================================
i = find(t>0.0002 & t<0.0027);  % set time duration for waveform plot
subplot(2,1,2)
plot(t(i),y(i))  
axis tight         
title(['Steady-state of ' file])
xlabel('Time (s)')
ylabel('Sample Value Ratio')
%=================================Above====================================
% i2 = find(t>0.00 & t<0.04);  % set time duration for waveform plot
% subplot(3,1,3)
% plot(t(i2),x(i2))  
% axis tight         
% title(['Steady-state of ' file2 ' (1 semitone above ' file ' )'])
% xlabel('Time (s)')
% ylabel('Sample Value Ratio')

%==========================================================================






%%
%Plots of the octaves and their individual notes (w,f,s)
file = 'A0+A1.wav';                %octave
file1 = 'A0 & A1 mix.wav' ;             %note 1
file2 = 'A4.wav';              %note 2
[y, Fs] = audioread(file);      % y is sound data, Fs is sample frequency.
[z, Fs1] = audioread(file1);    %note 1
[x, Fs2] = audioread(file2);    %note 2
t = (1:length(y))/Fs;           % time of sustain recording              

figure;
%===============================Octave=====================================
%Waveform
i = find(t>0.0 & t<0.06);   % set time duration for waveform plot
subplot(2,3,1)
plot(t(i),y(i))  
axis tight         
title(['Waveform of ' file])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

%Spectrum
N = 2^17;                     % number of points to analyze
c = abs(fft(y(1:N))/N);       % compute fft of sound data
f = (1:N)*Fs/N;           % frequency corresponding to c

subplot(2,3,4)
plot(f,c)
axis([0 2000 0.00001 0.024])                
title(['Frequency Spectrum of ' file])
xlabel('Frequency (Hz)')
ylabel('Magnitude')
%===============================Note 1=====================================
%Waveform
i = find(t>0.00 & t<0.06);   % set time duration for waveform plot
subplot(2,3,2)
plot(t(i),z(i))  
axis tight         
title(['Waveform of ' file1])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

%Spectrum 
N = 2^17;                     % number of points to analyze
c1 = abs(fft(z(1:N))/N);       % compute fft of sound data
f1 = (1:N)*Fs/N;           % frequency corresponding to c

subplot(2,3,5)
plot(f1,c1)
axis([0 2000 0.00001 0.024])                
title(['Frequency Spectrum of ' file1])
xlabel('Frequency (Hz)')
ylabel('Magnitude')
%===============================Note 2=====================================
%Waveform
i = find(t>0.0 & t<0.03);   % set time duration for waveform plot
subplot(2,3,3)
plot(t(i),x(i))  
axis tight         
title(['Waveform of ' file2])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

%Spectrum
N = 2^17;                     % number of points to analyze
c2 = abs(fft(x(1:N))/N);       % compute fft of sound data
f2 = (1:N)*Fs/N;           % frequency corresponding to c

subplot(2,3,6)
plot(f2,c2)
axis([0 2000 0.00001 0.014])                
title(['Frequency Spectrum of ' file2])
xlabel('Frequency (Hz)')
ylabel('Magnitude')

%% coincidence of partials
file = 'C3.wav';                %C4
file1 = 'C#3.wav' ;        %interval
[y, Fs] = audioread(file);      % y is sound data, Fs is sample frequency.
[z, Fs1] = audioread(file1);    %note 1
t = (1:length(y))/Fs;           % time of sustain recording              

figure;
%===============================C4=====================================
%Spectrum
N = 2^17;                     % number of points to analyze
c = abs(fft(y(1:N))/N);       % compute fft of sound data
f = (1:N)*Fs/N;           % frequency corresponding to c

subplot(2,1,1)
plot(f,c)
axis([0 2000 0.00001 0.03])                
title(['Frequency Spectrum of ' file])
xlabel('Frequency (Hz)')
ylabel('Magnitude')

%==============================interval====================================
%Spectrum
N = 2^17;                     % number of points to analyze
c = abs(fft(z(1:N))/N);       % compute fft of sound data
f = (1:N)*Fs/N;           % frequency corresponding to c

subplot(2,1,2)
plot(f,c)
axis([0 2000 0.00001 0.04])                
title(['Frequency Spectrum of ' file1])
xlabel('Frequency (Hz)')
ylabel('Magnitude')

%% Reconstruction
file = 'D6.wav';                %C4
file1 = 'D6 reconstruction.wav' ;        %interval
[y, Fs] = audioread(file);      % y is sound data, Fs is sample frequency.
[z, Fs1] = audioread(file1);    %note 1
t = (1:length(z))/Fs;           % time of sustain recording              

figure;
%Waveform
i = find(t>0.0 & t<1);   % set time duration for waveform plot
subplot(2,2,1)
plot(t(i),y(i))  
axis tight         
title(['Waveform of ' file])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

%Waveform
i = find(t>0.0 & t<1);   % set time duration for waveform plot
subplot(2,2,2)
plot(t(i),z(i))  
axis tight         
title(['Waveform of ' file1])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

i = find(t>0.3 & t<0.305);   % set time duration for waveform plot
subplot(2,2,3)
plot(t(i),y(i))  
axis tight         
title(['Waveform of ' file])
xlabel('Time (s)')
ylabel('Sample Value Ratio')

%Waveform
i = find(t>0.3 & t<0.305);   % set time duration for waveform plot
subplot(2,2,4)
plot(t(i),z(i))  
axis tight         
title(['Waveform of ' file1])
xlabel('Time (s)')
ylabel('Sample Value Ratio')