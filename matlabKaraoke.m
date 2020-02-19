fs = 44100;
[rola, fs] = audioread('morteza.mp3', [1 10*fs]);
izq = rola(:,1);
der = rola(:,2);
karaoke = der - izq;
sound(karaoke, fs)