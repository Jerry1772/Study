#from BTK_params import *
import scipy.constants
import matplotlib.pyplot as plt
import numpy as np

class anis_s_wave():
    def __init__(self, voltage=1, temp=0, btk_factor=1, Z=1, Gamma=1, alpha=1, delta1=1, delta2=1, const_G=1):
        super().__init__()
        self.voltage = voltage
        self.temp = temp
        self.btk_factor = btk_factor
        self.Z = Z
        self.Gamma = Gamma
        self.alpha = alpha
        self.delta1 = delta1
        self.delta2 = delta2
        self.const_G = const_G
        self.kbt = scipy.constants.value('Boltzmann constant in eV/K') * temp

    def dI_dV(self):
        dI_dV_oneside = self.btk_factor * self.dI_dV_BTK_int() + self.const_G
        dI_dV = np.concatenate((np.flip(dI_dV_oneside), dI_dV_oneside), axis=None)
        return dI_dV_oneside

    def dI_dV_BTK_int(self):
        V = self.voltage
        result = np.zeros(len(V))
        #calc2 = np.zeros(self.temp_int_acc)
        calc2 = np.zeros(150)
        #angle, ang_step = np.linspace(-np.pi/2, np.pi/2, self.angle_int_acc, retstep=True)
        angle, ang_step = np.linspace(-np.pi / 2, np.pi / 2, 512, retstep=True)
        term1 = scipy.integrate.simpson(self.tau(angle) * np.cos(angle), dx=ang_step)
        for i in range(len(result)):
            if self.kbt != 0:
                A = 15.0 * self.kbt + V[i]
                B = V[i] - 15.0 * self.kbt
                #x, temp_step = np.linspace(B, A, self.temp_int_acc, retstep=True)
                x, temp_step = np.linspace(B, A, 150, retstep=True)
                #for j in range(self.temp_int_acc):
                for j in range(150):
                    np.put(calc2, j, scipy.integrate.simpson(self.df_dV(x[j] - V[i]) * self.sigma(x[j], angle), dx=ang_step))
                calc = scipy.integrate.simpson(calc2, dx=temp_step)
            else:
                calc = self.sigma(V[i], angle)
            np.put(result, i, calc)
        return result / term1

    def tau(self, theta):
        return np.cos(theta) ** 2 / (np.cos(theta) ** 2 + self.Z ** 2)

    def sigma(self, E, theta):
        tau = self.tau(theta)
        return tau * (1 + tau * np.absolute(self.gamma(E, theta)) ** 2 + (tau - 1) * np.absolute(
            self.gamma(E, theta) ** 2) ** 2) / (np.absolute(1 + (tau - 1) * self.gamma(E, theta) ** 2) ** 2)

    def gamma(self, E, theta):
        a = E - self.Gamma * 1j
        b = np.absolute(self.delta1 + self.delta2 * np.cos(2*(theta - self.alpha)))
        return (a - np.sqrt(a ** 2 - b ** 2)) / b

    def df_dV(self, x):
        if self.kbt != 0:
            a = np.exp(x / self.kbt)
            return a / (self.kbt * ((a + 1) ** 2))
        else:
            return 1


if __name__ == '__main__':
    a = anis_s_wave(voltage=np.linspace(0.001,10,1999), temp=1)
    plt.plot(a.voltage, a.dI_dV(), 'r.')
    plt.show()
