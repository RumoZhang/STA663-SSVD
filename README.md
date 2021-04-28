# STA663 - SSVD

Authors: Xige Huang, Rumo Zhang

The project is a implementation of the SSVD algorithm to perform biclustering, approximation to the data, and detection of the spare structure proposed in _Biclustering via Singular Value Decomposition_ by Mihee Lee, Haipeng Shen, Jianhua Z. Huang, and J. S. Marron.

The package can be installed using `pip install git+https://github.com/RumoZhang/STA663-SSVD.git#egg=STA663-SSVD`.

The package contains two functions, which can be loaded using:

- `from SSVD.functions import SSVD_single`
- `from SSVD.functions import SSVD_multi_layer`

## SSVD

The function `SSVD` performs a rank-1 approximation to the data.

The inputs are:
- `X`, the data matrix **X**
- `gamma`, gamma_1, with default of 2
- `gamma`, gamma_2, with default of 2
- `tol`, tolerance of error, with default of 1e-6
- `max_iter`, maximum iteration until converge, with default of 50

The function returns u and v, the left- and right- sparsed singular vector, and iter, number of iterations until convergence.

_Note: According to Mihee Lee, Haipeng Shen, Jianhua Z. Huang, and J. S. Marron(2010), the algorithm will typically converge within 5 to 10 iterations, but if not converge within the default of 50 iterations (happens with very small probability), try to  further increase `max_iter`._


## SSVD_multi_layer

The function `SSVD_single` performs a user-specified rank-k approximation to the data.

The inputs are:
- `X`, the data matrix **X**
- `layer`, number of layers to perform the SSVD algorithm
