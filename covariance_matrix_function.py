import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

if __name__=="__main__":

    def give_covar_matrix(col_vector):
        print(col_vector)

        expected_value = col_vector.mean()
        print(expected_value)

        print(col_vector.shape)

        numel = col_vector.shape[0]

        cov = np.full([numel, numel], np.nan)
        print(cov)

        for i in range(numel):
            for j in range(numel):
                cov[i,j] = (col_vector[i]-expected_value)*(col_vector[j]-expected_value)

        print(cov)

        sns.set()
        ax = sns.heatmap(cov)
        ax.invert_yaxis()
        plt.show()

    col_vector = np.random.rand(10)
    give_covar_matrix(col_vector)






