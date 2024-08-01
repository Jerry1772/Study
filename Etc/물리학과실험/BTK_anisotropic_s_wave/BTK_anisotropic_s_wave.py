#from BTK_params import *
from scipy import integrate, constants
import matplotlib.pyplot as plt
import numpy as np

class anis_s_wave():
    def __init__(self, voltage:np.ndarray=1, temp=0, btk_factor=1, Z=1, Gamma=1, alpha=1, delta1=1, delta2=1, const_G=1):
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
        self.kbt = constants.value('Boltzmann constant in eV/K') * temp

        ## 테스트용
        self.a_array = self.voltage * 15.0 * self.kbt
        self.b_array = self.voltage - 15.0 * self.kbt

    def dI_dV(self):
        dI_dV_oneside = self.btk_factor * self.dI_dV_BTK_int() + self.const_G
        dI_dV = np.concatenate((np.flip(dI_dV_oneside), dI_dV_oneside), axis=None)
        return dI_dV_oneside

    def dI_dV_BTK_int(self):
        self.voltage = self.voltage
        result = np.zeros(len(self.voltage))
        calc2 = np.zeros(150)
        angle, ang_step = np.linspace(-np.pi / 2, np.pi / 2, 512, retstep=True)
        term1 = integrate.simpson(self.tau(angle) * np.cos(angle), dx=ang_step)

        A_array = self.voltage + 15.0 * self.kbt
        B_array = self.voltage - 15.0 * self.kbt

        # 그럴 일은 없겠지만 self.voltage 가 벡터 말고 2차원 이상으로 들어오면 의도와 다르게 흘러감
        X_array, temp_step_array = np.linspace(B_array, A_array, 150, retstep=True, axis=1)

        for i in range(len(result)):
            if self.kbt != 0:
                x, temp_step = X_array[i], temp_step_array[i]
                
                sigma = self.sigma(x, angle)
                calc2 = integrate.simpson(np.expand_dims(self.df_dV(x - self.voltage[i]), axis=1) * sigma, dx=ang_step)
                # for j in range(150):
                #     sigma = self.sigma(x[j], angle) # (512, )
                #     np.put(calc2, j, integrate.simpson(self.df_dV(x[j] - self.voltage[i]) * sigma, dx=ang_step))
                calc = integrate.simpson(calc2, dx=temp_step)
            else:
                calc = self.sigma(self.voltage[i], angle)

            np.put(result, i, calc)
        return result / term1

    def tau(self, theta):
        return np.cos(theta) ** 2 / (np.cos(theta) ** 2 + self.Z ** 2)

    def gamma(self, E, theta) -> np.ndarray:
        '''
        출력값 기존: (512, ), 목표: (1999, 512)
        '''
        a = E - self.Gamma * 1j
        a = np.expand_dims(a, axis=-1) # 이거 추가해봤음
        b = np.absolute(self.delta1 + self.delta2 * np.cos(2*(theta - self.alpha)))

        result = (a - np.sqrt(a ** 2 - b ** 2)) / b # (512,)
        return result

    def sigma(self, E, theta) -> np.ndarray:
        '''
        출력값 기존: (512, ), 목표: (1999, 512)
        '''
        tau:np.ndarray = self.tau(theta)  # (512, )
        return tau * (1 + tau * np.absolute(self.gamma(E, theta)) ** 2 + (tau - 1) * np.absolute(
            self.gamma(E, theta) ** 2) ** 2) / (np.absolute(1 + (tau - 1) * self.gamma(E, theta) ** 2) ** 2)

    def df_dV(self, x):
        if self.kbt != 0:
            a = np.exp(x / self.kbt)
            return a / (self.kbt * ((a + 1) ** 2))
        else:
            return 1


if __name__ == '__main__':
    import time
    t = time.time()
    a = anis_s_wave(voltage=np.linspace(0.001,10,1999), temp=1)
    plt.plot(a.voltage, a.dI_dV(), 'r.')
    print("total time cost (신규): ", time.time() - t)
    plt.show()
