def pix_space_ilc(map_list):
    "Input the maps you want to calculate weights of and it returns the weights however the pixel size of each map should be same"
    n=len(map_list)
    C=np.zeros(shape=(n,n))
    for i in range(n):
        for j in range(n):
                C[i,j]=np.sum((map_list[i]-np.mean(map_list[i]))*(map_list[j]-np.mean(map_list[j])))
    C=C/len(map_list[0])
    C_inv=np.copy(np.linalg.pinv(C))
    w=np.sum(C_inv,axis=1)/np.sum(C_inv)
    return w
