import thinkdsp as dsp
import thinkplot as plt
from soundfile import read, SoundFile
from numpy import reshape
from winsound import PlaySound, SND_ASYNC


archivo = input("Nombre del archivo .wav a convertir a karaoke\n     >")
archivo = archivo + '.wav'

data, Fs = read(archivo)

izq = data[:, 0]
der = data[:, 1]

karaoke = der - izq

largo = len(karaoke)

print("Cantidad de muestras: ", largo)

permiso = input("Continuar?\n   Si (0) No (1)\n     >")

if permiso == '0':
    karaoke = reshape(karaoke, (largo, 1 - largo))

    rola_karaoke = SoundFile(archivo)

    with SoundFile(archivo, 'w', Fs, 1, 'PCM_24') as f:
        f.write(karaoke)

    PlaySound(archivo, SND_ASYNC)

    grafica = input("Graficar?\n   Si (0) No (1)\n      >")

    if grafica == '0':
        data = dsp.read_wave(archivo)
        data.plot()
        plt.show()

        data_espectro = data.make_spectrum()
        data_espectro.plot()
        plt.show()
    else:
        pass

else:
    pass

