import scipy.linalg as la
import numpy as np
import scipy.linalg as la

def SSVD_single(x, gamma1 = 2, gamma2 = 2, tol = 1e-6, max_iter = 50):
    
    n, d = x.shape
    
    # Step1
    U, S, V = la.svd(x)
    Vt = V.T
    iters = 0
    converge_diff_u = tol + 1
    converge_diff_v = tol + 1
    
    U_old = U[:, 0]
    S_old = S[0]
    V_old = V[0, :]
    
    V_new = np.zeros(d)
    U_new = np.zeros(n)
    
    # Step 2
    while(converge_diff_u > tol and converge_diff_v > tol and iters < max_iter):
                
        iters += 1
        #update v
        V_hat = np.zeros(d)
        Xt_U = x.T @ U_old
        omega_2 = np.abs(Xt_U) ** (-gamma2)
        error_var = np.abs(np.sum(x ** 2) - sum(Xt_U**2))/(n*d-d)
        lambda_2 = np.unique(np.append(np.abs(Xt_U / omega_2), 0))
        lambda_2.sort()
        
        min_bic = np.Inf
        
        for l in lambda_2:
            
            ## Find all v's
            term1 = Xt_U / abs(Xt_U)
            term2 = abs(Xt_U) - l * omega_2 / 2
            term2 *= term2 >= 0
            V_hat = term1 * term2           
   
            ## Choose the best v based on bic
            bic = np.sum((x - U_old.reshape((-1, 1)) @
                          V_hat.reshape((1, -1)))**2) / error_var + np.sum(V_hat!=0) * np.log(n * d)
            if bic < min_bic:
                V_new = V_hat
                min_bic = bic
                
        s = np.linalg.norm(V_new)
        V_new = V_new / s
        
        #update U
        U_hat = np.zeros(n)
        X_V = x @ V_old
        
        omega_1 = np.abs(X_V) ** (-gamma1)
        error_var = np.abs(np.sum(x ** 2) - sum(X_V**2))/(n*d-n)
        lambda_1 = np.unique(np.append(np.abs(X_V / omega_1), 0))
        lambda_1.sort()
        
        min_bic = np.Inf
        
        for l in lambda_1:

            term1 = X_V / abs(X_V)
            term2 = abs(X_V) - l * omega_1 / 2
            term2 *= term2 >= 0
            U_hat = term1 * term2
            
            ## Choose the best v based on bic
            bic = np.sum((x - U_hat.reshape((-1, 1)) @
                          V_old.reshape((1, -1)))**2)/error_var + np.sum(U_hat!=0) * np.log(n * d)
            if bic < min_bic:
                U_new = U_hat
                min_bic = bic
                
        s = np.linalg.norm(U_new)
        U_new = U_new / s
                
        converge_diff_u = np.sqrt(np.sum((U_new - U_old) ** 2))
        converge_diff_v = np.sqrt(np.sum((V_new - V_old) ** 2))
        U_old = U_new
        V_old = V_new
                
    return U_new, S_old, V_new, iters


def SSVD_multi_layer(x, layers):
    
    n, d = x.shape
    all_layers_u = np.zeros((n, layers))
    all_layers_v = np.zeros((d, layers))
    all_layers_s = np.zeros(layers)
    
    for i in range(layers):
        u_new, s_new, v_new, iters = SSVD_single(x)
        layer = s_new * u_new.reshape((-1, 1)) @ v_new.reshape((1, -1))
        all_layers_u[:, i] = u_new
        all_layers_v[:, i] = v_new
        all_layers_s[i] = s_new
        x = x - layer
        
    return all_layers_u, all_layers_v
    
