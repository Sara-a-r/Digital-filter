import os
import numpy as np
import matplotlib.pyplot as plt

#--------------------Setup the main directories------------------#
#Define the various directories
script_dir = os.getcwd()                         #define current dir
main_dir = os.path.dirname(script_dir)           #go up of one directory
results_dir = os.path.join(main_dir, "figure")   #define results dir

if not os.path.exists(results_dir):              #if the directory does not exist create it
    os.mkdir(results_dir)

#-----------------------Transfer Function----------------------#
def HLowPass (f,fc):
    return 1 / (1 + 1j * (f / fc))

#----------------------------Phase-----------------------------#
def PhaseLowPass(Tf):
    return np.arctan(np.imag(Tf)/np.real(Tf)) * 180 /np.pi

#-------------------------Bode plot-----------------------------#
def Bode(Tf):
    return 20 * np.log10(np.abs(Tf))

if __name__ == '__main__':
    #create an array of frequencies
    f = np.linspace(0,1e3,10000)
    #define the cut-off frequency
    fc = 4 #[Hz]

    Tf = HLowPass(f,fc)
    A = Bode(Tf)
    phi = PhaseLowPass(Tf)

    # --------------------------Plot results----------------------#
    # SUBPLOTS
    fig, axs = plt.subplots(2, sharex='col', figsize=(7, 7))
    plt.rc('font', size=10)

    #adjuste space between plots
    plt.subplots_adjust(hspace=0.1)

    #set a unique title
    fig.suptitle('Bode plot for LPF', y=0.92)

    #plot transfer function
    axs[0].grid(True, color='grey', linestyle='-', alpha=0.3)
    axs[0].minorticks_on()
    axs[0].set_ylabel('Gain [dB]')
    axs[0].axvline(fc, linestyle = ':',linewidth=1, color = 'red', label = r'$f_c$ = 4 Hz')
    axs[0].plot(f, A, linestyle='-', linewidth=1.2, marker='')
    axs[0].legend()

    #plot phase
    axs[1].grid(True, color='grey', linestyle='-', alpha=0.3)
    axs[1].minorticks_on()
    axs[1].set_xlabel('f [Hz]')
    axs[1].set_ylabel(r'$\phi$ [degree]')
    axs[1].set_xscale('log')
    axs[1].axvline(fc, linestyle = ':',linewidth=1, color = 'red', label = r'$f_c$ = 4 Hz')
    axs[1].plot(f, phi, linestyle='-', linewidth=1.2, marker='')
    axs[1].legend()

    #save the plot in the results dir
    out_name = os.path.join(results_dir, "BodeLPF.png")
    plt.savefig(out_name)
    plt.show()

